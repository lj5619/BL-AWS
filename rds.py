import boto3
import psycopg2

rds_host = "leon-database-1.cna42i0ecj3c.ap-south-1.rds.amazonaws.com"
db_user = "postgres"
db_password = "Leonola"
db_port = 5432

try:
    conn = psycopg2.connect(
        host=rds_host,
        port=db_port,
        user=db_user,
        password=db_password,
    )
    print("Connected to RDS PostgreSQL!")

    cur = conn.cursor()
    cur.execute("SELECT version();")
    version = cur.fetchone()
    print("PostgreSQL version:", version)

    cur.close()
    conn.close()

except Exception as e:
    print("Connection failed:", e)
