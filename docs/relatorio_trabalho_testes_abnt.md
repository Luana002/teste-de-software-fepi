INSTITUIÇÃO DE ENSINO SUPERIOR

CURSO DE [NOME DO CURSO]

[NOME DO ALUNO OU DOS ALUNOS]


TESTES DE SOFTWARE EM SISTEMA DE LOCAÇÃO DE VEÍCULOS


[CIDADE]

2026

---

INSTITUIÇÃO DE ENSINO SUPERIOR

CURSO DE [NOME DO CURSO]

[NOME DO ALUNO OU DOS ALUNOS]


TESTES DE SOFTWARE EM SISTEMA DE LOCAÇÃO DE VEÍCULOS

Trabalho acadêmico apresentado à disciplina de [NOME DA DISCIPLINA], do curso de [NOME DO CURSO], como requisito parcial para avaliação.

Professor(a): [NOME DO PROFESSOR]


[CIDADE]

2026

---

**SUMÁRIO**

1 Introdução

2 Levantamento de requisitos

3 Elaboração do plano de testes

4 Criação dos casos de teste

5 Implementação dos testes automatizados

6 Execução dos testes manuais

7 Documentação dos resultados

8 Conclusão

Referências

Apêndice A - Casos de teste resumidos

Apêndice B - Evidências de execução

---

# 1 Introdução

Este trabalho apresenta a documentação do processo de testes aplicado a um sistema web simples de locação de veículos, desenvolvido em Python com o framework Flask e validado com a ferramenta Pytest. O sistema foi projetado para atender operações básicas de uma locadora de pequeno porte, permitindo cadastro de clientes, autenticação por nome e CPF, cadastro de veículos, consulta de disponibilidade, locação e devolução.

O objetivo deste trabalho é demonstrar o ciclo de testes de software desde o levantamento de requisitos até a consolidação dos resultados, contemplando planejamento, elaboração de casos de teste, automação, análise de defeitos e preparação para apresentação em sala.

Para fins acadêmicos, considerou-se como cliente uma locadora de veículos de pequeno porte que necessita de um sistema simples, de fácil operação e com resposta rápida para os fluxos mais frequentes do negócio.

# 2 Levantamento de requisitos

## 2.1 Descrição do sistema

O sistema de locação de veículos possui interface web com quatro telas principais:

1. Tela inicial com login e cadastro de cliente.
2. Tela inicial de veículos disponíveis para locação.
3. Tela de cadastro de veículo.
4. Tela de devolução de veículo.

As regras de negócio estão centralizadas em funções Python responsáveis por cadastrar clientes, cadastrar veículos, verificar disponibilidade, locar veículos e registrar devoluções.

## 2.2 Requisitos funcionais

Tabela 1 - Requisitos funcionais do sistema

| ID | Requisito funcional | Prioridade |
| --- | --- | --- |
| RF01 | O sistema deve permitir cadastrar clientes informando nome, e-mail e CPF. | Alta |
| RF02 | O sistema não deve permitir o cadastro de dois clientes com o mesmo CPF. | Alta |
| RF03 | O sistema deve permitir que o cliente realize login com nome e CPF previamente cadastrados. | Alta |
| RF04 | O sistema deve exibir a lista de veículos com identificação de disponibilidade. | Alta |
| RF05 | O sistema deve permitir a locação de um veículo disponível. | Alta |
| RF06 | O sistema não deve permitir a locação de veículo indisponível. | Alta |
| RF07 | O sistema deve permitir o cadastro de novos veículos por modelo e placa. | Média |
| RF08 | O sistema não deve permitir o cadastro de dois veículos com a mesma placa. | Média |
| RF09 | O sistema deve permitir a devolução de um veículo previamente cadastrado. | Alta |

## 2.3 Requisitos não funcionais

Tabela 2 - Requisitos não funcionais do sistema

| ID | Requisito não funcional | Critério |
| --- | --- | --- |
| RNF01 | O sistema deve possuir interface web simples e objetiva. | Navegação entre telas com botões visíveis e fluxo curto. |
| RNF02 | O sistema deve responder rapidamente às requisições principais. | Carregamento aceitável da listagem mesmo com volume ampliado de veículos. |
| RNF03 | O sistema deve manter consistência do estado em memória durante a execução. | Operações de cadastro, locação e devolução devem refletir imediatamente na interface. |
| RNF04 | O sistema deve ser executável em ambiente local acadêmico. | Execução em Windows com Python 3.x e Flask. |
| RNF05 | O sistema deve ser passível de automação de testes. | Regras de negócio isoladas e rotas acessíveis por cliente de teste Flask. |
| RNF06 | O sistema deve fornecer mensagens de erro compreensíveis. | Respostas para login inválido, CPF duplicado e locação indevida. |

