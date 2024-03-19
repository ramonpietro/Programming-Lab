# transforma a primeira letra de uma string em maiúscula
def upper(string):
    return string[0].upper() + string[1:]

# conta quantas vogais existem em uma determinada string
def count(string):
    vogais = 'aeiou'
    return sum(letra in vogais for letra in string.lower())

string = "laboratório"
string_upper = upper(string)

string = "laboratório"
string_count = count(string)

print(string_upper)
print(string_count)