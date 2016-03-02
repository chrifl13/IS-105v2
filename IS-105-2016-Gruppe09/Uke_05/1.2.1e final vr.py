

# liste med oversettelser fra binary til visse variabler og omvendt
binary = {'A': '00', 'B': '1110', 'C': '1111', 'D': '01', 'E': '110', 'F': '10'}
bokstav = {'00': 'A', '1110': 'B', '1111': 'C', '01': 'D', '110': 'E', '10': 'F'}

def binTrans(dictionary, text):
    res = ""
    while text:
        for k in dictionary:
            if text.startswith(k):
                res += dictionary[k]
                text = text[len(k):]
                return res


def stringTrans(string):

    translation = []
    placeholderstring = ""

    for letter in string:
        try:
            translation.append(binary[letter])

        except:
            print("Manglende bokstav")


    return translation




        
if __name__ == "__main__":
        print(stringTrans("A"))
        if __name__ == "__main__":
                print(stringTrans("B"))        
                if __name__ == "__main__":
                        print(stringTrans("C"))        
                        if __name__ == "__main__":
                                print(stringTrans("D"))        
                                if __name__ == "__main__":
                                        print(stringTrans("E"))
                                        if __name__ == "__main__":
                                                print(stringTrans("F"))
                                                                                                
     
     
     
     # 00111011110111010
     
     
 
if __name__ == "__main__":
        print(binTrans(bokstav, "00"))
        if __name__ == "__main__":
                print(binTrans(bokstav, "1110"))
                if __name__ == "__main__":
                        print(binTrans(bokstav, "1111"))
                        if __name__ == "__main__":
                                print(binTrans(bokstav, "01"))
                                if __name__ == "__main__":
                                    print(binTrans(bokstav, "110"))
                                    if __name__ == "__main__":
                                        print(binTrans(bokstav, "10"))                                                                  
                               
                                                                                          
                                                                                            
                                                                                            
