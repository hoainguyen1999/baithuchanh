class nguoi(object):
    def getGender(self):
        return "unknow"
class nam(nguoi):
    def getGender(self):
        return "nam"
class nu(nguoi):
    def getGender(self):
        return "nu"
anam=nam()
anu=nu()
print(anam.getGender())
print(anu.getGender())
