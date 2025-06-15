#!/usr/bin/env python
# coding: utf-8

# In[5]:


company_names = {
    "ADVANC": "บริษัท แอดวานซ์ อินโฟร์ เซอร์วิส จำกัด (มหาชน)",
    "AOT": "บริษัท ท่าอากาศยานไทย จำกัด (มหาชน)",
    "AWC": "บริษัท แอสเสท เวิรด์ คอร์ป จำกัด (มหาชน)",
    "BBL": "ธนาคารกรุงเทพ จำกัด (มหาชน)",
    "BCP": "บริษัท บางจาก คอร์ปอเรชั่น จำกัด (มหาชน)",
    "BDMS": "บริษัท กรุงเทพดุสิตเวชการ จำกัด (มหาชน)",
    "BEM": "บริษัท ทางด่วนและรถไฟฟ้ากรุงเทพ จำกัด (มหาชน)",
    "BGRIM": "บริษัท บี.กริม เพาเวอร์ จำกัด (มหาชน)",
    "BH": "บริษัท โรงพยาบาลบำรุงราษฎร์ จำกัด (มหาชน)",
    "BJC": "บริษัท เบอร์ลี่ ยุคเกอร์ จำกัด (มหาชน)",
    "BTS": "บริษัท บีทีเอส กรุ๊ป โฮลดิ้งส์ จำกัด (มหาชน)",
    "CBG": "บริษัท คาราบาวกรุ๊ป จำกัด (มหาชน)",
    "CENTEL": "บริษัท โรงแรมเซ็นทรัลพลาซา จำกัด (มหาชน)",
    "CPALL": "บริษัท ซีพี ออลล์ จำกัด (มหาชน)",
    "CPF": "บริษัท เจริญโภคภัณฑ์อาหาร จำกัด (มหาชน)",
    "CPN": "บริษัท เซ็นทรัลพัฒนา จำกัด (มหาชน)",
    "CRC": "บริษัท เซ็นทรัล รีเทล คอร์ปอเรชั่น จำกัด (มหาชน)",
    "DELTA": "บริษัท เดลต้า อีเลคโทรนิคส์ (ประเทศไทย) จำกัด (มหาชน)",
    "EA": "บริษัท พลังงานบริสุทธิ์ จำกัด (มหาชน)",
    "EGCO": "บริษัท ผลิตไฟฟ้า จำกัด (มหาชน)",
    "GLOBAL": "บริษัท สยามโกลบอลเฮ้าส์ จำกัด (มหาชน)",
    "GPSC": "บริษัท โกลบอล เพาเวอร์ ซินเนอร์ยี่ จำกัด (มหาชน)",
    "GULF": "บริษัท กัลฟ์ เอ็นเนอร์จี ดีเวลลอปเมนท์ จำกัด (มหาชน)",
    "HMPRO": "บริษัท โฮม โปรดักส์ เซ็นเตอร์ จำกัด (มหาชน)",
    "INTUCH": "บริษัท อินทัช โฮลดิ้งส์ จำกัด (มหาชน)",
    "ITC": "บริษัท ไอ-เทล คอร์ปอเรชั่น จำกัด (มหาชน)",
    "IVL": "บริษัท อินโดรามา เวนเจอร์ส จำกัด (มหาชน)",
    "KBANK": "ธนาคารกสิกรไทย จำกัด (มหาชน)",
    "KTB": "ธนาคารกรุงไทย จำกัด (มหาชน)",
    "KTC": "บริษัท บัตรกรุงไทย จำกัด (มหาชน)",
    "LH": "บริษัท แลนด์ แอนด์ เฮ้าส์ จำกัด (มหาชน)",
    "MINT": "บริษัท ไมเนอร์ อินเตอร์เนชั่นแนล จำกัด (มหาชน)",
    "MTC": "บริษัท เมืองไทย แคปปิตอล จำกัด (มหาชน)",
    "OR": "บริษัท ปตท. น้ำมันและการค้าปลีก จำกัด (มหาชน)",
    "OSP": "บริษัท โอสถสภา จำกัด (มหาชน)",
    "PTT": "บริษัท ปตท. จำกัด (มหาชน)",
    "PTTEP": "บริษัท ปตท. สำรวจและผลิตปิโตรเลียม จำกัด (มหาชน)",
    "PTTGC": "บริษัท พีทีที โกลบอล เคมิคอล จำกัด (มหาชน)",
    "RATCH": "บริษัท ราช กรุ๊ป จำกัด (มหาชน)",
    "SCB": "ธนาคารไทยพาณิชย์ จำกัด (มหาชน)",
    "SCC": "บริษัท ปูนซิเมนต์ไทย จำกัด (มหาชน)",
    "SCGP": "บริษัท เอสซีจี แพคเกจจิ้ง จำกัด (มหาชน)",
    "TIDLOR": "บริษัท เงินติดล้อ จำกัด (มหาชน)",
    "TISCO": "บริษัท ทิสโก้ไฟแนนเชียลกรุ๊ป จำกัด (มหาชน)",
    "TLI": "บริษัท ไทยประกันชีวิต จำกัด (มหาชน)",
    "TOP": "บริษัท ไทยออยล์ จำกัด (มหาชน)",
    "TRUE": "บริษัท ทรู คอร์ปอเรชั่น จำกัด (มหาชน)",
    "TTB": "ธนาคารทหารไทยธนชาต จำกัด (มหาชน)",
    "TU": "บริษัท ไทยยูเนี่ยน กรุ๊ป จำกัด (มหาชน)",
    "WHA": "บริษัท ดับบลิวเอชเอ คอร์ปอเรชั่น จำกัด (มหาชน)"
}


