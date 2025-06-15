from neo4j import GraphDatabase
import pandas as pd

NEO4J_URI = "bolt://neo4j:7687"
NEO4J_USERNAME = "neo4j"
NEO4J_PASSWORD = "password"

CSV_PATH = "data/sample_financials.csv"  # Update to your real file

class FinancialGraphLoader:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def load_data(self, df):
        with self.driver.session() as session:
            for _, row in df.iterrows():
                session.write_transaction(self._create_company_metric, row)

    @staticmethod
    def _create_company_metric(tx, row):
        tx.run(
            """
            MERGE (c:Company {name: $company})
            MERGE (y:Year {value: $year})
            MERGE (m:Metric {name: $metric})
            MERGE (c)-[:HAS_METRIC {value: $value}]->(m)
            MERGE (m)-[:RECORDED_IN]->(y)
            """,
            company=row["Company"],
            year=row["Year"],
            metric=row["Metric"],
            value=row["Value"]
        )

if __name__ == "__main__":
    print("📥 Loading financial data into Neo4j...")

    # Replace with your real CSV or data source
    df = pd.DataFrame([
        {"Company": "PTT", "Year": 2022, "Metric": "ROE", "Value": 12.5},
        {"Company": "CPALL", "Year": 2022, "Metric": "ROE", "Value": 15.3},
        {"Company": "PTT", "Year": 2021, "Metric": "ROE", "Value": 10.1},
    ])

    loader = FinancialGraphLoader(NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD)
    loader.load_data(df)
    loader.close()

    print("✅ Data loaded successfully.")
