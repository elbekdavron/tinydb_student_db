from tinydb import TinyDB, Query

# Create or connect to the database
db = TinyDB('students.json')

# Reference the default table
students_table = db.table('students')

student = {    
        "id": 192,
        "name": "Shamsiddin Nishonov",
        "age": 15,
        "gender": "Male",
        "contact": "911234567",
        "grade_level": "Grade 10",
        "subjects": {
            "math": 57,
            "science": 77,
            "english": 93
        },
        "attendance": 87,
        "activities": ["Online games", "Debate Club"],
        "address": {
            "street": "Buyuk ipak yo'li",
            "city": "Samarkand",
            "state": "Sam",
            "zip_code": "10400"
        }
    } 

db.insert(student)
