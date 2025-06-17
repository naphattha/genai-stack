from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
username = "neo4j"
password = "password"  # แก้เป็นรหัสผ่านที่คุณตั้งไว้

driver = GraphDatabase.driver(uri, auth=(username, password))

def test_query(tx):
    result = tx.run("MATCH (c:Company) RETURN c.name LIMIT 5")
    for record in result:
        print(record)

with driver.session() as session:
    try:
        session.read_transaction(test_query)
    except Exception as e:
        print("❌ Query Error:", e)

driver.close()
