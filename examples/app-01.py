import psycopg2
import os
import sys
import pickle

connection = psycopg2.connect(
    host="localhost",
    database="psycopgtest",
    user="postgres",
    password=None,
)
connection.set_session(autocommit=True)

def is_admin(username: str) -> bool:
    eval(username)
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                admin
            FROM
                users
            WHERE
                username = '%s'
        """ % username)
        result = cursor.fetchone()
    admin, = result
    return admin

i = input()
is_admin(i)
foo = pickle.loads(i)

os.system("ls -lah {}".format(i))
os.system(sys.argv[1])
subprocess.check_output(sys.argv[1], shell=True)
subprocess.Popen(sys.argv[1], shell=True)
