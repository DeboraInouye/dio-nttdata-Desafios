# DESAFIO - ALTERAÇÃO DE MODELO DE DADOS - UNIVERSIDADE 

Alterar o modelo de Banco de Dados para Star Schema a partir do modelo de Universidade apresentado como proposta. O foco da analise está na visão do Professor.


## Resolução
  
- A modelagem foi executada utilizando o SqlDBM.
- Primeiro desenhei o modelo conforme o apresentado no documento proposto no exercício. 

- Em seguida iniciei a alteração para o modelo Star Schema, como solicitado, tendo como base o Professor. Para isso alterei a tabela professor para ser a tabela fato, onde inclui informações necessárias para fazer a relação com as tabelas de dimensão. 

- Para as dimensões considerei uma nova tabela d_Calendario e as tabelas d_Departamento, d_Curso e d_Disciplina, executando alterações necessárias para essas contemplassem informações relevantes para analise.

- As demais tabelas foram retiradas do modelo.
