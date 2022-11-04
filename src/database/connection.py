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


## CRUD FUNCTIONS ##


##CREATE##

def create_hero(name,about,bio):
    execute_query("""
    INSERT INTO heroes(name, about_me, biography)
    VALUES(%s,%s,%s)
    """,[name, about, bio])


#READ##

def find_hero(hero):
    the_hero = execute_query("""
    SELECT name, about_me, biography
    FROM heroes
    WHERE name = %s""",[hero,]).fetchone()
    print(the_hero)


##UPDATE##

def update_bio(name,bio):
    new_update = execute_query(""" 
    UPDATE heroes
    SET biography = %s
    WHERE %s = heroes.name

    """, [bio,name])
    return new_update    
    print("Your hero can't keep their story straight")

##DELETE##

def cancel_hero(name):
    execute_query("""
    DELETE FROM heroes
    WHERE name = %s
    """,[name])
    print("Your hero has been cancelled")

## SEE ABILITIES##

def hero_abilities(name):
    hero_skill = execute_query("""
    SELECT heroes.name,ability_types.name
    FROM heroes 
    JOIN abilities ON heroes.id = abilities.hero_id
    JOIN ability_types ON ability_types.id = abilities.ability_type_id
    WHERE heroes.name = %s""",[name]).fetchone()
    print(hero_skill)


## SEE RELATIONSHIPS##

def show_friends(): 
    friends = execute_query("""
    SELECT h_1.name, r_type.name, h_2.name FROM relationship_types r_type
    JOIN relationships r ON r_type.id = r.relationship_type_id
    JOIN heroes h_1 ON r.hero1_id = h_1.id 
    JOIN heroes h_2 ON r.hero2_id = h_2.id
    ORDER BY r_type.name DESC;""",[]).fetchall()
    print(friends)


## USER INPUT FUNCTION  ##
## prompts user to make selections and will invoke one of the CRUD functions based on their selection ##

def main_function():
    user_choice = input("Please make a selection? \n 1: find a Hero \n 2: create your own Hero \n 3: change a story \n 4: cancel a hero \n 5: see abilities \n 6: see relationships")


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
        print('Whose story would you like to change?')
        name = input()
        print('enter a new bio')
        bio = input()
        update_bio(name,bio)
        main_function()

    elif user_choice == '4':
        print('which hero would you like to cancel?')
        name = input()
        cancel_hero(name)
        main_function()

    elif user_choice == '5':
        print('Enter a hero name')
        name = input()
        hero_abilities(name)
        main_function()

    elif user_choice == '6':
         show_friends()
         main_function()
    
main_function()





