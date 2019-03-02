"""
上海行情快照中交易状态
    该字段为8位字符串，左起每位表示特定的含义，无定义则填空格。
    第1位：‘S’表示启动（开市前）时段，‘C’表示集合竞价时段，‘T’表示连续交易时段，‘B’表示休市时段，‘E’表示闭市时段，‘P’表示产品停牌，
          ‘M’表示可恢复交易的熔断时段（盘中集合竞价），‘N’表示不可恢复交易的熔断时段（暂停交易至闭市），‘D’表示开盘集合竞价阶段结束到连续竞价阶段开始之前的时段（如有）。
    第2位： ‘0’表示此产品不可正常交易，‘1’表示此产品可正常交易，无意义填空格。
    第3位：‘0’表示未上市，‘1’表示已上市。
    第4位：‘0’表示此产品在当前时段不接受进行新订单申报，‘1’ 表示此产品在当前时段可接受进行新订单申

    说明：当日交易时段内，产品可能出现的状态包括：开盘集合竞价，连续交易，停牌，熔断（盘中集合竞价，暂停交易至闭市）。
    对于上述字段34（TradingPhaseCode），其取值的第2位（是否可正常交易）在产品进入开盘集合竞价、连续交易、熔断（盘中集合竞价）
    状态时值为‘1’，在产品进入停牌、熔断（暂停交易至闭市）
    状态时值为‘0’，且闭市后保持该产品盘前的是否可正常交易状态。
    其取值的第4位（是否接受新订单申报），仅在交易时段有效，在非交易时段无效。
上海成交买卖标识, 'B'为买, 'S'为卖, 'N'为未知一般出现于集合竞价其间的撮合成交
"""

shfile_address_base = r'f:\data\{}\shreportdata'
szfile_address_base = r'f:\data\{}\szreportdata'
date_list = ['20181224', '20181225', '20181226', '20181227', '20181228',
             '20190102', '20190103', '20190104', '20190107', '20190108',
             '20190109', '20190110', '20190111', '20190114', '20190115',
             '20190116', '20190117', '20190118', '20190121', '20190122',
             '20190123', '20190124', '20190125', '20190128', '20190129',
             '20190130', '20190131', '20190201']
trading_days_address = r'H:\vnpyStockEngine\data_process\trading_days.json'
# file_address = r'g:\20190124\shreportdata\shreport0.csv'
trade_shdata_base = r'h:\vnpyStockEngine\data_process\sh_temp'
trade_szdata_base = r'h:\vnpyStockEngine\data_process\sz_temp'

sh_address = r'H:\vnpyStockEngine\data_process\sh_stock_list.json'
sz_address = r'H:\vnpyStockEngine\data_process\sz_stock_list.json'

hs300_sh_address = r'H:\vnpyStockEngine\data_process\hs300_sh.json'
hs300_sz_address = r'H:\vnpyStockEngine\data_process\hs300_sz.json'

save_path = 'g:/l2_database/{}_data/{}'

