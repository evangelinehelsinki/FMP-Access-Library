"""FMP API endpoint definitions and tier requirements."""

from enum import Enum

from ..config import Tier


class Endpoint(str, Enum):
    """FMP API endpoints."""

    # Quote data
    QUOTE = "/v3/quote/{symbol}"
    AFTERMARKET_QUOTE = "/v4/pre-post-market/{symbol}"
    QUOTE_SHORT = "/v3/quote-short/{symbol}"

    # Company profile
    PROFILE = "/v3/profile/{symbol}"
    EXECUTIVES = "/v3/key-executives/{symbol}"

    # Corporate events
    DIVIDENDS_HISTORICAL = "/v3/historical-price-full/stock_dividend/{symbol}"
    STOCK_SPLIT_HISTORICAL = "/v3/historical-price-full/stock_split/{symbol}"
    EARNINGS_CALENDAR = "/v3/earnings-calendar"
    EARNINGS_HISTORICAL = "/v3/historical/earning_calendar/{symbol}"

    # Fundamental statements
    INCOME_STATEMENT = "/v3/income-statement/{symbol}"
    BALANCE_SHEET = "/v3/balance-sheet-statement/{symbol}"
    CASH_FLOW = "/v3/cash-flow-statement/{symbol}"

    # Financial metrics
    KEY_METRICS = "/v3/key-metrics/{symbol}"
    FINANCIAL_RATIOS = "/v3/ratios/{symbol}"
    FINANCIAL_SCORES = "/v4/score"

    # Valuation
    DCF = "/v3/discounted-cash-flow/{symbol}"
    HISTORICAL_DCF = "/v3/historical-discounted-cash-flow-statement/{symbol}"
    ENTERPRISE_VALUE = "/v3/enterprise-values/{symbol}"

    # Analyst data
    ANALYST_ESTIMATES = "/v3/analyst-estimates/{symbol}"
    PRICE_TARGET = "/v4/price-target"
    PRICE_TARGET_SUMMARY = "/v4/price-target-summary"
    PRICE_TARGET_CONSENSUS = "/v4/price-target-consensus"
    ANALYST_UPGRADES_DOWNGRADES = "/v4/upgrades-downgrades"
    ANALYST_RECOMMENDATIONS = "/v3/analyst-stock-recommendations/{symbol}"

    # Ownership
    INSTITUTIONAL_HOLDERS = "/v3/institutional-holder/{symbol}"
    INSIDER_TRADING = "/v4/insider-trading"
    INSIDER_ROSTER = "/v4/insider-roaster"

    # Historical prices
    HISTORICAL_PRICES = "/v3/historical-price-full/{symbol}"
    HISTORICAL_PRICES_DAILY = "/v3/historical-chart/{timeframe}/{symbol}"

    # Earnings transcripts
    EARNING_CALL_TRANSCRIPT = "/v3/earning_call_transcript/{symbol}"
    BATCH_EARNING_CALL_TRANSCRIPT = "/v4/batch_earning_call_transcript/{symbol}"

    # SEC filings
    SEC_FILINGS = "/v3/sec_filings/{symbol}"
    SEC_RSS_FEED = "/v4/rss_feed"

    # News
    STOCK_NEWS = "/v3/stock_news"
    STOCK_NEWS_SENTIMENT = "/v4/stock-news-sentiments-rss-feed"

    # Market data
    MARKET_HOURS = "/v3/market-hours"
    IS_MARKET_OPEN = "/v3/is-the-market-open"

    # Symbols and search
    SYMBOL_SEARCH = "/v3/search"
    SYMBOL_LIST = "/v3/stock/list"


# Tier requirements for each endpoint
TIER_REQUIREMENTS = {
    # Free/Starter tier endpoints
    Endpoint.QUOTE: Tier.STARTER,
    Endpoint.PROFILE: Tier.STARTER,
    Endpoint.HISTORICAL_PRICES: Tier.STARTER,
    Endpoint.INCOME_STATEMENT: Tier.STARTER,
    Endpoint.BALANCE_SHEET: Tier.STARTER,
    Endpoint.CASH_FLOW: Tier.STARTER,
    Endpoint.SYMBOL_SEARCH: Tier.STARTER,
    Endpoint.SYMBOL_LIST: Tier.STARTER,
    Endpoint.STOCK_NEWS: Tier.STARTER,
    Endpoint.DCF: Tier.STARTER,
    Endpoint.KEY_METRICS: Tier.STARTER,
    Endpoint.FINANCIAL_RATIOS: Tier.STARTER,
    Endpoint.MARKET_HOURS: Tier.STARTER,
    Endpoint.IS_MARKET_OPEN: Tier.STARTER,

    # Premium tier endpoints
    Endpoint.AFTERMARKET_QUOTE: Tier.PREMIUM,
    Endpoint.EXECUTIVES: Tier.PREMIUM,
    Endpoint.DIVIDENDS_HISTORICAL: Tier.PREMIUM,
    Endpoint.STOCK_SPLIT_HISTORICAL: Tier.PREMIUM,
    Endpoint.EARNINGS_CALENDAR: Tier.PREMIUM,
    Endpoint.EARNINGS_HISTORICAL: Tier.PREMIUM,
    Endpoint.ENTERPRISE_VALUE: Tier.PREMIUM,
    Endpoint.ANALYST_ESTIMATES: Tier.PREMIUM,
    Endpoint.INSTITUTIONAL_HOLDERS: Tier.PREMIUM,
    Endpoint.INSIDER_TRADING: Tier.PREMIUM,
    Endpoint.SEC_FILINGS: Tier.PREMIUM,
    Endpoint.EARNING_CALL_TRANSCRIPT: Tier.PREMIUM,

    # Ultimate tier endpoints
    Endpoint.PRICE_TARGET: Tier.ULTIMATE,
    Endpoint.PRICE_TARGET_SUMMARY: Tier.ULTIMATE,
    Endpoint.PRICE_TARGET_CONSENSUS: Tier.ULTIMATE,
    Endpoint.ANALYST_UPGRADES_DOWNGRADES: Tier.ULTIMATE,
    Endpoint.ANALYST_RECOMMENDATIONS: Tier.ULTIMATE,
    Endpoint.INSIDER_ROSTER: Tier.ULTIMATE,
    Endpoint.BATCH_EARNING_CALL_TRANSCRIPT: Tier.ULTIMATE,
    Endpoint.STOCK_NEWS_SENTIMENT: Tier.ULTIMATE,
    Endpoint.SEC_RSS_FEED: Tier.ULTIMATE,
    Endpoint.FINANCIAL_SCORES: Tier.ULTIMATE,
    Endpoint.HISTORICAL_DCF: Tier.ULTIMATE,
    Endpoint.QUOTE_SHORT: Tier.ULTIMATE,
    Endpoint.HISTORICAL_PRICES_DAILY: Tier.PREMIUM,
}


# Base URL for FMP API
BASE_URL = "https://financialmodelingprep.com/api"


def get_endpoint_url(endpoint: Endpoint, **path_params: str) -> str:
    """Get full endpoint URL with path parameters.

    Args:
        endpoint: Endpoint enum value
        **path_params: Path parameters to format into endpoint

    Returns:
        Full endpoint path

    Example:
        >>> get_endpoint_url(Endpoint.QUOTE, symbol="AAPL")
        '/v3/quote/AAPL'
    """
    endpoint_path = endpoint.value
    if path_params:
        endpoint_path = endpoint_path.format(**path_params)
    return endpoint_path
