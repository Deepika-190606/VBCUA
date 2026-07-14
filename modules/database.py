import sqlite3
from datetime import datetime

DB_NAME = "database/results.db"


# ---------------- CREATE DATABASE ---------------- #
def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS evaluations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT,
            topic TEXT,
            transcript TEXT,
            understanding_score REAL,
            fluency_score REAL,
            speech_rate REAL,
            duration REAL,
            filler_words INTEGER,
            overall_score REAL,
            evaluation_date TEXT
        )
    """)

    conn.commit()
    conn.close()


# ---------------- SAVE RESULT ---------------- #
def save_result(student_name,
                topic,
                transcript,
                understanding_score,
                fluency_score,
                speech_rate,
                duration,
                filler_words,
                overall_score):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO evaluations(
            student_name,
            topic,
            transcript,
            understanding_score,
            fluency_score,
            speech_rate,
            duration,
            filler_words,
            overall_score,
            evaluation_date
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        student_name,
        topic,
        transcript,
        understanding_score,
        fluency_score,
        speech_rate,
        duration,
        filler_words,
        overall_score,
        datetime.now().strftime("%d-%m-%Y %H:%M")
    ))

    conn.commit()
    conn.close()


# ---------------- GET HISTORY ---------------- #
def get_history():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            student_name,
            topic,
            overall_score,
            evaluation_date
        FROM evaluations
        ORDER BY id DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data