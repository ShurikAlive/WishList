import mysql.connector

class DBManager(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.cnx = mysql.connector.connect(user = 'root',password = '111111', host = '127.0.0.1')
            cls.cursor = cls.cnx.cursor()
            cls.instance = super(DBManager, cls).__new__(cls)
        return cls.instance

    def ExecuteSQLScript(self, script):
        try:
            self.cursor.execute(script)
        except mysql.connector.Error as error:
            print ('ERROR MESSAGE: ' + str(error.msg))
            print ('WITH ' + script)

        try:
            message = self.cursor.fetchall()
        except:
            message = self.cursor.fetchone()
        return message

    def ExecuteSQL(self, script):
        #ДЛЯ INSERT, UPDATE, DELETE
        self.ExecuteSQLScript(script)
        self.cnx.commit()

    def __del__(self):
        self.cursor.close()
        self.cnx.close()
