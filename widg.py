import ipywidgets as widgets
import matplotlib.pyplot as plt

paises_ocde= pd.array(['Canada', 'United States', 'United Kingdom', 'Denmark', 'Iceland', 'Norway',
          'Turkey','Spain', 'Portugal', 'France', 'Ireland', 'Belgium', 
          'Germany', 'Greece', 'Sweden', 'Switzerland','Austria', 'Netherlands',
          'Luxembourg', 'Italy', 'Japan', 'Finland', 'Australia', 'New Zealand',
          'Mexico', 'Czech Republic (Czechia)','Hungary', 'Poland', 'South Korea',
          'Slovakia', 'Chile', 'Slovenia', 'Israel', 'Estonia', 'Latvia', 'Lithuania',
          'Colombia'],dtype="string")


ocde=df_poblacion.loc[paises_ocde]
#display(ocde)




@widgets.interact()

def print_data(pais1=ocde.index,pais2=ocde.index):
  
    
    tab_titles = ['Confirmados','Recuperados','Decesos' ]
    
    size = widgets.IntSlider(value=50, min=0,max=100,step=1, description='size:')
    oneortwo = widgets.ToggleButtons(options=['Acumulados', 'Nuevos'], description='Casos:')
    threeorfour = widgets.ToggleButtons(options=['Absolutos', 'Relativos'], description='Casos:')
    fiveorsix = widgets.ToggleButtons(options=['Diarios', 'Semanales'], description='Casos:')
    
    def hist1(size, oneortwo, threeorfour, fiveorsix):
        data = pd.DataFrame(np.random.normal(size = size))
        data.plot.hist()
        return
    
    out1 = widgets.interactive(hist1, size=size, oneortwo=oneortwo, threeorfour=threeorfour, fiveorsix=fiveorsix)
    out2 = widgets.interactive(hist1, size=size, oneortwo=oneortwo, threeorfour=threeorfour, fiveorsix=fiveorsix)
    out3 = widgets.interactive(hist1, size=size, oneortwo=oneortwo, threeorfour=threeorfour, fiveorsix=fiveorsix)
    
    tab = widgets.Tab(children = [out1, out2, out3])
    
    for i in range(len(tab_titles)):
        tab.set_title(i, tab_titles[i])
    
    display(tab)

    