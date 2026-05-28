def build_report(on_track, at_risk, overdue):
    on_track_count = len(on_track)
    at_risk_count = len(at_risk)
    overdue_count = len(overdue)

    total_report = """ IT WEEKLY STATUS REPORT
                ON TRACK: {on_track_count} tickets
                AT RISK: {at_risk_count} tickets
                OVERDUE: {overdue_count} tickets
    """

    return total_report
    
