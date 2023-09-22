import sympy as sp #biblioteca para manipulação simbólica 

#Função para avaliar a composição de duas funções
def evaluate_composition(f, g, x_value, var):
    # f(g(x))
    fg = f.subs(var, g)
    #Avalia f(g(x)) para um valor específico de x
    return fg.subs(var, x_value)

#Variável simbólica #substituir x por um valor específico e depois obter o resultado numérico
x = sp.Symbol('x')

expr_f = input("Digite a expressão para f(x), use ^ para potência: ").replace('^', '**')
expr_g = input("Digite a expressão para g(x), use ^ para potência: ").replace('^', '**')

#Transforma a expressão do usuário em uma forma que o sympy possa entender
f = sp.sympify(expr_f)
g = sp.sympify(expr_g)

#Captura do valor de x para avaliação
x_value = int(input("Digite um valor para x: "))

#Calcula as composições
result_fg = evaluate_composition(f, g, x_value, x)
result_gf = evaluate_composition(g, f, x_value, x)
result_ff = evaluate_composition(f, f, x_value, x)
result_gg = evaluate_composition(g, g, x_value, x)

print(f"(f ∘ g)({x_value}) = {result_fg}")
print(f"(g ∘ f)({x_value}) = {result_gf}")
print(f"(f ∘ f)({x_value}) = {result_ff}")
print(f"(g ∘ g)({x_value}) = {result_gg}")
