from company_financials_stock_price_analysis.financial_scraper.request_objects.IRequestObject import IRequest


class RequestQuarterlyBalanceSheet(IRequest):

      FIELDS = [
            "quarterlyTotalAssets",
            "trailingTotalAssets",
            "quarterlyStockholdersEquity",
            "trailingStockholdersEquity",
            "quarterlyGainsLossesNotAffectingRetainedEarnings",
            "trailingGainsLossesNotAffectingRetainedEarnings",
            "quarterlyRetainedEarnings",
            "trailingRetainedEarnings",
            "quarterlyCapitalStock",
            "trailingCapitalStock",
            "quarterlyTotalLiabilitiesNetMinorityInterest",
            "trailingTotalLiabilitiesNetMinorityInterest",
            "quarterlyTotalNonCurrentLiabilitiesNetMinorityInterest",
            "trailingTotalNonCurrentLiabilitiesNetMinorityInterest",
            "quarterlyOtherNonCurrentLiabilities",
            "trailingOtherNonCurrentLiabilities",
            "quarterlyNonCurrentDeferredRevenue",
            "trailingNonCurrentDeferredRevenue",
            "quarterlyNonCurrentDeferredTaxesLiabilities",
            "trailingNonCurrentDeferredTaxesLiabilities",
            "quarterlyLongTermDebt",
            "trailingLongTermDebt",
            "quarterlyCurrentLiabilities",
            "trailingCurrentLiabilities",
            "quarterlyOtherCurrentLiabilities",
            "trailingOtherCurrentLiabilities",
            "quarterlyCurrentDeferredRevenue",
            "trailingCurrentDeferredRevenue",
            "quarterlyCurrentAccruedExpenses",
            "trailingCurrentAccruedExpenses",
            "quarterlyIncomeTaxPayable",
            "trailingIncomeTaxPayable",
            "quarterlyAccountsPayable",
            "trailingAccountsPayable",
            "quarterlyCurrentDebt",
            "trailingCurrentDebt",
            "quarterlyTotalNonCurrentAssets",
            "trailingTotalNonCurrentAssets",
            "quarterlyOtherNonCurrentAssets",
            "trailingOtherNonCurrentAssets",
            "quarterlyOtherIntangibleAssets",
            "trailingOtherIntangibleAssets",
            "quarterlyGoodwill",
            "trailingGoodwill",
            "quarterlyInvestmentsAndAdvances",
            "trailingInvestmentsAndAdvances",
            "quarterlyNetPPE",
            "trailingNetPPE",
            "quarterlyAccumulatedDepreciation",
            "trailingAccumulatedDepreciation",
            "quarterlyGrossPPE",
            "trailingGrossPPE",
            "quarterlyCurrentAssets",
            "trailingCurrentAssets",
            "quarterlyOtherCurrentAssets",
            "trailingOtherCurrentAssets",
            "quarterlyInventory",
            "trailingInventory",
            "quarterlyAccountsReceivable",
            "trailingAccountsReceivable",
            "quarterlyCashCashEquivalentsAndShortTermInvestments",
            "trailingCashCashEquivalentsAndShortTermInvestments",
            "quarterlyOtherShortTermInvestments",
            "trailingOtherShortTermInvestments",
            "quarterlyCashAndCashEquivalents",
            "trailingCashAndCashEquivalents"  
      ]

      def __init__(
                  self, 
                  ticker: str, 
      ):
            self.ticker = ticker
            self.headers = self._headers(ticker)
            self.payload = self._payload()
            self.proxies = self._proxies()
            self.url = self._url(ticker)

      @classmethod
      def _url(cls, ticker: str) -> str:
            BASE_URL = f"https://query2.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries/{ticker}"
            REQUEST_PARAMETERS = cls.__format_request_parameters(ticker)
            REQUEST_URL = f"{BASE_URL}?{REQUEST_PARAMETERS}"
            print(f"REQUEST_URL: {REQUEST_URL}")
            return REQUEST_URL

      @classmethod
      def __format_request_parameters(cls, ticker: str) -> str:
            PARAMETERISED_FIELDS = ""
            for FIELD in cls.FIELDS:
                  PARAMETERISED_FIELDS += f"{FIELD}%2C"
            PARAMETERISED_FIELDS = PARAMETERISED_FIELDS[:-3]
            URL_PARAMETERS = f"lang=en-GB&region=GB&symbol={ticker}&padTimeSeries=true&type={PARAMETERISED_FIELDS}&merge=false&period1=0&period2=3000000000&corsDomain=uk.finance.yahoo.com"
            return URL_PARAMETERS
      
      @classmethod
      def _headers(cls, ticker: str) -> dict:
            headers = {
                  "Accept": "*/*",
                  "Accept-Encoding": "gzip, deflate, br, zstd",
                  "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
                  "Origin": "https://uk.finance.yahoo.com",
                  "Referer": f"https://uk.finance.yahoo.com/quote/{ticker}/financials",
                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
            }
            return headers

      @classmethod
      def _payload(cls):
            return

      @classmethod
      def _proxies(cls):
            return
