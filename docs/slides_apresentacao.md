**Roteiro de Slides - Apresentação de 15 Minutos**

## Slide 1 - Capa

Título: Testes de Software em Sistema de Locação de Veículos

Informações:

1. Nome do aluno ou grupo.
2. Nome da instituição.
3. Disciplina.
4. Professor(a).
5. Ano.

Tempo sugerido: 1 minuto.

## Slide 2 - Contexto do projeto

Pontos para apresentar:

1. O sistema foi desenvolvido em Python e Flask.
2. O objetivo do sistema é permitir cadastro de clientes, cadastro de veículos, locação e devolução.
3. O projeto foi tratado como estudo de caso para aplicação de testes de software.

Tempo sugerido: 2 minutos.

## Slide 3 - Levantamento de requisitos

Pontos para apresentar:

1. Cadastro de clientes.
2. Login com nome e CPF.
3. Listagem de veículos disponíveis.
4. Locação e devolução de veículos.
5. Cadastro de novos veículos.
6. Requisitos não funcionais: simplicidade, desempenho e consistência do estado.

Tempo sugerido: 2 minutos.

## Slide 4 - Plano de testes

Pontos para apresentar:

1. Objetivo dos testes.
2. Tipos de testes definidos.
3. Ambiente utilizado.
4. Organização da suíte com Pytest.

Tempo sugerido: 2 minutos.

## Slide 5 - Casos de teste

Pontos para apresentar:

1. Cadastro de cliente com sucesso.
2. Bloqueio de CPF duplicado.
3. Login válido.
4. Locação de veículo disponível.
5. Tentativa de locação de veículo indisponível.
6. Devolução de veículo.

Tempo sugerido: 2 minutos.

## Slide 6 - Implementação dos testes automatizados

Pontos para apresentar:

1. Uso do `pytest`.
2. Separação por arquivos e marcadores.
3. Fixtures para limpar o estado entre testes.
4. Teste de regressão criado para o cadastro de veículo.

Tempo sugerido: 2 minutos.

## Slide 7 - Resultados obtidos

Pontos para apresentar:

1. `4` testes de unidade aprovados.
2. `3` testes de integração aprovados.
3. `1` teste de sistema aprovado.
4. `2` testes de aceitação aprovados.
5. `1` teste de regressão aprovado.
6. `1` teste de desempenho aprovado.
7. Resultado final: `12 testes aprovados`.

Tempo sugerido: 2 minutos.

## Slide 8 - Defeitos e melhorias

Pontos para apresentar:

1. Defeito encontrado no cadastro de veículo.
2. Correção realizada com centralização da regra de negócio.
3. Melhorias futuras: banco de dados, autenticação mais segura e testes de interface.

Tempo sugerido: 2 minutos.

## Slide 9 - Demonstração

Sugestão de demonstração ao vivo:

1. Abrir o terminal no projeto.
2. Executar `python -m pytest -m regression -q`.
3. Mostrar que o teste de regressão passa.
4. Se houver tempo, executar `python -m pytest -q` para exibir a suíte completa.

Tempo sugerido: 1 minuto.

## Slide 10 - Conclusão

Pontos para apresentar:

1. O trabalho mostrou a importância do planejamento de testes.
2. Mesmo um sistema pequeno se beneficia de automação.
3. Os testes aumentaram a confiabilidade do sistema.
4. A documentação facilita manutenção e apresentação acadêmica.

Tempo sugerido: 1 minuto.
