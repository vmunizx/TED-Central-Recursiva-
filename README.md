# TED-Central-Recursiva-

## Integrantes
- Vinicius Muniz Lopes dos Santos — R.A: 26.1.14496
- Katson Kawan — R.A: 24.1.89730

## Descrição do projeto
Projeto que implementa dois algoritmos clássicos usando recursão: o cálculo do MDC (máximo divisor comum) pelo algoritmo de Euclides e a soma dos dígitos de um número. O sistema lê operações da entrada padrão, valida os dados e retorna o resultado ou uma mensagem de erro apropriada para cada caso, sem interromper a execução do programa.

## Instruções de execução

**Passo a passo:**
1. Clone o repositório ou baixe o arquivo `.py`.
2. Abra um terminal na pasta do projeto.
3. Prepare a entrada no formato esperado: a primeira linha contém a quantidade de operações (`q`), e cada linha seguinte contém uma operação, `M a b` (MDC de a e b) ou `S n` (soma dos dígitos de n).
4. Execute o script informando a entrada. Há duas formas:

   - **Via arquivo de entrada:**

  - **Via digitação manual:** rode `python "ted vinicius e katson.py"`, digite a quantidade e as operações linha a linha, e finalize a entrada (no Windows, `Ctrl+Z` seguido de Enter; no Linux/Mac, `Ctrl+D`).

5. A saída é impressa no terminal, uma linha por operação, na mesma ordem da entrada.

**Exemplo de entrada:**

M 48 18
S 1234
M 10 0
S abc
X 5

**Saída correspondente:**

MDC = 6
SOMA = 10
ERRO: EntradaInvalida
ERRO: EntradaInvalida
ERRO: OperacaoInvalida


## Algoritmos recursivos

**MDC pelo algoritmo de Euclides (`mdc`)**

Calcula o máximo divisor comum entre dois números aplicando repetidamente a propriedade de que `mdc(a, b) = mdc(b, a % b)`, até que o segundo valor chegue a zero — nesse ponto, o primeiro valor é o resultado. Cada chamada reduz o tamanho dos números envolvidos, garantindo que a recursão termine.

**Soma dos dígitos (`soma_digitos`)**

Calcula a soma dos dígitos de um número separando o último dígito (`n % 10`) e chamando a função novamente sobre o restante do número (`n // 10`), somando os resultados na volta da recursão. O caso base ocorre quando o número já tem um único dígito.

## Tratamento de exceções

O projeto não define classes de exceção próprias; a validação de entrada é feita de forma defensiva, prevenindo falhas em vez de propagar exceções, através de dois mecanismos:

- **`parse_int`**: encapsula a conversão de texto para inteiro (`int()`) em um bloco `try/except ValueError`, retornando `None` quando a conversão falha, em vez de deixar a exceção interromper o programa.
- **Códigos de erro personalizados**: cada operação verifica o formato e os valores recebidos antes de calcular algo, retornando:
  - `ERRO: EntradaInvalida` — quando faltam ou sobram argumentos, quando um valor não é um número válido, ou quando viola uma regra do domínio (MDC exige inteiros positivos; soma dos dígitos exige inteiro não negativo).
  - `ERRO: OperacaoInvalida` — quando o código da operação não é `M` nem `S`.

Esse padrão garante que uma entrada malformada gere uma mensagem de erro controlada na saída, e não uma interrupção abrupta do programa (`traceback`).
