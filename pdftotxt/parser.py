
import sys      
import os      
import os.path  
import shutil  

#cette fonction convertit le pdf en txt 
def convertir(dossier):
 
    t = "{}/t".format(dossier)
    if os.path.exists(t):
        shutil.rmtree(t)
    
    
    os.mkdir(t)

    
    for fichier in os.listdir(dossier):
        if fichier.endswith('.pdf'):
            
            f = os.path.splitext(fichier)[0]
            
            fichier1 = fichier.replace(' ','_')

            
            os.rename("{0}/{1}".format(dossier,fichier), "{0}/{1}".format(dossier,fichier1))
          
            Command = "pdftotext -f 1 {1}/{2} {1}/t/{3}.txt".format(os.getcwd(),dossier, fichier1, f)
           
            os.system(Command)
            
 #cette fonction crée un dossier FichierTXT et met les fichier txt dedans
def creeDossierWithtxt(directory):
    t = "{}/fichierTXT".format(directory)
    if os.path.exists(t):
        shutil.rmtree(t)
    os.mkdir(t)
    t = "{}/t".format(directory)
    for element in os.listdir(t):
	    if element.endswith('.txt'):
		    a = "{0}/fichierTXT/".format(directory)
		    s = "{0}/t/".format(directory)
		    source = open(s+element,"r")
		    destination = open(a+element, "w")	
		    extract(source,destination,element)
		    source.close()
		    destination.close()
		    
		    
		    
# cette fonction extrait les données du pdf et les met dans le fichier txt 		     
def extract(pdf,txt,element):
		titre = element.replace('.txt','').replace('_',' ')
		txt.write("Name : "+titre+"\n")				 							
		for i in range(2000,2019) :								
			if str(i) in titre :
				year = str(i)	
		txt.write("Title : "+  titre.split(year)[1] + "\n") 
		text = pdf.read()
		if "ABSTRACT" in text :										
			debut = text.split("ABSTRACT",1)						
								
		elif "Abstract" in text :
			debut = text.split("Abstract",1)
		
		fin="1"
		if "Keywords" in text :										
			fin="Keywords"
			
		elif "Index" in text :
			fin="Index"
		
		a1 = debut[1].split(fin)
		a2 = a1[0].split("\n")
		txt.write("Resume : ")
		for i in range(0,len(a2)) :									
			txt.write(a2[i])

		text = text.lower()
		auteur = titre.split(year)[1].split(" ")
		auteur1 = auteur[len(auteur)-1]
		auteur1= auteur1.lower()
		if auteur1 in text :
			author = text.split(auteur1)									
			if "abstract" in text :
				author1 = author[1].split("abstract",1)
				
			txt.write("\n"+"Author : "+author1[0])
		



          
            
   #main         
print("****** CONVERT TO TXT **********")

if len(sys.argv) != 3: 
    print("Erreur" )
    sys.exit(2)
else:
    current = os.getcwd()
    directory = sys.argv[1]

    if sys.argv[2] == '-t':
        print ("Conversion du repertoire <" + directory+"> en cours ...")
        convertir(directory)	
        creeDossierWithtxt(directory)
        t = "{}/t".format(directory)
        shutil.rmtree(t) 
    
  
    

      
