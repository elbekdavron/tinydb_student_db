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

students = [
    {
        "id": 193,
        "name": "Azizbek Karimov",
        "age": 16,
        "gender": "Male",
        "contact": "911234568",
        "grade_level": "Grade 11",
        "subjects": {
            "math": 65,
            "science": 85,
            "english": 89
        },
        "attendance": 90,
        "activities": ["Football", "Chess Club"],
        "address": {
            "street": "Amir Temur ko'chasi",
            "city": "Tashkent",
            "state": "Tash",
            "zip_code": "100000"
        }
    },
    {
        "id": 194,
        "name": "Dilnoza Abdullaeva",
        "age": 14,
        "gender": "Female",
        "contact": "911234569",
        "grade_level": "Grade 9",
        "subjects": {
            "math": 70,
            "science": 80,
            "english": 95
        },
        "attendance": 88,
        "activities": ["Dancing", "Art Club"],
        "address": {
            "street": "Navoiy ko'chasi",
            "city": "Bukhara",
            "state": "Bux",
            "zip_code": "200100"
        }
    },
    {
        "id": 195,
        "name": "Jahongir Ismoilov",
        "age": 15,
        "gender": "Male",
        "contact": "911234570",
        "grade_level": "Grade 10",
        "subjects": {
            "math": 60,
            "science": 75,
            "english": 90
        },
        "attendance": 85,
        "activities": ["Basketball", "Science Club"],
        "address": {
            "street": "Alisher Navoiy ko'chasi",
            "city": "Andijan",
            "state": "And",
            "zip_code": "170100"
        }
    },
    {
        "id": 196,
        "name": "Sevara Tursunova",
        "age": 16,
        "gender": "Female",
        "contact": "911234571",
        "grade_level": "Grade 11",
        "subjects": {
            "math": 68,
            "science": 82,
            "english": 91
        },
        "attendance": 89,
        "activities": ["Singing", "Literature Club"],
        "address": {
            "street": "Bogishamol ko'chasi",
            "city": "Namangan",
            "state": "Nam",
            "zip_code": "160100"
        }
    },
    {
        "id": 197,
        "name": "Farrukh Bekmurodov",
        "age": 14,
        "gender": "Male",
        "contact": "911234572",
        "grade_level": "Grade 9",
        "subjects": {
            "math": 55,
            "science": 70,
            "english": 85
        },
        "attendance": 86,
        "activities": ["Swimming", "Math Club"],
        "address": {
            "street": "Yunusobod ko'chasi",
            "city": "Tashkent",
            "state": "Tash",
            "zip_code": "100100"
        }
    },
    {
        "id": 198,
        "name": "Laylo Qodirova",
        "age": 15,
        "gender": "Female",
        "contact": "911234573",
        "grade_level": "Grade 10",
        "subjects": {
            "math": 62,
            "science": 78,
            "english": 92
        },
        "attendance": 87,
        "activities": ["Painting", "History Club"],
        "address": {
            "street": "Shahrisabz ko'chasi",
            "city": "Qarshi",
            "state": "Qar",
            "zip_code": "180100"
        }
    },
    {
        "id": 199,
        "name": "Rustam Usmonov",
        "age": 16,
        "gender": "Male",
        "contact": "911234574",
        "grade_level": "Grade 11",
        "subjects": {
            "math": 67,
            "science": 83,
            "english": 88
        },
        "attendance": 90,
        "activities": ["Volleyball", "Debate Club"],
        "address": {
            "street": "Mirzo Ulug'bek ko'chasi",
            "city": "Tashkent",
            "state": "Tash",
            "zip_code": "100200"
        }
    },
    {
        "id": 200,
        "name": "Zarina Yusupova",
        "age": 14,
        "gender": "Female",
        "contact": "911234575",
        "grade_level": "Grade 9",
        "subjects": {
            "math": 58,
            "science": 76,
            "english": 94
        },
        "attendance": 88,
        "activities": ["Reading", "Art Club"],
        "address": {
            "street": "Chorsu ko'chasi",
            "city": "Tashkent",
            "state": "Tash",
            "zip_code": "100300"
        }
    },
    {
        "id": 201,
        "name": "Bekzod Rahimov",
        "age": 15,
        "gender": "Male",
        "contact": "911234576",
        "grade_level": "Grade 10",
        "subjects": {
            "math": 63,
            "science": 79,
            "english": 89
        },
        "attendance": 86,
        "activities": ["Football", "Science Club"],
        "address": {
            "street": "Sirdaryo ko'chasi",
            "city": "Gulistan",
            "state": "Sir",
            "zip_code": "120100"
        }
    },
    {
        "id": 202,
        "name": "Gulnora Xolmirzaeva",
        "age": 16,
        "gender": "Female",
        "contact": "911234577",
        "grade_level": "Grade 11",
        "subjects": {
            "math": 66,
            "science": 84,
            "english": 90
        },
        "attendance": 89,
        "activities": ["Dancing", "Literature Club"],
        "address": {
            "street": "Xorazm ko'chasi",
            "city": "Urgench",
            "state": "Xor",
            "zip_code": "220100"
        }
    }
]
db.insert_multiple(students)