# In[ ]:


from neo4j import GraphDatabase
import json
from datetime import datetime

# Neo4j Connection Setup
uri = "bolt://localhost:7687"
user = "neo4j"
password = "Neo4jpassword"
driver = GraphDatabase.driver(uri, auth=(user, password))

# Load JSON Data
with open('FilteredEODData.json') as eod_file:
    eod_data = json.load(eod_file)

with open('FilteredFinancialData.json') as fin_file:
    financial_data = json.load(fin_file)

# Function to Get Company Name
def get_company_name(symbol):
    return company_names.get(symbol, symbol)

# Extract Year & Quarter from Date
def extract_year_and_quarter(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    year = date_obj.year
    quarter = (date_obj.month - 1) // 3 + 1
    return year, quarter

# Run Cypher Queries
def run_query(query, parameters=None):
    with driver.session() as session:
        session.run(query, parameters)

# --- Insert Companies and Market Data ---
for record in eod_data:
    symbol = record['symbol']
    name = get_company_name(symbol)
    dateAsof = record['date']
    year, quarter = extract_year_and_quarter(dateAsof)

    # Create Company Node
    run_query("""
    MERGE (c:Company {symbol: $symbol})
    ON CREATE SET c.name = $name
    """, {'symbol': symbol, 'name': name})

    # Create Market Data Node
    run_query("""
    MERGE (m:MarketData {symbol: $symbol, year: $year, quarter: $quarter, date: $date})
    SET m.prior = $prior, m.open = $open, m.high = $high, m.low = $low, m.close = $close, m.average = $average,
        m.aomVolume = $aomVolume, m.aomValue = $aomValue, m.trVolume = $trVolume, m.trValue = $trValue,
        m.totalVolume = $totalVolume, m.totalValue = $totalValue
    MERGE (c:Company {symbol: $symbol})
    MERGE (c)-[:HAS_MARKET_DATA]->(m)
    """, {
        'symbol': symbol, 'year': year, 'quarter': quarter, 'date': dateAsof,
        'prior': record.get('prior'), 'open': record.get('open'), 'high': record.get('high'),
        'low': record.get('low'), 'close': record.get('close'), 'average': record.get('average'),
        'aomVolume': record.get('aomVolume'), 'aomValue': record.get('aomValue'),
        'trVolume': record.get('trVolume'), 'trValue': record.get('trValue'),
        'totalVolume': record.get('totalVolume'), 'totalValue': record.get('totalValue')
    })

    # Create Market Ratios
    market_ratios = {
        'PE': record.get('pe'),
        'PBV': record.get('pbv'),
        'BVPS': record.get('bvps'),
        'DividendYield': record.get('dividendYield'),
        'MarketCap': record.get('marketCap'),
        'VolumeTurnover': record.get('volumeTurnover')
    }

    for ratio_type, value in market_ratios.items():
        if value is not None:
            run_query("""
            MERGE (r:Ratio {symbol: $symbol, year: $year, quarter: $quarter, date: $date, type: $type})
            SET r.value = $value
            MERGE (c:Company {symbol: $symbol})
            MERGE (c)-[:HAS_RATIO]->(r)
            """, {
                'symbol': symbol, 'year': year, 'quarter': quarter, 'date': dateAsof, 
                'type': ratio_type,'value': value
            })

# --- Insert Financial Data ---
for record in financial_data:
    symbol = record['symbol']
    year = record['year']
    quarter = record['quarter']
    dateAsof = record['dateAsof']

    # Create Financial Metrics
    financial_metrics = {
        'TotalAssets': record.get('totalAssets'),
        'TotalLiabilities': record.get('totalLiabilities'),
        'PaidupShareCapital': record.get('paidupShareCapital'),
        'ShareholderEquity': record.get('shareholderEquity'),
        'TotalEquity': record.get('totalEquity'),
        'TotalRevenueQuarter': record.get('totalRevenueQuarter'),
        'TotalRevenueAccum': record.get('totalRevenueAccum'),
        'TotalExpensesQuarter': record.get('totalExpensesQuarter'),
        'TotalExpensesAccum': record.get('totalExpensesAccum'),
        'EBITQuarter': record.get('ebitQuarter'),
        'EBITAccum': record.get('ebitAccum'),
        'NetProfitQuarter': record.get('netProfitQuarter'),
        'NetProfitAccum': record.get('netProfitAccum'),
        'EPSQuarter': record.get('epsQuarter'),
        'EPSAccum': record.get('epsAccum'),
        'OperatingCashFlow': record.get('operatingCashFlow'),
        'InvestingCashFlow': record.get('investingCashFlow'),
        'FinancingCashFlow': record.get('financingCashFlow')
    }

    for metric, value in financial_metrics.items():
        if value is not None:
            run_query("""
            MERGE (m:Metric {symbol: $symbol, year: $year, quarter: $quarter, date: $date, type: $type})
            SET m.value = $value
            MERGE (c:Company {symbol: $symbol})
            MERGE (c)-[:HAS_METRIC]->(m)
            """, {
                'symbol': symbol,
                'year': year,
                'quarter': quarter,
                'date': dateAsof,
                'type': metric,
                'value': value
            })

    # Create Financial Ratios
    financial_ratios = {
        'ROE': record.get('roe'),
        'ROA': record.get('roa'),
        'NetProfitMarginQuarter': record.get('netProfitMarginQuarter'),
        'NetProfitMarginAccum': record.get('netProfitMarginAccum'),
        'DE': record.get('de'),
        'FixedAssetTurnover': record.get('fixedAssetTurnover'),
        'TotalAssetTurnover': record.get('totalAssetTurnover'),
    }

    for ratio_type, value in financial_ratios.items():
        if value is not None:
            run_query("""
            MERGE (r:Ratio {symbol: $symbol, year: $year, quarter: $quarter, date: $date, type: $type})
            SET r.value = $value
            MERGE (c:Company {symbol: $symbol})
            MERGE (c)-[:HAS_RATIO]->(r)
            """, {
                'symbol': symbol,
                'year': year,
                'quarter': quarter,
                'date': dateAsof,
                'type': ratio_type,
                'value': value
            })

# --- Add Frequently Used Metrics Relationship ---
top_metrics = ["netProfitQuarter", "NetProfitMarginQuarter", "epsQuarter", "PE", "DividendYield"]

for metric in top_metrics:
    run_query("""
    MATCH (c:Company)-[:HAS_RATIO|HAS_METRIC|HAS_MARKET_DATA]->(m {type: $metric})
    MERGE (c)-[:FREQUENTLY]->(m)
    """, {'metric': metric})

# --- Add PopularCompany Label ---
top_companies = ["AOT", "PTT", "BDMS", "SCB", "CPALL"]

for company in top_companies:
    run_query("""
    MATCH (c:Company {symbol: $symbol})
    SET c:PopularCompany
    """, {'symbol': company})

print("Neo4j Database Updated Successfully!")

# Close the Neo4j connection
driver.close()