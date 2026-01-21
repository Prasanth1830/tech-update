#!/usr/bin/env python3
"""
Tech News Agent - Fetches and summarizes tech news articles
Focuses on business impact for key technology topics
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict
from dotenv import load_dotenv

# Fix encoding for Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from src.news_fetcher import NewsFetcher
from src.summarizer import Summarizer

load_dotenv()


class TechNewsAgent:
    """
    Main orchestrator for the tech news fetching and summarization pipeline.
    """
    
    def __init__(self):
        self.fetcher = NewsFetcher()
        self.summarizer = Summarizer()
        self.output_dir = Path("output")
        self.output_dir.mkdir(exist_ok=True)
    
    def generate_report(self) -> Dict:
        """
        Generate a complete news report with summaries and business impact analysis.
        
        Returns:
            Dictionary containing the complete report
        """
        print("=" * 80)
        print("🚀 TECH NEWS AGENT - DAILY BRIEFING")
        print(f"📅 Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 80)
        
        # Step 1: Fetch articles
        articles = self.fetcher.fetch_all_articles()
        
        if not articles:
            print("\n❌ No articles found. Exiting.")
            return {"status": "failed", "message": "No articles fetched"}
        
        # Step 2: Summarize articles
        summarized_articles = self.summarizer.summarize_articles(articles)
        
        # Step 3: Organize by business impact
        high_impact = [a for a in summarized_articles if a.get("business_impact") == "HIGH"]
        medium_impact = [a for a in summarized_articles if a.get("business_impact") == "MEDIUM"]
        low_impact = [a for a in summarized_articles if a.get("business_impact") == "LOW"]
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "total_articles": len(summarized_articles),
            "impact_breakdown": {
                "high": len(high_impact),
                "medium": len(medium_impact),
                "low": len(low_impact)
            },
            "articles_by_impact": {
                "high": high_impact,
                "medium": medium_impact,
                "low": low_impact
            },
            "articles": summarized_articles
        }
        
        return report
    
    def save_report(self, report: Dict) -> str:
        """
        Save the report to a JSON file.
        
        Args:
            report: Report dictionary
            
        Returns:
            Path to saved file
        """
        timestamp = datetime.now().strftime("%Y-%m-%d")
        filename = f"tech_news_report_{timestamp}.json"
        filepath = self.output_dir / filename
        
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"\n✓ Report saved to: {filepath}")
        return str(filepath)
    
    def print_summary(self, report: Dict) -> None:
        """
        Print a formatted summary of the report.
        
        Args:
            report: Report dictionary
        """
        print("\n" + "=" * 80)
        print("📊 REPORT SUMMARY")
        print("=" * 80)
        
        impact = report.get("impact_breakdown", {})
        print(f"\nTotal Articles Processed: {report.get('total_articles')}")
        print(f"  🔴 HIGH Impact: {impact.get('high', 0)}")
        print(f"  🟡 MEDIUM Impact: {impact.get('medium', 0)}")
        print(f"  🟢 LOW Impact: {impact.get('low', 0)}")
        
        print("\n" + "-" * 80)
        print("🔴 HIGH IMPACT ARTICLES")
        print("-" * 80)
        
        high_articles = report.get("articles_by_impact", {}).get("high", [])
        if high_articles:
            for idx, article in enumerate(high_articles[:5], 1):
                print(f"\n{idx}. {article.get('title', 'Unknown')}")
                print(f"   Source: {article.get('source', 'Unknown')}")
                print(f"   Summary: {article.get('summary', 'N/A')[:150]}...")
                print(f"   Impact: {article.get('impact_explanation', 'N/A')[:100]}...")
                print(f"   URL: {article.get('url', 'N/A')}")
        else:
            print("No high impact articles found.")
        
        print("\n" + "=" * 80)
    
    def run(self, save_report: bool = True, print_summary: bool = True) -> Dict:
        """
        Run the complete news agent pipeline.
        
        Args:
            save_report: Whether to save report to file
            print_summary: Whether to print summary to console
            
        Returns:
            Report dictionary
        """
        try:
            report = self.generate_report()
            
            if save_report and report.get("status") != "failed":
                self.save_report(report)
            
            if print_summary and report.get("status") != "failed":
                self.print_summary(report)
            
            return report
            
        except Exception as e:
            print(f"\n❌ Error running agent: {str(e)}")
            import traceback
            traceback.print_exc()
            return {"status": "error", "message": str(e)}


if __name__ == "__main__":
    agent = TechNewsAgent()
    report = agent.run()
    print("\n✓ Tech news agent run completed successfully!")
