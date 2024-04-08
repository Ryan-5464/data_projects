from company_financials_stock_price_analysis.financial_scraper.request_objects.IRequestObject import IRequest


class YahooFinanceRequestObject(IRequestObject):

      def __init__(
                  self, 
                  base_url: str,
                  referer: str,
                  fields: list[str],
                  #crumb=None
      ):
            self._base_url = base_url
            self._referer = referer
            self._fields = fields
            #self._crumb = crumb

      def url(self, ticker: str) -> str:
            BASE_URL = self._base_url.replace("[TICKER]", ticker)
            #if self._crumb == None:
            REQUEST_PARAMETERS = self.__format_request_parameters(ticker)
            #if self._crumb != None:
                  #REQUEST_PARAMETERS = self.__format_request_parameters_with_crumb(ticker)
            REQUEST_URL = f"{BASE_URL}?{REQUEST_PARAMETERS}"
            print(f"REQUEST_URL: {REQUEST_URL}")
            return REQUEST_URL

      def __format_request_parameters(self, ticker: str) -> str:
            PARAMETERISED_FIELDS = ""
            for FIELD in self._fields:
                  PARAMETERISED_FIELDS += f"{FIELD}%2C"
            PARAMETERISED_FIELDS = PARAMETERISED_FIELDS[:-3]
            URL_PARAMETERS = f"lang=en-GB&region=GB&symbol={ticker}&padTimeSeries=true&type={PARAMETERISED_FIELDS}&merge=false&period1=0&period2=3000000000&corsDomain=uk.finance.yahoo.com"
            return URL_PARAMETERS

      #def __format_request_parameters(self, ticker: str) -> str:
            #PARAMETERISED_FIELDS = ""
            #for FIELD in self._fields:
                  #PARAMETERISED_FIELDS += f"{FIELD}%2C"
            #PARAMETERISED_FIELDS = PARAMETERISED_FIELDS[:-3]
            #URL_PARAMETERS = f"lang=en-GB&region=GB&symbol={ticker}&padTimeSeries=true&modules={PARAMETERISED_FIELDS}&merge=false&period1=0&period2=3000000000&corsDomain=uk.finance.yahoo.com"
            #return URL_PARAMETERS
      
      def headers(self, ticker: str) -> dict:
            headers = {
                  "Accept": "*/*",
                  "Accept-Encoding": "gzip, deflate, br, zstd",
                  "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
                  "Origin": "https://uk.finance.yahoo.com",
                  "Referer": self._referer.replace("[TICKER]", ticker),
                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
            }
            return headers

      def _payload(self):
            return

      def _proxies(self):
            return


