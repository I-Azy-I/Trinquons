# -- encoding: utf-8 --
import random
import datetime
import liste_dates
class Text_generator():
    def find_text(self):
        choice=random.randint(1,self.rand_sum)
        i=0
        y=0
        #print(tags_items)
        #print(choice)
        while i<choice:
            #print(f"-> {tags_items[y][1]+weight_tag}")
            i=i+(self.tags_items[y][1]*self.weight_text)+self.weight_tag
            y+=1
        data=(self.tags_items[y-1][0],self.data[self.today][self.tags_items[y-1][0]][random.randint(0,len(self.data[self.today][self.tags_items[y-1][0]])-1)])
        return data
    def init_get_text(self):
        #prend la date
        #obtient la liste
        random.seed()

        self.tags_items=[]
        self.rand_sum=(self.weight_tag*len(self.data[self.today]))#créé l'interval aléatoire selon la pondération
        for tag_name, tag_value in self.data[self.today].items():
            self.tags_items.append((tag_name,len(tag_value)))#génère la liste pondérée
            self.rand_sum=self.rand_sum+(len(tag_value)*self.weight_text)
        return True

    def get_text(self, input_day=False):
        if isinstance(input_day,str):
            if self.today != input_day:
                self.today=input_day
                if not self.today in self.data:
                    self.today="0.0"
                    return ("",[""])
                self.init_get_text()
        else:
            if self.today !=datetime.datetime.now().strftime("%d.%m"):
                self.today = datetime.datetime.now().strftime("%d.%m")
                if not self.today in self.data:
                    self.today="0.0"
                    return ("",[""])
                self.init_get_text()

        return self.find_text()

    def init(self,weight_tag=0, weight_text=1):
        self.today="0.0"
        self.data=liste_dates.get_data()
        self.weight_tag=weight_tag
        self.weight_text=weight_text
