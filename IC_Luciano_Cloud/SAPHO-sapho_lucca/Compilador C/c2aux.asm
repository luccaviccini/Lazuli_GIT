LOAD 0
#PRNAME detetor_top
#DIRNAM "C:"
#DATYPE 0
#NUBITS 32
#NBMANT 22
#NBEXPO 7
#NDSTAC 16
#SDEPTH 5
#NUIOIN 34
#NUIOOU 19
@main LOAD 1
CALL int2float
PLD 455081984 // 2.0
CALL denorm
LOAD float_aux1
EQU float_aux3
LINV
JZ L1else
@L1else @fim JMP fim