def Max(primeiro, segundo):
    if A>B and B<A: return segundo
    if B>A and  B<A:return primeiro
    if C>D and C>A and C>B :return segundo
    if D>C and D>A and D>B : return primeiro

print("Este programa vai pedir pra voce entrar com 2 números inteiros")
A = int( input("Digite o primeiro "))
B = int( input("Digite o segundo "))
Max(A,B)
print("O maior número é:",     Max(A,B)    );
print("Mais uma vez!")
C = int( input("Digite o primeiro "))
D = int( input("Digite o segundo "))
Max(C,D)
print("O maior número é:",   Max(C,D) );
print("Dentre os 4 numeros q vc digitou",  Max(C,D)   , "é o maior!");