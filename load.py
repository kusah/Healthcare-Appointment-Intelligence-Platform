import pymysql

try:
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="sah123",
        database="healthcare_db"
    )

    print("Connected Successfully!")

except Exception as e:
    print("Error:", e)