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
 
# def my_function():
#      user_selection = input("""
#         READ:Learn about SQL Heroes
#         CREATE:Create a Hero
#         UPDATE:Add an ability
#         DELETE:Eliminate a Hero
    
#     """)
# my_function()

####################
## CRUD FUNCTIONS ##
####################

##CREATE##

# what parameters am I going to pass in?
# also change to the correct column names

def create_hero(name,about,bio):
    execute_query("""
    INSERT INTO heroes(name, about_me, biography)
    VALUES(%s,%s,%s)
    """,[name, about, bio])


##READ##
# what parameters am I going to pass in?
# also change to the correct column names

def find_hero(hero):
    the_hero = execute_query("""
    SELECT name, about_me, biography
    FROM heroes
    WHERE name = %s""",[hero,]).fetchone()
    print(the_hero)


##UPDATE##
# what parameters am I going to pass in?
# also change to the correct column names

def update_bio(name,bio):
    new_update = execute_query(""" 
    UPDATE heroes
    SET biography = %s
    WHERE name = %s
    """, [name,bio])
    return new_update
    print("Your hero can't keep their story straight")


##DELETE##
# what parameters am I going to pass in?
# also change to the correct column names

def cancel_hero(name):
    execute_query("""
    DELETE FROM heroes
    WHERE name = %s    
    """,[name])
    print("Your hero has been cancelled")


###########################
## USER INPUT FUNCTIONS ##
##########################

## prompt user to make selections and will invoke one of the CRUD functions based on their selection ##

def main_function():
    user_choice = input("Please make a selection? \n 1: find a Hero \n 2: create your own Hero \n 3: change a story \n 4: cancel a hero \n")


    if user_choice == '1':
        print('enter a name')
        hero = input()
        find_hero(hero)
        main_function()

    elif user_choice == '2':
        print('enter a name')
        hero_name = input()
        print('what can they do?')
        hero_ability = input()
        print("What's their story?")
        hero_bio = input()
        create_hero(hero_name,hero_ability,hero_bio)
        main_function()

    elif user_choice == '3':
        update = input('Whose story would you like to change?')
        name = input()
        print('enter a new bio')
        bio = input()
        update_bio(name,bio)
        main_function()

    elif user_choice == '4':
        print('which hero would you like to cancel?')
        name = input()
        cancel_hero()
        main_function()


main_function()


