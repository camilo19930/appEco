import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="localhost",  # Cambia esto a la dirección de tu servidor PostgreSQL
        database="db_ecoparadise" , # Cambia esto al nombre de tu base de datos
        user="postgres",  # Cambia esto al usuario de PostgreSQL
        password="1234"  # Cambia esto a tu contraseña de PostgreSQL
    )
    return conn

def get_generic_all_records(query):
    conn = get_connection()
    cursor = conn.cursor()
    select_query = query
    cursor.execute(select_query)
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    return records

def get_all_records(name, password):
    conn = get_connection()
    cursor = conn.cursor()
    select_query = "SELECT * FROM usuarios WHERE nombre_usuario = %s AND clave = %s"
    cursor.execute(select_query, (name, password))
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    return records

def create_user(name, password):
    conn = get_connection()
    cursor = conn.cursor()
    insert_query = "INSERT INTO mytable (name, pet) VALUES (%s, %s)"
    cursor.execute(insert_query, (name, password))
    conn.commit()
    cursor.close()
    conn.close()
    
def create_reserva(fecha, dias_reserva, cabana_id, usuario_id ):
    conn = get_connection()
    cursor = conn.cursor()
    insert_query = "INSERT INTO reservas(fecha_reserva, dias_reserva, cabana_id, usuario_id) VALUES (%s, %s, %s, %s);"
    cursor.execute(insert_query, (fecha, dias_reserva, cabana_id, usuario_id))
    conn.commit()
    cursor.close()
    conn.close()