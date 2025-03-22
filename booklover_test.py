import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Dune", 5)
        self.assertIn("Dune", test_object.book_list['book_name'].values)

    def test_2_add_book(self):
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Dune", 5)
        test_object.add_book("Dune", 5)
        self.assertEqual(test_object.book_list['book_name'].value_counts().loc["Dune"], 1)
                
    def test_3_has_read(self):
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Dune", 5)
        self.assertTrue(test_object.has_read("Dune"))
        
    def test_4_has_read(self): 
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        self.assertFalse(test_object.has_read("Children of Dune"))
        
    def test_5_num_books_read(self): 
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Dune", 5)
        test_object.add_book("Children of Dune", 4)
        test_object.add_book("Dune Messiah", 2)
        self.assertEqual(test_object.num_books_read(), 3)

    def test_6_fav_books(self):
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Dune", 5)
        test_object.add_book("Children of Dune", 4)
        test_object.add_book("Dune Messiah", 2)
        fav_books = test_object.fav_books()
        self.assertTrue(all(fav_books['book_rating'] > 3))
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)
    
