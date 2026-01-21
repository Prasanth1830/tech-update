import os
from typing import List, Dict
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

class Summarizer:
    """
    Uses OpenAI GPT-4 to summarize articles with focus on business impact.
    """
    
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model = os.getenv("MODEL_NAME", "gpt-4")
        
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        
        self.client = OpenAI(api_key=self.api_key)
    
    def generate_summary(self, article: Dict) -> Dict:
        """
        Generate a business-focused summary of an article using GPT-4.
        
        Args:
            article: Dictionary containing article data (title, content)
            
        Returns:
            Dictionary with original article data plus summary and business impact
        """
        title = article.get("title", "")
        content = article.get("content", "")
        
        if not content or content == "[Removed]":
            return {
                **article,
                "summary": "Unable to generate summary - content not available",
                "business_impact": "Unknown",
                "key_takeaways": []
            }
        
        try:
            # Truncate content to avoid token limits
            content_truncated = content[:2000]
            
            prompt = f"""You are a tech industry analyst. Analyze the following article and provide:
1. A concise 2-3 sentence summary
2. Business impact (HIGH/MEDIUM/LOW) with explanation
3. Key takeaways (2-3 bullet points)

Article Title: {title}
Article Content: {content_truncated}

Respond in JSON format with keys: summary, business_impact, impact_explanation, key_takeaways (array)"""
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a tech industry analyst. Always respond with valid JSON."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=500
            )
            
            response_text = response.choices[0].message.content
            
            # Parse JSON response
            import json
            try:
                parsed = json.loads(response_text)
                return {
                    **article,
                    "summary": parsed.get("summary", ""),
                    "business_impact": parsed.get("business_impact", "MEDIUM"),
                    "impact_explanation": parsed.get("impact_explanation", ""),
                    "key_takeaways": parsed.get("key_takeaways", [])
                }
            except json.JSONDecodeError:
                return {
                    **article,
                    "summary": response_text,
                    "business_impact": "MEDIUM",
                    "impact_explanation": "Unable to parse response",
                    "key_takeaways": []
                }
            
        except Exception as e:
            print(f"✗ Error summarizing article: {str(e)}")
            return {
                **article,
                "summary": f"Error: {str(e)}",
                "business_impact": "UNKNOWN",
                "impact_explanation": "Processing error",
                "key_takeaways": []
            }
    
    def summarize_articles(self, articles: List[Dict]) -> List[Dict]:
        """
        Summarize a list of articles.
        
        Args:
            articles: List of article dictionaries
            
        Returns:
            List of articles with summaries and business impact
        """
        print(f"\n🤖 Summarizing {len(articles)} articles using GPT-4...\n")
        
        summarized = []
        for idx, article in enumerate(articles, 1):
            print(f"Processing article {idx}/{len(articles)}: {article.get('title', 'Unknown')[:60]}...")
            summary = self.generate_summary(article)
            summarized.append(summary)
        
        print(f"\n✓ All articles summarized\n")
        return summarized
