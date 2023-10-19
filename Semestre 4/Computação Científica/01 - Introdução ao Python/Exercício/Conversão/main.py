from conversor import converter_de_pes_para_metros
from conversor import converter_de_metros_para_pes
from conversor import converter_de_jardas_para_metros
from conversor import converter_de_jardas_para_pes


print("\tMenu\t\n"
      "1 - Pés -> Metros\n"
      "2 - Metros -> Pés\n"
      "3 - Jardas -> Metros\n"
      "4 - Jardas -> Pés\n")

menu_option = int(input("Entre com um opção de conversão: "))

if menu_option == 1:
    value = int(input("Entre com o valor em pés a ser convetido para metros: "))
    result = converter_de_pes_para_metros(value)
    print(f"O resultado da conversão é {result} metros.")

elif menu_option == 2:
    value = int(input("Entre com o valor em metros a ser convetido para pés: "))
    result = converter_de_metros_para_pes(value)
    print(f"O resultado da conversão é {result} pés.")

elif menu_option == 3:
    value = int(input("Entre com o valor em jardas a ser convetido para metros: "))
    result = converter_de_jardas_para_metros(value)
    print(f"O resultado da conversão é {result} metros.")

elif menu_option == 4:
    value = int(input("Entre com o valor em jardas a ser convetido para pés: "))
    result = converter_de_jardas_para_pes(value)
    print(f"O resultado da conversão é {result} pés.")

else:
    print("Opção errada.")
