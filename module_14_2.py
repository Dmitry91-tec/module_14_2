import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL

)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# for i in range(1,11):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)",
#                    (f"User{i}", f"example{i}@gmail.com", f"{i}0", "1000"))          #добавлять данные
#
# for i in range(1,11,2):
#     cursor.execute("UPDATE Users SET balance = ? WHERE username = ?",
#                    (500, f"User{i}"))        #обновлять значения
#
# for i in range(1,11,3):
#     cursor.execute("DELETE FROM Users WHERE username=?",(f"User{i}",))        #удалять данные
#
# cursor.execute("SELECT username, email, age, balance  FROM Users WHERE age != ?",
#                (60,))                                                              #считывать данные
# users = cursor.fetchall()                                                                #записываем данные в переменную
# for user in users:
#     print(user)

cursor.execute("DELETE FROM Users WHERE id=?",(6,))

cursor.execute("SELECT COUNT (*) FROM Users")                                   #общее количество записей
total_users = cursor.fetchone()[0]
# print(total_users)

cursor.execute("SELECT SUM(balance) FROM Users")                               #сумму всех балансов
all_balances  = cursor.fetchone()[0]
# print(all_balances )
print(all_balances /total_users)
connection.commit()
connection.close()
