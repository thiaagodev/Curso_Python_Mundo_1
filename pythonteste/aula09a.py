frase = 'Curso em Vídeo Python'
print(frase[::2])
#frase[13] | frase[13:] | frase[:13] | frase[13:20] | frase[13:20:2]

print("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.""")

print(frase.count('o'))

print(frase.upper())

print(len(frase))

print(frase.replace('Python', 'Android'))

print('Curso' in frase)

print(frase.find('Curso')) # Se não achar, retorna -1, se achar retorna a posição

dividido = frase.split()

print(dividido[3][0]) #Pode mostrar o array das palavras divididas, mostrar apenas uma palavra e uma letra de uma palavra

