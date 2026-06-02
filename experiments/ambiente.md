# Ambiente experimental

Este arquivo registra o ambiente usado nos experimentos do artigo.

## Identificação

- **Local:** máquina local do autor
- **Data da coleta:** 2 jun. 2026
- **Responsáveis pela coleta:** a preencher

## Hardware

| Componente | Especificação |
|---|---|
| Máquina | Dell Inc. XPS 9320 |
| CPU | 13th Gen Intel(R) Core(TM) i7-1360P, 12 núcleos, 16 threads, 2,2 GHz |
| Memória RAM | 33.949.044.736 bytes, aproximadamente 32 GB |
| GPU | Intel(R) Iris(R) Xe Graphics, memória reportada de 2.147.479.552 bytes |
| Armazenamento | NVMe KXG80ZNV1T02 NVMe KIOXIA 1024GB, 1.024.203.640.320 bytes |
| Rede | Não avaliada neste experimento |
| Fonte/energia | Não avaliada neste experimento |
| Refrigeração | Não avaliada neste experimento |

## Software

| Item | Versão/descrição |
|---|---|
| Sistema operacional | Microsoft Windows 11 Pro 10.0.26200, 64 bits |
| Linguagem/runtime | Python 3.11.9 |
| Bibliotecas | NumPy 2.1.2; Matplotlib 3.10.9 |
| Ferramentas de medição | Scripts `experiments/benchmark_matriz_numpy.py` e `experiments/analisar_benchmark_matriz.py` |
| Ferramenta de IA generativa | Não utilizada diretamente; carga matricial representativa |

## Observações

- O experimento executa multiplicação de matrizes com NumPy em CPU.
- A GPU integrada foi identificada, mas não foi usada diretamente pelo benchmark.
- Os resultados representam a máquina local testada e não devem ser generalizados para clusters HPC.
