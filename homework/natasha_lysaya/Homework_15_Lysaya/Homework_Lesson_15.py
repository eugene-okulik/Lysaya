import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    password='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)
cursor = db.cursor()


cursor.execute('''
INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)
''', ('PYTHON', 'SQL', None))
student_id = cursor.lastrowid


cursor.execute('''
INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)
''', ('SQL Team', '2025-06-01', '2025-09-01'))
group_id = cursor.lastrowid


cursor.execute('''
UPDATE students SET group_id = %s WHERE id = %s
''', (group_id, student_id))


books = [
    ('SQL для чайников', student_id),
    ('SQL expert', student_id),
    ('SQL developer', student_id)
]
cursor.executemany('''
INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)
''', books)


subjects = [('Programming',), ('SQL Databases',)]
cursor.executemany('''
INSERT INTO subjets (title) VALUES (%s)
''', subjects)
db.commit()


cursor.execute('SELECT id, title FROM subjets')
subject_id_map = {title: id for id, title in cursor.fetchall()}


# Вставка уроков и получение их ID по одному
lessons = [
    ('Introduction', subject_id_map['Programming']),
    ('SQL syntax', subject_id_map['Programming']),
    ('SQL injections', subject_id_map['SQL Databases']),
    ('SQL security', subject_id_map['SQL Databases'])
]


lesson_id_map = {}
for lesson in lessons:
    cursor.execute('''
    INSERT INTO lessons (title, subject_id) VALUES (%s, %s)
    ''', lesson)
    lesson_id_map[lesson[0]] = cursor.lastrowid


marks = [
    (5, student_id, lesson_id_map['Introduction']),
    (5, student_id, lesson_id_map['SQL syntax']),
    (5, student_id, lesson_id_map['SQL injections']),
    (5, student_id, lesson_id_map['SQL security'])
]
cursor.executemany('''
INSERT INTO marks (value, student_id, lesson_id) VALUES (%s, %s, %s)
''', marks)

print("Все оценки студента:")
cursor.execute('SELECT * FROM marks WHERE student_id = %s', (student_id,))
print(cursor.fetchall())


print("Книги, которые взял студента:")
cursor.execute('SELECT * FROM books WHERE taken_by_student_id = %s', (student_id,))
print(cursor.fetchall())


print("Всё, что о нем есть в базе данных:")
cursor.execute('''
SELECT
    s.name,
    s.second_name,
    g.title AS group_title,
    g.start_date,
    g.end_date,
    b.title AS book_title,
    sub.title AS subject_title,
    l.title AS lesson_title,
    m.value AS mark
FROM
    students s
LEFT JOIN
    `groups` g ON s.group_id = g.id
LEFT JOIN
    books b ON s.id = b.taken_by_student_id
LEFT JOIN
    marks m ON s.id = m.student_id
LEFT JOIN
    lessons l ON m.lesson_id = l.id
LEFT JOIN
    subjets sub ON l.subject_id = sub.id
WHERE
    s.id = %s
''', (student_id,))
print(cursor.fetchall())


db.commit()
db.close()
