# -- encoding: utf-8 --
import random
import datetime
import liste_dates


class Text_generator():

    def get_text(self):
        if len(self.list_evenement)!=0:
            evenement=self.list_evenement[0]
            #print(evenement)
            self.list_evenement.pop(0)
            if len(self.list_evenement)==0:
                self.update()
            return evenement
        else:
            return ("",["","",""])


        return self.find_text()
    def update(self):
        if self.today in liste_dates.get_data():
            self.data=liste_dates.get_data()[self.today]
        else:
            self.data=[""]
        #print(f"1. data: {self.data}")
        #retire les elément blacklistés
        if self.tag_blacklist!=[]:
            for tag in self.tag_blacklist:
                if tag in self.data:
                    self.data.pop(tag)
        #print(f"2. data-blacklisted tag: {self.data}")
        self.list_evenement=[] #liste de tout les événenemt réparties dans un ordre "aléatoire".
        for tag_tuple in self.sequence_tag:
            self.transition_list_evenement=[] #sers à mélanger des bouts de liste précis
            for tag in tag_tuple:
                if tag in self.data:
                    for evenement in self.data[tag]:
                        self.transition_list_evenement.append((tag, evenement))
                        #print(f"3. transition: {self.transition_list_evenement}")
            self.transition_list_evenement=random.sample(self.transition_list_evenement,k=len(self.transition_list_evenement))
            self.list_evenement.extend(self.transition_list_evenement)
            #print(f"4. list_evenement: {self.list_evenement}")






    def init(self,weight_tag=0, weight_text=1):
        #initalise
        random.seed()
        self.tag_blacklist=[]
        self.today=datetime.datetime.now().strftime("%d.%m")
        self.sequence_tag=[("fetes_nationales",),("histoire","royaute"),("journee",)]
        self.weight_tag=weight_tag
        self.weight_text=weight_text
