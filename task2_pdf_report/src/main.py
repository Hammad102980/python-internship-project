import pandas as pd
from fpdf import FPDF
from pathlib import Path

def analyze_sales_data(csv_path: Path) -> dict:
    """Analyze sales data and return summary stats."""
    df = pd.read_csv(csv_path)
    
    total_revenue = df['revenue'].sum()
    total_units = df['units_sold'].sum()
    avg_profit_margin = df['profit_margin'].mean()
    top_product = df.loc[df['revenue'].idxmax(), 'product']
    
    return {
        'total_revenue': total_revenue,
        'total_units': total_units,
        'avg_profit_margin': avg_profit_margin,
        'top_product': top_product,
        'total_products': len(df),
        'df': df
    }

def create_pdf_report(analysis: dict, output_path: Path):
    """Generate formatted PDF report."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=24)
    pdf.cell(200, 10, text="Sales Report - Task 2", new_x="LMARGIN", new_y="NEXT", align='C')
    
    pdf.ln(10)
    pdf.set_font("Helvetica", size=16)
    pdf.cell(200, 10, text="Executive Summary", new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_font("Helvetica", '', 12)
    pdf.cell(200, 10, text=f"Total Revenue: Rs.{analysis['total_revenue']:,.0f}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(200, 10, text=f"Total Units Sold: {analysis['total_units']:,}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(200, 10, text=f"Average Profit Margin: {analysis['avg_profit_margin']:.1f}%", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(200, 10, text=f"Top Product: {analysis['top_product']}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(200, 10, text=f"Total Products: {analysis['total_products']}", new_x="LMARGIN", new_y="NEXT")
    
    pdf.ln(10)
    pdf.set_font("Helvetica", size=16)
    pdf.cell(200, 10, text="Product Details", new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_font("Helvetica", '', 10)
    # Table header
    col_widths = [50, 40, 40, 40]
    pdf.cell(col_widths[0], 10, 'Product', 1)
    pdf.cell(col_widths[1], 10, 'Units', 1)
    pdf.cell(col_widths[2], 10, 'Revenue', 1)
    pdf.cell(col_widths[3], 10, 'Margin %', 1)
    pdf.ln()
    
    # Table data
    for _, row in analysis['df'].iterrows():
        pdf.cell(col_widths[0], 10, str(row['product']), 1)
        pdf.cell(col_widths[1], 10, str(row['units_sold']), 1)
        pdf.cell(col_widths[2], 10, f"Rs.{row['revenue']:,.0f}", 1)
        pdf.cell(col_widths[3], 10, f"{row['profit_margin']}%", 1)
        pdf.ln()
    
    pdf.output(output_path)
    print(f"✅ PDF Report saved: {output_path}")

def main():
    print("=== Task 2: PDF Report Generation ===")
    
    # Ensure directories
    project_root = Path(__file__).resolve().parent.parent
    data_dir = project_root / "data"
    reports_dir = project_root / "reports"
    data_dir.mkdir(exist_ok=True)
    reports_dir.mkdir(exist_ok=True)
    
    # Read and analyze data
    csv_path = project_root / "src" / "sample_data.csv"
    analysis = analyze_sales_data(csv_path)
    
    print("📊 Analysis Summary:")
    print(f"   Total Revenue: Rs.{analysis['total_revenue']:,.0f}")
    print(f"   Top Product: {analysis['top_product']}")
    
    # Generate PDF
    pdf_path = reports_dir / "sales_report.pdf"
    create_pdf_report(analysis, pdf_path)
    
    print("🎉 Task 2 COMPLETED!")
    print(f"📁 Check: task2_pdf_report/reports/sales_report.pdf")

if __name__ == "__main__":
    main()
