import pandas as pd

#classe do modelo
class modelo:      
    def __init__(self):
        self.item = []  #cria lista de submarinos
    
    #método que adiciona itens a lista anterior
    def add_item(self,auv):  
        self.item.append(auv)
    
    #método que exibe todos os submarinos em uma tabela
    def display_all(self):  
        df = pd.DataFrame([vars(auv) for auv in self.item])
        print(df)
    
    #método que exibe um submarino apenas
    def display_one(self,auv_name):  
        for auv in self.item:
            if auv.nome == auv_name:
                df = pd.DataFrame([vars(auv)])
                print(df)
    
    #método que exibe sumarinos por ordem de ano de criação
    def rank_ano(self):    
        df = pd.DataFrame([vars(auv) for auv in self.item])
        df = df.sort_values('ano')
        print(df[['nome', 'ano']])

    #método que exibe sumarinos por ordem de numero de propulsores    
    def rank_thrusters(self):   
        df = pd.DataFrame([vars(auv) for auv in self.item])
        df = df.sort_values('nThru')
        print(df[['nome', 'nThru']])
    


mymodel=modelo()  #inicia iteração do modelo


#classe de sumarino
class AUVs:  
    def __init__(self, nome, nThru, senList, ano, teamSize):
        self.nome = nome            #Attributo de nome
        self.nThru = nThru          #Attributo de número de propulsores
        self.senList = senList      #Attributo de lista de sensores
        self.ano = ano              #Attributo de ano de criação
        self.teamSize = teamSize    #Attributo de numero da equipe responsável


#listas de sensores de cada submarino
luaSen = ["BAR30 (external pressure/depth)", "BMP180 (internal pressure)", "leak sensor"]
brhueSen =["pressure/depth"]

#criação dos objetos representando os submarinos, com suas caracteristicas
BrHue = AUVs("BrHue", 6, brhueSen, 2020, 35)
Lua = AUVs("Lua", 8, luaSen, 2022, 47)

#inserção desses objetos na lista de itens no modelo
mymodel.add_item(BrHue)
mymodel.add_item(Lua)


# TESTES COM MÉTODOS, DESCOMENTAR CASO NECESSÁRIO


#mymodel.display_all()
#mymodel.display_one(BrHue)
#mymodel.rank_ano()
#mymodel.rank_thrusters()

