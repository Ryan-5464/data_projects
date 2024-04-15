import json

with open("./data/data0.text", 'r') as f:
      data = json.loads(f.read())
"""
print(data["timeseries"]["result"])


for sec in data["timeseries"]["result"]:
      print(sec)

print(data.get("timeseries").get("result")[0].get("meta").get("type"))
ty = data.get("timeseries").get("result")[0].get("meta").get("type")[0]
print(ty)
print(data.get("timeseries").get("result")[0].get("meta"))
print(data.get("timeseries").get("result")[0].get("timestamp"))
print(data.get("timeseries").get("result")[0].get(ty)[0].get("asOfDate"))
print(data.get("timeseries").get("result")[0].get(ty)[0].get("reportedValue").get("raw"))
print(data.get("timeseries").get("result")[0].get(ty)[1].get("asOfDate"))
print(data.get("timeseries").get("result")[0].get(ty)[1].get("reportedValue").get("raw"))
print(data.get("timeseries").get("result")[0].get(ty)[2].get("asOfDate"))
print(data.get("timeseries").get("result")[0].get(ty)[2].get("reportedValue").get("raw"))
"""


class YFAnnualBalanceSheetData():

      def __init__(self, date, value, data_type, symbol):
            self.date = date
            self.value = value 
            self.data_type = data_type
            self.symbol = symbol



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


data_objects = parse_data(data)
for i, object in enumerate(data_objects):
      print("\n", i, object.date, object.value, object.data_type, object.symbol)
#print(data_objects)
