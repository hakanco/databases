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

    print("--------------------------------------------------------------")
    cur.execute(
        "insert into test (id, age, first, last) values (100, 25, 'jafer', 'alhaboubi')"
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

    conn.close()