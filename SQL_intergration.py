#from secrets import SQL_USR_NAME as sql_username, SQL_PW as sql_pw
import mysql.connector
from main_cli import new_unique_string
from faker import Faker
import random

fake = Faker()

Faker.seed(42)




db = mysql.connector.connect(
    host='192.168.1.188',
    port=3306,
    user='automation',
    passwd='pi_SQL_pw1!',
    database='social_media_platform'
)
my_cursor = db.cursor()

rows = []
for i in range(10):
    rows.append((
        fake.first_name(),
        random.randint(13,80),
        fake.country_code(),
        fake.last_name(),
        fake.unique.email(),
        new_unique_string(),
        False,

    ))

my_cursor.executemany(
'insert into users (first_name, age, country_code, last_name, email, unique_str, is_admin) '
    'values (%s,%s,%s,%s,%s,%s,%s)',
    rows,

    )
db.commit()
my_cursor.execute('SELECT * FROM users limit 25')

for row in my_cursor.fetchall():
    print(row)


