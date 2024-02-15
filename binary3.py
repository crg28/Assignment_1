from automata.fa.dfa import DFA


def eliminar_vacios(cadena):
    return cadena.replace('b','')
    
#Definimos estados:
estados = {'q0','q1','q2'}

#Definimos alfabeto:
alfabeto = {'0','1'}

#Definimos transiciones:
transiciones = {
    'q0':{'1':'q1','0':'q0'},
    'q1':{'1':'q0','0':'q2'},
    'q2':{'0':'q1','1':'q2'}
}

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
cadena_nueva = eliminar_vacios(cadena)

if automata.accepts_input(cadena_nueva):
    print(f"The DFA accepts the string '{cadena}'")

elif automata.accepts_input(cadena_nueva) == False:
    print(f"The DFA rejects the string '{cadena}'")