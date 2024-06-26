import unittest
import manga_down

class TestMangaReader(unittest.TestCase):
    
    def test_chapter_list(self):
        naruto = manga_down.mangareader.Chapter_list("naruto")
        chapter_lists = naruto.get_chapter_list()
        links_list = naruto.get_links()
        self.assertEqual(type(chapter_lists),list,"Return type was not list")
        self.assertGreater(len(chapter_lists),0,"Returned an empty list")
        self.assertEqual(type(links_list),list,"Return type was not list")
        self.assertGreater(len(links_list),0,"Returned an empty list")


    def test_chapter_reader(self):
        naruto = manga_down.mangareader.Chapter_reader("naruto")
        all_image_links = naruto.get_image_links("25")
        self.assertEqual(type(all_image_links),list,"Return type was not list")
        self.assertGreater(len(all_image_links),0,"Returned an empty list")


class TestMangaPanda(unittest.TestCase):
    def test_chapter_list(self):
        naruto = manga_down.mangapanda.Chapter_list("naruto")
        chapter_lists = naruto.get_chapter_list()
        links_list = naruto.get_links()
        self.assertEqual(type(chapter_lists),list,"Return type was not list")
        self.assertGreater(len(chapter_lists),0,"Returned an empty list")
        self.assertEqual(type(links_list),list,"Return type was not list")
        self.assertGreater(len(links_list),0,"Returned an empty list")


    def test_chapter_reader(self):
        naruto = manga_down.mangapanda.Chapter_reader("naruto")
        all_image_links = naruto.get_image_links("25")
        self.assertEqual(type(all_image_links),list,"Return type was not list")
        self.assertGreater(len(all_image_links),0,"Returned an empty list")

if __name__ == "__main__":
    unittest.main()
