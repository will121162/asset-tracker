import os
from dotenv import load_dotenv
import mysql.connector
from main import new_unique_string
from faker import Faker
import random

load_dotenv()

fake = Faker()

Faker.seed(42)




db = mysql.connector.connect(
    host=os.environ['HOST'],
    port=os.environ['PORT'],
    user='automation',
    password=os.environ["SQL_PW"],
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