class YahooFinanceRequestObjectFactory():

      ANNUAL_BALANCE_SHEET_BASE_URL = "https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries"
      ANNUAL_BALANCE_SHEET_REFERER = "https://uk.finance.yahoo.com/quote/[TICKER]/balance-sheet"
      ANNUAL_BALANCE_SHEET_FIELDS = ['annualTotalAssets', 'trailingTotalAssets', 'annualStockholdersEquity', 'trailingStockholdersEquity', 'annualGainsLossesNotAffectingRetainedEarnings', 'trailingGainsLossesNotAffectingRetainedEarnings', 'annualRetainedEarnings', 'trailingRetainedEarnings', 'annualCapitalStock', 'trailingCapitalStock', 'annualTotalLiabilitiesNetMinorityInterest', 'trailingTotalLiabilitiesNetMinorityInterest', 'annualTotalNonCurrentLiabilitiesNetMinorityInterest', 'trailingTotalNonCurrentLiabilitiesNetMinorityInterest', 'annualOtherNonCurrentLiabilities', 'trailingOtherNonCurrentLiabilities', 'annualNonCurrentDeferredRevenue', 'trailingNonCurrentDeferredRevenue', 'annualNonCurrentDeferredTaxesLiabilities', 'trailingNonCurrentDeferredTaxesLiabilities', 'annualLongTermDebt', 'trailingLongTermDebt', 'annualCurrentLiabilities', 'trailingCurrentLiabilities', 'annualOtherCurrentLiabilities', 'trailingOtherCurrentLiabilities', 'annualCurrentDeferredRevenue', 'trailingCurrentDeferredRevenue', 'annualCurrentAccruedExpenses', 'trailingCurrentAccruedExpenses', 'annualIncomeTaxPayable', 'trailingIncomeTaxPayable', 'annualAccountsPayable', 'trailingAccountsPayable', 'annualCurrentDebt', 'trailingCurrentDebt', 'annualTotalNonCurrentAssets', 'trailingTotalNonCurrentAssets', 'annualOtherNonCurrentAssets', 'trailingOtherNonCurrentAssets', 'annualOtherIntangibleAssets', 'trailingOtherIntangibleAssets', 'annualGoodwill', 'trailingGoodwill', 'annualInvestmentsAndAdvances', 'trailingInvestmentsAndAdvances', 'annualNetPPE', 'trailingNetPPE', 'annualAccumulatedDepreciation', 'trailingAccumulatedDepreciation', 'annualGrossPPE', 'trailingGrossPPE', 'annualCurrentAssets', 'trailingCurrentAssets', 'annualOtherCurrentAssets', 'trailingOtherCurrentAssets', 'annualInventory', 'trailingInventory', 'annualAccountsReceivable', 'trailingAccountsReceivable', 'annualCashCashEquivalentsAndShortTermInvestments', 'trailingCashCashEquivalentsAndShortTermInvestments', 'annualOtherShortTermInvestments', 'trailingOtherShortTermInvestments', 'annualCashAndCashEquivalents', 'trailingCashAndCashEquivalents']

      QUARTERLY_BALANCE_SHEET_BASE_URL = "https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries"
      QUARTERLY_BALANCE_SHEET_REFERER = "https://uk.finance.yahoo.com/quote/[TICKER]/balance-sheet"
      QUARTERLY_BALANCE_SHEET_FIELDS = ['annualTotalAssets', 'trailingTotalAssets', 'annualStockholdersEquity', 'trailingStockholdersEquity', 'annualGainsLossesNotAffectingRetainedEarnings', 'trailingGainsLossesNotAffectingRetainedEarnings', 'annualRetainedEarnings', 'trailingRetainedEarnings', 'annualCapitalStock', 'trailingCapitalStock', 'annualTotalLiabilitiesNetMinorityInterest', 'trailingTotalLiabilitiesNetMinorityInterest', 'annualTotalNonCurrentLiabilitiesNetMinorityInterest', 'trailingTotalNonCurrentLiabilitiesNetMinorityInterest', 'annualOtherNonCurrentLiabilities', 'trailingOtherNonCurrentLiabilities', 'annualNonCurrentDeferredRevenue', 'trailingNonCurrentDeferredRevenue', 'annualNonCurrentDeferredTaxesLiabilities', 'trailingNonCurrentDeferredTaxesLiabilities', 'annualLongTermDebt', 'trailingLongTermDebt', 'annualCurrentLiabilities', 'trailingCurrentLiabilities', 'annualOtherCurrentLiabilities', 'trailingOtherCurrentLiabilities', 'annualCurrentDeferredRevenue', 'trailingCurrentDeferredRevenue', 'annualCurrentAccruedExpenses', 'trailingCurrentAccruedExpenses', 'annualIncomeTaxPayable', 'trailingIncomeTaxPayable', 'annualAccountsPayable', 'trailingAccountsPayable', 'annualCurrentDebt', 'trailingCurrentDebt', 'annualTotalNonCurrentAssets', 'trailingTotalNonCurrentAssets', 'annualOtherNonCurrentAssets', 'trailingOtherNonCurrentAssets', 'annualOtherIntangibleAssets', 'trailingOtherIntangibleAssets', 'annualGoodwill', 'trailingGoodwill', 'annualInvestmentsAndAdvances', 'trailingInvestmentsAndAdvances', 'annualNetPPE', 'trailingNetPPE', 'annualAccumulatedDepreciation', 'trailingAccumulatedDepreciation', 'annualGrossPPE', 'trailingGrossPPE', 'annualCurrentAssets', 'trailingCurrentAssets', 'annualOtherCurrentAssets', 'trailingOtherCurrentAssets', 'annualInventory', 'trailingInventory', 'annualAccountsReceivable', 'trailingAccountsReceivable', 'annualCashCashEquivalentsAndShortTermInvestments', 'trailingCashCashEquivalentsAndShortTermInvestments', 'annualOtherShortTermInvestments', 'trailingOtherShortTermInvestments', 'annualCashAndCashEquivalents', 'trailingCashAndCashEquivalents']

      ANNUAL_CASH_FLOW_BASE_URL = "https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries/"
      ANNUAL_CASH_FLOW_REFERER = "https://uk.finance.yahoo.com/quote/[TICKER]/cash-flow"
      ANNUAL_CASH_FLOW_FIELDS = ['annualFreeCashFlow', 'trailingFreeCashFlow', 'annualCapitalExpenditure', 'trailingCapitalExpenditure', 'annualOperatingCashFlow', 'trailingOperatingCashFlow', 'annualEndCashPosition', 'trailingEndCashPosition', 'annualBeginningCashPosition', 'trailingBeginningCashPosition', 'annualChangeInCashSupplementalAsReported', 'trailingChangeInCashSupplementalAsReported', 'annualCashFlowFromContinuingFinancingActivities', 'trailingCashFlowFromContinuingFinancingActivities', 'annualNetOtherFinancingCharges', 'trailingNetOtherFinancingCharges', 'annualCashDividendsPaid', 'trailingCashDividendsPaid', 'annualRepurchaseOfCapitalStock', 'trailingRepurchaseOfCapitalStock', 'annualCommonStockIssuance', 'trailingCommonStockIssuance', 'annualRepaymentOfDebt', 'trailingRepaymentOfDebt', 'annualInvestingCashFlow', 'trailingInvestingCashFlow', 'annualNetOtherInvestingChanges', 'trailingNetOtherInvestingChanges', 'annualSaleOfInvestment', 'trailingSaleOfInvestment', 'annualPurchaseOfInvestment', 'trailingPurchaseOfInvestment', 'annualPurchaseOfBusiness', 'trailingPurchaseOfBusiness', 'annualOtherNonCashItems', 'trailingOtherNonCashItems', 'annualChangeInAccountPayable', 'trailingChangeInAccountPayable', 'annualChangeInInventory', 'trailingChangeInInventory', 'annualChangesInAccountReceivables', 'trailingChangesInAccountReceivables', 'annualChangeInWorkingCapital', 'trailingChangeInWorkingCapital', 'annualStockBasedCompensation', 'trailingStockBasedCompensation', 'annualDeferredIncomeTax', 'trailingDeferredIncomeTax', 'annualDepreciationAndAmortization', 'trailingDepreciationAndAmortization', 'annualNetIncome', 'trailingNetIncome']

      QUARTERLY_CASH_FLOW_BASE_URL = "https://query2.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries"
      QUARTERLY_CASH_FLOW_REFERER = "https://uk.finance.yahoo.com/quote/[TICKER]/cash-flow"
      QUARTERLY_CASH_FLOW_FIELDS = ['quarterlyFreeCashFlow', 'trailingFreeCashFlow', 'quarterlyCapitalExpenditure', 'trailingCapitalExpenditure', 'quarterlyOperatingCashFlow', 'trailingOperatingCashFlow', 'quarterlyEndCashPosition', 'trailingEndCashPosition', 'quarterlyBeginningCashPosition', 'trailingBeginningCashPosition', 'quarterlyChangeInCashSupplementalAsReported', 'trailingChangeInCashSupplementalAsReported', 'quarterlyCashFlowFromContinuingFinancingActivities', 'trailingCashFlowFromContinuingFinancingActivities', 'quarterlyNetOtherFinancingCharges', 'trailingNetOtherFinancingCharges', 'quarterlyCashDividendsPaid', 'trailingCashDividendsPaid', 'quarterlyRepurchaseOfCapitalStock', 'trailingRepurchaseOfCapitalStock', 'quarterlyCommonStockIssuance', 'trailingCommonStockIssuance', 'quarterlyRepaymentOfDebt', 'trailingRepaymentOfDebt', 'quarterlyInvestingCashFlow', 'trailingInvestingCashFlow', 'quarterlyNetOtherInvestingChanges', 'trailingNetOtherInvestingChanges', 'quarterlySaleOfInvestment', 'trailingSaleOfInvestment', 'quarterlyPurchaseOfInvestment', 'trailingPurchaseOfInvestment', 'quarterlyPurchaseOfBusiness', 'trailingPurchaseOfBusiness', 'quarterlyOtherNonCashItems', 'trailingOtherNonCashItems', 'quarterlyChangeInAccountPayable', 'trailingChangeInAccountPayable', 'quarterlyChangeInInventory', 'trailingChangeInInventory', 'quarterlyChangesInAccountReceivables', 'trailingChangesInAccountReceivables', 'quarterlyChangeInWorkingCapital', 'trailingChangeInWorkingCapital', 'quarterlyStockBasedCompensation', 'trailingStockBasedCompensation', 'quarterlyDeferredIncomeTax', 'trailingDeferredIncomeTax', 'quarterlyDepreciationAndAmortization', 'trailingDepreciationAndAmortization', 'quarterlyNetIncome', 'trailingNetIncome']

      ANNUAL_INCOME_STATEMENT_BASE_URL = "https://query2.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries/"
      ANNUAL_INCOME_STATEMENT_REFERER = "https://uk.finance.yahoo.com/quote/[TICKER]/financials"
      ANNUAL_INCOME_STATEMENT_FIELDS = ['annualEbitda', 'trailingEbitda', 'annualDilutedAverageShares', 'trailingDilutedAverageShares', 'annualBasicAverageShares', 'trailingBasicAverageShares', 'annualDilutedEPS', 'trailingDilutedEPS', 'annualBasicEPS', 'trailingBasicEPS', 'annualNetIncomeCommonStockholders', 'trailingNetIncomeCommonStockholders', 'annualNetIncome', 'trailingNetIncome', 'annualNetIncomeContinuousOperations', 'trailingNetIncomeContinuousOperations', 'annualTaxProvision', 'trailingTaxProvision', 'annualPretaxIncome', 'trailingPretaxIncome', 'annualOtherIncomeExpense', 'trailingOtherIncomeExpense', 'annualInterestExpense', 'trailingInterestExpense', 'annualOperatingIncome', 'trailingOperatingIncome', 'annualOperatingExpense', 'trailingOperatingExpense', 'annualSellingGeneralAndAdministration', 'trailingSellingGeneralAndAdministration', 'annualResearchAndDevelopment', 'trailingResearchAndDevelopment', 'annualGrossProfit', 'trailingGrossProfit', 'annualCostOfRevenue', 'trailingCostOfRevenue', 'annualTotalRevenue', 'trailingTotalRevenue']

      QUARTERLY_INCOME_STATEMENT_BASE_URL = "https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries/"
      QUARTERLY_INCOME_STATEMENT_REFERER = "https://uk.finance.yahoo.com/quote/[TICKER]/financials"
      QUARTERLY_INCOME_STATEMENT_FIELDS = ['quarterlyEbitda', 'trailingEbitda', 'quarterlyDilutedAverageShares', 'trailingDilutedAverageShares', 'quarterlyBasicAverageShares', 'trailingBasicAverageShares', 'quarterlyDilutedEPS', 'trailingDilutedEPS', 'quarterlyBasicEPS', 'trailingBasicEPS', 'quarterlyNetIncomeCommonStockholders', 'trailingNetIncomeCommonStockholders', 'quarterlyNetIncome', 'trailingNetIncome', 'quarterlyNetIncomeContinuousOperations', 'trailingNetIncomeContinuousOperations', 'quarterlyTaxProvision', 'trailingTaxProvision', 'quarterlyPretaxIncome', 'trailingPretaxIncome', 'quarterlyOtherIncomeExpense', 'trailingOtherIncomeExpense', 'quarterlyInterestExpense', 'trailingInterestExpense', 'quarterlyOperatingIncome', 'trailingOperatingIncome', 'quarterlyOperatingExpense', 'trailingOperatingExpense', 'quarterlySellingGeneralAndAdministration', 'trailingSellingGeneralAndAdministration', 'quarterlyResearchAndDevelopment', 'trailingResearchAndDevelopment', 'quarterlyGrossProfit', 'trailingGrossProfit', 'quarterlyCostOfRevenue', 'trailingCostOfRevenue', 'quarterlyTotalRevenue', 'trailingTotalRevenue']

      STATISTICS_BASE_URL = "https://query2.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries/"
      STATISTICS_REFERER = "https://uk.finance.yahoo.com/quote/[TICKER]/key-statistics"
      STATISTICS_FIELDS = ['quarterlyMarketCap', 'trailingMarketCap', 'quarterlyEnterpriseValue', 'trailingEnterpriseValue', 'quarterlyPeRatio', 'trailingPeRatio', 'quarterlyForwardPeRatio', 'trailingForwardPeRatio', 'quarterlyPegRatio', 'trailingPegRatio', 'quarterlyPsRatio', 'trailingPsRatio', 'quarterlyPbRatio', 'trailingPbRatio', 'quarterlyEnterprisesValueRevenueRatio', 'trailingEnterprisesValueRevenueRatio', 'quarterlyEnterprisesValueEBITDARatio', 'trailingEnterprisesValueEBITDARatio']

      #ANALYSIS_BASE_URL = "https://query1.finance.yahoo.com/v10/finance/quoteSummary/[TICKER]"
      #ANALYSIS_REFERER = "https://uk.finance.yahoo.com/quote/[TICKER]/analysis"
      #ANALYSIS_FIELDS = ['upgradeDowngradeHistory', 'recommendationTrend', 'financialData', 'earningsHistory', 'earningsTrend', 'industryTrend', 'indexTrend', 'sectorTrend']
      #ANALYSIS_CRUMB = "45WGS5sXKp6"
      #analysis_formatted = "true"

      @classmethod
      def make_request_object(cls, ticker:str, request_object_type:str) -> YahooFinanceRequestObject:
            match request_object_type:
                  case "annual_balance_sheet":
                        request_object = YahooFinanceRequestObject(
                              ticker, 
                              cls.ANNUAL_BALANCE_SHEET_BASE_URL, 
                              cls.ANNUAL_BALANCE_SHEET_REFERER, 
                              cls.ANNUAL_BALANCE_SHEET_FIELDS
                        )
                  case "quarterly_balance_sheet":
                        request_object = YahooFinanceRequestObject(
                              ticker, 
                              cls.QUARTERLY_BALANCE_SHEET_BASE_URL, 
                              cls.QUARTERLY_BALANCE_SHEET_REFERER, 
                              cls.QUARTERLY_BALANCE_SHEET_FIELDS
                        )
                  case "annual_cash_flow":
                        request_object = YahooFinanceRequestObject(
                              ticker, 
                              cls.ANNUAL_CASH_FLOW_BASE_URL, 
                              cls.ANNUAL_CASH_FLOW_REFERER, 
                              cls.ANNUAL_CASH_FLOW_FIELDS
                        )
                  case "quarterly_cash_flow":
                        request_object = YahooFinanceRequestObject(
                              ticker, 
                              cls.QUARTERLY_CASH_FLOW_BASE_URL, 
                              cls.QUARTERLY_CASH_FLOW_REFERER, 
                              cls.QUARTERLY_CASH_FLOW_FIELDS
                        )
                  case "annual_income_statement":
                        request_object = YahooFinanceRequestObject(
                              ticker, 
                              cls.ANNUAL_INCOME_STATEMENT_BASE_URL, 
                              cls.ANNUAL_INCOME_STATEMENT_REFERER, 
                              cls.ANNUAL_INCOME_STATEMENT_FIELDS
                        )
                  case "quarterly_income_statement":
                        request_object = YahooFinanceRequestObject(
                              ticker, 
                              cls.QUARTERLY_INCOME_STATEMENT_BASE_URL, 
                              cls.QUARTERLY_INCOME_STATEMENT_REFERER, 
                              cls.QUARTERLY_INCOME_STATEMENT_FIELDS
                        )
                  case "ANALYSIS":
                        request_object = YahooFinanceRequestObject(
                              ticker, 
                              cls.STATISTICS_BASE_URL, 
                              cls.STATISTICS_REFERER, 
                              cls.STATISTICS_FIELDS
                        )
                  #case "analysis":
                        #request_object = YahooFinanceRequestObject(
                              #ticker, 
                              #cls.ANALYSIS_BASE_URL, 
                              #cls.ANALYSIS_REFERER, 
                              #cls.ANALYSIS_FIELDS,
                              #cls.ANALYSIS_CRUMB,
                        #)
            return request_object


