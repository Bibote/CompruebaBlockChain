import re
import hashlib
def comprobar(padre,hijo):
    f1 = open(padre, "r")  
    f2 = open(hijo, "r")  
    
    i = 0
    iguales=1
    for line1 in f1:
        i += 1
        
        for line2 in f2:
            
            # matching line1 from both files
            if line1.strip() != line2.strip():  
                iguales=0     
            break

                
    
    # closing files
    f1.close()                                       
    
    if(iguales==1):
        for line in f2:
            pass
        last_line = line
        x = re.search("[a-f0-9]{8}G([0-9]{2})+", last_line) 

        if(x!="None"):      
            f2.close()
            f= open(hijo,"rb") #abrimos el archivo en modo binario
            bytes = f.read() # read entire file as bytes
            
            readable_hash = hashlib.sha256(bytes).hexdigest()

            if(readable_hash[0]=="0"):

                i=1
                while(readable_hash[i]=="0"):
                    i=i+1
                return i
            else:
                return 0
                
    else:

        return 0

