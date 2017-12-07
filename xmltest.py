import  xml.etree.ElementTree as ET
from  bs4 import  BeautifulSoup



def write_xml(filename,path,width,height,depth,name,xmin,ymin,xmax,ymax,save_path):
    soup = BeautifulSoup(open("1.xml"),"xml")

    filename__ = soup.find("filename")
    filename__.string = filename

    path__ = soup.find("path")
    path__.string = path

    width__ = soup.find("width")
    width__.string = width

    height__ = soup.find("height")
    height__.string = height

    depth__ = soup.find("depth")
    depth__.string = depth

    name__ = soup.find("name")
    name__.string = name

    xmin__ = soup.find("xmin")
    xmin__.string = xmin

    ymin__ = soup.find("ymin")
    ymin__.string = ymin

    xmax__ = soup.find("ymin")
    xmax__.string =xmax

    ymax__ = soup.find("ymax")
    ymax__.string = ymax


    file = open(save_path+'\\'+filename.split(".")[0] +".xml","w")
    file.write(soup.prettify())

