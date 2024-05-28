INSERT INTO students (name, second_name, group_id) VALUES ('NAME', 'SURNAME', 708)


INSERT INTO `groups` (title, start_date, end_date) VALUES ('QA Team', 'June 2024', 'September 2024')


INSERT INTO books (title, taken_by_student_id) VALUES
('QA Automation', 1211),
('QA Manual', 1211),
('QA FullStack', 1211);


INSERT INTO subjets (title) VALUES ('Math'), ('Mechanics');


INSERT INTO lessons (title, subject_id) VALUES
('Arithmetic', 1618),
('Geometry', 1618),
('Kinematics', 1619),
('Dynamics', 1619);


INSERT INTO marks (value, student_id, lesson_id) VALUES
(5, 1211, 3902),
(5, 1211, 3903),
(5, 1211, 3904),
(5, 1211, 3905);


# Все оценки студента
SELECT * FROM marks WHERE student_id = 1211;


# Все книги, которые находятся у студента
SELECT * FROM books WHERE taken_by_student_id = 1211;


# Всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов
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
    s.id = 1211
