import psycopg2


def create_tables(conn):
    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS client(
            client_id SERIAL PRIMARY KEY,
            first_name VARCHAR(40) NOT NULL,
            last_name VARCHAR(40) NOT NULL,
            email VARCHAR(40) NOT NULL
        );
        """)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS client_phone(
            phone_id SERIAL PRIMARY KEY,
            client_id SERIAL NOT NULL REFERENCES client(client_id),
            phone VARCHAR(11) NOT NULL
        );
        """)
        conn.commit()


def create_client(conn, first_name, last_name, email, phones=[]):
    with conn.cursor() as cur:
        cur.execute("""
        INSERT INTO client(first_name, last_name, email)
        VALUES(%s, %s, %s) RETURNING client_id;
        """, (first_name, last_name, email))
        client_id = cur.fetchone()[0]

    if phones and client_id:
        for phone in phones:
            add_phone(conn, client_id, phone)


def delete_client(conn, client_id):
    with conn.cursor() as cur:
        cur.execute("""
        SELECT phone FROM client_phone WHERE client_id=%s;
        """, (client_id,))
        client_phones = cur.fetchall()

        if client_phones:
            for client_phone in client_phones:
                delete_phone(conn, client_phone[0])

        cur.execute("""
        DELETE FROM client WHERE client_id=%s;
        """, (client_id, ))
        conn.commit()


def add_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute("""
        INSERT INTO client_phone(client_id, phone)
        VALUES(%s, %s);
        """, (client_id, phone))
        conn.commit()


def delete_phone(conn, phone):
    with conn.cursor() as cur:
        cur.execute("""
        DELETE FROM client_phone WHERE phone=%s;
        """, (phone, ))
        conn.commit()


def update_info_client(conn, client_id, first_name=None, last_name=None, email=None):
    with conn.cursor() as cur:
        if first_name:
            cur.execute("""
            UPDATE client SET first_name=%s WHERE client_id=%s;
            """, (first_name, client_id))
            conn.commit()
        elif last_name:
            cur.execute("""
            UPDATE client SET last_name=%s WHERE client_id=%s;
            """, (last_name, client_id))
            conn.commit()
        elif email:
            cur.execute("""
            UPDATE client SET email=%s WHERE client_id=%s;
            """, (email, client_id))
            conn.commit()

    return "Done"


def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    result = None

    with conn.cursor() as cur:
        if first_name:
            cur.execute("""
                    SELECT * FROM client WHERE first_name=%s;
                    """, (first_name,))
            result = cur.fetchall()
        elif last_name:
            cur.execute("""
                    SELECT * FROM client WHERE last_name=%s;
                    """, (last_name,))
            result = cur.fetchall()
        elif email:
            cur.execute("""
                    SELECT * FROM client WHERE email=%s;
                    """, (email,))
            result = cur.fetchall()

        elif phone:
            cur.execute("""
                    SELECT client_id FROM client_phone WHERE phone=%s;
                    """, (phone,))
            client_id = cur.fetchall()
            if client_id:
                cur.execute("""
                        SELECT * FROM client WHERE client_id=%s;
                        """, (client_id[0],))
                result = cur.fetchall()

    return result


phones_1 = ["79898947380", "79591989225", "79723222285"]
phones_2 = ["79898947389", "79591989234", "79723222294"]

customers = [
    ('Jared', 'Ely', 'jared.ely@sakilacustomer.org'),
    ('Mary', 'Smith', 'mary.smith@sakilacustomer.org'),
    ('Patricia', 'Johnson', 'patricia.johnson@sakilacustomer.org'),
    ('Linnda', 'Williams', 'linnda.williams@sakilacustomer.org'),
    ('Barbara', 'Jones', 'barbara.jones@sakilacustomer.org')]

with psycopg2.connect(database="netology_db", user="postgres", password="RtpZV7ow", host="localhost") as conn:
    with conn.cursor() as cur:
        # Create tables if not exists
        create_tables(conn)

        # Create new clients
        for first_name, last_name, email in customers:
            print(first_name, last_name, email)
            create_client(conn, first_name, last_name, email)

        # Add phones to client 3
        for phone in phones_1:
            add_phone(conn, "3", phone)

        # Add phones to client 4
        for phone in phones_2:
            add_phone(conn, "4", phone)

        # Delete client with id 5 without phones
        delete_client(conn, "5")

        # Delete client with id 3 with phones
        delete_client(conn, "3")

        # Update client information
        print(update_info_client(conn, client_id="4", first_name="Linda"))
        print(update_info_client(conn, client_id="4", last_name="Ely"))
        print(update_info_client(conn, client_id="4", email="linda.williams@sakilacustomer.org"))

        # Search clients by values
        # Expected client info
        print(find_client(conn, first_name="Jared"))
        print(find_client(conn, last_name="Smith"))
        print(find_client(conn, email="mary.smith@sakilacustomer.org"))
        print(find_client(conn, phone="79898947389"))
        # Expected None
        print(find_client(conn, phone="79591987225"))

conn.close()






