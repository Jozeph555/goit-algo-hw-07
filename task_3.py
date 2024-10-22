"""
Модуль для обчислення суми всіх значень в AVL-дереві.
"""


from avl_node import AVLNode, insert


def sum_all_values(root: AVLNode) -> int:
    """
    Обчислює суму всіх значень в AVL-дереві.

    Використовує рекурсивний обхід дерева для підрахунку суми всіх значень.
    Обходить ліве піддерево, додає значення поточного вузла,
    потім обходить праве піддерево.

    Args:
        root (AVLNode): Корінь AVL-дерева.

    Returns:
        int: Сума всіх значень в дереві.
        0: Якщо дерево порожнє.
    """
    if root is None:
        return 0

    # Рекурсивно обчислюємо суму лівого піддерева,
    # додаємо значення поточного вузла,
    # додаємо суму правого піддерева
    return (sum_all_values(root.left) +
            root.key +
            sum_all_values(root.right))


def main():
    """Демонстрація роботи функції обчислення суми всіх значень."""
    # Створюємо AVL-дерево
    root = None
    values = [10, 5, 15, 3, 7, 12, 18]

    # Додаємо значення до дерева
    for value in values:
        root = insert(root, value)

    # Виводимо структуру дерева
    print("AVL-дерево:")
    print(root)

    # Обчислюємо суму всіх значень
    total_sum = sum_all_values(root)
    print(f"Сума всіх значень в дереві: {total_sum}")


if __name__ == "__main__":
    main()
