from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests


class SessionHandler(ABC):

    @abstractmethod
    def new_session():
        NotImplementedError

class RequestHandler(ABC):

    @abstractmethod
    def request_data():
        NotImplementedError

class SaveHandler(ABC):

    @abstractmethod
    def save():
        NotImplementedError

class S3SaveHandler(SaveHandler):

    def save():
        pass

class PostgresSaveHandler(SaveHandler):

    def save():
        pass

class LocalSaveHandler(SaveHandler):

    def save():
        pass

class YahooFinanceSessionHandler(SessionHandler):

    def __init__(self):
        self.session = None
    
    def new_session(self):
        self.session = requests.Session()
        requests.utils.add_dict_to_cookiejar(self.session.cookies, self.__get_site_cookies())
        return
        
    @staticmethod
    def __get_site_cookies():
        driver = webdriver.Chrome()
        driver.get("https://uk.finance.yahoo.com/")
        button = driver.find_element(by=By.CLASS_NAME, value="btn.secondary.accept-all")
        button.click()
        all_cookies=driver.get_cookies();
        cookies_dict = {}
        for cookie in all_cookies:
                cookies_dict[cookie['name']] = cookie['value']
        return cookies_dict

session_handler = SessionHandler()
session_handler.new_session()

class YahooFinanceRequestHandler(RequestHandler):

    def __init__(self):
        self.response = None

    def request_data(self, request_object: APIRequest, session_handler: SessionHandler, retries=1, max_retries=10):
            if retries >= max_retries:
                print(f"REQUEST FAILED :: aborting request.")
                return     
            if session == None:
                request_object.session = session_handler.new_session()   
            response = request_object.request_data()
            if response.status_code != 200:
                print(f"REQUEST FAILED :: STATUS CODE: {response.status_code} :: RETRIES : {retries}")
                retries += 1
                session = session_handler.new_session()
                self.request_data(request_object, session_handler, retries)
            else:
                self.response = response
            return

class YahooFinanceRequestStatistics(APIRequest):

    def request_data(self):
        pass

class YahooFinanceRequestAnalysis(APIRequest):

    def request_data(self):
        pass

class YahoooFinanceRequestIncomeStatement(APIRequest):

    def request_data(self):
        pass

class YahooFinanceRequestCashFlow(APIRequest):

    def request_data(self):
        pass




class CompanyStatistics:
    def __init__(self):
        valuation_measures = ValuationMeasures()
        financial_highlights = FinancialHighlights()
        financial_summary = FinancialsSummary()
        stock_price_history = StockPriceHistory()
        share_statistics = ShareStatistics()
        dividends_and_splits = DividendsAndSplits()

class Financials:
    def __init__(self):
        balance_sheet = BalanceSheet()
        income_statement = IncomeStatement()
        cash_flow = CashFlow()

class Analysis:
    def __init__(self):
        earnings_estimate = EarningsEstimate()
        revenue_estimate = RevenueEstimate()
        earnings_history = EarningHistory()
        eps_trend = EpsTrend()
        eps_revisions = EpsRevisions()
        growth_estimates = GrowthEstimates()

class ValuationMeasures:
    def __init__(self):
        market_cap = None
        enterprise_value = None
        trailing_pe = None
        forward_pe = None
        peg_ratio = None
        price_sales = None
        price_book = None
        enterprise_value_revenue = None
        enterprise_value_ebitda = None

class FinancialHighlights:
    def __init__(self):
        fiscal_year_ends = None
        most_recent_quarter = None
        profit_margin = None
        operating_margin = None
        return_on_assets = None
        return_on_equity = None

class FinancialsSummary:
    def __init__(self):
        revenue = None
        revenue_per_share = None
        quarterly_revenue_growth = None
        gross_profit = None
        ebitda = None
        net_income_avi_to_common = None
        diluted_eps = None
        quarterly_earnings_growth = None
        total_cash = None
        total_cash_share = None
        total_debt = None
        total_debt_equity = None
        current_ratio = None
        book_value_per_share = None
        operating_cash_flow = None
        levered_free_cash_flow = None

class StockPriceHistory:
    def __init__(self):
        beta = None
        delta_52week = None
        snp500_delta_52week = None
        high_52week = None
        low_52week = None
        moving_ave_50day = None
        moving_ave_200day = None

