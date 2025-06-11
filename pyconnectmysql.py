import mysql.connector  

conn = mysql.connector.connect(host = 'localhost',username=  'root',password='puwDFjJLMi85Id',
                               database= 'codewithsaksham' )

my_cursor=conn.cursor()

conn.commit()
conn.close()

print('conn success')