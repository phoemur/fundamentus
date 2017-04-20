# Bovespa Stock Ratings
Uma plataforma para analisar dados fundamentalistas das ações da BOVESPA utilizando um crawler em python e um database em firebase.
Acesso: https://daniloaleixo.github.io/bovespaStockRatings/


## Análise 
Estou fazendo uma análise baseada nos princípios fundamentalistas do livro [Investidor Inteligente](https://en.wikipedia.org/wiki/The_Intelligent_Investor) do Benjamin Graham: 

* Tamanho Adequado 
  * Patrimônio Líquido menor que R$2bi
* Posição Financeira Forte
  * Liquidez Corrente maior que 1,5
  * Dívida Bruta / Patrimônio Líquido
* Histórico de Dividendos contínuos por, pelo menos, os últimos 20 anos.
  * Ainda não consegui pegar essa informação, estou colocando só o último DY
* Estabilidade nos Ganhos, Nenhum prejuízo nos últimos 10 anos.
  * Ainda não consegui verificar se teve algum prejuízo
* Crescimento nos Ganhos: 10 anos de crescimento nos lucros-por-ação de, pelo menos,
um terço.
  * Ainda não consegui colocar essa informação, mas tenho só 
  * Crescimento no últimos 5 anos maior que 5%
  * ROE > 20%
* Preço sobre Valor de Mercado: O preço da ação inferior a 1,5 x o valor dos ativos
líquidos.
  * P/VPA < 2
* P/L Moderado: O preço da ação inferior a 15x o lucro dos últimos 3 anos
  * P/L < 15
* Teste alternativo: Graham multiplicava o P/L pelo preço sobre o valor de mercado e
verifica se o resultado está abaixo de 22.5
  * Ainda não implementei
