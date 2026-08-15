local_carro = 100
velocidade = 60

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

passou_radar = (
    local_carro == LOCAL_1
    or local_carro == (LOCAL_1 - RADAR_RANGE)
    or local_carro == (LOCAL_1 + RADAR_RANGE)
)

acima_limite = velocidade > RADAR_1

if passou_radar and acima_limite:
    print('Carro passou pelo radar')
    print('Carro com velocidade acima do permitido')
    print('Carro Multado!')

else:
    print('Carro não multado')