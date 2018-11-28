

class Model:

    def __init__(self):
        self.xpoint = 200
        self.ypoint = 200

        self.live_view_pictures = []
        self.live_view_current_picture = 0


    def get_live_view_next_picture(self):
    	if len(self.live_view_pictures) == 0:
    		return ""

    	self.live_view_current_picture += 1
    	self.live_view_current_picture = self.live_view_current_picture % len(self.live_view_pictures)
    	return self.live_view_pictures[self.live_view_current_picture]

    def get_live_view_previous_picture(self):
    	if len(self.live_view_pictures) == 0:
    		return ""

    	self.live_view_current_picture -= 1
    	self.live_view_current_picture = self.live_view_current_picture % len(self.live_view_pictures)
    	return self.live_view_pictures[self.live_view_current_picture]

    def set_live_view_pictures(self, pictures):
    	self.live_view_pictures = pictures
