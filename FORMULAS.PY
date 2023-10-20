# https://www.infoteca.cnptia.embrapa.br/infoteca/bitstream/doc/662332/1/boletim6ATUAL.pdf
# ARAquá – Software para Avaliação de Risco Ambiental de Agrotóxico


##Estimativa da Lixiviação e da Concentração em Água Subterrânea
AF = exp(-tr*k)
#AF é o fator de atenuação, tr representa o tempo de percurso, e k a constante da taxa de degradação do agrotóxico no solo

#A meia-vida do agrotóxico (t½) está relacionada com a cosntante da taxa de degradação (k)conforme a equação:

k= 0,693/t**(1/2)

#O tempo de percurso é calculado pela seguinte equação:

tr = (L*FC/q)*RF

# L representa a distância até a água subterrânea, FC a capacidade de campo do solo e q a taxa de recarga hídrica líquida

# fator de retardamento (RF) do movimento do agrotóxico é obtido pela equação:

RF = 1+(BD*OC*Koc)/FC

# BD é a densidade do solo, OC a fração de carbono orgânico do solo, Koc o coeficiente departição do agrotóxico normalizado para a fração de carbono orgânico.
# A concentração (C) do agrotóxico na água subterrânea é estimada através da expressão:

C = M/(p*d*a)

#M é a massa prevista do agrotóxico chegando até o lençol freático, p representa a porosidade do aqüífero, d é a profundidade de mistura dentro do corpo d’água subterrâneo (assumido como 2 m) e a representa a área de 1 hectare (10.000 m2)





















#Estimativa do Carreamento e da Concentração em Água Superficial
################################
# Estimativa do Carreamento e da Concentração em Água Superficial
################################
#A estimativa da concentração do agrotóxico na água superficial, por sua vez, é feita
#considerando um cenário conforme definido por Parker et al. (1995), no qual uma área cultivada de 10
#hectares está localizada ao redor de um “lago padrão” de 1 hectare e 2 m de profundidade. Nesse
#cenário a precipitação que incide na área cultivada contribui integralmente, através do escoamento
#superficial, para o abastecimento do lago. 
#Assim, os cálculos do carreamento do agrotóxico na superfície do solo e da consequente
#concentração no corpo d’água superficial (na coluna d’água) são feitos a partir dos dados de entrada de
#quantidade (massa) de solo erodido e de volume de água escoada. Esses cálculos são baseados em
#Berezen et al. (2005) e Spadotto et al. (2006).
#Cálculo da perda de agrotóxico no solo erodido (PPs)


PPs = Dx * ps /(Kd+1)* z * d *10**2
#onde, D é a dose do agrotóxico, ps é a massa de solo erodido, Kd é o coeficiente de partição do
#agrotóxico, z é a profundidade do solo que sofreu erosão e d é a densidade do solo.

#Cálculo da perda de agrotóxico na água escoada, portanto em solução (PPa):
PPa = Ca * pa

#Ca é a concentração do agrotóxico na água de escoamento superficial e pa é o volume de água escoada superficialmente.
# Estimativa da concentração do agrotóxico na água (C)

C = PPa + PPs * "lambda"/2

# onde, "lambda" representa a proporção da massa do agrotóxico perdido com o solo erodido que contribui para a sua concentração na coluna água.



##Padrões de Potabilidade e Parâmetros para Organismos Aquáticos
linha_header= ["Ingredinete_Ativo", " Padrao_de_potabilidadeugL", "Parametro_para_Organismos_AquaticosugL"  ] 
coluna_1_ingredientes = ["Diuron", "Malation", "2,4-D_Amina", "Ametrina", "Bentazobe", "Glifosfate", "Atrazina", "Trifluralina"]
Padrao_de_potabilidadeugL = [10, 100, 20, 60, 20, 700, 3, 5]
Parametro_para_Organismos_AquaticosugL = [4900, 200, 100000, 3200, 635, 8300, 4500, 41]
##Fonte: Ministério da Saúde - Portaria no. 518/2004 e 2004 Edition of the Drinking Water Standards and Health Advisories. EPA 822-R-04-005. Office of Water U.S. Environmental Protection Agency Washington, DC.
















