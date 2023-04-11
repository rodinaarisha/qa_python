from main import BooksCollector
import pytest


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_add_two_books_with_fixture(self, collector):
        collector.add_new_book('Война и мир')
        assert len(collector.get_books_rating()) == 3

    def test_add_new_book_add_the_same_book(self, collector):
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    def test_get_book_rating_check_rating_nine(self, collector):
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 9)
        collector.get_book_rating('Что делать, если ваш кот хочет вас убить')
        assert collector.get_book_rating('Что делать, если ваш кот хочет вас убить') == 9

    @pytest.mark.parametrize('positive_rating', [1, 5, 10])
    def test_set_book_rating_add_new_rating_for_one_book_value_from_one_to_ten(self, collector, positive_rating):
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', positive_rating)
        assert collector.get_book_rating('Что делать, если ваш кот хочет вас убить') == positive_rating

    @pytest.mark.parametrize('rating', [0, 11])
    def test_set_book_rating_add_new_rating_for_one_book_less_1_and_more_ten(self, collector, rating):
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', rating)
        assert collector.get_book_rating('Что делать, если ваш кот хочет вас убить') == 1

    def test_set_book_rating_add_rating_for_a_non_existent_book(self, collector):
        collector.set_book_rating('Война и Мир', 5)
        assert 'Война и Мир' not in collector.get_books_rating()

    def test_get_books_with_specific_rating_getting_a_book_with_a_rating_of_9(self, collector):
        collector.get_books_with_specific_rating(9)
        assert list(collector.books_rating.keys())[list(collector.books_rating.values()).index(9)] == 'Гордость и предубеждение и зомби'

    def test_get_books_rating_getting_books(self, collector):
        collector.add_new_book('Горе от Ума')
        collector.add_new_book('Анна Каренина')
        collector.get_books_rating()
        assert len(collector.get_books_rating()) == 4

    def test_add_book_in_favorites_add_one_book_in_favorites(self, collector):
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_re_adding_one_book_to_favorites(self, collector):
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_delete_one_book_from_favorites(self, collector):
        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        assert 'Что делать, если ваш кот хочет вас убить' not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_delete_non_existent_book_from_favorites(self, collector):
        collector.add_book_in_favorites('Война и Мир')
        assert len(collector.get_list_of_favorites_books()) == 1
