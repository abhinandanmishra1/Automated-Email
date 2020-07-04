import psycopg2
passe=input("Enter Your Password")
conn = psycopg2.connect(database="AutoEmail", user = "postgres", password = passe, host = "127.0.0.1", port = "5432")
print("jai hind")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS Students")
cur.execute('''CREATE TABLE Students
      (ID INT PRIMARY KEY     NOT NULL,
       FIRST_NAME TEXT    NOT NULL,
       LAST_NAME TEXT    NOT NULL,
       EMAIL TEXT    NOT NULL,
       CONTACT_NO TEXT,
       BRANCH TEXT,
       YEAR TEXT,
       REGISTRATION_DATE DATE,
       LAST_EMAIL_SENT DATE,
       COURSE TEXT NOT NULL 
        )''')

cur.execute("INSERT INTO Students (ID,FIRST_NAME,LAST_NAME,EMAIL,CONTACT_NO,BRANCH,YEAR,REGISTRATION_DATE,LAST_EMAIL_SENT,COURSE) \
      VALUES (6, 'Abhinandan','Mishra', 'iamabhimishra1@gmail.com','7007241631','IT','TH','2020-06-22','1975-1-1','Python')");

cur.execute("INSERT INTO Students (ID,FIRST_NAME,LAST_NAME,EMAIL,CONTACT_NO,BRANCH,YEAR,REGISTRATION_DATE,LAST_EMAIL_SENT ,COURSE) \
      VALUES (7, 'Ekansh','Saxena', 'mishraabhirock@gmail.com','9927875747','IT','FE','2020-06-12','1975-1-1','IOT')");

cur.execute("INSERT INTO Students (ID,FIRST_NAME,LAST_NAME,EMAIL,CONTACT_NO,BRANCH,YEAR,REGISTRATION_DATE,LAST_EMAIL_SENT ,COURSE) \
      VALUES (8, 'Vinay','Kushwaha', 'myselfravana@gmail.com','7272739374','ECE','TH','2020-02-10','1975-1-1','Web Development')");

cur.execute("INSERT INTO Students (ID,FIRST_NAME,LAST_NAME,EMAIL,CONTACT_NO,BRANCH,YEAR,REGISTRATION_DATE,LAST_EMAIL_SENT ,COURSE) \
      VALUES (9, 'Ekansh Saxena','Tripathi', 'ekanshsaxena9927@gmail.com','70072488831','ECE','TH','2020-01-01','1975-1-1','C++')");

cur.execute("INSERT INTO Students (ID,FIRST_NAME,LAST_NAME,EMAIL,CONTACT_NO,BRANCH,YEAR,REGISTRATION_DATE,LAST_EMAIL_SENT ,COURSE) \
      VALUES (10, 'Harsh','Mishra', 'imaginaryboyharshmishra759@gmail.com','772888900961','CSE','TH','2019-06-01','1975-1-1','Python')");


cur.execute("INSERT INTO Students (ID,FIRST_NAME,LAST_NAME,EMAIL,CONTACT_NO,BRANCH,YEAR,REGISTRATION_DATE,LAST_EMAIL_SENT ,COURSE) \
      VALUES (1, 'Abhinandan','Mishra', 'iamabhimishra1@gmail.com','7007331631','IT','TH','2020-06-22','1975-1-1','Python')");

cur.execute("INSERT INTO Students (ID,FIRST_NAME,LAST_NAME,EMAIL,CONTACT_NO,BRANCH,YEAR,REGISTRATION_DATE,LAST_EMAIL_SENT ,COURSE) \
      VALUES (2, 'Ekansh','Saxena', 'mishraabhirock@gmail.com','9927875747','IT','FE','2020-06-12','1975-1-1','IOT')");

cur.execute("INSERT INTO Students (ID,FIRST_NAME,LAST_NAME,EMAIL,CONTACT_NO,BRANCH,YEAR,REGISTRATION_DATE,LAST_EMAIL_SENT ,COURSE) \
      VALUES (3, 'Vinay','Kushwaha', 'myselfravana@gmail.com','7272739374','ECE','TH','2020-02-10','1975-1-1','Web Development')");

cur.execute("INSERT INTO Students (ID,FIRST_NAME,LAST_NAME,EMAIL,CONTACT_NO,BRANCH,YEAR,REGISTRATION_DATE,LAST_EMAIL_SENT ,COURSE) \
      VALUES (4, 'Ekansh Saxena','Tripathi', 'ekanshsaxena9927@gmail.com','70072488831','ECE','TH','2020-01-01','1975-1-1','C++')");

cur.execute("INSERT INTO Students (ID,FIRST_NAME,LAST_NAME,EMAIL,CONTACT_NO,BRANCH,YEAR,REGISTRATION_DATE,LAST_EMAIL_SENT,COURSE) \
      VALUES (5, 'Harsh','Mishra', 'imaginaryboyharshmishra759@gmail.com','772888900961','CSE','TH','2019-06-01','1975-1-1','Python')");



conn.commit()
print("Records created successfully")
