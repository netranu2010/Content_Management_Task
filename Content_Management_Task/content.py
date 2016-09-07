class content():
    """description of class"""
    pageid="1"
    contentid="1.1"
    content="This is page description"
 
def __init__(self, realpart, imagpart):
    self.r = realpart
    self.i = imagpart


def get_services(id):
   a = "this content is returned from content class %s" %id
   return a

def save_services():
    b = "this will save service"
    return b


