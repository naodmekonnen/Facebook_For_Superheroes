import psycopg
from psycopg import OperationalError

def create_connection(db_name, db_user, db_password, db_host = "localhost", db_port = "5432"):
    connection = None
    try:
        connection = psycopg.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def execute_query(query, params=None):
    connection = create_connection("postgres", "postgres", "postgres")
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        connection.commit()
        print("Query executed successfully")
        connection.close()
        return cursor
    except OSError as e:
        print(f"The error '{e}' occurred or the hero name is already taken")

    


# def select_all():
#     query = """
#         SELECT * from heroes
#     """

#     list_of_heroes = execute_query(query).fetchall()
#     print(list_of_heroes)
#     for record in list_of_heroes:
#         print(record[1])

# select_all()

# def select_some():
#     query = """
#         SELECT * from relationships
#     """

#     relationship_list = execute_query(query).fetchall()
#     print(relationship_list)
#     for record in relationship_list:
#         print(record)

# select_some()

# def select_abilities():
#     query = """
#         SELECT * from ability_types
#     """

#     abilities = execute_query(query).fetchall()
#     print(abilities)

# select_abilities()

# def joined_tables():
#          query = """
#             SELECT heros.id, relationships.relationship_type.id,
#             FROM heroes,
#             JOIN relationships,
#             ON heroes.id = relationships.relationship_type.id;
#         """

# new_table = execute_query(query).fetchall()
# print(new_table)

# joined_tables()

# def new_table():
#     query = """
#     SELECT heroes.id, abilities.id,
#     FROM heroes, abilities,
#     WHERE heroes.id = abilities.id
#     """

# newtable = execute_query(query).fetchall()
# print(newtable)

# new_table()
 
