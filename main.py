def processar_dados_cidade(cidade):
    print(f"\n--- Processando: {cidade} ---")
    temperaturas = []
    
    # DADOS
    for i in range(1, 5):
        while True:
            try:
                temp = float(input(f"Digite a temperatura do trimestre {i}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Entrada inválida! Digite apenas números (ex: 25.5).")
                
    media = sum(temperaturas) / 4
    temp_maxima = max(temperaturas)
    temp_minima = min(temperaturas)
    amplitude_termica = temp_maxima - temp_minima
    
    print(f"\n Média Anual: {media:.1f}°C")
    print(f" Pico de Calor: {temp_maxima}°C | Pico de Frio: {temp_minima}°C")
    
    # CONHECIMENTO (Tomada de Decisão baseada na média)
    if media < 15:
        print("Sugestão: Use roupas pesadas de frio (Sobretudos/Lãs).")
    elif 15 <= media <= 25:
        print("Sugestão: Use roupas de meia-estação (Cardigans/Calças).")
    else:
        print("Sugestão: Use roupas leves (Bermudas/Camisetas).")
        
    # NOVO CONHECIMENTO (Tomada de Decisão baseada na amplitude)
    if amplitude_termica >= 15:
        print("Alerta: O clima varia muito nessa cidade. Tenha um guarda-roupa versátil!")
    else:
        print("Clima estável: As temperaturas não sofrem mudanças extremas ao longo do ano.")

def main():
    cidades = ["São Paulo", "Curitiba", "Rio de Janeiro"]

    while True:
        print("\n" + "="*30)
        print("    SISTEMA DE CLIMA")
        print("="*30)
        
        for i, cidade in enumerate(cidades):
            print(f"[{i + 1}] {cidade}")
        
        # Opção dinâmica sempre no final da lista
        print(f"[{len(cidades) + 1}] Adicionar nova cidade")
        print("[0] Sair do programa")
        print("="*30)

        escolha = input("Escolha uma opção: ")

        if escolha == '0':
            print("\nEncerrando o programa...")
            break
        
        try:
            escolha_int = int(escolha)
            
            # Se escolheu uma cidade da lista
            if 1 <= escolha_int <= len(cidades):
                cidade_escolhida = cidades[escolha_int - 1]
                processar_dados_cidade(cidade_escolhida)
                
            # Se escolheu adicionar uma nova cidade
            elif escolha_int == len(cidades) + 1:
                cidade_escolhida = input("\nDigite o nome da nova cidade: ").strip().title()
                if cidade_escolhida:
                    cidades.append(cidade_escolhida)
                    print(f"\nCidade '{cidade_escolhida}' adicionada com sucesso no menu!")
                    # Já processa a cidade recém-adicionada
                    processar_dados_cidade(cidade_escolhida)
                else:
                    print("Nome inválido. Voltando ao menu...")
            
            # Se digitou um número fora das opções
            else:
                print("\nOpção inválida! Escolha um número do menu.")
                
        except ValueError:
            print("\nPor favor, digite apenas números correspondentes ao menu.")

if __name__ == "__main__":
    main()