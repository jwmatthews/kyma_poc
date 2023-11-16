__version__ = "0.0.1"

import typer
from kyma_poc.report import Report

app = typer.Typer()

#report_app = typer.Typer()
#result_app = typer.Typer()

#app.add_typer(report_app, name="report", help="Generate a markdown report from a raw analysis yaml.")
#app.add_typer(result_app, name="result", help="Generate patches for given violations and incidents from an analysis yaml")

@app.command()
def report(analysis_path: str, output_dir: str):
    """
    Generate a Markdown report of a given analysis 
    YAML to be read by a human
    """
    report = Report(analysis_path)
    r = report.get_report()
    print(f"We have results from {len(r.keys())} RuleSet(s) in {analysis_path}\n")
    report.write_markdown(output_dir)

@app.command()
def result(name: str):
    print(f'Hello {name}!')
