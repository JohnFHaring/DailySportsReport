import datetime

def get_report():
    today = datetime.date.today()

    # placeholder (we'll replace with real sports data later)
    mlb_scores = "MLB: Yankees 5 - Red Sox 3"
    nba_scores = "NBA: Knicks 102 - Nets 99"

    report = f"""
SPORTS REPORT - {today}

{mlb_scores}
{nba_scores}
"""

    return report

if __name__ == "__main__":
    print(get_report())
