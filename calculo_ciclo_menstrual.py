from datetime import datetime, timedelta

def calcular_ciclo(data_ultima, duracao_ciclo=28):
    """
    Calcula a próxima menstruação, o período fértil e as faixas de atraso.
    """
    ultima = datetime.strptime(data_ultima, "%d/%m/%Y")

    # Próxima menstruação estimada
    proxima = ultima + timedelta(days=duracao_ciclo)

    # Ovulação e período fértil (14 dias antes da menstruação)
    ovulacao = proxima - timedelta(days=14)
    inicio_fertil = ovulacao - timedelta(days=3)
    fim_fertil = ovulacao + timedelta(days=3)

    # Intervalos possíveis de atraso
    dentro_normal = proxima + timedelta(days=3)
    atraso_leve = proxima + timedelta(days=7)
    atraso_grave = proxima + timedelta(days=10)

    return proxima, inicio_fertil, fim_fertil, dentro_normal, atraso_leve, atraso_grave


def diagnostico(proxima, dentro_normal, atraso_leve, atraso_grave):
    """
    Gera mensagem educativa com base na data atual.
    """
    hoje = datetime.today()

    if hoje <= dentro_normal:
        return "Sua menstruação está dentro do prazo esperado."
    elif dentro_normal < hoje <= atraso_leve:
        return "Menstruação em leve atraso. Isso ainda é considerado normal."
    elif atraso_leve < hoje <= atraso_grave:
        return "Atraso perceptível. Continue observando seu corpo."
    else:
        return "Atraso acima do comum. Se persistir, procure orientação médica."


def main():
    print("=== Calculadora de Ciclo Menstrual e Período Fértil ===\n")

    # Solicitar data da última menstruação
    while True:
        data_ultima = input("Digite a data da última menstruação (DD/MM/AAAA): ").strip()
        try:
            datetime.strptime(data_ultima, "%d/%m/%Y")
            break
        except ValueError:
            print("Data inválida. Use o formato DD/MM/AAAA (ex: 12/08/2025).\n")

    # Escolher tipo de ciclo
    while True:
        tipo = input("\nDeseja usar o ciclo normal (28 dias) ou ciclo específico? [N/E]: ").strip().upper()
        if tipo not in ['N', 'E']:
            print("Opção inválida. Digite 'N' para ciclo normal ou 'E' para ciclo específico.\n")
            continue

        if tipo == 'N':
            duracao = 28
            print("Ciclo normal selecionado (28 dias).")
            break

        elif tipo == 'E':
            while True:
                duracao_input = input("Digite a duração média do seu ciclo (entre 20 e 40 dias): ").strip()
                try:
                    duracao = int(duracao_input)
                    if duracao < 20 or duracao > 40:
                        print("Valor fora do intervalo. Informe entre 20 e 40 dias.\n")
                        continue
                    break
                except ValueError:
                    print("Valor inválido. Digite apenas números inteiros.\n")
            break

    # Calcular ciclo e diagnóstico
    try:
        proxima, inicio_fertil, fim_fertil, dentro_normal, atraso_leve, atraso_grave = calcular_ciclo(data_ultima, duracao)
        mensagem = diagnostico(proxima, dentro_normal, atraso_leve, atraso_grave)

        print("\n=== RESULTADO DO CÁLCULO ===")
        print(f"Data estimada da próxima menstruação: {proxima.strftime('%d/%m/%Y')}")
        print(f"Período fértil estimado: {inicio_fertil.strftime('%d/%m/%Y')} até {fim_fertil.strftime('%d/%m/%Y')}\n")

        print("=== POSSÍVEIS DATAS DE REFERÊNCIA ===")
        print(f"Se vier até {dentro_normal.strftime('%d/%m/%Y')} → ciclo dentro do normal.")
        print(f"Se vier até {atraso_leve.strftime('%d/%m/%Y')} → pequeno atraso (ainda aceitável).")
        print(f"Se vier até {atraso_grave.strftime('%d/%m/%Y')} → atraso perceptível, observe os sinais.\n")

        print("=== ANÁLISE ===")
        print(mensagem)
        print("=====================================")

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    main()
