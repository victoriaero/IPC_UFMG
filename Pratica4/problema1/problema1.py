# problema 1

def populacao(num_h_a, tx_anual_a, num_h_b, tx_anual_b):
    count_anos = 0
    while (num_h_a < num_h_b):
        num_h_a = num_h_a + (num_h_a * tx_anual_a / 100)
        num_h_b = num_h_b + (num_h_b * tx_anual_b / 100)
        count_anos += 1
    else:
        return count_anos