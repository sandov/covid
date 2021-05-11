def mostrar_resumen_tasa(tipo, tasa_sorted):
    tasa_ocde_sorted = tasa_sorted.loc[paises_ocde].sort_values()
    tasa_latam_sorted = tasa_sorted.loc[paises_latam].sort_values()
    print('Resumen datos de', tipo, 'a nivel internacional:')
    print(tasa_sorted.describe(), '\n')
    print('Resumen datos de', tipo, 'entre países de la OCDE:')
    print(tasa_ocde_sorted.describe(), '\n')
    print('Resumen datos de', tipo, 'entre países latinoamericanos:')
    print(tasa_latam_sorted.describe(), '\n')
    print('Tasa de', tipo, 'en Chile:', tasa_sorted.at['Chile'])
    print('Puesto de Chile en el ranking mundial de', tipo + ":",
          str(tasa_sorted.index.get_loc('Chile')) + '/' +
          str(len(tasa_sorted.index)))
    print('Puesto de Chile entre países de la OCDE en', tipo + ":",
          str(tasa_ocde_sorted.index.get_loc('Chile')) + '/' +
          str(len(tasa_ocde_sorted.index)))
    print('Puesto de Chile entre países de latinoamérica en', tipo + ":",
          str(tasa_latam_sorted.index.get_loc('Chile')) + '/' +
          str(len(tasa_latam_sorted.index)), ' \n')

paises_ocde = ['Australia', 'Austria', 'Belgium', 'Canada', 'Chile', 'Colombia',
               'Czechia', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany',
               'Greece', 'Hungary', 'Iceland', 'Ireland', 'Israel', 'Italy',
               'Japan', 'Korea, South', 'Latvia', 'Lithuania', 'Luxembourg',
               'Mexico', 'Netherlands', 'New Zealand', 'Norway', 'Poland',
               'Portugal', 'Slovakia', 'Slovenia', 'Spain', 'Sweden',
               'Switzerland', 'Turkey', 'US', 'United Kingdom']

paises_latam = ['Argentina', 'Bolivia', 'Brazil', 'Chile',
                'Colombia', 'Costa Rica', 'Ecuador', 'El Salvador',
                'Guatemala', 'Guyana', 'Honduras', 'Mexico', 'Nicaragua',
                'Panama', 'Paraguay', 'Peru', 'Suriname', 'Uruguay',
                'Venezuela']
                

