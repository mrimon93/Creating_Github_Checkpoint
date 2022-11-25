import psycopg2
import time


conn = psycopg2.connect(
   host="localhost",
   database="Phonelistdv",
   user="postgres",
   password="Monasogsql@12"
)

print("Welcome Put one of these Commands ")
print("list, add, delete or quit. \n")


# If you want to see the changes check branch development and you will discover some changes :)
def insert_word(C, word, translation):
    return f"returning ''{word} and {translation}"

def read_dict(C):
    cur = C.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows
def add_word(C, word, translation):
    cur = C.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()
def delete_word(C, ID):
    cur = C.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()
def save_dict(C):
    cur = C.cursor()
    cur.execute("COMMIT;")
    cur.close()

text_file()

while True: ## REPL - Read Execute Program Loop
    cmd = input("What is your COMMAND your highness : ").lower()
    if cmd == "list":
        print(read_dict(conn))
    elif cmd == "add":
        name = input("  Word: ")
        phone = input("  Translation: ")
        add_word(conn, name, phone)
        print(f"Word '{name}' and Translation '{phone}' has been added")
    elif cmd == "delete":
        ID = input("  ID: ")
        delete_word(conn, ID)
    elif cmd == "quit":
        save_dict(conn)
        print("See you next time")
        time.sleep(2)
        exit()
