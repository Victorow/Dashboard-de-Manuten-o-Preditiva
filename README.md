Este repositório contém um Dashboard de Manutenção Preditiva desenvolvido utilizando a biblioteca Dash em Python. O dashboard permite visualizar e analisar dados relacionados à manutenção preditiva de máquinas, com foco em variáveis como temperatura, velocidade de rotação, torque e desgaste da ferramenta. O objetivo é fornecer uma interface interativa para monitorar e prever falhas em equipamentos, facilitando a tomada de decisões em processos industriais.

O dashboard oferece funcionalidades interativas, como filtros para selecionar o tipo de produto, o tipo de falha e a faixa de tempo de desgaste da ferramenta. Esses filtros permitem que o usuário explore os dados de forma dinâmica, ajustando as visualizações conforme necessário. Os gráficos exibidos incluem a relação entre o tempo de desgaste da ferramenta e as temperaturas do ar e do processo, a velocidade de rotação, o torque e o desgaste da ferramenta. Cada gráfico é atualizado em tempo real com base nas seleções do usuário.

O código utiliza bibliotecas como Pandas para carregar e manipular a base de dados, Plotly para criar gráficos interativos e Dash para construir a interface web. Além disso, o Dash Bootstrap Components (dbc) é utilizado para estilizar e organizar os componentes do dashboard de forma responsiva.

Para executar o dashboard, é necessário instalar as dependências, como Pandas, Plotly, Dash e Dash Bootstrap Components, utilizando o gerenciador de pacotes do Python. Após a instalação, o dashboard pode ser iniciado executando o script Python, onde o usuário pode interagir com os filtros e visualizar os gráficos atualizados.

O código está estruturado em três partes principais: o carregamento dos dados a partir de um arquivo CSV, a definição do layout do dashboard utilizando componentes HTML e Bootstrap, e as funções de callback que atualizam os gráficos com base nas entradas do usuário. Essas funções garantem que o dashboard seja dinâmico e responsivo às interações.

Contribuições para melhorar o código, adicionar novas funcionalidades ou corrigir bugs são bem-vindas.
Este dashboard é uma ferramenta poderosa para análise de dados de manutenção preditiva, proporcionando insights valiosos para a gestão de ativos e a prevenção de falhas em equipamentos industriais. Explore o código e adapte-o às suas necessidades!

Como Executar
Instalação das Dependências:
Certifique-se de ter Python instalado. Em seguida, instale as bibliotecas necessárias executando:


pip install pandas plotly dash dash-bootstrap-components


Executando o Dashboard:


python app.py
