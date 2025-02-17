import cx_Oracle


def oracle_test(hostname: str, port: int, sid: str, username: str, password: str):
    dsn = cx_Oracle.makedsn(hostname, 1521, service_name=sid)
    try:
        conn = cx_Oracle.connect(user=username, password=password, dsn=dsn, mode=cx_Oracle.SYSDBA)
        print("Successful connection to Oracle!")

        cursor = conn.cursor()
        cursor.execute("SELECT 'value' name_field FROM dual")

        for row in cursor:
            print(row)

        cursor.close()
        conn.close()

    except cx_Oracle.DatabaseError as e:
        print("Connection error:", e)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    oracle_test("oracle-xe", 1521, "xe", "sys", "xe")
