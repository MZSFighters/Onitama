li =[1,2,3,4,5,6,7,8,9,10]

class storelist:

    def __init__(self, li) -> None:
        self.li =li
        input("YOoooo?")


    
    def changeli(self):

        return storelist(self.li[0:5])



sl= storelist(li)
s2 =sl.changeli()
print(s2.li)