from datetime import datetime, timedelta
def categorize_ticket(ticket):
    fields = ticket["fields"]
    status = fields["status"]["name"]
    assignment = fields["assignee"]
    update = fields["updated"]
    due_date = fields["duedate"]

    now = datetime.now()

    if due_date_has_passed or updated_more_than_7_days_ago:
        return "overdue"
    elif assignee is None or updated_between_3_and_7_days_ago:
        return "at_risk"
    else:
        return "on_track"
    

def analyze_all_tickets(tickets):
    overdue = []
    at_risk = []
    on_track = []
    
    for ticket in tickets:
        ticket_status = categorize_ticket(ticket)
        if ticket_status == "overdue":
            overdue.append(ticket)
        elif ticket_status == "at_risk":
            at_risk.append(ticket)
        else:
            on_track.append(ticket)
    
    return overdue, at_risk, on_track





    


    