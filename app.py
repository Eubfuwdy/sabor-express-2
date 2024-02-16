from modelos.restaurante import Restaurante

restaurante_pizza = Restaurante('Pizza Express', 'Pizza')
#restaurante_churrasco = Restaurante('Churrasco no Ponto', 'Carne')
#restaurante_hamburguer = Restaurante('Big Kahuna Burguer', 'Hamburgueria')

restaurante_pizza.receber_avaliacao('Marcos', 10)
restaurante_pizza.receber_avaliacao('maria', 8)
restaurante_pizza.receber_avaliacao('will', 5)



def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()