import unittest
from interfaces.ISessionHandler import ISessionHandler
from factories.YFRequestFactory import YFRequestFactory
import requests

class TestYFRequestHandler(unittest.TestCase):

      def test_request_handler_correctly_formats_request_url(self):
            expected_url = "https://query1.finance.yahoo.com/v10/finance/quoteSummary/[TestTicker]?formatted=true&crumb=[TestCrumb]&lang=en-GB&region=GB&modules=upgradeDowngradeHistory%2CrecommendationTrend%2CfinancialData%2CearningsHistory%2CearningsTrend%2CindustryTrend%2CindexTrend%2CsectorTrend&symbol=[TestTicker]&corsDomain=uk.finance.yahoo.com"
            session_handler = TestSessionHandler()
            request_handler = YFRequestFactory.make_request_object(session_handler, "analysis")
            result_url = request_handler.url(ticker="[TestTicker]")
            self.assertEqual(result_url, expected_url)

      def test_request_handler_correctly_formats_request_headers(self):
            expected_headers = {
                  "Accept": "*/*",
                  "Accept-Encoding": "gzip, deflate, br, zstd",
                  "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
                  "Origin": "https://uk.finance.yahoo.com",
                  "Referer": "https://uk.finance.yahoo.com/quote/[TestTicker]/analysis",
                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
            }
            session_handler = TestSessionHandler()
            request_handler = YFRequestFactory.make_request_object(session_handler, "analysis")
            result_headers = request_handler.headers(ticker="[TestTicker]")
            self.assertEqual(result_headers, expected_headers)


class TestSessionHandler(ISessionHandler):

      def __init__(self):
            self.new_session()
            self.new_crumb()

      def new_session(self):
            self.session = None

      def new_crumb(self):
            self.crumb = "[TestCrumb]"


if __name__=="__main__":
      unittest.main()