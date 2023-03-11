class Ponto:
    
    def __init__(self, x, y, ddp) -> None:
        self.coordenada = {"x": x, "y": y}
        self.ddp = ddp
    
    @property
    def ddp(self) -> float:
        return self._ddp
    
    @ddp.setter
    def ddp(self, ddp) -> None:
        if -100 < ddp < 100:
            self._ddp = ddp
        else:
            raise ValueError("ddp inválida!")
    
    def printar(self) -> None:
        print("[", self.coordenada["x"], ",", self.coordenada["y"], "] -> ", self.ddp, "V")
    