class ShareStatistics:
    def __init__(self):
        ave_vol_3month = None
        ave_vol_10day = None
        shares_outstanding = None
        implied_shares_outstanding = None
        float = None
        pc_held_by_insiders = None
        pc_held_by_institutions = None
        shares_short = None
        short_ratio = None
        short_pc_of_float = None
        short_pc_of_shares_outstanding = None
        shares_short = None

class DividendsAndSplits:
    def __init__(self):
        forward_annual_dividend_rate = None
        forward_annual_dividend_yield = None
        trailing_annual_dividend_rate = None
        trailing_annual_dividend_yield = None
        dividend_yield_5year_ave = None
        payout_ratio = None
        dividend_rate = None
        ex_dividend_date = None
        last_split_factor = None
        last_split_date = None

class IncomeStatement:
    def __init__(self):
        total_revenue = None
        cost_of_revenue = None
        gross_profit = None
        research_development = None
        selling_general_n_admin = None
        total_operating_expenses = None
        operating_income_or_loss = None
        interest_expense = None
        total_other_income_expenses_net = None
        income_before_tax = None
        income_tax_expense = None
        income_from_continuing_operations = None
        net_income = None
        net_income_available_to_common_shareholders = None
        basic_eps = None
        diluted_eps = None
        basic_average_shares = None
        diluted_average_shares = None
        date = None
        annual = None

class BalanceSheet:
    def __init__(self):
        cash_n_cash_equivalents = None
        other_short_term_investments = None
        total_cash = None
        net_recievables = None
        inventory = None
        other_current_assets = None
        total_current_assets = None
        gross_property_plant_n_equipment = None
        accumulated_depreciation = None
        net_property_plant_n_equipment = None
        goodwill = None
        intangible_assets = None
        other_long_term_assets = None
        total_non_current_assets = None
        total_assets = None
        current_debt = None
        accounts_payable = None
        accrued_liabilities = None
        deferred_revenues = None
        other_current_liabilities = None
        total_current_liabilities = None
        long_term_debt = None
        deferred_tx_laibilities = None
        deferred_revenues = None
        other_long_term_liabilities = None
        total_non_current_liabilities = None
        total_liabilities = None
        common_stock = None
        retained_earnings = None
        accumulated_other_comprehensive_income = None
        total_stockholder_equity = None
        total_liabilities_and_stockholders_equity = None
        date = None
        annual = None

class CashFlow:
    def __init__(self):
        net_income = None
        deprication_n_amortisation = None
        deferred_income_taxes = None
        stock_based_compensation = None
        change_in_working_capital = None
        accounts_receivable = None
        inventory = None
        accounts_payable = None
        other_working_capital = None
        other_non_cash_items = None
        net_cash_provided_by_operating_activities = None
        investments_in_property_plant_n_equipment = None
        acquisitions_net = None
        purchases_of_investments = None
        sales_maturities_of_investments = None
        other_investing_activities = None
        net_cash_used_for_investing_activities = None
        debt_repayment = None
        common_stock_issued = None
        other_financing_activities = None
        net_cash_provided_by_used_for_financing_activities = None
        net_change_in_cash = None
        cash_at_beginning_of_period = None
        cash_at_end_of_period = None
        operating_cash_flow = None
        capital_expenditure = None
        free_Cash_flow = None
        date = None
        annual = None

class EarningsEstimate:
    def __init__(self):
        no_of_analysts = None
        ave_estimate = None
        low_estimate = None
        high_estimate = None
        year_ago_eps = None
        quarter = None
        year = None

class RevenueEstimate:
    def __init__(self):
        no_of_analysts = None
        ave_estimate = None
        low_estimate = None
        high_estimate = None
        year_ago_sales = None
        sales_growth_year_est = None
        quarter = None
        year = None

class EarningsHistory:
    def __init__(self):
        est_eps = None
        actual_eps = None
        difference = None
        surprise_pc = None
        date = None

class EpsTrend:
    def __init__(self):
        currrent_estimate = None
        days_ago_7 = None
        days_ago_30 = None
        days_ago_60 = None
        days_ago_90 = None
        quarter = None
        year = None

class EpsRevisions:
    def __init__(self):
        up_last_7_days = None
        up_last_30_days = None
        down_last_7_days = None
        down_last_30_days = None
        quarter = None
        year = None

class GrowthEstimates:
    def __init__(self):
        current_quarter = None
        next_quarter = None
        current_year = None
        next_year = None
        next_5_years_per_annum = None
        past_5_years_per_annum = None 