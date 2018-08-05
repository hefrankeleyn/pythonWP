class Restaurant():
    def __init__(self,res_name,res_people_num):
        self.res_name=res_name
        self.res_people_num=res_people_num
    def show_restaurant(self):
        print(self.res_name+'\t'+self.res_people_num)
