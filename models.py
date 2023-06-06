import sqlite3

class Nudge:
    def __init__(self, title, image, time, description, icon, invitation):
        self.title = title
        self.image = image
        self.time = time
        self.description = description
        self.icon = icon
        self.invitation = invitation

    def create_nudge(self):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO nudges (title, image, time, description, icon, invitation) VALUES (?, ?, ?, ?, ?, ?)",
                           (self.title, self.image, self.time, self.description, self.icon, self.invitation))
            conn.commit()