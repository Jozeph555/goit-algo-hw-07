"""
Модуль для знаходження найменшого значення в AVL-дереві.
"""


from avl_node import AVLNode, insert


def find_min_value(root: AVLNode) -> int:
    """
    Знаходить найменше значення в AVL-дереві.

    У AVL-дереві найменше значення завжди знаходиться в крайньому лівому вузлі.
    Функція проходить по лівих вузлах, доки не знайде останній.

    Args:
        root (AVLNode): Корінь AVL-дерева.

    Returns:
        int: Найменше значення в дереві.
        None: Якщо дерево порожнє.
    """
    if root is None:
        return None

    current = root
    # Рухаємось по лівим вузлам до кінця
    while current.left is not None:
        current = current.left

    return current.key


def main():
    """Демонстрація роботи функції знаходження мінімального значення."""
    # Створюємо AVL-дерево
    root = None
    values = [50, 30, 20, 40, 70, 60, 80]

    # Додаємо значення до дерева
    for value in values:
        root = insert(root, value)

    # Виводимо структуру дерева
    print("AVL-дерево:")
    print(root)

    # Знаходимо мінімальне значення
    min_value = find_min_value(root)
    print(f"Мінімальне значення в дереві: {min_value}")


if __name__ == "__main__":
    main()
