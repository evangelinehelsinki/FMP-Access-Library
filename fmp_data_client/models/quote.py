"""Quote and after-market quote models."""

from datetime import datetime
from typing import Optional

from pydantic import Field

from .base import FMPBaseModel


class Quote(FMPBaseModel):
    """Real-time stock quote data."""

    symbol: str = Field(..., description="Stock ticker symbol")
    price: float = Field(..., description="Current price")
    volume: int = Field(..., description="Trading volume")

    # Price changes
    change: float = Field(..., description="Price change in dollars")
    change_percent: float = Field(
        ...,
        alias="changesPercentage",
        description="Price change percentage"
    )

    # Day range
    day_high: float = Field(..., alias="dayHigh", description="Day high price")
    day_low: float = Field(..., alias="dayLow", description="Day low price")

    # Previous close
    previous_close: float = Field(
        ...,
        alias="previousClose",
        description="Previous closing price"
    )

    # Market cap
    market_cap: Optional[int] = Field(
        None,
        alias="marketCap",
        description="Market capitalization"
    )

    # 52-week range
    year_high: Optional[float] = Field(
        None,
        alias="yearHigh",
        description="52-week high"
    )
    year_low: Optional[float] = Field(
        None,
        alias="yearLow",
        description="52-week low"
    )

    # Trading metrics
    open: Optional[float] = Field(None, description="Opening price")
    avg_volume: Optional[int] = Field(
        None,
        alias="avgVolume",
        description="Average volume"
    )

    # Valuation metrics
    pe: Optional[float] = Field(None, description="P/E ratio")
    eps: Optional[float] = Field(None, description="Earnings per share")

    # Timestamp
    timestamp: Optional[int] = Field(
        None,
        description="Unix timestamp of quote"
    )

    # Exchange
    exchange: Optional[str] = Field(
        None,
        description="Exchange where stock is traded"
    )

    # Name
    name: Optional[str] = Field(None, description="Company name")

    @property
    def timestamp_dt(self) -> Optional[datetime]:
        """Get timestamp as datetime object.

        Returns:
            Datetime object if timestamp is set, else None
        """
        if self.timestamp:
            return datetime.fromtimestamp(self.timestamp)
        return None

    @property
    def is_positive_change(self) -> bool:
        """Check if price change is positive.

        Returns:
            True if change is positive, else False
        """
        return self.change >= 0


class AftermarketQuote(FMPBaseModel):
    """After-hours and pre-market quote data."""

    symbol: str = Field(..., description="Stock ticker symbol")

    # Pre-market
    pre_market_price: Optional[float] = Field(
        None,
        alias="preMarketPrice",
        description="Pre-market price"
    )
    pre_market_change: Optional[float] = Field(
        None,
        alias="preMarketChange",
        description="Pre-market change in dollars"
    )
    pre_market_change_percent: Optional[float] = Field(
        None,
        alias="preMarketChangePercentage",
        description="Pre-market change percentage"
    )

    # After-hours
    after_hours_price: Optional[float] = Field(
        None,
        alias="afterHoursPrice",
        description="After-hours price"
    )
    after_hours_change: Optional[float] = Field(
        None,
        alias="afterHoursChange",
        description="After-hours change in dollars"
    )
    after_hours_change_percent: Optional[float] = Field(
        None,
        alias="afterHoursChangePercentage",
        description="After-hours change percentage"
    )

    # Volume
    pre_market_volume: Optional[int] = Field(
        None,
        alias="preMarketVolume",
        description="Pre-market volume"
    )
    after_hours_volume: Optional[int] = Field(
        None,
        alias="afterHoursVolume",
        description="After-hours volume"
    )

    # Timestamp
    timestamp: Optional[int] = Field(
        None,
        description="Unix timestamp"
    )

    @property
    def has_pre_market_data(self) -> bool:
        """Check if pre-market data is available."""
        return self.pre_market_price is not None

    @property
    def has_after_hours_data(self) -> bool:
        """Check if after-hours data is available."""
        return self.after_hours_price is not None
