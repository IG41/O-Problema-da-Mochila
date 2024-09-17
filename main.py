import os
import time

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

def PGulosoMenorPeso(v, p, m, L):
    itens_selecionados = []
    peso_total = 0
    valor_total = 0
    
    itens_ordenados = sorted(range(m), key=lambda i: p[i])

    for i in itens_ordenados:
        if peso_total + p[i] <= L:
            itens_selecionados.append(i + 1)
            peso_total += p[i]
            valor_total += v[i]

    return valor_total, itens_selecionados

def PGulosoCustoBeneficio(v, p, m, L):
    itens_selecionados = []
    peso_total = 0
    valor_total = 0
    
    custo_beneficio = [(v[i] / p[i], i) for i in range(m)]
    custo_beneficio.sort(reverse=True)

    for _, i in custo_beneficio:
        if peso_total + p[i] <= L:
            itens_selecionados.append(i + 1)
            peso_total += p[i]
            valor_total += v[i]

    return valor_total, itens_selecionados

def read_data_from_txt(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        items = []

        line = lines.pop(0)
        m = int(line.split()[0])
        L = int(line.split()[1])
        
        for line in lines:
            values = line.split()
            if len(values) >= 2:
                try:
                    value = int(values[0])
                    weight = int(values[1])
                    if weight != 0:
                        items.append((value, weight))
                except ValueError:
                    pass
        items.sort(key=lambda x: x[0] / x[1], reverse=True)
        v = [item[0] for item in items]
        p = [item[1] for item in items]
        return v, p, m, L

def main():
    folder = "large_scale"
    with open("relatorio.txt", "w") as report_file:
        folder_path = os.path.join(os.getcwd(), folder)
        files = os.listdir(folder_path)
        report_file.write(f"\nExecutando para a pasta {folder}:\n")
        for file in files:
            file_path = os.path.join(folder_path, file)
            v, p, m, L = read_data_from_txt(file_path)
            
            tempo_inicial = time.time()
            max_valor, itens_selecionados = PDinamica(v, p, m, L)
            tempo_final_dinamica = time.time() - tempo_inicial
            tempo_inicial = time.time()
            max_valor_guloso_menor_peso, itens_selecionados_guloso_menor_peso = PGulosoMenorPeso(v, p, m, L)
            tempo_final_menor_peso = time.time() - tempo_inicial
            tempo_inicial = time.time()
            max_valor_guloso_custo_beneficio, itens_selecionados_guloso_custo_beneficio = PGulosoCustoBeneficio(v, p, m, L)
            tempo_final_guloso_custo_beneficio = time.time() - tempo_inicial
            report_file.write(f"\nPara o arquivo {file}:\n")
            report_file.write("    Capacidade da mochila: {}\n".format(L))
            report_file.write("    Quantidade de itens total na mochila: {}\n".format(m))
            
            # PDinamica
            report_file.write("  Programacao Dinamica:\n")
            report_file.write("    Valor maximo que pode ser carregado na mochila: {}\n".format(max_valor))
            report_file.write("    Quantidade de itens na mochila: {}\n".format(len(itens_selecionados)))
            report_file.write(f"    Tempo de execucao: {tempo_final_dinamica}.")
            # report_file.write("    \nItens selecionados, peso: ")
            # for item in itens_selecionados:
            #     report_file.write("[{} = {}], ".format(item, p[item-1]))
            report_file.write("\n")
            
            # PGulosoMenorPeso
            report_file.write("  Programacao Gulosa para menor peso:\n")
            report_file.write("    Valor maximo que pode ser carregado na mochila: {}\n".format(max_valor_guloso_menor_peso))
            report_file.write("    Quantidade de itens na mochila: {}\n".format(len(itens_selecionados_guloso_menor_peso)))
            report_file.write(f"    Tempo de execucao: {tempo_final_menor_peso}.")
            # report_file.write("    \nItens selecionados, peso: ")
            # for item in itens_selecionados_guloso_menor_peso:
            #     report_file.write("[{} = {}], ".format(item, p[item-1]))
            report_file.write("\n")
            
            # PGulosoCustoBeneficio
            report_file.write("  Programacao Gulosa para custo beneficio:\n")
            report_file.write("    Valor maximo que pode ser carregado na mochila: {}\n".format(max_valor_guloso_custo_beneficio))
            report_file.write("    Quantidade de itens na mochila: {}\n".format(len(itens_selecionados_guloso_custo_beneficio)))
            report_file.write(f"    Tempo de execucao: {tempo_final_guloso_custo_beneficio}.")
            # report_file.write("    \nItens selecionados, peso: ")
            # for item in itens_selecionados_guloso_custo_beneficio:
            #     report_file.write("[{} = {}], ".format(item, p[item-1]))
            report_file.write("\n")


if __name__ == "__main__":
    main()
