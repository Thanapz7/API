from conDB import Con 
c = Con

class Action:
    def getHW():
        data = c.getHW()
        return data
    
    def updateHW(ID, status):
        data = c.updateHW(ID, status)
        return data
    
    def updateHWvalue(ID, value):
        data = c.updateHWvalue(ID, value)
        return data
    
    def selectHW_byid(ID):
        data = c.selectHW_byid(ID)
        return data
    
    def insertHW(name, hw_name):
        data = c.insertHW(name, hw_name)
        return data
    
    def deleteHW(ID):
        data = c.deleteHW(ID)
        return data
    
    
            