## 2.4 Premissas e restrições

1. O sistema utiliza armazenamento em memória e não possui banco de dados persistente.
2. Os dados são reiniciados a cada nova execução da aplicação.
3. O fluxo de autenticação é simplificado e não utiliza senha criptografada.
4. O projeto foi concebido para fins educacionais, sem objetivo de produção.

# 3 Elaboração do plano de testes

## 3.1 Objetivos dos testes

Os testes foram planejados com os seguintes objetivos:

1. Validar se as principais funcionalidades do sistema atendem aos requisitos definidos.
2. Identificar defeitos de lógica, integração entre camadas e comportamento das rotas web.
3. Garantir que correções realizadas não provoquem regressões.
4. Avaliar se o sistema apresenta desempenho aceitável em cenário simples de carga.
5. Documentar evidências que permitam a apresentação acadêmica do trabalho.

## 3.2 Escopo

Foram incluídos no escopo:

1. Cadastro de cliente.
2. Login do cliente.
3. Cadastro de veículo.
4. Listagem de veículos.
5. Locação de veículo.
6. Devolução de veículo.
7. Regras de duplicidade de CPF e placa.

Não foram incluídos no escopo:

1. Persistência em banco de dados.
2. Controle de permissões por perfil de usuário.
3. Segurança avançada de autenticação.
4. Integração com meios de pagamento.

## 3.3 Estratégia de testes

Tabela 3 - Estratégia de testes adotada

| Tipo de teste | Objetivo | Ferramenta ou abordagem |
| --- | --- | --- |
| Unidade | Validar funções isoladas da regra de negócio. | Pytest |
| Integração | Verificar integração entre rotas Flask e regras de negócio. | Pytest + cliente Flask |
| Sistema | Executar o fluxo principal da aplicação ponta a ponta. | Pytest + cliente Flask |
| Aceitação | Confirmar critérios importantes para o usuário final. | Pytest |
| Regressão | Impedir retorno de bugs já corrigidos. | Pytest |
| Desempenho | Medir comportamento em cenário de carga simples. | Pytest + medição por tempo |
| Manual | Avaliar usabilidade, clareza visual e navegação. | Inspeção e roteiro manual |

## 3.4 Ambiente de testes

Tabela 4 - Ambiente utilizado

| Item | Descrição |
| --- | --- |
| Sistema operacional | Windows 10, versão 10.0.19045.6466 |
| Linguagem | Python 3.x |
| Framework web | Flask |
| Ferramenta de testes | Pytest 9.0.2 |
| Estrutura do sistema | Aplicação web local com armazenamento em memória |

## 3.5 Critérios de entrada e saída

Critérios de entrada:

1. Código-fonte disponível e executável localmente.
2. Dependências instaladas no ambiente Python.
3. Casos de teste definidos e organizados por tipo.

Critérios de saída:

1. Todos os testes automatizados executados.
2. Registro de evidências dos resultados.
3. Relatório consolidado com análise de defeitos e melhorias.

## 3.6 Cronograma proposto

Tabela 5 - Cronograma do trabalho

| Etapa | Período sugerido | Entregável |
| --- | --- | --- |
| Levantamento de requisitos | Semana 1 | Documento de requisitos |
| Plano de testes | Semana 1 | Plano de testes |
| Casos de teste | Semana 2 | Casos documentados |
| Implementação dos testes automatizados | Semana 2 | Scripts em Python |
| Execução dos testes manuais | Semana 3 | Relatório de defeitos |
| Consolidação dos resultados | Semana 3 | Relatório final |
| Preparação da apresentação | Semana 4 | Slides e demonstração |

# 4 Criação dos casos de teste

Os casos de teste foram elaborados com foco nas funcionalidades centrais do sistema e em cenários de sucesso e falha.

Tabela 6 - Casos de teste documentados

| ID | Funcionalidade | Cenário | Pré-condição | Resultado esperado | Tipo |
| --- | --- | --- | --- | --- | --- |
| CT01 | Cadastro de cliente | Cadastrar cliente com dados válidos | Sistema em execução | Cliente registrado com sucesso | Unidade / Integração |
| CT02 | Cadastro de cliente | Tentar cadastrar CPF já existente | Cliente já cadastrado | Sistema deve impedir duplicidade | Unidade / Aceitação |
| CT03 | Login | Realizar login com nome e CPF válidos | Cliente previamente cadastrado | Redirecionamento para a tela inicial de veículos | Integração |
| CT04 | Listagem | Exibir veículos cadastrados | Aplicação carregada | Lista de veículos exibida com status | Sistema |
| CT05 | Locação | Locar veículo disponível | Veículo com status disponível | Veículo passa para indisponível | Unidade / Integração |
| CT06 | Locação | Tentar locar veículo indisponível | Veículo já locado | Operação rejeitada com mensagem de erro | Aceitação |
| CT07 | Devolução | Devolver veículo locado | Veículo previamente locado | Veículo retorna para disponível | Unidade / Sistema |
| CT08 | Cadastro de veículo | Cadastrar novo veículo | Tela de cadastro disponível | Veículo incluído na listagem | Regressão |
| CT09 | Desempenho | Carregar tela com volume ampliado de veículos | Lista populada com 500 veículos adicionais | Tela responde em tempo aceitável | Desempenho |

