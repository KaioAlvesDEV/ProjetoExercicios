class Canal:
    def __init__(self, nome, arroba, inscritos):
        self.nome = nome
        self._arroba = arroba
        self.inscritos = inscritos
    
    def inscrever(self):
        self.inscritos += 1
    
    def desinscrever(self):
        
        if self.inscritos > 0:
            self.inscritos -= 1
        else:
            print('Um canal não pode ter menos que 0 inscritos')
            
    @property
    def arroba(self):
        return self._arroba
    
    @arroba.setter
    def mudarArroba(self, novo_arroba):
        
        if len(novo_arroba) > 30:
            print('Um arroba não pode ter mais que 30 caracteres')
            return
        
        if not novo_arroba.startswith("@"):
            novo_arroba = "@" + novo_arroba.replace(" ", "_")
            self._arroba = novo_arroba
