# STATUS desta pasta (2026-06-30)

**Parte A (não-pairwise) e Parte B (NESS perpétuo): execução NÃO concluída e
SUPERSEDIDA** pela tarefa de síntese analítica `../SINTESE_SETE_MORTES/RESULTADO.md`.

O que permanece **válido e citado** pela síntese:
- `campaigns/PARTE_A_NAO_PAIRWISE/A2_ANALISE.md` — **resultado analítico que vale**:
  correlações de **qualquer ordem finita sobre Poisson** caem por Slivnyak–Mecke
  (fecha a porta "não-pairwise sobre Poisson"). Citado na FRONTEIRA §7 e no RESULTADO.

O que **NÃO** é resultado (não usar):
- `gibbs_triple.py` / `validation_gate.json` — o gate de equilíbrio do MC ficou
  VERMELHO (cadeia não-equilibrada, acc baixa) e o scan de escala **não foi rodado**.
  Nenhuma conclusão física foi extraída desta execução parcial. O C4 alto observado no
  gate é **artefato de não-equilíbrio**, não um achado.
- `PARTE_B_NEQ/` — pré-registros e critério travados, **nada executado**. A Parte B foi
  reclassificada como categoria COMBINATÓRIA (ver RESULTADO §2.1 / §3) e fica **atrás**
  de uma tentativa de **teorema combinatório** antes de qualquer motor (pendência).

Os pré-registros e o critério B.2 permanecem como registro de disciplina, caso a
pendência combinatória autorize reabrir a Parte B depois.
