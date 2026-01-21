import requests
import os
from datetime import datetime, timedelta
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()

class NewsFetcher:
    """
    Fetches tech news articles from NewsAPI based on keywords.
    """
    
    def __init__(self):
        self.api_key = os.getenv("NEWS_API_KEY")
        self.base_url = "https://newsapi.org/v2/everything"
        self.keywords = ["AI", "software", "cloud", "infrastructure", "security", "analyst"]
        self.max_articles = int(os.getenv("MAX_ARTICLES_PER_KEYWORD", 5))
        
        if not self.api_key:
            raise ValueError("NEWS_API_KEY not found in environment variables")
    
    def fetch_articles_by_keyword(self, keyword: str) -> List[Dict]:
        """
        Fetch articles for a specific keyword from the past 7 days.
        
        Args:
            keyword: Search term for articles
            
        Returns:
            List of article dictionaries
        """
        try:
            # Calculate date from 7 days ago
            from_date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
            
            params = {
                "q": keyword,
                "from": from_date,
                "sortBy": "relevancy",
                "language": "en",
                "apiKey": self.api_key,
                "pageSize": self.max_articles
            }
            
            response = requests.get(self.base_url, params=params, timeout=30, verify=False)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get("status") != "ok":
                print(f"API Error for keyword '{keyword}': {data.get('message', 'Unknown error')}")
                return []
            
            articles = data.get("articles", [])
            print(f"✓ Fetched {len(articles)} articles for keyword: {keyword}")
            
            return articles
            
        except requests.exceptions.RequestException as e:
            print(f"✗ Error fetching articles for '{keyword}': {str(e)}")
            return []
    
    def fetch_all_articles(self) -> List[Dict]:
        """
        Fetch articles for all keywords.
        
        Returns:
            Combined list of articles from all keywords
        """
        all_articles = []
        
        print("\n📰 Fetching tech news articles...\n")
        
        for keyword in self.keywords:
            articles = self.fetch_articles_by_keyword(keyword)
            all_articles.extend(articles)
        
        # Remove duplicates based on URL
        unique_articles = {article["url"]: article for article in all_articles}
        
        print(f"\n✓ Total unique articles fetched: {len(unique_articles)}")
        return list(unique_articles.values())
    
    def get_articles_sample(self) -> List[Dict]:
        """
        Return a formatted sample of fetched articles.
        """
        articles = self.fetch_all_articles()
        
        formatted = []
        for article in articles[:10]:  # Limit to first 10
            formatted.append({
                "title": article.get("title"),
                "source": article.get("source", {}).get("name"),
                "url": article.get("url"),
                "content": article.get("description"),
                "published_at": article.get("publishedAt")
            })
        
        return formatted
