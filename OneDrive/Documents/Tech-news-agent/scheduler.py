"""
Local Cron Scheduler for Tech News Agent
Run this script to schedule daily news fetching using APScheduler
"""

import schedule
import time
from datetime import datetime
from src.main import TechNewsAgent


def schedule_job():
    """Job to be executed on schedule"""
    print(f"\n{'='*80}")
    print(f"🕐 Scheduled job started at {datetime.now()}")
    print(f"{'='*80}\n")
    
    agent = TechNewsAgent()
    report = agent.run(save_report=True, print_summary=True)
    
    print(f"\n{'='*80}")
    print(f"✓ Job completed successfully at {datetime.now()}")
    print(f"{'='*80}\n")


def main():
    """Main scheduler function"""
    print("Starting Tech News Agent Scheduler...")
    print(f"Current time: {datetime.now()}")
    
    # Schedule job to run every day at 8:00 AM
    schedule.every().day.at("08:00").do(schedule_job)
    
    print("✓ Scheduled: Daily run at 08:00 AM")
    print("Press Ctrl+C to stop the scheduler\n")
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
    except KeyboardInterrupt:
        print("\n✓ Scheduler stopped by user")


if __name__ == "__main__":
    main()
