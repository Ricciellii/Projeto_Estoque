
while True:
 produto = input('Digite o nome do produto:  ')
 volume = input('vc deseja registrar a "unidade" ou a "quantidade"?: ')
 unidade = ''
 quantidade = ''

 if volume == "unidade": 
  unidade = int(input('Digite a quantidade em unidades: '))
  valor = float(input('Digite o valor do produto em unidades: '))
  valor_t = unidade * valor
  print('valor total em estoque: ', valor_t)
  print('nome do produto :', produto) 
      
 if volume == "quantidade":
  quantidade = float(input('Digite a quantidade de caixas: '))
  valor = float(input('Digite o valor do produto em caixa: '))
  valor_t = quantidade * valor
  print('valor total de caixas em estoque: ', valor_t)
  print('nome do produto :', produto) 
 
 else:   
    while True: 
     sair = input('deseja adicionar mais um produto: ').lower().startswith('n')
     if sair is True:
         continue
     break
