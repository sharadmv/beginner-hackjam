import sqlite3
conn = sqlite3.connect('cheeps.db')

c = conn.cursor()
c.execute("delete from cheeps")
conn.commit()
conn.close()
