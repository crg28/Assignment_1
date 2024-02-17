from automata.fa.dfa import DFA


#Definimos estados:
estados = {'q0','q1','q2'}

#Definimos alfabeto:
alfabeto = {'0','1','b'}

#Definimos transiciones:
transiciones = {
    'q0':{'1':'q1','0':'q0','b':'q0'},
    'q1':{'1':'q0','0':'q2','b':'q1'},
    'q2':{'0':'q1','1':'q2','b':'q2'}
}
#Nota: Se implementa en cada estado un bucle para manejar la cadena vacía.

#Definimos estado inicial:
estado_inicial = 'q0'


#Definimos estados finales:
estados_finales = {'q0'}

#Creamos el automata:
automata = DFA(
    states = estados,
    input_symbols = alfabeto,
    transitions = transiciones,
    initial_state = estado_inicial,
    final_states = estados_finales
)



cadena = str(input(">>>"))


if automata.accepts_input(cadena):
    print(f"The DFA accepts the string '{cadena}'")

elif automata.accepts_input(cadena) == False:
    print(f"The DFA rejects the string '{cadena}'")