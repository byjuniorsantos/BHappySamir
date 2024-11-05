import time
import sys

mensagem = """
*************************************************
*                                               *
*            Parabéns Samirzão! 🎉🎉🎉          *
*                                               *
*  Que Deus sempre te abençoe, te dê muitos     *
*  anos de vida, saúde e sucesso em tudo que    *
*  fizer.                                       *
*                                               *
*   E lembre-se: que seus bugs sejam raros e    *
*   seus códigos sempre rodem na primeira! 😄   *
*                                               *
*************************************************
"""

for char in mensagem:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.01)  # Ajuste o tempo para alterar a velocidade
