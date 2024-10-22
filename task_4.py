"""
Модуль для реалізації системи коментарів з ієрархічною структурою.
"""


class Comment:
    """
    Клас, що представляє коментар у системі коментарів.
    
    Attributes:
        text (str): Текст коментаря
        author (str): Автор коментаря
        replies (list): Список відповідей на коментар
        is_deleted (bool): Прапорець видалення коментаря
    """

    def __init__(self, text: str, author: str):
        """
        Ініціалізація нового коментаря.

        Args:
            text (str): Текст коментаря
            author (str): Автор коментаря
        """
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply: 'Comment'):
        """
        Додає відповідь до поточного коментаря.

        Args:
            reply (Comment): Коментар-відповідь
        """
        self.replies.append(reply)

    def remove_reply(self):
        """
        Позначає коментар як видалений.
        Змінює текст на стандартне повідомлення про видалення.
        """
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    def display(self, level: int = 0):
        """
        Рекурсивно виводить коментар та всі його відповіді.

        Args:
            level (int): Рівень вкладеності для відступів (за замовчуванням 0)
        """
        # Формуємо відступ залежно від рівня вкладеності
        indent = "    " * level

        # Виводимо коментар
        if self.is_deleted:
            print(f"{indent}{self.text}")
        else:
            print(f"{indent}{self.author}: {self.text}")

        # Рекурсивно виводимо всі відповіді
        for reply in self.replies:
            reply.display(level + 1)


def main():
    """
    Демонстрація роботи системи коментарів.
    """
    # Створюємо кореневий коментар
    root_comment = Comment("Яка чудова книга!", "Бодя")

    # Додаємо відповіді першого рівня
    reply1 = Comment("Книга повне розчарування :(", "Андрій")
    reply2 = Comment("Що в ній чудового?", "Марина")

    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)

    # Додаємо відповідь другого рівня
    reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
    reply1.add_reply(reply1_1)

    # Видаляємо коментар
    reply1.remove_reply()

    # Виводимо всю структуру коментарів
    print("\nСтруктура коментарів:")
    root_comment.display()


if __name__ == "__main__":
    main()
