
def TypeOfFilter(comuna, periodo):
    message = ""
    if (comuna != "" and periodo != ""):
        message = f"SELECT * from fija LEFT OUTER JOIN codigo_comuna_region on fija.cod_com = codigo_comuna_region.cod_com WHERE codigo_comuna_region.comuna = 'ARICA' AND fija.periodo = '2-2019'"
    elif comuna != "" and periodo == "":
        message = f"SELECT * from fija LEFT OUTER JOIN codigo_comuna_region on fija.cod_com = codigo_comuna_region.cod_com WHERE codigo_comuna_region.comuna = 'ARICA'"
    elif comuna == "" and periodo != "":
        message = f"SELECT * from fija WHERE fija.periodo = '2-2019'"

    return message