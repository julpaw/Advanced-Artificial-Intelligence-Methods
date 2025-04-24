def knapsack(weights, values, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Wypełnianie tablicy DP
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # Odtwarzanie wybranych przedmiotów
    w = capacity
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)  # dodajemy indeks przedmiotu
            w -= weights[i - 1]

    selected_items.reverse()  # żeby były w oryginalnej kolejności
    return dp[n][capacity], selected_items

# Przykład użycia
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

max_value, items = knapsack(weights, values, capacity)
print("Maksymalna możliwa wartość:", max_value)
print("Wybrane przedmioty (indeksy):", items)
