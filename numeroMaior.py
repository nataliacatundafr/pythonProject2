def Max(primeiro, segundo):
    if primeiro>segundo: return primeiro
    else: return segundo
print("Este programa vai pedir pra voce entrar com 2 números inteiros")
A = int( input("Digite o primeiro "))
B = int( input("Digite o segundo "))
X = Max(A,B)
print("O maior número é:",     X   );
print("Mais uma vez!")
C = int( input("Digite o primeiro "))
D = int( input("Digite o segundo "))
Y = Max(C,D)
print("O maior número é:",    Y  );
print("Dentre os 4 numeros q vc digitou",    Max(X,Y)    , "é o maior!");