## 4.1 Passos resumidos dos casos principais

### CT01 - Cadastro de cliente com dados válidos

1. Acessar a tela inicial.
2. Informar nome, e-mail e CPF no formulário de cadastro.
3. Acionar o botão de cadastro.
4. Verificar o redirecionamento para a página inicial.

Resultado esperado: o cliente deve ser incluído na lista interna do sistema.

### CT02 - Bloqueio de CPF duplicado

1. Cadastrar um cliente com CPF válido.
2. Repetir o cadastro usando o mesmo CPF.
3. Observar a resposta da aplicação.

Resultado esperado: o sistema deve retornar mensagem de erro e manter apenas um cliente com o CPF informado.

### CT05 - Locação de veículo disponível

1. Acessar a tela de veículos.
2. Selecionar um veículo marcado como disponível.
3. Acionar o botão de locação.
4. Verificar o retorno à tela inicial.

Resultado esperado: o status do veículo deve mudar para indisponível.

### CT07 - Devolução de veículo

1. Garantir que o veículo esteja locado.
2. Acessar a tela de devolução.
3. Informar a placa do veículo.
4. Confirmar a devolução.

Resultado esperado: o veículo deve voltar ao status disponível.

# 5 Implementação dos testes automatizados

## 5.1 Estrutura dos scripts

Os testes automatizados foram implementados em Python com Pytest e organizados por tipo:

1. `tests/test_sistema_locacao.py` para testes de unidade.
2. `tests/test_integracao.py` para testes de integração.
3. `tests/test_sistema.py` para teste de sistema.
4. `tests/test_aceitacao.py` para testes de aceitação.
5. `tests/test_regressao.py` para teste de regressão.
6. `tests/test_desempenho.py` para teste de desempenho.
7. `tests/conftest.py` para fixtures compartilhadas e preparação do ambiente.

Os marcadores dos testes foram registrados no arquivo `pytest.ini`, permitindo a execução segmentada por categoria.

## 5.2 Regras de implementação adotadas

1. Cada teste deve ser independente dos demais.
2. O estado em memória deve ser limpo entre execuções por meio de fixtures.
3. Os cenários devem refletir requisitos reais do sistema.
4. Um teste de regressão deve proteger correção já realizada.
5. O teste de desempenho deve utilizar limite compatível com o porte acadêmico do projeto.

## 5.3 Comandos de execução

Tabela 7 - Comandos utilizados

| Finalidade | Comando |
| --- | --- |
| Executar toda a suíte | `python -m pytest -q` |
| Executar unidade | `python -m pytest -m unit -q` |
| Executar integração | `python -m pytest -m integration -q` |
| Executar sistema | `python -m pytest -m system -q` |
| Executar aceitação | `python -m pytest -m acceptance -q` |
| Executar regressão | `python -m pytest -m regression -q` |
| Executar desempenho | `python -m pytest -m performance -q` |

## 5.4 Resultados da execução automatizada

Em 27 de março de 2026, a suíte automatizada foi executada localmente com os resultados a seguir.

Tabela 8 - Resultado por categoria

| Categoria | Resultado obtido |
| --- | --- |
| Unidade | 4 testes aprovados |
| Integração | 3 testes aprovados |
| Sistema | 1 teste aprovado |
| Aceitação | 2 testes aprovados |
| Regressão | 1 teste aprovado |
| Desempenho | 1 teste aprovado |
| Total | 12 testes aprovados |

Resultado consolidado da suíte completa: `12 passed in 0.18s`.

# 6 Execução dos testes manuais

## 6.1 Objetivo dos testes manuais

Os testes manuais foram definidos para avaliar aspectos que não são totalmente contemplados pela automação, como clareza de interface, compreensão das mensagens exibidas ao usuário e fluidez da navegação entre páginas.

## 6.2 Roteiro manual proposto

Tabela 9 - Roteiro de testes manuais

| ID | Objetivo | Procedimento | Resultado esperado |
| --- | --- | --- | --- |
| TM01 | Avaliar clareza da tela inicial | Abrir a página de login e cadastro e observar os elementos visuais | O usuário deve compreender onde cadastrar e onde entrar |
| TM02 | Avaliar navegação principal | Navegar entre tela inicial, home, cadastro de veículo e devolução | O fluxo deve ocorrer sem confusão e com links visíveis |
| TM03 | Avaliar mensagens de erro | Forçar login inválido, CPF duplicado e locação de veículo indisponível | As mensagens devem informar o problema de forma clara |

