class Ponto:
    
    def __init__(self, x:int, y:int, ddp:float) -> None:
        self.coordenada = {"x": x, "y": y}
        self.ddp = ddp
    
    @property
    def ddp(self) -> float:
        return self._ddp
    
    @ddp.setter
    def ddp(self, ddp:float) -> None:
        if -100 < ddp < 100:
            self._ddp = ddp
        else:
            raise ValueError("ddp inválida!")
    
    def printar(self) -> None:
        print("[", self.coordenada["x"], ",", self.coordenada["y"], "] -> ", self.ddp, "V")
    
    
# o ponto possui um dicionário com as coordenadas x e y, além de uma ddp associada a elas