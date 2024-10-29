DESAFIO - Transformação de Dados

RESOLUÇÃO

	1 - Azure
		- Criando conta
		- Configuração do banco

	2 - Criando banco de dados a partir do script fornecido:
		script_db_company.sql

	3 - Inserindo dados a partir do script:
		insercao_de_dados_e_queries.sql

> Integração do Power BI para carregar os dados do Azure

> Alterações Efetuadas 

	Tabela Employee
		- FName,Minit e Lname : mesclei as colunas separando por espaço e renomeando a 
			coluna para Nome_Empregado

		- Ssn renomeada para Matricula_empregado 

		- bdate renomeada para Dt_Nasc_empregado e tipo data

		- Address dividi as colunas separando numero, logradouro, cidade e estado
   		
		- Salary alterado para Salario_empregado, com tipo decimal fixo
    
		- Super_ssn alterado nome para Matricula_gerente
   



	Tabelas dept_locations, departament, Project, dependent
		 - Alterado cabeçalho das colunas
		 - colunas de data alterado para date

	

	Mesclei as tabelas employee com departament criando uma nova tabela FuncionarioDpto
		- 
		- inclusão do gerente no registro que constava nulo
		- mesclei as tabelas employee e departament (junção externa 		esquerda, através do campo Matricula_gerente), criando uma nova 		"consulta" e renomeei para 'FuncionarioDpto'
		- drill down em localizacao na tabela de departamento, mesclei 		os campos nome_depto e local_depto para torna-los únicos.
		- alteração da coluna hora para número
		- adicionei o nome do gerente através da matricula_gerente
		- removi colunas desnecessárias


	Para saber quantos fucnionários são atribuídos a cada gerente:

select e.Super_ssn as Ssn_mngr, CONCAT(e2.Fname,' ',e2.Lname) as name_mngr,
count(*) as total_employees
from employee e
left join employee e2 on e.Super_ssn = e2.Ssn
where e.Super_ssn is not null
group by e.Super_ssn;


	 Desenvolvi um relatório no Power Bi o qual disponibilizei a visão em PDF.