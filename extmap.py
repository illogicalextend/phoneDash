
def getTop(extension):
    if extension in extensions.keys():
        return extensions[extension]
    else:
        return "https://cdn1.iconfinder.com/data/icons/simple-icons/256/android-256-black.png"


extensions = {
    "0001": "https://avatars1.githubusercontent.com/u/2021405?v=3&s=460",
    "0002": "http://simpleicon.com/wp-content/uploads/phone-symbol-2-256x256.png"
}
