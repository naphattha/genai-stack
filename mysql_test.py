import mysql.connector

try:
    # เชื่อมต่อฐานข้อมูล
    conn = mysql.connector.connect(
        host="localhost",
        port=3307,  # Host port จาก docker-compose
        user="root",
        password="Wealth3visual%",
        database="set50"
    )

    cursor = conn.cursor()

    # ลองยิง query
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    print("📋 Tables in database 'set50':")
    for table in tables:
        print("-", table[0])

    # ลอง select จากตารางแรก (ถ้ามี)
    if tables:
        first_table = tables[0][0]
        print(f"\n🔍 Preview first 5 rows from `{first_table}`:")
        cursor.execute(f"SELECT * FROM {first_table} LIMIT 5;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    cursor.close()
    conn.close()

except Exception as e:
    print("❌ Error connecting to MySQL:", e)
