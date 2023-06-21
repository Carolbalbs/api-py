import re as regex
import random

# pip install venv
# pip install spacy
# pip install nome do pacote
# criar repositorio - usar comando git init


#1 - Ordem textual correta: Contexto, Lacuna, Propósito, Metodologia, Resultado, Conclusão
def ordem_estrutura():
 return print('ordem da estrutura')

#2- Visualizações de exemplos
def exemplos():
    opcoes = ['• titulo','• resumo','• palavras_chave','• contexto','• lacuna','• proposito','• metodologia','• resultado','• conclusao']
    print('Exemplos disponiveis:\n', '\n '.join(opcoes))
    
    exemplo = input('Qual padrão de texto voce deseja visualizar?')
    
    if exemplo == 'titulo':
     titulo = ['<TITULO>Dificuldades em Conceitos Básicos de Matemática no Ensino Superior: Uma Revisão Sistemática</TITULO>']
   
     padrao = regex.compile(">.*<")

     x = regex.findall(padrao,titulo)
     x.random.choice(titulo)
     print(x)
     
    elif exemplo == 'resumo':
     resumo = "<RESUMO>Este artigo completo apresenta o processo e os resultados de uma revisão sistemática sobre as dificuldades dos alunos em conceitos básicos de matemática no ensino superior. O principal objetivo desta revisão é identificar os tópicos básicos de matemática nos quais os alunos enfrentam mais dificuldades. Essa dura relação com a matemática começa muito antes da universidade, pode ser identificada nos primeiros níveis, durante a educação básica, quando os alunos são introduzidos à aritmética. Segundo estudos, na maioria dos casos, existem dois tipos de problemas que podem explicar essa dificuldade de aprendizagem: o primeiro é identificado quando está relacionado ao desenvolvimento cognitivo da criança, enquanto o segundo tipo de dificuldade comum de aprendizagem está relacionado a problemas fora do ambiente escolar criança ou em outro problema específico. Também, identificou-se na literatura que, ao estudar matemática, uma gama de sentimentos pode ser desencadeada nos alunos, desde sentimentos positivos até sentimentos negativos. Essa percepção pode explicar por que alunos com histórico de reprovação em matemática acreditam que não são capazes de construir o conhecimento necessário para cursar o ensino superior em cursos STEM (ciências, tecnologia, engenharia e matemática). No Brasil, por exemplo, apenas 17% dos alunos se inscrevem em um curso STEM, enquanto em países da América do Norte e Europa esse percentual chega a 24%. Portanto, esta revisão sistemática foi realizada com o objetivo de analisar as publicações sobre as dificuldades relacionadas à matemática básica, enfrentadas pelos alunos do ensino superior. Os resultados indicam vários níveis de dificuldade em uma variedade de tópicos de matemática, incluindo funções e frações em situações práticas. Os artigos analisados ​​também apontam para o fato de que os problemas são enfrentados quando os alunos estão no ensino fundamental e persistem no ensino superior.</RESUMO>"
   
     padrao = regex.compile(">.*<")

     x = regex.findall(padrao, resumo)
     print(x)
  
    elif exemplo == 'palavras_chave':
     palavras_chave  ="<PALAVRAS_CHAVE>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Laudantium quis sapiente omnis inventore est eaque provident minus expedita harum optio, veritatis cum dolore recusandae. Libero reiciendis cupiditate quae quia labore.\n Lorem ipsum dolor sit amet, consectetur adipisicing elit. Laudantium quis sapiente omnis inventore est eaque provident minus expedita harum optio, veritatis cum dolore recusandae. Libero reiciendis cupiditate quae quia labore.</PALAVRAS_CHAVE>"
    
     padrao = regex.compile(">.*<")

     x = regex.findall(padrao, palavras_chave)
     print(x)
    elif exemplo == 'contexto':
     contexto = "<CONTEXTO>Este artigo completo apresenta o processo e os resultados de uma revisão sistemática sobre as dificuldades dos alunos em conceitos básicos de matemática no ensino superior. O principal objetivo desta revisão é identificar os tópicos básicos de matemática nos quais os alunos enfrentam mais dificuldades. Essa dura relação com a matemática começa muito antes da universidade, pode ser identificada nos primeiros níveis, durante a educação básica, quando os alunos são introduzidos à aritmética. Segundo estudos, na maioria dos casos, existem dois tipos de problemas que podem explicar essa dificuldade de aprendizagem: o primeiro é identificado quando está relacionado ao desenvolvimento cognitivo da criança, enquanto o segundo tipo de dificuldade comum de aprendizagem está relacionado a problemas fora do ambiente escolar criança ou em outro problema específico.</CONTEXTO>"
     padrao = regex.compile(">.*<")

     x = regex.findall(padrao, contexto)
     print(x)
    elif exemplo == 'lacuna':
     lacuna = "<LACUNA>Também, identificou-se na literatura que, ao estudar matemática, uma gama de sentimentos pode ser desencadeada nos alunos, desde sentimentos positivos até sentimentos negativos. Essa percepção pode explicar por que alunos com histórico de reprovação em matemática acreditam que não são capazes de construir o conhecimento necessário para cursar o ensino superior em cursos STEM (ciências, tecnologia, engenharia e matemática). No Brasil, por exemplo, apenas 17% dos alunos se inscrevem em um curso STEM, enquanto em países da América do Norte e Europa esse percentual chega a 24%.</LACUNA>"
     padrao = regex.compile(">.*<")

     x = regex.findall(padrao, lacuna)
     print(x)
    elif exemplo == 'proposito':
     proposito = "<PROPOSITO>O principal objetivo desta revisão é identificar os tópicos básicos de matemática nos quais os alunos enfrentam mais dificuldades.</PROPOSITO>"
     padrao = regex.compile(">.*<")

     x = regex.findall(padrao, proposito)
     print(x)
    elif exemplo == 'metodologia':
     metodologia = "<METODOLOGIA>Portanto, esta revisão sistemática foi realizada com o objetivo de analisar as publicações sobre as dificuldades relacionadas à matemática básica, enfrentadas pelos alunos do ensino superior.</METODOLOGIA>"
     padrao = regex.compile(">.*<")

     x = regex.findall(padrao, metodologia)
     print(x)
    elif exemplo == 'resultado':
     resultado = "<RESULTADOS>Os resultados indicam vários níveis de dificuldade em uma variedade de tópicos de matemática, incluindo funções e frações em situações práticas.</RESULTADOS>"
     padrao = regex.compile(">.*<")

     x = regex.findall(padrao, resultado)
     print(x)
    elif exemplo == 'conclusao':        
     conclusao = "<CONCLUSAO>Os artigos analisados ​​também apontam para o fato de que os problemas são enfrentados quando os alunos estão no ensino fundamental e persistem no ensino superior.</CONCLUSAO>"
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
    


