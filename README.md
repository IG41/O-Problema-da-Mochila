# 🧳 PDinamica - Otimização de Mochila Dinâmica

## Descrição 📜

Este projeto implementa uma solução dinâmica para o problema da mochila, utilizando uma abordagem de programação dinâmica para determinar o valor máximo que pode ser carregado com base nos itens e seus respectivos pesos e valores. Ele lê arquivos de texto contendo valores e pesos e realiza a otimização para cada um deles, gerando um relatório detalhado com os resultados. 

## Funcionalidades 🔧

- **Função PDinamica**:
  - Recebe como parâmetros os valores, pesos, número de itens e a capacidade da mochila.
  - Calcula o valor máximo que pode ser carregado.
  - Retorna a lista de itens selecionados com seus pesos.

- **Leitura de dados**:
  - Função que lê dados de um arquivo `.txt` com valores e pesos.
  - Verifica se os valores e pesos são válidos antes de processar.

- **Execução em várias pastas**:
  - Processa arquivos de diferentes diretórios e gera um relatório em `relatorio.txt` com o resultado de cada pasta.

## Pastas Processadas 📂

- `large_scale`
- `large_scale-optimum`
- `low-dimensional`
- `low-dimensional-optimum`

## Como usar 🚀

1. **Organize os dados**:
   - Coloque seus arquivos com os valores e pesos nas pastas mencionadas acima.

2. **Rodar o script**:
   - Execute o script com o comando:
     ```bash
     python3 script.py
     ```

3. **Relatório gerado**:
   - O relatório com os resultados será salvo no arquivo `relatorio.txt`.

## Estrutura dos arquivos de dados 📄

Cada linha de arquivo de dados deve conter dois valores:
- O **valor** do item.
- O **peso** do item.

Exemplo:

```txt
100 20
200 30
300 50
```

## Exemplo de execução 📝
- Após rodar o script, você verá algo como:

Executando para a pasta large_scale:
Para o arquivo example.txt:
Valor máximo que pode ser carregado na mochila: 500
Itens selecionados, peso: [1 = 20], [3 = 50], 
Capacidade da mochila: 300
Quantidade de itens na mochila: 3

 
## Contribuindo 🤝

Sinta-se à vontade para fazer um fork do projeto e enviar pull requests para melhorias ou correções!

## Licença 📄

Este projeto é livre para uso sob a licença MIT.

---

Divirta-se resolvendo o problema da mochila com esta implementação! 🎒✨
