import sqlite3
class database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id INTEGER UNIQUE,
            user_id INTEGER NOT NULL UNIQUE,
            Name varchar(255) NOT NULL,
            PRIMARY KEY (id AUTOINCREMENT)
            );
"""
        self.execute(sql, commit=True)

    def create_table_product(self):
        sql = """
        CREATE TABLE Products (
            id INTEGER UNIQUE,
            user_id INTEGER,
            photo TEXT,
            caption TEXT,
            order_id TEXT,
            info TEXT,
            PRIMARY KEY (id AUTOINCREMENT)
            );
"""
        self.execute(sql, commit=True)
    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, user_id: int, name: str):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(user_id, Name) VALUES(?, ?)
        """
        self.execute(sql, parameters=(user_id, name), commit=True)

    def add_product(self, user_id: int, photo: str, caption: str, order_id: str, info: str):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Products(user_id, photo, caption, order_id, info) VALUES(?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(user_id, photo, caption, order_id, info), commit=True)

    def is_product(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Products WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)
def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
