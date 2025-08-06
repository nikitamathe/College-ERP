import pyodbc

# Connection string for SQL Server
conn_str = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-2NAMNK1\\SQLEXPRESS;"
    "Database=CollegeERP;"
    "Trusted_Connection=yes;"
)

try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    print("✅ Connected to SQL Server successfully!")

    # Fetch data from Students table
    cursor.execute("SELECT * FROM Students")
    rows = cursor.fetchall()

    print("\n--- Students Table ---")
    for row in rows:
        print(row)

    conn.close()

except Exception as e:
    print("❌ Error:", e)
