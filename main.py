# python connection with MariaDB

# Module Imports

import mariadb
import sys


def get_all_employees():
    cur.execute(
        "select * from employees"
    )

    for i in cur:
        print(i)


def generate_user_table():
    cur.execute(
        "drop table IF EXISTS user_table"
    )

    cur.execute(
        "create table user_table("
        "email VARCHAR(100), name VARCHAR(50), password VARCHAR(30))"
    )
    cur.execute(
        "insert into user_table (email, name, password) values ('ywbaek@perscholas.org', 'young', 'letsgomets'),"
    )
    cur.execute(
        "insert into user_table (email, name, password) values ('mcordon@perscholas.org', 'marcial', 'perscholas')"
    )
    cur.execute(
        "insert into user_table (email, name, password) values ('mhaseeb@perscholas.org', 'haseeb', 'platform')"
    )


def get_all_users():
    cur.execute(
        "select * from user_table"
    )
    for i in cur:
        print(i)


def get_user_by_name(name):
    cur.execute(
        "select email, password from user_table where name = ?", (name,)
    )
    for i in cur:
        print(f"Here is the {name}\'s email and password {i}")


def validate_user(email, password):
    cur.execute(
        "select email, password from user_table"
    )
    for i in cur:
        if email == i[0] and password == i[1]:
            return True
        else:
            continue
    return False


if __name__ == '__main__':

    try:
        conn = mariadb.connect(
            user="root",
            password="root",
            host="127.0.0.1",
            port=3306,
            database="classicmodels"

        )
        conn.autocommit = True
    except mariadb.Error as e:
        print("Error connecting to MariaDB Platform:  {}".format(e))
        sys.exit(1)

    cur = conn.cursor()
    print("--------------------------------------------------------------")
    cur.execute(
        "show tables"
    )
    for i in cur:
        print(i[0], end=' | ')
    print()

    print("---------------------SHOW FIELDS-----------------------------------------")
    cur.execute(
        "show fields from employees"
    )
    for i in cur:
        print(i[0], end=" | ")
    print()

    get_all_employees()

    print("-----------------------JOB TITLE---------------------------------------")
    cur.execute(
        "select firstName, lastName, email from employees where jobTitle = ? order by firstName",
        ("Sales Rep",)
    )

    for i in cur:
        print(i)
    print("------------------------------LIKE--------------------------------")
    cur.execute(
        "select contactLastName, contactFirstName from customers where contactLastName like ?",
        ("S%",)
    )

    for i in cur:
        print(i)
    print("--------------------------DROP TABLE------------------------------------")
    cur.execute(
        "drop table IF EXISTS test"
    )
    cur.execute(
        "create table test("
        "id INT PRIMARY KEY,age INT, first VARCHAR(30), last VARCHAR(30))"
    )

    cur.execute(
        "describe test"
    )
    for i in cur:
        print(i)

    print("--------------------------INSERT INTO------------------------------------")
    cur.execute(
        "insert into test (id, age, first, last) values (100, 25, 'jafer', 'alhaboubi')"
    )
    cur.execute(
        "insert into test (id, age, first, last) values (101, 26, 'x', 'y')"
    )

    cur.execute(
        "select * from test"
    )

    for i in cur:
        print(i)
    print("--------------------------------------------------------------")
    # cur.execute(
    #     "delete from test where id = 100"
    # )

    generate_user_table()
    get_all_users()
    print("----------------")
    get_user_by_name('young')

    conn.close()
