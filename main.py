
golpes={'player1':[['DSDP','SDK','P','K'],[['un Taladoken',3],['un Remuyuken',2],['un Puñetazo',1],['una Patada',1]]],
        'player2':[['SAK','ASAP','P','K'],[['un Remuyuken',3],['un Taladoken',2],['un Puñetazo',1],['una Patada',1]]]}

movimientos={'player1':{'W':'Salta','A':'Retrocede','S':'Se agacha','D':'Avanza'},
             'player2':{'W':'Salta','A':'Avanza','S':'Se agacha','D':'Retrocede'}}

players={'player1':'Tonyn','player2': 'Arnaldor'}
  
def quien_inicia(secuencia):
    mov_p1=len([x for x in secuencia['player1']['movimientos'] if x!='']) 
    mov_p2=len([x for x in secuencia['player2']['movimientos'] if x!=''])
    gol_p1=len([x for x in secuencia['player1']['golpes'] if x!=''])
    gol_p2=len([x for x in secuencia['player2']['golpes'] if x!=''])
    p1=((mov_p1+gol_p1)*3 + mov_p1*2 + gol_p1)
    p2=((mov_p2+gol_p2)*3 + mov_p2*2 + gol_p2)
    # print(f'P1={p1} P2={p2}')
    duracion=max([mov_p1,mov_p2,gol_p1,gol_p2])
    if p2<p1:
        print('inicia 2')
        return ['player2','player1',duracion]
    else:
        print('inicia 1')
        return ['player1','player2',duracion]
    
    
def evaluar_secuencia(player,player2,mov, gol,energy):
    secuencia=mov+gol
    golpe=''
    for x in range(0,len(golpes[player][0])):
        if golpes[player][0][x] in secuencia:
            golpe=golpes[player][1][x]
            for i in range(len(golpes[player][0][x])):
                secuencia = secuencia.replace(golpes[player][0][x][i],"")
            break
    if secuencia!='':
        print(f'{players[player]} se mueve', end=' ')
        if golpe!='':
            print(f' y pega {golpe[0]} a {players[player2]}')
            energy[player2]-=golpe[1]
        else:
            print(' ')
    elif golpe!='':
        print(f'{players[player]} pega {golpe[0]} a {players[player2]}')
        energy[player2]-=golpe[1]
    return energy
    
    
def pelea(secuencia):
    inicio=quien_inicia(secuencia)
    print('Se inicia la Pelea....')
    energy={'player1':6,'player2':6}  
    for i in range(0,inicio[2]):
        if len(secuencia[inicio[0]]['movimientos'])>i and len(secuencia[inicio[0]]['golpes'])>i:
            energy=evaluar_secuencia(inicio[0],inicio[1],secuencia[inicio[0]]['movimientos'][i],secuencia[inicio[0]]['golpes'][i],energy)
            # print(energy)
            if energy[inicio[1]]<=0:
                print(f'==>{players[inicio[0]]} Gana la pelea y aún le queda {energy[inicio[0]]} de Energía.')
                break
        if len(secuencia[inicio[1]]['movimientos'])>i and len(secuencia[inicio[1]]['golpes'])>i:
            energy=evaluar_secuencia(inicio[1],inicio[0],secuencia[inicio[1]]['movimientos'][i],secuencia[inicio[1]]['golpes'][i],energy)
            # print(energy)
            if energy[inicio[0]]<=0:
                print(f'==>{players[inicio[1]]} Gana la pelea y aún le queda {energy[inicio[1]]} de Energía.')
                break
            
    if energy[inicio[0]]>0 and energy[inicio[1]]>0:
        if energy[inicio[0]]<energy[inicio[1]]:
            print(f'==>{players[inicio[1]]} Gana la pelea por tiempo,  Energías: {players[inicio[1]]}/{energy[inicio[1]]} vs {players[inicio[0]]}/{energy[inicio[0]]}')
        if energy[inicio[1]]<energy[inicio[0]]:
            print(f'==>{players[inicio[0]]} Gana la pelea por tiempo,  Energías: {players[inicio[0]]}/{energy[inicio[0]]} vs {players[inicio[1]]}/{energy[inicio[0]]}')


if __name__=='__main__':
    
    secuencia={"player1":{"movimientos":["D","DSD","S","DSD","SD"],"golpes":["K","P","","K","P"]},
              "player2": {"movimientos":["SA","SA","SA","ASA","SA"],"golpes":["K","","K","P","P"]}} 
    # secuencia={"player1":{"movimientos":["SDD", "DSD", "SA", "DSD"] ,"golpes":["K", "P", "K", "P"]},
    #           "player2":{"movimientos":["DSD", "WSAW", "ASA", "", "ASA", "SA"],"golpes":["P", "K", "K", "K", "P", "k"]}}  
    # secuencia={"player1":{"movimientos":["DSD", "S"] ,"golpes":[ "P", ""]}, 
    #            "player2":{"movimientos":["", "ASA", "DA", "AAA", "", "SA"],"golpes":["P", "", "P", "K", "K", "K"]}} 

    pelea(secuencia)