import os
import csv
import mysql.connector as mysql
import dotenv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
    database=os.getenv('DB_NAME')
)
cursor = db.cursor()


base_path = os.path.dirname(__file__)
file_path = os.path.dirname(os.path.dirname(base_path))
csv_path = os.path.join(file_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')


data_csv = []
with open(csv_path, newline='') as csv_file:
    file_data = csv.reader(csv_file)
    data = []
    header = next(file_data)
    for row in file_data:
        data.append(row)


missing_database_data = []


def get_id(table, title):
    query = f"SELECT id FROM `{table}` WHERE title = %s"
    cursor.execute(query, (title,))
    result = cursor.fetchone()
    return result[0] if result else None


for row in data:
    name, second_name, group_title, book_title, subject_title, lesson_title, mark_value = row

    group_id = get_id('groups', group_title)
    subject_id = get_id('subjets', subject_title)
    lesson_id = get_id('lessons', lesson_title)

    if group_id is None or subject_id is None or lesson_id is None:
        missing_database_data.append(row)
        continue

    query = """
    SELECT students.id FROM students
    JOIN `groups` ON students.group_id = groups.id
    JOIN books ON books.taken_by_student_id = students.id
    JOIN marks ON marks.student_id = students.id
    JOIN lessons ON marks.lesson_id = lessons.id
    JOIN subjets ON lessons.subject_id = subjets.id
    WHERE students.name = %s AND students.second_name = %s
    AND students.group_id = %s AND books.title = %s
    AND subjets.title = %s AND lessons.title = %s AND marks.value = %s
    """
    cursor.execute(query, (name, second_name, group_id, book_title, subject_title, lesson_title, mark_value))
    result = cursor.fetchone()

    if result is None:
        missing_database_data.append(row)


cursor.close()
db.close()


if missing_database_data:
    print("Эти данные отсутствуют в базе данных:")
    for row in missing_database_data:
        print(row)
else:
    print("Все данные есть в базе данных.")
