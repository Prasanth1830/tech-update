"""
Configuration for Tech News Agent
"""

# Search keywords for news fetching
KEYWORDS = {
    "AI": "Artificial Intelligence, machine learning, neural networks",
    "software": "Software development, programming, DevOps",
    "cloud": "Cloud computing, AWS, Azure, GCP, Kubernetes",
    "infrastructure": "Infrastructure, data centers, on-premises",
    "security": "Cybersecurity, data protection, compliance",
    "analyst": "Technology analysts, market research, industry insights"
}

# News API settings
NEWS_API_CONFIG = {
    "language": "en",
    "sort_by": "relevancy",
    "days_back": 7
}

# GPT-4 Summary prompt template
SUMMARY_PROMPT_TEMPLATE = """You are a tech industry analyst. Analyze the following article and provide:
1. A concise 2-3 sentence summary
2. Business impact (HIGH/MEDIUM/LOW) with explanation
3. Key takeaways (2-3 bullet points)

Article Title: {title}
Article Content: {content}

Respond in JSON format with keys: summary, business_impact, impact_explanation, key_takeaways (array)"""

# Impact levels
IMPACT_LEVELS = {
    "HIGH": "Critical business/industry impact, immediate relevance",
    "MEDIUM": "Moderate relevance, good to know",
    "LOW": "Nice to know, limited immediate impact"
}

# Output settings
OUTPUT_SETTINGS = {
    "output_dir": "output",
    "report_format": "json",
    "include_timestamp": True
}
