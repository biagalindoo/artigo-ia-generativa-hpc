# Artigo SSCAD-WIC 2026 - IA Generativa e HPC

Repositório de apoio ao artigo científico da disciplina de Infraestrutura de Hardware.

## Tema

**IA Generativa e HPC**

## Evento escolhido

**SSCAD-WIC 2026 - Workshop de Iniciação Científica em Arquitetura de Computadores e Computação de Alto Desempenho**, realizado junto ao XXVII Simpósio em Sistemas Computacionais de Alto Desempenho da SBC.

## Caminho da disciplina

Foi escolhido o **Caminho A - Artigo com submissão**, conforme o roadmap da disciplina.

## Proposta inicial

Investigar como características de infraestrutura de hardware impactam a execução de cargas de IA generativa, relacionando conceitos de HPC, arquitetura de computadores, medições técnicas e experimentos práticos realizados em laboratório.

## Entregáveis previstos

- Artigo em LaTeX no template SBC/SSCAD-WIC.
- PDF final do artigo.
- Dados, scripts ou registros usados nos experimentos.
- Comprovante de submissão, após revisão do professor.

## Ambiente e reprodução

Os resultados atuais foram coletados em Ubuntu 24.04 LTS no WSL2, com Python 3.12.3, NumPy 1.26.4, SciPy 1.11.4, Matplotlib 3.6.3 e OpenBLAS 0.3.26.

Comandos usados para preparar o ambiente Linux:

```bash
sudo apt-get update
sudo apt-get install -y python3-numpy python3-scipy python3-matplotlib libopenblas0-pthread libopenblas-dev
```

Para reproduzir os dados:

```bash
python3 experiments/benchmark_matriz_numpy.py
python3 experiments/analisar_benchmark_matriz.py
```

## Estrutura do repositório

```text
.
├── docs/
│   └── plano-artigo.md
├── experiments/
│   └── README.md
├── data/
│   └── README.md
└── README.md
```

## Fontes de orientação

- Portal da disciplina: https://infra-hw.netlify.app/
- Roadmap da disciplina: https://github.com/0x03c1/fluxo-infra-hw/
- Chamada SSCAD-WIC 2026: https://sscad2026.imd.ufrn.br/cfp_wic/
- Projeto Overleaf: https://www.overleaf.com/4823178581zsbvcxvrwbkg
