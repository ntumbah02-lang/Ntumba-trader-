from threading import Event
import ccxt

from config import DEFAULT_SYMBOL, EXCHANGE, MAX_POSITION_SIZE, RISK_PER_TRADE


class PaperTrader:
    def __init__(self):
        self.exchange = ccxt.binance({
            "enableRateLimit": True,
            "options": {"defaultType": "spot"},
        })
        self.symbol = DEFAULT_SYMBOL
        self.running = Event()

    def get_market_price(self):
        ticker = self.exchange.fetch_ticker(self.symbol)
        return float(ticker["last"])

    def analyze(self, price):
        if price > 0:
            return {
                "symbol": self.symbol,
                "side": "buy",
                "price": price,
                "risk": RISK_PER_TRADE,
                "position_size": MAX_POSITION_SIZE,
                "status": "paper",
            }
        return {"symbol": self.symbol, "side": "hold", "price": price, "status": "paper"}

    def run(self):
        self.running.set()
        while self.running.is_set():
            price = self.get_market_price()
            signal = self.analyze(price)
            print(f"[{self.symbol}] {signal}")
            break


def main():
    bot = PaperTrader()
    bot.run()


if __name__ == "__main__":
    main()
