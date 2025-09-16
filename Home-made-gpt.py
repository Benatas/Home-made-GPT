import sqlite3
import tkinter as tk

connection = sqlite3.connect(r"klausimynas.db")
cursor = connection.cursor()

command1 = """
CREATE TABLE IF NOT EXISTS tid1 (
    klausimo_id INTEGER PRIMARY KEY,
    klausimas TEXT,
    ats TEXT
)
"""
cursor.execute(command1)


class Pamokymas:
    def __init__(self, klausimas):
        self.klausimas = klausimas  
        self.root = tk.Tk()
        self.root.geometry("600x600")
        self.root.title("Home made gpt")

        self.label = tk.Label(
            self.root,
            text="""I dont know the answer to that.
    Can you please teach me?
    
    Answer:""",
            font=("Arial", 18)
        )
        self.label.pack(padx=20, pady=20)

        self.text = tk.Text(self.root, font=("Arial", 18), height=5, width=20)
        self.text.pack(padx=20, pady=20)

        self.button = tk.Button(
            self.root, font=("Arial", 18), text="Reply", command=self.atsakyti
        )
        self.button.pack(padx=20, pady=20)

        self.root.mainloop()

    def atsakyti(self):
        atsakymas2 = self.text.get("1.0", "end-1c").strip()
        if atsakymas2:
            cursor.execute(
                "INSERT INTO tid1 (klausimas, ats) VALUES (?, ?)",
                (self.klausimas, atsakymas2)
            )
            connection.commit()
        self.root.destroy()


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x600")
        self.root.title("Home made GPT")

        self.label = tk.Label(self.root, text="Home made GPT", font=("Arial", 18))
        self.label.pack(padx=20, pady=20)

        self.label2 = tk.Label(self.root, text="Question:", font=("Arial", 18))
        self.label2.pack(padx=20, pady=20)

        self.text = tk.Text(self.root, font=("Arial", 18), height=5, width=20)
        self.text.pack(padx=20, pady=20)

        self.button = tk.Button(
            self.root, text="Submit", font=("Arial", 18), command=self.paspaudimas
        )
        self.button.pack(padx=20, pady=10)

        self.atsakymas = tk.Label(self.root, text="", font=("Arial", 18))
        self.atsakymas.pack(padx=20, pady=20)

        self.root.mainloop()

    def paspaudimas(self):
        klausimas = self.text.get("1.0", "end-1c").strip().upper()

        cursor.execute("SELECT * FROM tid1 WHERE klausimas = ?", (klausimas,))
        row = cursor.fetchone()

        if row:
            self.atsakymas.configure(text=f"{row[2]}")  
        else:
            self.root.destroy()
            Pamokymas(klausimas)


if __name__ == "__main__":
    MainWindow()
