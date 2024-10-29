# DESAFIO - USANDO A SAMPLE FINANCIALS - ALTERAR MODELO PARA STAR SCHEMA

## RESOLUÇÃO

> Transformação de dados da tabela Financials: nomes dos campos, tipo dos campos

> Criando dimensões:
	> d_Produtos: duplicada a tabela financials e aplicada a função de agrupamento, conforme apresentado no documento de instrução:
		'Unidades Vendidas': Soma do 'Unidades Vendidas' por produtp
		'Valor Máximo de Venda': calculou o valor maximo de 'Valor de Vendas' por produto
		'Valor Mínimo de Vendas': calculou o valor minimo de 'Valor de Vendas' por produto
		'Média do Valor de Vendas': calculou a media de 'Valor de Vendas' agrupada por produto
		'Mediana do Valor de Vendas': calculou a mediana de 'Valor de Vendas' agrupada por produto
		'Média do Valor de Manufatura': calculou a media de 'Preço de Produção' agrupada por produto

Em seguida foi gerado o Id_produto para esta tabela. Adicionando uma coluna condicional de acordo com a descrição do produto.

				
	> D_Produtos_Detalhes: Gerado a partir da Mescla de tabelas Financials com d_Produtos, removida colunas desnecessárias

	> D_Descontos: Gerado a partir da Mescla de tabelas Financials com d_Produtos, removidas as colunas desnecessárias
		
	> D_Detalhes (*): gerada a partir da duplicação da tabela Financials

	> F_Vendas Gerado a partir da Mescla de tabelas Financials com d_Produtos, em seguinda foi adicionado uma coluna de índice para o SK_id. 

	> D_Calendário – Criada por DAX :
		D_Calendario = 
    			ADDCOLUMNS(
       				 CALENDAR(DATE(2013, 1, 1), DATE(2014, 12, 31)),
        			"Ano", YEAR([Date]),
        			"Mês", MONTH([Date]),
        			"Nome_Mês", FORMAT([Date], "MMMM"),
       				"Dia_Semana", FORMAT([Date], "dddd"),
        			"Quarter" , QUARTER([Date])
    			)

	

