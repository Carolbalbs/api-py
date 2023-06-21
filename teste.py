import re as regex

# pip install venv
# pip install spacy
# pip install nome do pacote
# criar repositorio - usar comando git init


#1 - Ordem textual correta(resumo nao ser mostrado depois da da introducao)
def ordem_estrutura():
 return print('ordem da estrutura')

#2- Vizualizações de exemplos 
def exemplos():
    opcoes = ['• titulo','• resumo','• palavras_chave','• contexto','• lacuna','• proposito','• metodologia','• resultado','• conclusao']
    print('Exemplos disponiveis:\n', '\n '.join(opcoes))
    
    exemplo = input('Qual padrão de texto voce deseja visualizar?')
    
    if exemplo == 'titulo':
     titulo = "<TITULO>Lorem ipsum dolor sit amet</TITULO>"

     padrao = regex.compile(">.*<")

     x = regex.findall(padrao,titulo)
     print(x)
     
    elif exemplo == 'resumo':
     resumo = "<RESUMO>Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus ullam alias quidem nam omnis rem tempore quam? Quis quia dolorum temporibus labore ea, praesentium vero, veniam sit inventore explicabo velit.</RESUMO>"
   
     padrao = regex.compile(">.*<")

     x = regex.findall(padrao, resumo)
     print(x)
  
    elif exemplo == 'palavras_chave':
     palavras_chave  ="<PALAVRAS_CHAVE>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Laudantium quis sapiente omnis inventore est eaque provident minus expedita harum optio, veritatis cum dolore recusandae. Libero reiciendis cupiditate quae quia labore.\n Lorem ipsum dolor sit amet, consectetur adipisicing elit. Laudantium quis sapiente omnis inventore est eaque provident minus expedita harum optio, veritatis cum dolore recusandae. Libero reiciendis cupiditate quae quia labore.</PALAVRAS_CHAVE>"
    
     padrao = regex.compile(">.*<")

     x = regex.findall(padrao, palavras_chave)
     print(x)
    elif exemplo == 'contexto':
     contexto = "<CONTEXTO>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Rerum quos omnis modi perferendis vel iure. Delectus autem blanditiis praesentium quis beatae consequatur iure nobis quaerat facilis sequi, recusandae suscipit doloremque!</CONTEXTO>"
     padrao = regex.compile(">.*<")

     x = regex.findall(padrao, contexto)
     print(x)
    elif exemplo == 'lacuna':
     lacuna = "<LACUNA>Lorem ipsum dolor sit amet consectetur adipisicing elit. Soluta quaerat maiores sed ducimus impedit quo aperiam culpa non eaque et quisquam quam ab dolorem, quia sequi doloremque, quibusdam labore repellat?</LACUNA>"
     padrao = regex.compile(">.*<")

     x = regex.findall(padrao, lacuna)
     print(x)
    elif exemplo == 'proposito':
     proposito = "<PROPOSITO>Lorem ipsum dolor sit amet consectetur adipisicing elit. Soluta quaerat maiores sed ducimus impedit quo aperiam culpa non eaque et quisquam quam ab dolorem, quia sequi doloremque, quibusdam labore repellat?</PROPOSITO>"
     padrao = regex.compile(">.*<")

     x = regex.findall(padrao, proposito)
     print(x)
    elif exemplo == 'metodologia':
     metodologia = "<METODOLOGIA>Lorem ipsum dolor sit amet consectetur adipisicing elit. Soluta quaerat maiores sed ducimus impedit quo aperiam culpa non eaque et quisquam quam ab dolorem, quia sequi doloremque, quibusdam labore repellat?</METODOLOGIA>"
     padrao = regex.compile(">.*<")

     x = regex.findall(padrao, metodologia)
     print(x)
    elif exemplo == 'resultado':
     resultado = "<RESULTADOS>Lorem ipsum dolor sit amet consectetur adipisicing elit. Soluta quaerat maiores sed ducimus impedit quo aperiam culpa non eaque et quisquam quam ab dolorem, quia sequi doloremque, quibusdam labore repellat?</RESULTADOS>"
     padrao = regex.compile(">.*<")

     x = regex.findall(padrao, resultado)
     print(x)
    elif exemplo == 'conclusao':        
     conclusao = "<CONCLUSAO>Lorem ipsum dolor sit amet consectetur adipisicing elit. Soluta quaerat maiores sed ducimus impedit quo aperiam culpa non eaque et quisquam quam ab dolorem, quia sequi doloremque, quibusdam labore repellat?</CONCLUSAO>"
     padrao = regex.compile(">.*<")

     x = regex.findall(padrao, conclusao)
     print(x)    
    else:
        print('Exemplo invalido')



    
#3 - Contagem de caracteres e contagem de palavras
def contagem():
 texto_usuario = input("Digite um texto: ")

 # Contagem de palavras
 palavras = texto_usuario.split()
 quantidade_palavras = len(palavras)

 # Contagem de caracteres
 quantidade_caracteres = len(texto_usuario)

 # Imprime o resultado
 print("Quantidade de palavras:", quantidade_palavras)
 print("Quantidade de caracteres:", quantidade_caracteres)

   
print('MENU')
escolha = input('Digite o que deseja realizar: \n1 - Ordem textual correta \n2 - Vizualizações de exemplos\n3 - Contagem de caracteres e contagem de palavras\n')
if escolha == '1':
    ordem_estrutura() 
elif escolha == '2':
     exemplos()  
elif escolha == '3':
    contagem()
else:
    print('Opcao invalida')
    