## 6.3 Relatório de defeitos

Durante a validação funcional e a preparação da suíte de testes, foi identificado o defeito descrito na Tabela 10.

Tabela 10 - Defeitos identificados

| ID | Descrição | Severidade | Situação |
| --- | --- | --- | --- |
| D01 | A rota de cadastro de veículo não estava integrada corretamente à regra de negócio, impedindo o fluxo esperado. | Alta | Corrigido |

Análise do defeito D01:

1. Impacto: o usuário não conseguia concluir corretamente o cadastro de um novo veículo.
2. Causa provável: desacoplamento entre a rota Flask e a função de regra de negócio.
3. Ação corretiva: centralização do estado em memória e uso direto das funções do módulo de domínio.
4. Prevenção: criação de teste de regressão específico para a rota de cadastro de veículo.

## 6.4 Observações sobre a execução manual

A presente entrega concentrou-se na automação e na documentação acadêmica do processo de testes. Os cenários manuais foram definidos e preparados para execução em navegador por avaliador humano, permanecendo recomendados para uma apresentação presencial ou banca de avaliação.

# 7 Documentação dos resultados

## 7.1 Consolidação geral

Os resultados demonstraram que o sistema atende aos principais requisitos funcionais previstos para um protótipo acadêmico de locação de veículos. A suíte automatizada validou a lógica central, a integração entre rotas e regras de negócio, o fluxo completo do sistema, os critérios essenciais de aceite, a prevenção de regressão e o tempo de resposta da listagem.

## 7.2 Análise crítica

Pontos positivos observados:

1. Estrutura simples e adequada para demonstração didática.
2. Regras de negócio pequenas e testáveis.
3. Cobertura dos fluxos mais importantes do sistema.
4. Execução rápida da suíte automatizada.

Limitações identificadas:

1. Ausência de persistência em banco de dados.
2. Autenticação simplificada apenas com nome e CPF.
3. Ausência de controle de sessão de usuário.
4. Baixa robustez para cenários de produção.

## 7.3 Melhorias recomendadas

1. Integrar banco de dados relacional ou não relacional para persistência.
2. Implementar autenticação com senha e proteção de sessão.
3. Adicionar validações de formato para CPF, e-mail e placa.
4. Implementar logs de auditoria para locação e devolução.
5. Adicionar testes de interface com ferramenta de automação de navegador.
6. Incluir relatório HTML de testes para documentação visual dos resultados.

# 8 Conclusão

Conclui-se que o processo de testes aplicado ao sistema de locação de veículos foi suficiente para validar os fluxos principais do software e demonstrar, em contexto acadêmico, a importância do planejamento e da automação na garantia da qualidade.

O uso de Pytest permitiu organizar a suíte em categorias distintas, o que facilitou tanto a execução quanto a apresentação dos resultados. Além disso, o trabalho evidenciou que mesmo sistemas pequenos se beneficiam de testes de unidade, integração, sistema, aceitação, regressão e desempenho.

Como continuidade, recomenda-se evoluir o sistema com persistência de dados, autenticação mais segura e testes de interface, elevando o nível de maturidade da solução.

# Referências

PALLETS. Flask Documentation. Disponível em: <https://flask.palletsprojects.com/>. Acesso em: 27 mar. 2026.

PYTEST DEVELOPMENT TEAM. pytest documentation. Disponível em: <https://docs.pytest.org/>. Acesso em: 27 mar. 2026.

PYTHON SOFTWARE FOUNDATION. Python Documentation. Disponível em: <https://docs.python.org/3/>. Acesso em: 27 mar. 2026.

# Apêndice A - Casos de teste resumidos

Tabela 11 - Associação entre requisitos e testes

| Requisito | Testes associados |
| --- | --- |
| RF01 | CT01 |
| RF02 | CT02 |
| RF03 | CT03 |
| RF04 | CT04 |
| RF05 | CT05 |
| RF06 | CT06 |
| RF07 | CT08 |
| RF08 | CT08 |
| RF09 | CT07 |

# Apêndice B - Evidências de execução

Tabela 12 - Evidências registradas

| Execução | Evidência |
| --- | --- |
| Suíte completa | `12 passed in 0.18s` |
| Unidade | `4 passed, 8 deselected` |
| Integração | `3 passed, 9 deselected` |
| Sistema | `1 passed, 11 deselected` |
| Aceitação | `2 passed, 10 deselected` |
| Regressão | `1 passed, 11 deselected` |
| Desempenho | `1 passed, 11 deselected` |
