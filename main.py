import os

def PDinamica(v, p, m, L):
    G = [[0 for _ in range(L + 1)] for _ in range(m + 1)]
    dec = [[0 for _ in range(L + 1)] for _ in range(m + 1)]

    for j in range(L + 1):
        G[0][j] = 0

    for i in range(1, m + 1):
        for j in range(L + 1):
            if p[i - 1] <= j and v[i - 1] + G[i - 1][j - p[i - 1]] > G[i - 1][j]:
                G[i][j] = v[i - 1] + G[i - 1][j - p[i - 1]]
                dec[i][j] = 1
            else:
                G[i][j] = G[i - 1][j]
                dec[i][j] = 0

    items_selected = []
    i, j = m, L
    while i > 0 and j > 0:
        if dec[i][j] == 1:
            items_selected.append(i)
            j -= p[i - 1]
        i -= 1

    return G[m][L], items_selected

def read_data_from_txt(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        items = []
        for line in lines:
            values = line.split()
            if len(values) >= 2:  # Verifica se a linha possui pelo menos dois valores
                try:
                    value = int(values[0])
                    weight = int(values[1])
                    if weight != 0:  # Verifica se o peso é diferente de zero para evitar a divisão por zero
                        items.append((value, weight))
                except ValueError:
                    pass  # Ignora linhas com valores não numéricos
        items.sort(key=lambda x: x[0] / x[1], reverse=True)  # Ordena os itens pela relação benefício/custo
        v = [item[0] for item in items]
        p = [item[1] for item in items]
        m = len(v)
        return v, p, m

def main():
    folders = ["large_scale", "large_scale-optimum", "low-dimensional", "low-dimensional-optimum"]
    L = 300  
    with open("relatorio.txt", "w") as report_file:
        for folder in folders:
            folder_path = os.path.join(os.getcwd(), folder)
            files = os.listdir(folder_path)
            report_file.write(f"Executando para a pasta {folder}:\n")
            for file in files:
                file_path = os.path.join(folder_path, file)
                v, p, m = read_data_from_txt(file_path)
                max_valor, itens_selecionados = PDinamica(v, p, m, L)
                report_file.write(f"Para o arquivo {file}:\n")
                report_file.write("Valor máximo que pode ser carregado na mochila: {}\n".format(max_valor))
                report_file.write("Itens selecionados, peso: ")
                for item in itens_selecionados:
                    report_file.write("[{} = {}], ".format(item, p[item-1]))
                report_file.write("\n")
                report_file.write("Capacidade da mochila: {}\n".format(L))
                report_file.write("Quantidade de itens na mochila: {}\n".format(m))
                report_file.write("\n")


if __name__ == "__main__":
    main()
