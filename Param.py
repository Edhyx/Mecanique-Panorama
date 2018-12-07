class Param:
    iso = None
    app = None
    
    def __init__(self,iso,app):
        self.iso = iso
        self.app = app
    
    def get_iso(self):
        return self.iso
    
    def set_iso(self,iso=0):
        self.iso = iso


    def get_app(self):
        return self.app
    
    def set_app(self,app=0):
        self.app = app
        