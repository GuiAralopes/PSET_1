# PSET 1 Linguagens de programação - Algoritmo de Luhn.

## O projeto deste Problem Set se baseia em validar cartões de crédito pela verificação através do algoritmo de Luhn. 
> "O algoritmo Da fórmula LUHN FOI desenvolvido por um cientista alemão chamado Hans Peter Luhn EM 1954 enquanto trabalhava Como pesquisador Na IBM.﻿﻿ O funcionamento do algoritmo é Baseado Na aritmética modular, uma técnica matemática desenvolvida por Carl Friedrich Gauss no início do século XIX." -source EMMTRADE
> 
O projeto além de validar um cartão, ele também verifica de qual bandeira tal número de cartão pertence, podendo retornar:

| Número cartão         | Retorno      |
| :-------------------- | :----------- |
| `378282246310005`     | `AMEX`       |
| `2223016768739313`    | `Mastercard` |
| `4111111111111111`    | ` Visa`      |
|     `6176292929`      | `INVÁLIDO`   |
