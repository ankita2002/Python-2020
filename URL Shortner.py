import pyshorteners 
def short(url):
    link = pyshorteners.Shortener()
    return link.tinyurl.short(url)

if __name__=="__main__":
    url = input("Enter Link:")
    print(f"\n{short(url)}")
