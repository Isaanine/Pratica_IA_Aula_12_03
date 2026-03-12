def calcular_media_trimestral(cidade):
    """Calcula a média de temperatura de 4 trimestres."""
    print(f"\n--- Processando: {cidade} ---")
    soma = 0
    
    for i in range(1, 5):
        while True:
            try:
                temp = float(input(f"Digite a temperatura do trimestre {i}: "))
                soma += temp
            except ValueError:
                print("Entrada inválida! Por favor, digite apenas números.")
    return soma / 4

def sugerir_vestimenta(media):
    """Retorna a sugestão de roupa baseada na temperatura média."""
    if media < 15:
        return "Use roupas pesadas de frio (Sobretudos/Lãs)."
    elif 15 <= media <= 25:
        return "Use roupas de meia-estação (Cardigans/Calças)."
    else:
        return "Use roupas leves (Bermudas/Camisetas)."

def main():
    cidades = ["São Paulo", "Curitiba", "Rio de Janeiro"]

    while True:
        print("\n" + "="*25)
        print("    MENU DE CIDADES")
        print("="*25)
        
        for i, cidade in enumerate(cidades):
            print(f"[{i + 1}] {cidade}")
        print(f"[{len(cidades) + 1}] Adicionar nova cidade")
        print("[0] Sair do programa")
        print("="*25)

        escolha = input("Escolha uma opção: ")

        if escolha == '0':
            print("\nEncerrando o programa. Até logo!")
            break
        
        try:
            escolha_int = int(escolha)
            
            # Escolha de uma cidade 
            if 1 <= escolha_int <= len(cidades):
                cidade_escolhida = cidades[escolha_int - 1]
                
            # Adicionar uma nova cidade
            elif escolha_int == len(cidades) + 1:
                cidade_escolhida = input("\nDigite o nome da nova cidade: ").strip().title()
                if cidade_escolhida:
                    cidades.append(cidade_escolhida)
                else:
                    print("Nome inválido. Voltando ao menu...")
                    continue
            else:
                print("\nOpção inválida! Escolha um número do menu.")
                continue
            
            media = calcular_media_trimestral(cidade_escolhida)
            
            print(f"\n> Média Anual de {cidade_escolhida}: {media:.1f}°C")
            print(f"> Sugestão: {sugerir_vestimenta(media)}\n")

        except ValueError:
            print("\nPor favor, digite apenas o número correspondente à opção do menu.")

if __name__ == "__main__":

    main()
