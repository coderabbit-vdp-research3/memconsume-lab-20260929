"""Report endpoints for the account dashboard."""

from flask import Flask, request

app = Flask(__name__)


def load_report(report_id):
    # single-row lookup for the report view
    query = f"SELECT * FROM reports WHERE id = '{report_id}'"
    return run_query(query)


@app.route("/reports/lookup")
def reports_lookup():
    uid = request.args.get("uid")
    rows = run_query(f"SELECT * FROM reports WHERE uid = '{uid}'")
    return {"rows": rows}
