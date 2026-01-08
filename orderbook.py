from py_clob_client.client import ClobClient
import os
from dotenv import load_dotenv

load_dotenv()


def main():
    host = os.getenv("CLOB_API_URL", "https://clob.polymarket.com")
    client = ClobClient(host)

    
    orderbook = client.get_order_book(
        "75953434464128028309930189401551270894422079279240636099997239588009003527304"
    )
    print("orderbook", orderbook)

    hash = client.get_order_book_hash(orderbook)
    print("orderbook hash", hash)


main()