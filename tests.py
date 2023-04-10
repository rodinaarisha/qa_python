from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

        # Проверка добавления двух книг
        def test_add_new_book_add_two_books_with_fixture(self, collector):
            collector.add_new_book('Война и мир')
            assert len(collector.get_books_rating()) == 3

        # Проверка невозможности добавления одной и той же книги
        def test_add_new_book_add_the_same_book(self, collector):
            collector.add_new_book('Что делать, если ваш кот хочет вас убить')
            assert len(collector.get_books_rating()) == 2

        #  Проверка рейтинга книги по ее имени
        def test_get_book_rating_check_rating_nine(self, collector):
            assert collector.get_book_rating('Гордость и предубеждение и зомби') == 9

        # Проверка добавления рейтинга для одной книги больше 1 и меньше 10
        import pytest

        @pytest.mark.parametrize('positive_rating', [1, 5, 10])
        def test_set_book_rating_add_new_rating_for_one_book_value_from_one_to_ten(self, collector, positive_rating):
            collector.set_book_rating('Что делать, если ваш кот хочет вас убить', positive_rating)
            assert collector.books_rating['Что делать, если ваш кот хочет вас убить'] == positive_rating

        # Проверка невозможности добавления рейтинга меньше 1 и больше 10
        @pytest.mark.parametrize('rating', [0, 11])
        def test_set_book_rating_add_new_rating_for_one_book_less_1_and_more_ten(self, collector, rating):
            collector.set_book_rating('Что делать, если ваш кот хочет вас убить', rating)
            assert collector.books_rating['Что делать, если ваш кот хочет вас убить'] == 1

        # Проверка добавления рейтинга несуществующей книги
        def test_set_book_rating_add_rating_for_a_non_existent_book(self, collector):
            collector.set_book_rating('Война и Мир', 5)
            assert 'Война и Мир' not in collector.get_books_rating()

        #  Проверка вывода книги с рейтингом 9
        def test_get_books_with_specific_rating_getting_a_book_with_a_rating_of_9(self, collector):
            assert collector.get_books_with_specific_rating(9) == ['Гордость и предубеждение и зомби']

        # Проверка вывода словаря
        def test_get_books_rating_getting_books(self, collector):
            assert len(collector.get_books_rating()) == 2

        # Проверка добавление книги в избранное add_book_in_favorites
        def test_add_book_in_favorites_add_one_book_in_favorites(self, collector):
            collector.add_book_in_favorites('Гордость и предубеждение и зомби')
            assert 'Гордость и предубеждение и зомби' in collector.get_list_of_favorites_books()

        # Проверка повторного добавления книги в избранное
        def test_add_book_in_favorites_re_adding_one_book_to_favorites(self, collector):
            collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
            assert len(collector.get_list_of_favorites_books()) == 1

        # Проверка удаления книги из избранного delete_book_from_favorites
        def test_delete_book_from_favorites_delete_one_book_from_favorites(self, collector):
            collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
            assert 'Что делать, если ваш кот хочет вас убить' not in collector.get_list_of_favorites_books()

        # Проверка удаления несуществующей книги из избранного
        def test_delete_book_from_favorites_delete_non_existent_book_from_favorites(self, collector):
            collector.add_book_in_favorites('Война и Мир')
            assert len(collector.get_list_of_favorites_books()) == 1