import psycopg2
#establishing the connection
conn = psycopg2.connect(
   database="sample_db", host='127.0.0.1', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("select * from user_details")

# Fetch a single row using fetchone() method.
rows = cursor.fetchall()
for row in rows:
   print(row)
else:
   print("No records found")
#Closing the connection
conn.close()
