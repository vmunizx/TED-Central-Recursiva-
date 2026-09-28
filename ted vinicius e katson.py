import sys

def mdc(a, b):
    # Algoritmo recursivo de Euclides
    if b == 0:
        return a
    return mdc(b, a % b)

def soma_digitos(n):
    if n < 10:
        return n
    return n % 10 + soma_digitos(n // 10)

def parse_int(s):
    try:
        return int(s)
    except ValueError:
        return None

def main():
    data = sys.stdin.read().split('\n')
    q = int(data[0].strip())
    out = []
    for i in range(1, q + 1):
        line = data[i].strip() if i < len(data) else ""
        parts = line.split()
        op = parts[0] if parts else ""

        if op == "M":
            if len(parts) != 3:
                out.append("ERRO: EntradaInvalida")
                continue
            a, b = parse_int(parts[1]), parse_int(parts[2])
            if a is None or b is None or a <= 0 or b <= 0:
                out.append("ERRO: EntradaInvalida")
            else:
                out.append(f"MDC = {mdc(a, b)}")
        elif op == "S":
            if len(parts) != 2:
                out.append("ERRO: EntradaInvalida")
                continue
            n = parse_int(parts[1])
            if n is None or n < 0:
                out.append("ERRO: EntradaInvalida")
            else:
                out.append(f"SOMA = {soma_digitos(n)}")
        else:
            out.append("ERRO: OperacaoInvalida")

    print("\n".join(out))

main()
