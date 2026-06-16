# Ambiente experimental

Este arquivo registra o ambiente usado nos experimentos do artigo.

## Identificação

- **Local:** máquina local do autor
- **Data da coleta:** 15 jun. 2026
- **Responsáveis pela coleta:** autor/equipe do artigo

## Hardware

| Componente | Especificação |
|---|---|
| Máquina | Dell Inc. XPS 9320 |
| CPU | 13th Gen Intel(R) Core(TM) i7-1360P, 16 CPUs lógicas visíveis no WSL2 |
| Memória RAM | 33.949.044.736 bytes físicos, aproximadamente 32 GB; cerca de 15 GiB visíveis no WSL2 |
| Cache | L1d 384 KiB, L1i 256 KiB, L2 10 MiB, L3 18 MiB, conforme `lscpu` no WSL2 |
| GPU | Intel(R) Iris(R) Xe Graphics, memória reportada de 2.147.479.552 bytes |
| Armazenamento | NVMe KXG80ZNV1T02 NVMe KIOXIA 1024GB, 1.024.203.640.320 bytes |
| Rede | Não avaliada neste experimento |
| Fonte/energia | Não avaliada neste experimento |
| Refrigeração | Não avaliada neste experimento |

## Software

| Item | Versão/descrição |
|---|---|
| Sistema operacional | Ubuntu 24.04 LTS no WSL2, kernel 6.18.33.1-microsoft-standard-WSL2 |
| Linguagem/runtime | Python 3.12.3 |
| Bibliotecas | NumPy 1.26.4; Matplotlib 3.6.3; SciPy 1.11.4; OpenBLAS 0.3.26 |
| Threads OpenBLAS | 16 threads confirmadas por `openblas_get_num_threads` |
| Ferramentas de medição | Scripts `experiments/benchmark_matriz_numpy.py` e `experiments/analisar_benchmark_matriz.py` |
| Ferramenta de IA generativa | Não utilizada diretamente; carga matricial representativa |

## Observações

- O experimento executa multiplicação de matrizes com NumPy/OpenBLAS em CPU.
- A GPU integrada foi identificada, mas não foi usada diretamente pelo benchmark.
- A execução ocorreu no Ubuntu 24.04 LTS via WSL2, com swap disponível e sem isolamento rígido de processos do sistema hospedeiro.
- O uso do WSL2 foi adotado por acessibilidade educacional, por permitir ambiente Linux em máquina comum de estudante.
- Os resultados representam a máquina local testada e não devem ser generalizados para clusters HPC.
