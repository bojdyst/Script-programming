import zadanie_na_lekcji
import unittest

class Tests(unittest.TestCase):
    def test_add_course(self):
        self.assertEqual(zadanie_na_lekcji.add_course({}, "name", 3), {'name': []})
    def test_add_course_existing_course(self):
        self.assertEqual(zadanie_na_lekcji.add_course({'name': []}, "name", 3), "This course already exists! Enter other name.\n")
    def test_add_course_above_limit(self):
        self.assertEqual(zadanie_na_lekcji.add_course({'name': []}, "name123", 1), "You reached the limit of available courses! Delete one to be able to create new one.\n")
    
    def test_add_to_course(self):
        self.assertEqual(zadanie_na_lekcji.add_to_course({'name': []}, "name",  "Person", 3), {'name': ['Person']})
    def test_add_to_nonexisting_course(self):
        self.assertEqual(zadanie_na_lekcji.add_to_course({'name': []}, "name123",  "Person", 3), "There's no such a course! Enter valid one.\n")
    def test_add_to_course_above_limit(self):
        self.assertEqual(zadanie_na_lekcji.add_to_course({'name1234': ['Person1', 'Person2']}, "name1234",  "Person3", 2), "You reached the limit of available places in this course! Enroll to other course or free space in this course.\n")
    def test_add_to_course_already_signed_in(self):
        self.assertEqual(zadanie_na_lekcji.add_to_course({'name1': ['Person1', 'Person2']}, "name1",  "Person1", 3), "This person is already regisered! Enter other name.\n")
   
    def test_delete_from_course(self):
         self.assertEqual(zadanie_na_lekcji.delete_from_course({'name': ['Person00']}, "name", "Person00"), {'name': []})
    def test_delete_from_nonexising_course(self):
        self.assertEqual(zadanie_na_lekcji.delete_from_course({'name': ['Person00']}, "name123", "Person00"), "There's no such a course! Enter valid one.\n")
    def test_delete_nonexisting_attendant_from_course(self):
        self.assertEqual(zadanie_na_lekcji.delete_from_course({'name': ['Person00']}, "name", "Person11"), "This person doesn't attend this course! Enter valid one.\n")
    
    def test_modify_course(self):
        self.assertEqual(zadanie_na_lekcji.modify_course({'name': []}, "name", "name123"), {'name123': []})
    def test_modify_course_to_already_existing_name(self):
        self.assertEqual(zadanie_na_lekcji.modify_course({'name': [], 'name123': []}, "name", "name123"), "This course already exists! Enter new one.\n")
    def test_modify_nonexisting_course(self):
        self.assertEqual(zadanie_na_lekcji.modify_course({}, "name", "name123"), "There's no such a course! Enter valid one.\n")
    
    def test_delete_course(self):
        self.assertEqual(zadanie_na_lekcji.delete_course({'name': []}, "name"), {})
    def test_delete_nonexisting_course(self):
        self.assertEqual(zadanie_na_lekcji.delete_course({'name': []}, "name1234"), "There's no such a course! Enter valid one.\n")
   
   
if __name__ == "__main__":
    unittest.main()