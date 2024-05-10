import difflib
import bs4 as bs
import urllib.request

class URL:
    Url1 = "https://www.abc.es/"
    Url2 = "https://www.eldiario.es/"

    source = urllib.request.urlopen(Url1).read()

    source2 = urllib.request.urlopen(Url2).read()

    soup = bs.BeautifulSoup(source, 'lxml')
    soup2 = bs.BeautifulSoup(source2, 'lxml')

    titulos1 = soup.find('h2')
    titulos2 = soup2.find('h2')

    titulos3 = list(titulos1)
    titulos4 = list(titulos2)
class Similitudes(URL):
    # Define a function to calculate the similarity ratio between two strings
    
    @staticmethod
    def string_similarity(str1,str2):
        # Create a SequenceMatcher object with the lowercase versions of the input strings
        result = difflib.SequenceMatcher(a=str1, b=str2)
    
    # Return the similarity ratio between the two strings
        return result.ratio()

    
    # Print the original strings
    print("Original string:")
    print(URL.titulos1)
    print(URL.titulos2)

    # Print a message indicating the similarity between the two strings
    print("Similarity between two said strings:")
    print(string_similarity(URL.titulos3, URL.titulos4))

    # Repeat the process with different pairs of strings

 