"""Модуль для знаходження найбільшого значення в AVL-дереві."""


from avl_node import AVLNode, insert


def find_max_value(root: AVLNode) -> int:
    """
    Знаходить найбільше значення в AVL-дереві.

    У AVL-дереві найбільше значення завжди знаходиться в крайньому правому вузлі.
    Функція проходить по правих вузлах, доки не знайде останній.

    Args:
        root (AVLNode): Корінь AVL-дерева.

    Returns:
        int: Найбільше значення в дереві.
        None: Якщо дерево порожнє.
    """
    if root is None:
        return None

    current = root
    # Рухаємось по правим вузлам до кінця
    while current.right is not None:
        current = current.right

    return current.key


def main():
    """Демонстрація роботи функції знаходження максимального значення."""
    # Створюємо AVL-дерево
    root = None
    values = [10, 20, 30, 40, 50, 25]

    # Додаємо значення до дерева
    for value in values:
        root = insert(root, value)

    # Виводимо структуру дерева
    print("AVL-дерево:")
    print(root)

    # Знаходимо максимальне значення
    max_value = find_max_value(root)
    print(f"Максимальне значення в дереві: {max_value}")


if __name__ == "__main__":
    main()
