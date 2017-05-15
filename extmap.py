# Extension to pic mapping.

def getdata():
    return extensions

def getTop(extension):
    if extension in extensions.keys():
        return extensions[extension]
    else:
        return "http://northeastextension.org/wp-content/uploads/2014/12/PhoneIcon.png"


extensions = {
    "0001": "https://avatars1.githubusercontent.com/u/2021405",
    "0002": "http://3.bp.blogspot.com/-poURVItINz4/UDPtlEOE7sI/AAAAAAAAAUw/VJvZgo1_Tls/s1600/Android-Particle-Ring-Bootanimation-Green.png",
    "0232": "http://3.bp.blogspot.com/-poURVItINz4/UDPtlEOE7sI/AAAAAAAAAUw/VJvZgo1_Tls/s1600/Android-Particle-Ring-Bootanimation-Green.png"
}
