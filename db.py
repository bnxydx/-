import pymysql
class DBHelper:
    def __init__(self, host="127.0.0.1", port="3306", user="root", password="123456", db="zqdb1", charset='utf8mb4'):
        # 初始化数据库连接参数
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset
        self.connection = None  # 初始化连接对象为None
        self.cursor = None      # 初始化游标对象为None

    def connect(self):
        try:
            #建立数据库连接
            self.connection = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                db=self.db,
                charset=self.charset,
                cursorclass=pymysql.cursors.DictCursor   # 使用字典游标，方便操作
            )
            self.cursor = self.connection.cursor()
        except pymysql.MySQLError as e:
            print(f"Error connecting to the database: {e}")
            raise

    def close(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
        except pymysql.MySQLError as e:
            print(f"Error closing the database connection: {e}")

    def execute_query(self, query, params=()):
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except pymysql.MySQLError as e:
            print(f"Error executing query: {e}")
            raise

    def fetch_all(self, query, params=()):
        self.connect()
        try:
            result = self.execute_query(query, params)
        finally:
            self.close()
        return result

    def insert(self, query, params=()):
        self.connect()
        try:
            self.execute_query(query, params)
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            print(f"Error inserting data: {e}")
            raise
        finally:
            self.close()

    def update(self, query, params=()):
        self.connect()
        try:
            self.execute_query(query, params)
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            print(f"Error updating data: {e}")
            raise
        finally:
            self.close()

    def delete(self, query, params=()):
        self.connect()
        try:
            self.execute_query(query, params)
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            print(f"Error deleting data: {e}")
            raise
        finally:
            self.close()