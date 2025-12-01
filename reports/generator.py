import pdfkit
from pathlib import Path
from datetime import datetime

TEMPLATE_DIR = Path("./reports/templates")

# Optional: manually define wkhtmltopdf path if it's not in PATH
WKHTML_PATH = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=WKHTML_PATH)


def load_template(template_name: str) -> str:
    """Load template text file."""
    return (TEMPLATE_DIR / template_name).read_text(encoding="utf-8")


def fill_template(template: str, context: dict) -> str:
    for key, value in context.items():
        template = template.replace(f"{{{{{key}}}}}", str(value))
    return template


def generate_markdown_report(context: dict, output_name: str) -> Path:
    """Save filled markdown report."""
    md = load_template("report_template.md")
    output = fill_template(md, context)

    out_file = Path(f"./data/reports/{output_name}.md")
    out_file.write_text(output, encoding="utf-8")
    print(f"📄 Markdown report saved → {out_file}")
    return out_file


def generate_html_report(context: dict, output_name: str) -> Path:
    """Generate HTML report."""
    html = load_template("report_template.html")
    output = fill_template(html, context)

    out_file = Path(f"./data/reports/{output_name}.html")
    out_file.write_text(output, encoding="utf-8")
    print(f"🌎 HTML report saved → {out_file}")
    return out_file


def generate_pdf_report(context: dict, output_name: str) -> Path:
    """Generate PDF using wkhtmltopdf."""
    html_file = generate_html_report(context, output_name)
    out_file = Path(f"./data/reports/{output_name}.pdf")

    pdfkit.from_file(str(html_file), str(out_file), configuration=config)

    print(f"📕 PDF report saved → {out_file}")
    return out_file


def build_full_report(result_dict: dict, repo_name="UnknownRepo"):
    """Creates all formats of the report."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"{repo_name}_audit_{timestamp}"

    context = {
        "repo_name": repo_name,
        "scan_date": datetime.now().strftime("%d %B %Y"),
        **result_dict
    }

    generate_markdown_report(context, filename)
    generate_pdf_report(context, filename)

    return filename
