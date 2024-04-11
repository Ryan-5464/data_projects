from coding.github.personal.data_projects.company_financials_stock_price_analysis.interfaces.IRequestFactory import IRequestFactory
from coding.github.personal.data_projects.company_financials_stock_price_analysis.interfaces.IRequestHandler import IRequestHandler
from coding.github.personal.data_projects.company_financials_stock_price_analysis.interfaces.ISessionHandler import ISessionHandler
from coding.github.personal.data_projects.company_financials_stock_price_analysis.financial_scraper.handlers.YFRequestHandler import YFRequestHandler
import requests



class YFRequestFactory(IRequestFactory):

      HEADERS = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Origin": "https://uk.finance.yahoo.com",
            "Referer": "[REFERER]",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
      }

      URL_PARAMETERS_FINANCIALS = f"lang=en-GB&region=GB&symbol=[TICKER]&padTimeSeries=true&type=[PARAMETERISED_FIELDS]&merge=false&period1=0&period2=3000000000&corsDomain=uk.finance.yahoo.com"
      URL_PARAMETERS_ANALYSIS = f"formatted=true&crumb=[CRUMB]&lang=en-GB&region=GB&modules=[PARAMETERISED_FIELDS]&symbol=[TICKER]&corsDomain=uk.finance.yahoo.com"

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

      ANALYSIS_BASE_URL = "https://query1.finance.yahoo.com/v10/finance/quoteSummary/[TICKER]"
      ANALYSIS_REFERER = "https://uk.finance.yahoo.com/quote/[TICKER]/analysis"
      ANALYSIS_FIELDS = ['upgradeDowngradeHistory', 'recommendationTrend', 'financialData', 'earningsHistory', 'earningsTrend', 'industryTrend', 'indexTrend', 'sectorTrend']

      @classmethod
      def make_request_object(cls, session_handler:ISessionHandler, request_object_type:str) -> IRequestHandler:

            match request_object_type:
                  case "annual_balance_sheet":

                        request_object = YFRequestHandler(
                              session_handler = session_handler,
                              url=cls.__url(
                                    base_url=cls.ANNUAL_BALANCE_SHEET_BASE_URL, 
                                    fields=cls.ANNUAL_BALANCE_SHEET_FIELDS, 
                                    parameters=cls.URL_PARAMETERS_FINANCIALS
                              ), 
                              headers=cls.__headers(
                                    headers=cls.HEADERS, 
                                    referer=cls.ANNUAL_BALANCE_SHEET_REFERER
                              ), 
                        )

                  case "quarterly_balance_sheet":

                        request_object = YFRequestHandler(
                              session_handler = session_handler,
                              url=cls.__url(
                                    base_url=cls.QUARTERLY_BALANCE_SHEET_BASE_URL, 
                                    fields=cls.QUARTERLY_BALANCE_SHEET_FIELDS, 
                                    parameters=cls.URL_PARAMETERS_FINANCIALS
                              ), 
                              headers=cls.__headers(
                                    headers=cls.HEADERS, 
                                    referer=cls.QUARTERLY_BALANCE_SHEET_REFERER
                              ), 
                        )

                  case "annual_cash_flow":

                        request_object = YFRequestHandler(
                              session_handler = session_handler,
                              url=cls.__url(
                                    base_url=cls.ANNUAL_CASH_FLOW_BASE_URL, 
                                    fields=cls.ANNUAL_CASH_FLOW_FIELDS, 
                                    parameters=cls.URL_PARAMETERS_FINANCIALS
                              ), 
                              headers=cls.__headers(
                                    headers=cls.HEADERS, 
                                    referer=cls.ANNUAL_CASH_FLOW_REFERER
                              ), 
                        )

                  case "quarterly_cash_flow":

                        request_object = YFRequestHandler(
                              session_handler = session_handler,
                              url=cls.__url(
                                    base_url=cls.QUARTERLY_CASH_FLOW_BASE_URL, 
                                    fields=cls.QUARTERLY_CASH_FLOW_FIELDS, 
                                    parameters=cls.URL_PARAMETERS_FINANCIALS
                              ), 
                              headers=cls.__headers(
                                    headers=cls.HEADERS, 
                                    referer=cls.QUARTERLY_CASH_FLOW_REFERER
                              ), 
                        )

                  case "annual_income_statement":

                        request_object = YFRequestHandler(
                              session_handler = session_handler,
                              url=cls.__url(
                                    base_url=cls.ANNUAL_INCOME_STATEMENT_BASE_URL, 
                                    fields=cls.ANNUAL_INCOME_STATEMENT_FIELDS, 
                                    parameters=cls.URL_PARAMETERS_FINANCIALS
                              ), 
                              headers=cls.__headers(
                                    headers=cls.HEADERS, 
                                    referer=cls.ANNUAL_INCOME_STATEMENT_REFERER
                              ), 
                        )

                  case "quarterly_income_statement":

                        request_object = YFRequestHandler(
                              session_handler = session_handler,
                              url=cls.__url(
                                    base_url=cls.QUARTERLY_INCOME_STATEMENT_BASE_URL, 
                                    fields=cls.QUARTERLY_INCOME_STATEMENT_FIELDS, 
                                    parameters=cls.URL_PARAMETERS_FINANCIALS
                              ), 
                              headers=cls.__headers(
                                    headers=cls.HEADERS, 
                                    referer=cls.QUARTERLY_INCOME_STATEMENT_REFERER
                              ), 
                        )

                  case "statistics":

                        request_object = YFRequestHandler(
                              session_handler = session_handler,
                              url=cls.__url(
                                    base_url=cls.STATISTICS_BASE_URL, 
                                    fields=cls.STATISTICS_FIELDS, 
                                    parameters=cls.URL_PARAMETERS_FINANCIALS
                              ), 
                              headers=cls.__headers(
                                    headers=cls.HEADERS, 
                                    referer=cls.STATISTICS_REFERER
                              ), 
                        )

                  case "analysis":

                        request_object = YFRequestHandler(
                              session_handler = session_handler,
                              url=cls.__url(
                                    base_url=cls.ANALYSIS_BASE_URL, 
                                    fields=cls.ANALYSIS_FIELDS, 
                                    parameters=cls.URL_PARAMETERS_ANALYSIS
                              ), 
                              headers=cls.__headers(
                                    headers=cls.HEADERS, 
                                    referer=cls.ANALYSIS_REFERER
                              ), 
                        )

            return request_object

      @classmethod
      def __headers(cls, headers, referer) -> dict:
            headers["Referer"] = referer
            return headers

      @classmethod
      def __url(cls, base_url, fields, parameters) -> str:
            parameterised_fields = ""
            for FIELD in fields:
                  parameterised_fields += f"{FIELD}%2C"
            parameterised_fields = parameterised_fields[:-3]
            request_parameters = parameters.replace("[PARAMETERISED_FIELDS]", parameterised_fields)
            request_url = f"{base_url}?{request_parameters}"
            print(f"REQUEST_URL: {request_url}")
            return request_url



