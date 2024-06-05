Case0 = {
    "Edges": [(1, 2), (2, 3), (3, 1)],
    "Ans": {frozenset((1, 2, 3))}
}

Case1 = {
    "Edges": [(1, 2), (2, 3), (3, 1), (4, 2), (4, 3), (4, 5), (5, 4), (5, 6), (6, 3), (6, 7), (7, 6), (8, 5), (8, 7), (8, 8)],
    "Ans": {frozenset((1, 2, 3)), frozenset((4, 5)), frozenset((6, 7)), frozenset((8,))}
}

Case2 = {
    "Edges": [(1, 2), (1, 3), (2, 1), (2, 4), (3, 1), (3, 4), (4, 5), (5, 4), (6, 2), (6, 5), (6, 8), (7, 6), (8, 5), (8, 7), (9, 7), (9, 8), (9, 9)],
    "Ans": {frozenset((1, 2, 3)), frozenset((4, 5)), frozenset((6, 7, 8)), frozenset((9,))}
}

Case3 = {
    "Edges": [(1, 2), (2, 3), (3, 1), (2, 4), (4, 2)],
    "Ans": {frozenset((1, 2, 3, 4))}
}

Case4 = {
    "Edges": [(1, 2), (1, 3), (2, 1), (2, 4), (3, 1), (3, 4), (4, 5), (5, 4), (6, 2), (6, 5), (6, 8), (7, 6), (8, 5), (8, 7), (9, 7), (9, 8), (9, 9), (9, 10)],
    "Ans": {frozenset((1, 2, 3)), frozenset((4, 5)), frozenset((6, 7, 8)), frozenset((9,)), frozenset((10,))}
}

Case5 = {
    "Edges": [(1, 2), (1, 3), (2, 1), (2, 4), (3, 1), (3, 4), (4, 5), (5, 4), (6, 2), (6, 5), (6, 8), (7, 6), (8, 5), (8, 7), (9, 7), (9, 8), (9, 9), (9, 10), (10, 9)],
    "Ans": {frozenset((1, 2, 3)), frozenset((4, 5)), frozenset((6, 7, 8)), frozenset((9, 10))}
}