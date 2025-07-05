from decimal import Decimal
dict_conversion = {
    "h" : {"h" : 1, "min" : 60},
    "d": {"h" : 24, "min": 1440},
    "m":{"d" : 30, "h"  : 720},
    "a":{"m" : 12, "d" : 365}
}

dict_vazao =  {
    "min": 1/60,
    "h": 1,
    "d":  24,
    "m": 720,
    "a": 8640
    }

def converter_vazao(unidade_tempo, vazao):
    return Decimal( Decimal( dict_vazao[ unidade_tempo ] ) * Decimal( vazao ))

def converter_quantidadetempo(unidade_tempo, unidade_convertida, quantidade_tempo):
    return Decimal( Decimal( dict_conversion[unidade_tempo][unidade_convertida] )* Decimal(quantidade_tempo) )