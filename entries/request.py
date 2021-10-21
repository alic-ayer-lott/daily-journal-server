import sqlite3 #sqlite3 is a package that we are importing and then using on line 7 to connect with database
import json
from models import Entry


def get_all_entries():
    with sqlite3.connect("./dailyjournal.db") as conn: #connecting to the database and naming it conn for connection; with allows us to use sqlite3
      conn.row_factory = sqlite3.Row
      db_cursor = conn.cursor()
      # .connect method returns a connection
      #row_factory is a method and we are setting it to equal sqlite3.Row; tells how to get rows out of the database
      #.cursor is a method on conn; creates an environment so we can access the sqlite query

      db_cursor.execute("""
      SELECT
        a.id,
        a.concept,
        a.entry,
        a.date,
        a.mood_id
      FROM entries a
      """)
      #execute is telling us what exactly we are going to execute

      entries = []

      dataset = db_cursor.fetchall()

      for row in dataset:
        entry = Entry(row['id'], row['concept'], row['entry'], row['date'], row['mood_id'])
        entries.append(entry.__dict__) #turning into a dictionary here
    
    return json.dumps(entries) #turning into a string here to return to user


def get_single_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
      conn.row_factory = sqlite3.Row
      db_cursor = conn.cursor()
      
      db_cursor.execute("""
      SELECT
        e.id,
        e.concept,
        e.entry,
        e.date,
        e.mood_id
      FROM entries e
      WHERE e.id = ?
      """, ( id, ))

      data = db_cursor.fetchone()

      entry = Entry(data['id'], data['concept'], data['entry'], data['date'], data['mood_id'])

      return json.dumps(entry.__dict__)

def delete_entry(id):
  with sqlite3.connect("./dailyjournal.db") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()

    db_cursor.execute("""
    DELETE FROM entries
    WHERE id = ?
    """, (id, ))