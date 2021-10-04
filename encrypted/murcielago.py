def Encode_M(String):
    Abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    Traductor = ['7','B','3','D','5','F','8','H','4','J','K','6','0','N','9','P','Q','2','S','T','1','V','W','X','Y','Z']
    for i in range(26):
        String = String.replace(Abecedario[i],Traductor[i])
    return String
 
def Decode_M(String):
    Abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    Traductor = ['7','B','3','D','5','F','8','H','4','J','K','6','0','N','9','P','Q','2','S','T','1','V','W','X','Y','Z']
    for i in range(26):
        String = String.replace(Traductor[i],Abecedario[i])
    return String