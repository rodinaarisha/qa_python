import pytest


from main import BooksCollector


@pytest.fixture(scope="function")  # Добавление fixture где добавлены две книги в словарь, плюс книга для избранного
def collector():
    collector = BooksCollector()
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    collector.set_book_rating('Гордость и предубеждение и зомби', 9)
    collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
    return collector
