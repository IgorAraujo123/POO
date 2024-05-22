from funcinalidades import *

tv = Televisor('SONY', 'SONY-123')

controle = ControleRemoto(tv)

controle.sintonizaCanal('SBT')
controle.trocarCanal('SBT')

print(tv.canal_atual)