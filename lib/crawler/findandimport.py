from getchuoi import *
from phpaccept import *
def findandimport(noidung,tukhoa,mang):
    timkiem=noidung.find(tukhoa)
    while timkiem!=-1:
        get = getchuoi(noidung,timkiem,'"')
        if phpaccept(get)!="fail":
            if get.rfind("="):
                a= get.rfind("=")+1
                get = get[a:]
            mang.append(get)
        timkiem=noidung.find(tukhoa,timkiem+1+len(tukhoa)+1)

