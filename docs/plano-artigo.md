# Plano do artigo

## Dados principais

- **Evento:** SSCAD-WIC 2026
- **Template:** Modelo de publicação da SBC, disponível no Overleaf
- **Limite:** até 8 páginas de texto, sem contar referências
- **Idioma:** português
- **Tema do evento:** IA Generativa e HPC
- **Caminho da disciplina:** Caminho A - artigo com submissão

## Título provisório

**Avaliação de Infraestrutura de Hardware para Cargas de IA Generativa em um Contexto de Computação de Alto Desempenho**

## Problema de pesquisa

Cargas de IA generativa exigem grande capacidade de processamento, memória, armazenamento e comunicação entre componentes. Em ambientes de ensino e laboratório, nem sempre há infraestrutura dedicada de larga escala, mas ainda é possível observar gargalos e compreender como decisões de hardware afetam desempenho, eficiência e viabilidade de execução.

## Pergunta de pesquisa

Como características de infraestrutura de hardware observadas em laboratório influenciam o desempenho e a viabilidade de execução de cargas de IA generativa em um contexto introdutório de HPC?

## Objetivo geral

Analisar, com base em experimentos e medições técnicas, a relação entre componentes de infraestrutura de hardware e a execução de cargas associadas à IA generativa, conectando conceitos de arquitetura de computadores e computação de alto desempenho.

## Objetivos específicos

- Levantar os componentes de hardware e software utilizados nos experimentos da disciplina.
- Registrar métricas técnicas relevantes, como tempo de execução, uso de CPU, uso de memória, armazenamento, temperatura, consumo ou utilização de GPU, quando disponível.
- Executar uma carga experimental relacionada a IA generativa ou simulação de carga computacional intensiva.
- Identificar gargalos de infraestrutura a partir dos dados coletados.
- Discutir como os resultados se relacionam com requisitos de HPC para IA generativa.

## Hipótese inicial

A execução de cargas de IA generativa é limitada não apenas pelo processador principal, mas por um conjunto de fatores de infraestrutura, incluindo memória disponível, aceleração por GPU, largura de banda de armazenamento, comunicação entre componentes e capacidade de refrigeração/energia.

## Metodologia proposta

1. **Caracterização do ambiente:** registrar CPU, memória, armazenamento, GPU, sistema operacional, bibliotecas e ferramentas utilizadas.
2. **Definição da carga experimental:** selecionar uma tarefa ligada a IA generativa, como inferência de modelo pequeno, benchmark de matriz/tensor, geração de texto local ou teste sintético compatível com o laboratório.
3. **Coleta de métricas:** medir tempo de execução, uso de recursos e comportamento do sistema durante os testes.
4. **Organização dos dados:** armazenar tabelas, logs e scripts no repositório.
5. **Análise:** comparar resultados, identificar gargalos e relacionar achados com conceitos de HPC.
6. **Discussão científica:** interpretar limites, validade dos testes e relação com cenários reais de IA generativa em HPC.

## Estrutura prevista do artigo

1. **Resumo:** contextualização, objetivo, metodologia, principais resultados e contribuição.
2. **Introdução:** motivação, problema, pergunta de pesquisa, objetivo e organização do artigo.
3. **Fundamentação teórica:** IA generativa, HPC, arquitetura de computadores e infraestrutura para cargas intensivas.
4. **Trabalhos relacionados:** estudos sobre IA generativa, aceleração por GPU, benchmarks e infraestrutura HPC.
5. **Metodologia:** ambiente, ferramentas, procedimentos, métricas e critérios de análise.
6. **Resultados:** tabelas e gráficos com medições realizadas.
7. **Discussão:** interpretação dos resultados, gargalos e limitações.
8. **Conclusão:** síntese, contribuição e trabalhos futuros.
9. **Referências:** fontes acadêmicas e documentação técnica.

## Dados que ainda precisam ser coletados

- Especificações completas das máquinas usadas em laboratório.
- Ferramentas utilizadas durante as aulas.
- Experimentos ou comandos executados.
- Métricas coletadas.
- Prints, logs, tabelas ou arquivos gerados.
- Integrantes da equipe e divisão de responsabilidades.

## Checklist para o próximo commit

- [ ] Confirmar integrantes da equipe.
- [ ] Copiar do Overleaf os arquivos principais do template para o repositório, se o professor permitir.
- [ ] Criar o esqueleto LaTeX do artigo.
- [ ] Preencher resumo provisório e introdução inicial.
- [ ] Registrar o ambiente de laboratório em `experiments/ambiente.md`.
