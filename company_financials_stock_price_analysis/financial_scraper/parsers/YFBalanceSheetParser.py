from IParser import IParser


class YFAnnualBalanceSheetData():

      def __init__(self, date, value, data_type, symbol):
            self.date = date
            self.value = value 
            self.data_type = data_type
            self.symbol = symbol



class YFAnnualBalanceSheetParser(IParser):

      @staticmethod
      def parse_data(data):
            data_objects = []
            timeseries = data.get("timeseries")
            if timeseries is None:
                        return
            results = timeseries.get("result")
            if results is None:
                        return
            for result in results:
                  if result is None:
                        continue
                  meta = result.get("meta")
                  if meta is None:
                        continue
                  symbol = meta.get("symbol")
                  if symbol is None:
                        continue
                  symbol = symbol[0]
                  data_type = meta.get("type")
                  if data_type is None:
                        continue
                  data_type = data_type[0]
                  data = result.get(data_type)
                  if data is None:
                        continue
                  for entry in data:
                        if entry is None:
                              continue
                        date = entry.get("asOfDate")
                        values = entry.get("reportedValue")
                        if values is None:
                              continue
                        value = values.get("raw")
                        if value is None:
                              continue
                        data_object = YFAnnualBalanceSheetData(date, value, data_type, symbol)   
                        data_objects.append(data_object)
            return data_objects
