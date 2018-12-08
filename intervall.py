class Inter:

    nbphotos = None
    inter = None

    def __init__(self, nbphotos, inter):
        self.nbphotos = nbphotos
        self.inter = inter

    def get_nbphotos(self):
        return self.nbphotos

    def set_nbphotos(self, nbphotos=0):
        self.nbphotos = nbphotos

    def get_inter(self):
        return self.inter

    def set_inter(self, inter=0):
        self.inter = inter
        
