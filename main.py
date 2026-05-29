from jira_client import get_open_tickets
from formatter import build_report
from analyzer import analyze_all_tickets
from slack_client import post_report

tickets = get_open_tickets()
on_track, at_risk, overdue = analyze_all_tickets(tickets)
report = build_report(on_track, at_risk, overdue)
post_report(report)