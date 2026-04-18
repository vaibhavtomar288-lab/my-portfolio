import argparse
from pathlib import Path

PROJECTS = [
    {
        "title": "AI-driven Resume Builder",
        "description": "Developed a Python application that generates tailored resume content, project descriptions, and skill summaries using natural language processing.",
        "tech": ["Python", "NLTK", "OpenAI API", "JSON"],
        "impact": "Reduced resume writing time by 70% and produced optimized resume sections for technical roles."
    },
    {
        "title": "Data Pipeline Automation",
        "description": "Designed an ETL pipeline to ingest, clean, and transform CSV and JSON datasets into analytics-ready data lakes.",
        "tech": ["Python", "Pandas", "Airflow", "SQL"],
        "impact": "Automated daily data ingestion and reporting workflows, improving data freshness and reliability."
    },
    {
        "title": "Interactive Analytics Dashboard",
        "description": "Built a dashboard for business stakeholders to explore customer and sales metrics with interactive charts and drill-down filters.",
        "tech": ["Python", "Streamlit", "Plotly", "Pandas"],
        "impact": "Enabled stakeholders to identify trends faster and supported data-driven decision-making across the company."
    },
    {
        "title": "Cloud Deployment Tooling",
        "description": "Created a deployment automation toolkit for containerized Python services using infrastructure-as-code and CI/CD integration.",
        "tech": ["Python", "Docker", "GitHub Actions", "AWS"],
        "impact": "Deployed microservices consistently across staging and production, reducing deployment errors by over 50%."
    }
]


def build_markdown(projects):
    lines = ["# Resume Project Portfolio", "", "Generated project summaries for resume presentation:", ""]
    for project in projects:
        lines.extend([
            f"## {project['title']}",
            "",
            project["description"],
            "",
            f"**Tech stack:** {', '.join(project['tech'])}",
            f"**Impact:** {project['impact']}",
            ""
        ])
    return "\n".join(lines)


def create_project_scaffold(base_dir: str, projects):
    base_path = Path(base_dir)
    base_path.mkdir(parents=True, exist_ok=True)

    for project in projects:
        project_dir = base_path / project["title"].lower().replace(" ", "-")
        project_dir.mkdir(parents=True, exist_ok=True)
        readme_path = project_dir / "README.md"
        content = [
            f"# {project['title']}",
            "",
            project["description"],
            "",
            "## Tech Stack",
            "",
            *[f"- {tech}" for tech in project["tech"]],
            "",
            "## Impact",
            "",
            project["impact"],
            ""
        ]
        readme_path.write_text("\n".join(content), encoding="utf-8")

    summary_path = base_path / "PROJECTS_SUMMARY.md"
    summary_path.write_text(build_markdown(projects), encoding="utf-8")
    return summary_path


def main():
    parser = argparse.ArgumentParser(description="Generate resume project summaries and optional project scaffolds.")
    parser.add_argument("--output", "-o", default="resume_projects", help="Output folder for generated projects")
    parser.add_argument("--no-scaffold", action="store_true", help="Only print the Markdown summary without creating folders")
    args = parser.parse_args()

    markdown = build_markdown(PROJECTS)
    print(markdown)

    if not args.no_scaffold:
        summary_path = create_project_scaffold(args.output, PROJECTS)
        print(f"\nCreated project scaffold at: {summary_path}")


if __name__ == "__main__":
    main()
