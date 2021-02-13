class MLModel:
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y
    def preprocess(self):
        pass
    def fit(self):
        pass


class TP_Lin_Reg(MLModel):
    def preprocess(self):
        print("Working in clild class")

x = TP_Lin_Reg(10,20)
print(x.X,x.Y)
x.preprocess()