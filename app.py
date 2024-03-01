from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_pizza = Restaurante('Pizza Express', 'Pizza')
bebida_suco = Bebida('Suco de Laranja', 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_pizza = Prato('Pizza de Calabresa', 12.0, 'calabreasa com queijo')
prato_pizza.aplicar_desconto()
restaurante_pizza.adicionar_no_cardapio(bebida_suco)
restaurante_pizza.adicionar_no_cardapio(prato_pizza)


def main():
    restaurante_pizza.exibir_cardapio

if __name__ == '__main__':
    main()