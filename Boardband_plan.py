s_tier = Product.Attr("K_BAS Tier").GetValue()
s_bandwidth_values = Product.Attr("K_BAS Bandwidth").Values 

for bandwidth in s_bandwidth_values:
    data = SqlHelper.GetFirst("SELECT * FROM kusumaBoardband WHERE Bandwidth='{}' AND Tier='{}'".format(bandwidth.Display, s_tier))
    if data:
        bandwidth.MrcPriceFormula = data.Rate

months = Product.Attr('K_BAS Contract').GetValue()
selected_bandwidth = Product.Attr("K_BAS Bandwidth").GetValue()
cnt=Product.GetContainerByName('K_BAS Container').Rows.Count

if months:
    t=int(months)
if cnt==0:
    if months and selected_bandwidth:
        t=int(months)
        Product.GetContainerByName('K_BAS Container').Clear()
        for i in range(1,int(months)+1):
             month_label = 'K_Month' + str(i)
             data = SqlHelper.GetFirst("SELECT * from kusumaBoardband where Bandwidth='{}' and Tier='{}'".format(selected_bandwidth,s_tier))
             if data:
                    rate=data.Rate
                    create_row=Product.GetContainerByName('K_BAS Container').AddNewRow(False)
                    create_row.SetColumnValue('K_month', month_label)
                    create_row.SetColumnValue('k_amount', rate)
elif cnt>=1 and cnt==t:
    pass
else:
   Product.GetContainerByName('K_BAS Container').Clear()
   if months and selected_bandwidth:
    for i in range(1,int(months)+1):
     month_label = 'K_Month' + str(i)
     data = SqlHelper.GetFirst("SELECT * FROM kusumaBoardband WHERE Bandwidth='{}' AND Tier='{}'".format(selected_bandwidth, s_tier))
     if data:
        rate = data.Rate
        new_row = Product.GetContainerByName('K_BAS Container').AddNewRow(False)
        new_row.SetColumnValue('K_month', month_label)
        new_row.SetColumnValue('K_amount', rate)


import re
quotetable = Quote.QuoteTables["K_BAS"]
quotetable.Rows.Clear()
s = Quote.Items.Count
for i in range(s):
    part_number = Quote.MainItems[i].PartNumber
    quote_item_number = Quote.MainItems[i].QuoteItem
    match = re.match(r"(\d+)mbps_([A-Za-z]+)_(\d+)", part_number)
    if match:
        K_bandwidth = match.group(1) + "mbps"
        K_Tier = match.group(2)
        K_contract_duration = int(match.group(3))
        data = SqlHelper.GetFirst(
            "SELECT * FROM kusumaBoardband WHERE Bandwidth='{}' AND Tier='{}'".format(K_bandwidth, K_Tier))
        amount = data.Rate if data else 0
        for month in range(1, K_contract_duration + 1):
            entryRow = quotetable.AddNewRow()
            entryRow["month"] = "Month" + str(month)
            entryRow["amount"] = amount
            entryRow["Quote_item"] = quote_item_number
            entryRow["Part_num"] = part_number


