from tkinter import*
import random


estados = ("Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Chiapas","Chihuahua","Coahuila", "Colima", "Durango","Estado de México","Guanajuato","Guerrero","Hidalgo","Jalisco","Michoacán","Morelos","Nayarit","Nuevo León","Oaxaca","Puebla","Querétaro","Quintana Roo", "San Luis Potosí", "Sinaloa","Sonora","Tabasco","Tamaulipas","Tlaxcala","Veracruz","Yucatán","Zacatecas")
capitales = ("Aguascalientes","Mexicali","La Paz","Campeche","Tuxtla Gutierrez","Chichuahua","Saltillo","Colima","Durango","Toluca","Guanajuato","Chilpancingo","Pachuca","Guadalajara","Morelia","Cuernavaca","Tepic","Monterrey","Oaxaca","Puebla","Querétaro", "Chetumal","San Luis Potosí","Culiacán","Hermosillo", "Villahermosa","Ciudad Victoria","Tlaxcala","Xalapa","Mérida","Zacatecas")
print (capitales[17])
print(estados[17])
preguntas=["¿Dónde se posa el águila que forma parte del escudo nacional de México?","¿Qué mexicano inventó la televisión en color?","¿Cómo se llama la famosa marca de cerveza mexicana que exporta a todo el mundo?","Es la pirámide más grande del mundo en volumen, no en altura, y se encuentra en México. ¿Cuál es su nombre?", "¿A qué presidente mexicano se le conoce como Benemérito de las Américas?", "¿Cuál es el monte más alto de México?", "¿Cómo se llama el lago más grande de México?","¿En qué estado se encuentra la ciudad de Cancún?", "¿Qué famoso anfibio en peligro de extinción es endémico del Valle de México?", "¿Qué famoso líder militar de la Revolución mexicana fue conocido como «Caudillo del Sur»?", "¿Qué maravilla del mundo moderno se encuentra en México?", "¿Qué zona turística es la más visitada en México?", "¿Qué científico mexicano obtuvo el Premio Nobel de Química por sus estudios sobre la capa de ozono?", "¿Quién declaró la independencia de México en 1810?", "¿Cuál es el periódico más antiguo de México?", "¿Qué película mexicana estrenada en 2018 ganó el globo de oro a la mejor película extranjera?", "¿Quién tuvo el primer cargo de Emperador de México?", "¿Qué empresa estatal mexicana controla en su totalidad la industria petrolera?", "¿Qué estado actual de los Estados Unidos formó parte de México?", "¿Cuál era uno de los seis niños héroes?", "¿Quién fue el último gobernante de la ciudad del Imperio azteca Tenochtitlan?", "¿Qué famoso y bello cañón se encuentra en Chiapas?", "¿Qué leyenda mexicana habla de una mujer que se lamenta por las noches por la muerte de sus hijos?", "¿Qué famoso mexicano dijo esta frase: Algo malo debe tener el trabajo, o los ricos ya lo habrían acaparado?", "¿De qué cultura forman parte las zonas arqueológicas La Venta y Tres Zapotes?", "¿En qué antigua ciudad se encuentra la famosa Pirámide del Sol?", "¿Cuál es el nombre científico de la flor de muertos?", "¿En qué área cultural se encontraba la cultura Hohokam?", "¿Cuál era el nombre artístico del luchador Rodolfo Guzmán Huerta?", "¿En qué área cultural se encontraban los pueblos chichimecas?", "¿Qué famoso escritor mexicano escribió la obra El laberinto de la soledad?", "¿De qué cultura formaba parte la ciudad de Chichén Itzá?", "¿Cuál es el área metropolitana de México que tiene más habitantes?", "¿Qué famoso actor mexicano recibió el Oscar a la mejor dirección por la película El Renacido?", "¿Qué escritor mexicano obtuvo el Premio Nobel de literatura en 1990?", "¿En qué cerro se encuentra la Basílica de Guadalupe?", "¿Quién ha sido el máximo medallista olímpico mexicano", "¿Cuál era el nombre de México durante el periodo colonial?", "¿Cuál era la gran ciudad de los Mexicas?"]
respuestas=["Nopal ","Guillermo González","Corona", "La Gran Pirámide de Cholula","Benito Juárez","Pico de Orizaba","Chapala", "Quintana Roo", " Ajolote", "Emiliano Zapata", "Templo de Kukulkán", "Riviera Maya", "Mario Molina", "Miguel Hidalgo", "El Universal", "Roma", "Agustín de Iturbide", "PEMEX", "Texas", "Juan Escutia", "Cuauhtémoc", "Cañón del Sumidero", "La Llorona", "Cantinflas", "Olmeca", "Teotihuacán", "Tagetes erecta", "Oasisamérica", "El Santo", "Aridoamérica", "Octavio Paz", "Maya", "Ciudad de México", "Alejandro González", "Octavio Paz", "Tepeyac", "Joaquín Capilla", "Nueva España", "Tenochtitlán"]
azar=[]
print(len(preguntas))
print(len(respuestas))
eliminar=[]
eliminar2=[]
eliminar3=[]


def gameover():
    perdio=Toplevel()

    perdio.geometry("200x200")
    perdio.resizable(0,0)
    perdio["bg"]="#F0D973"

    comeback=Label(perdio,text="\n\nHas perdido todas tus vidas.\n Comienza de nuevo.\n\n", font =("Georgia"), bg="#F0D973")
    comeback.pack()
    
    
    return1=Button(perdio, text="Regresar",font=("Georgia"),bg="#FA78BE", command=lambda:[continuar1(), menu.deiconify(),perdio.iconify(),est.iconify(), cap.iconify(),pre.iconify()])
    return1.pack()  
def reset():
    global eliminar
    global eliminar2
    global eliminar3
    global count
    global reset
    eliminar=[]
    eliminar2=[]
    eliminar3=[]
    count=4
    lifes.set(count)
    botones=Label(text="")
    botones.configure(text="Estado: ")

def terminar():
    global eliminar
    global eliminar2
    global eliminar3
    global cap
    global pre
    global est
    global completo
    completo=Toplevel()
    completo.geometry("200x200")
    completo.resizable(0,0)
    completo["bg"]="#F0D973"
    eliminar=[]
    eliminar2=[]
    eliminar3=[]

    felicidades=Message(completo,text="\n\n\n¡¡¡Felicidades!!!\nHas contestado todo correctamente",font=("Georgia"),bg="#F0D973", justify=CENTER)
    felicidades.pack()

    return1=Button(completo, text="Regresar",font=("Georgia"),bg="#FA78BE", command=lambda:[continuar1(), menu.deiconify(),completo.iconify(), est.iconify(), cap.iconify(),pre.iconify(), reset()])
    return1.pack()

def continuepre():
    global azar1dos
    global azar2dos
    global azar3dos
    global azar2
    global delete
    global pregunta2
    global preguntas2

    print (eliminar3)
    preguntas2=["¿Dónde se posa el águila que forma parte del escudo nacional de México?","¿Qué mexicano inventó la televisión en color?","¿Cómo se llama la famosa marca de cerveza mexicana que exporta a todo el mundo?","Es la pirámide más grande del mundo en volumen, no en altura, y se encuentra en México. ¿Cuál es su nombre?", "¿A qué presidente mexicano se le conoce como Benemérito de las Américas?", "¿Cuál es el monte más alto de México?", "¿Cómo se llama el lago más grande de México?","¿En qué estado se encuentra la ciudad de Cancún?", "¿Qué famoso anfibio en peligro de extinción es endémico del Valle de México?", "¿Qué famoso líder militar de la Revolución mexicana fue conocido como «Caudillo del Sur»?", "¿Qué maravilla del mundo moderno se encuentra en México?", "¿Qué zona turística es la más visitada en México?", "¿Qué científico mexicano obtuvo el Premio Nobel de Química por sus estudios sobre la capa de ozono?", "¿Quién declaró la independencia de México en 1810?", "¿Cuál es el periódico más antiguo de México?", "¿Qué película mexicana estrenada en 2018 ganó el globo de oro a la mejor película extranjera?", "¿Quién tuvo el primer cargo de Emperador de México?", "¿Qué empresa estatal mexicana controla en su totalidad la industria petrolera?", "¿Qué estado actual de los Estados Unidos formó parte de México?", "¿Cuál era uno de los seis niños héroes?", "¿Quién fue el último gobernante de la ciudad del Imperio azteca Tenochtitlan?", "¿Qué famoso y bello cañón se encuentra en Chiapas?", "¿Qué leyenda mexicana habla de una mujer que se lamenta por las noches por la muerte de sus hijos?", "¿Qué famoso mexicano dijo esta frase: Algo malo debe tener el trabajo, o los ricos ya lo habrían acaparado?", "¿De qué cultura forman parte las zonas arqueológicas La Venta y Tres Zapotes?", "¿En qué antigua ciudad se encuentra la famosa Pirámide del Sol?", "¿Cuál es el nombre científico de la flor de muertos?", "¿En qué área cultural se encontraba la cultura Hohokam?", "¿Cuál era el nombre artístico del luchador Rodolfo Guzmán Huerta?", "¿En qué área cultural se encontraban los pueblos chichimecas?", "¿Qué famoso escritor mexicano escribió la obra El laberinto de la soledad?", "¿De qué cultura formaba parte la ciudad de Chichén Itzá?", "¿Cuál es el área metropolitana de México que tiene más habitantes?", "¿Qué famoso actor mexicano recibió el Oscar a la mejor dirección por la película El Renacido?", "¿Qué escritor mexicano obtuvo el Premio Nobel de literatura en 1990?", "¿En qué cerro se encuentra la Basílica de Guadalupe?", "¿Quién ha sido el máximo medallista olímpico mexicano", "¿Cuál era el nombre de México durante el periodo colonial?", "¿Cuál era la gran ciudad de los Mexicas?"]
    respuestas2=["Nopal ","Guillermo González","Corona", "La Gran Pirámide de Cholula","Benito Juárez","Pico de Orizaba","Chapala", "Quintana Roo", " Ajolote", "Emiliano Zapata", "Templo de Kukulkán", "Riviera Maya", "Mario Molina", "Miguel Hidalgo", "El Universal", "Roma", "Agustín de Iturbide", "PEMEX", "Texas", "Juan Escutia", "Cuauhtémoc", "Cañón del Sumidero", "La Llorona", "Cantinflas", "Olmeca", "Teotihuacán", "Tagetes erecta", "Oasisamérica", "El Santo", "Aridoamérica", "Octavio Paz", "Maya", "Ciudad de México", "Alejandro González", "Octavio Paz", "Tepeyac", "Joaquín Capilla", "Nueva España", "Tenochtitlán"]

    azar2=[]

    while True:
        pregunta2=random.choice(preguntas2)
        delete=preguntas2.index(pregunta2)
        print(delete)
        if delete in eliminar3:
            continue
        else:
            elegirpre.set(pregunta2)
            break

    azar1dos=IntVar()
    position1dos=preguntas2.index(pregunta2)
    azar1dos=respuestas[position1dos]

    azar3dos=StringVar()
    while True:
            azar2dos=random.choice(respuestas2)
            azar3dos=random.choice(respuestas2)

            if azar1dos==azar2dos or azar1dos==azar3dos or azar1dos==azar2dos or azar2dos==azar3dos:
                continue
            else:
                break

        
    azar2.append(azar2dos)
    azar2.append(azar3dos)
    posazar2=random.randrange(3)
    azar2.insert(posazar2, azar1dos)

    search.set(azar2.index(azar1dos))
    searchpre.set(preguntas2.index(pregunta2))

    uno.set(azar2[0])
    dos.set(azar2[1])
    tres.set(azar2[2])
    checkpre.configure(text="")


    if len(eliminar3)==9:
        terminar()


def check1():
    global count
    if search.get()==0:
        checkpre.configure(text="Correcto")
        eliminar3.append(searchpre.get())
    else:
        checkpre.configure(text="Incorrecto")
        while True:
            if count>1:
                count=count-1
                lifes.set(count)
                break
            else:
                reset()
                gameover()
        print (lifes.get())
def check2():
    global count
    if search.get()==1:
        checkpre.configure(text="Correcto")
        eliminar3.append(searchpre.get())
    else:
        checkpre.configure(text="Incorrecto")
        while True:
            if count>1:
                count=count-1
                lifes.set(count)
                break
            else:
                reset()
                gameover()
        print (lifes.get())
def check3():
    global count
    if search.get()==2:
        checkpre.configure(text="Correcto")
        eliminar3.append(searchpre.get())
    else:
        checkpre.configure(text="Incorrecto")
        while True:
            if count>1:
                count=count-1
                lifes.set(count)
                break
            else:
                reset()
                gameover()
        print (lifes.get())

    
def continuar1 ():
    global informacion
    estados2= ("Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Chiapas","Chihuahua","Coahuila", "Colima", "Durango","Estado de México","Guanajuato","Guerrero","Hidalgo","Jalisco","Michoacán","Morelos","Nayarit","Nuevo León","Oaxaca","Puebla","Querétaro","Quintana Roo", "San Luis Potosí", "Sinaloa","Sonora","Tabasco","Tamaulipas","Tlaxcala","Veracruz","Yucatán","Zacatecas")
    capitales2 = ("Aguascalientes","Mexicali","La Paz","Campeche","Tuxtla Gutierrez","Chichuahua","Saltillo","Colima","Durango","Toluca","Guanajuato","Chilpancingo","Pachuca","Guadalajara","Morelia","Cuernavaca","Tepic","Monterrey","Oaxaca","Puebla","Querétaro", "Chetumal","San Luis Potosí","Culiacán","Hermosillo", "Villahermosa","Ciudad Victoria","Tlaxcala","Xalapa","Mérida","Zacatecas")

    print(eliminar)
    print(eliminar2)

    informacion.configure(text="\nContesta correctamente para ver información del estado")

    while True:
        nuevo=random.choice(capitales2)
        num=capitales2.index(nuevo)
        if num in eliminar:
            continue
        else:
            buscar.set(nuevo)
            buscar2.set(num)
            break

    while True:
        nuevo2=random.choice(estados2)
        num2=estados2.index(nuevo2)
        if num2 in eliminar2:
            continue
        else:
            estado.set(nuevo2)
            buscar3.set(num2)
            break
        
    resultado.configure(text="")
 


    if len(eliminar)==30 or len(eliminar2)==30:
        buscar.set("Completado")
        estado.set("Completado")
        terminar()

    
    

def funcionaguas():
    global count
    if buscar2.get() == 0:
        resultado.configure(text="Correcto")
        eliminar.append(buscar2.get())
    elif buscar3.get()== 0:
        resultado.configure(text="Correcto")
        informacion.configure(text="\nAguascalientes: \n \nNombre Completo: Aguacalientes \n \nCapital: Aguascalientes \n \nLocalización: Se encuentra en la región central de México. Está abrazado en el norte por Zacatecas, y en el sur por Jalisco\n \nLugar Turístico: Pueblo mágico de Calvillo \n \n Dato General: La industria ferrocarrilera, fue un auge en la época de Porfirio Díaz, quien impulsó el ferrocarril en todo México, siendo Aguascalientes una de sus principales sedes en cuanto a talleres, reparación y construcción.")
        eliminar2.append(buscar3.get())
        
    else:
        resultado.configure(text="Incorrecto")
        count=count-1
        lifes.set(count)

    
def funcioncal():
    global count
    if buscar2.get() == 1:
        resultado.configure(text="Correcto")
        eliminar.append(buscar2.get())
    elif buscar3.get()== 1:
        resultado.configure(text="Correcto")
        informacion.configure(text="\nBaja California: \n \nNombre Completo: Baja California \n \nCapital: Mexicali\n \nLocalización: Se encuentra en la región del nororeste de México, con Baja California Sur al sur y Sonora al este. A su oeste hay agua, así como en la mitad de su este\n \nLugar Turístico: Playas de Rosarito \n \n Dato General: Es un estado bastante joven, pues se fundó el 16 de enero de 1952.")
        eliminar2.append(buscar3.get())
    else:
        resultado.configure(text="Incorrecto")
        while True:
            if count>1:
                count=count-1
                lifes.set(count)
                break
            else:
                reset()
                gameover()
        print (lifes.get())
        
def funcioncalsur():
    global count
    if buscar2.get() == 2:
        resultado.configure(text="Correcto")
        eliminar.append(buscar2.get())
    elif buscar3.get()== 2:
        resultado.configure(text="Correcto")
        informacion.configure(text="\nBaja California Sur: \n \nNombre Completo: Baja California \n \nCapital: La Paz\n \nLocalización: Se encuentra en la región noroeste de México, y únicamente colinda con Baja California en el norte. El resto de su territorio está rodeado por agua\n \nLugar Turístico: Cabo San Lucas \n \n Dato General: Es el estado con más litorales en todo México. Baja California Sur cuenta con 2 mil 131 kilómetros de litorales, lo que representa un 19.2 % de todas las aguas mexicanas.")
        eliminar2.append(buscar3.get())
    else:
        resultado.configure(text="Incorrecto")
        while True:
            if count>1:
                count=count-1
                lifes.set(count)
                break
            else:
                reset()
                gameover()
        print (lifes.get())
def funcioncamp():
    global count
    if buscar2.get() == 3:
        resultado.configure(text="Correcto")
        eliminar.append(buscar2.get())
    elif buscar3.get()== 3:
        resultado.configure(text="Correcto")
        informacion.configure(text="\nCampeche:\n\nNombre Completo: Campeche \n\nCapital: Campeche\n\nLocalización: Está ubicado en la península de Yucatán en la región sureste del país, colindando al norte y noreste con Yucatán, al este con Quintana Roo, al sur con Guatemala, al oeste con el Golfo de México y al suroeste con Tabasco.\n\nLugar Turístico: Es conocida por sus edificios coloniales barrocos conservados, la arquitectura militar y el distrito histórico amurallado. En respuesta a los ataques piratas, la ciudad se fortificó en el siglo XVII y 2 fortalezas sobre cerros son museos en la actualidad. El Fuerte de San Miguel alberga el Museo Arqueológico de Campeche, con artefactos de sitios mayas locales, como Edzná, Isla Jaina y Calakmul. \n \nDato General: Actualmente el 40% de su territorio es selva, en 1999 esta zona fue declarada Patrimonio Cultural de la Humanidad por la Organización de las Naciones Unidas para la Educación, la Ciencia y la Cultura")
        eliminar2.append(buscar3.get())
    else:
        resultado.configure(text="Incorrecto")
        while True:
            if count>1:
                count=count-1
                lifes.set(count)
                break
            else:
                reset()
                gameover()
        print (lifes.get())
def funcionchiap():
    global count
    if buscar2.get() == 4:
        resultado.configure(text="Correcto")
        eliminar.append(buscar2.get())
    elif buscar3.get()== 4:
        resultado.configure(text="Correcto")
        informacion.configure(text="\nChiapas: \n \nNombre Completo: Chiapas\n \nCapital: Tuxtla Gutiérrez \n \nLocalización: se localiza al sureste de México; colinda al norte con el estado de Tabasco, al oeste con Veracruz y Oaxaca, al sur con el Océano Pacífico y al este con la República de Guatemala.\n \nLugar Turístico: \nMuseo Regional de Antropología e Historia, Palenque, San Cristóbal de las Casas \n\n Dato General: Su población total es aproximadamente de 754 730 habitantes, el 0,7 % del total del país.")
        eliminar2.append(buscar3.get())
    else:
        resultado.configure(text="Incorrecto")
        while True:
            if count>1:
                count=count-1
                lifes.set(count)
                break
            else:
                reset()
                gameover()
        print (lifes.get())
def funcionchihua():
    global count
    if buscar2.get() == 5:
        resultado.configure(text="Correcto")
        eliminar.append(buscar2.get())
    elif buscar3.get()== 5:
        resultado.configure(text="Correcto")
        informacion.configure(text="\nChihuahua:\n \nNombre Completo: Chihuahua \n \nCapital: Chihuahua \n \nLocalización: Chihuahua se localiza en la parte central del norte del país. Colinda  al norte con los estados de Nuevo México y Texas de los Estados Unidos de América; al este con los estados de Coahuila de Zaragoza y Durango; al sur con Durango y Sinaloa; al oeste con Sinaloa, Sonora y los Estados Unidos de América.\n \nLugar Turístico: Cascada de Basaseachi \n \n Dato General:La palabra Chihuahua (nombre tanto del estado como de su capital) se traduce como la dama del desierto. Una razón de este nombre sería que este desierto es el más extenso de América del Norte y ocupa el 36% del total de área desértica del continente")
        eliminar2.append(buscar3.get())
    else:
        resultado.configure(text="Incorrecto")
        while True:
            if count>1:
                count=count-1
                lifes.set(count)
                break
            else:
                reset()
                gameover()
        print (lifes.get())
def funcioncoa():
    global count
    if buscar2.get() == 6:
        resultado.configure(text="Correcto")
        eliminar.append(buscar2.get())
    elif buscar3.get()== 6:
        resultado.configure(text="Correcto")
        informacion.configure(text="\nCoahuila: \n \nNombre Completo: Coahuila \n \nCapital: Saltillo \n \nLocalización: El estado de Coahuila se encuentra en el centro de la parte septentrional de la República. Limita al norte con los Estados Unidos de América; al oriente con el estado de Nuevo León; al sur con los estados de San Luis Potosí, Zacatecas y Durango, y al poniente con Durango y Chihuahua.\n \nLugar Turístico: Cristo de las Noas, Iglesia de Santo Madero, Poza Azul, etc.  \n \n Dato General: Tiene la moneda más grande del país.")
        eliminar2.append(buscar3.get())
    else:
        resultado.configure(text="Incorrecto")
        while True:
            if count>1:
                count=count-1
                lifes.set(count)
                break
            else:
                reset()
                gameover()
        print (lifes.get())
def funcioncolima():
    global count
    if buscar2.get() == 7:
        resultado.configure(text="Correcto")
        eliminar.append(buscar2.get())
    elif buscar3.get()== 7:
        resultado.configure(text="Correcto")
        informacion.configure(text="\nColima: \n \nNombre Completo: Colima\n \nCapital: Colima \n \nLocalización: El estado de Colima está localizado en la parte media de la costa Sur del Océano Pacífico.\n \nLugar Turístico: Zona Arqueológica La Campana,  Catedral Basílica Menor, etc. \n \n Dato General: La ciudad de Manzanillo es conocida a nivel internacional como la capital mundial del pez vela.")
        eliminar2.append(buscar3.get())
    else:
        resultado.configure(text="Incorrecto")
        while True:
            if count>1:
                count=count-1
                lifes.set(count)
                break
            else:
                reset()
                gameover()
        print (lifes.get())
def funcionduran():
    global count
    if buscar2.get() == 8:
        resultado.configure(text="Correcto")
        eliminar.append(buscar2.get())
    elif buscar3.get()== 8:
        resultado.configure(text="Correcto")
        informacion.configure(text="\nDurango: \n \nNombre Completo: Durango \n \nCapital: Durango \n \nLocalización: El Estado de Durango colinda al Norte con Chihuahua y Coahuila de Zaragoza; al Este con Coahuila de Zaragoza y Zacatecas, al Sur con Zacatecas, Nayarit y Sinaloa; al Oeste con Sinaloa y Chihuahua. \n \nLugar Turístico: Museo Francisco Villa, Museo Regional de Durango, etc. \n \n Dato General: Tiene 39 municipios")
        eliminar2.append(buscar3.get())
    else:
        resultado.configure(text="Incorrecto")
        while True:
            if count>1:
                count=count-1
                lifes.set(count)
                break
            else:
                reset()
                gameover()
        print (lifes.get())
def funcionedo():
    global count
    if buscar2.get() == 9:
        resultado.configure(text="Correcto")
        eliminar.append(buscar2.get())
    elif buscar3.get()== 9:
        resultado.configure(text="Correcto")
        informacion.configure(text="\nEstado de México:  \n \nNombre Completo: Estado de México\n \nCapital: Toluca de Lerdo\n \nLocalización: Colinda al norte con los estados de Querétaro e Hidalgo; al sur con Guerrero y Morelos; al este con Puebla y Tlaxcala; al oeste con Guerrero y Michoacán, así como con el Distrito Federal, al que rodea al norte, este y oeste.\n \nLugar Turístico: Tepotzotlán, Zoológico de Zacango, Volcán Popocatépetl.  \n \n Dato General: México significa el ombligo de la luna.")
        eliminar2.append(buscar3.get())
    else:
        resultado.configure(text="Incorrecto")
        while True:
            if count>1:
                count=count-1
                lifes.set(count)
                break
            else:
                reset()
                gameover()
        print (lifes.get())
def funcionguanajuato():
    global count
    if buscar2.get() == 10:
        resultado.configure(text="Correcto")
        eliminar.append(buscar2.get())
    elif buscar3.get()== 10:
        resultado.configure(text="Correcto")
        informacion.configure(text="\nGuanajuato:  \n \nNombre Completo: Guanajuato \n \nCapital: Guanajuato \n \nLocalización:Ubicado en el bajío que se encuentra en la región centro norte del país. Limita al norte con Zacatecas y San Luis, al este con Querétaro, al sur con Michoacán y al oeste con Jalisco \n \nLugar Turístico: Las momias de Guanajuato, el callejón callejón beso, Alhóndiga de Granaditas y Sierra de Santa Rosa\n \n Dato General: Su nombre deriva de Quanaxhuato, que en purépecha significa “Lugar montuoso de ranas” o “Lugar de muchos cerros”. Debe su fundación a los reales de minas del siglo XVI que al paso del tiempo la convirtieron en el centro minero más importante de la Nueva España.")
        eliminar2.append(buscar3.get())
    else:
        resultado.configure(text="Incorrecto")
        while True:
            if count>1:
                count=count-1
                lifes.set(count)
                break
            else:
                reset()
                gameover()
        print (lifes.get())
def funcionguerrero():
    global count
    if buscar2.get() == 11:
        resultado.configure(text="Correcto")
        eliminar.append(buscar2.get())
    elif buscar3.get()== 11:
        resultado.configure(text="Correcto")
        informacion.configure(text="\nGuerrero: \n \nNombre Completo: Guerrero \n \nCapital: Chilpancingo \n \nLocalización: Está ubicado en la región suroeste del país, limitando al norte con el Estado de México, Morelos y Puebla, al sureste con Oaxaca, al suroeste con el océano Pacífico y al noroeste con el río Balsas que lo separa de Michoacán. \n \nLugar Turístico: Playas de acapulco y Zihuatanejo, la quebrada,  la catedral de santa prisca y mina prehispánica de taxco.\n \n Dato General: tiene una extensión territorial de 63,794 kilómetros cuadrados, que representan el 3.2% de la superficie total de la República Mexicana.")
        eliminar2.append(buscar3.get())
    else:
        resultado.configure(text="Incorrecto")
        while True:
            if count>1:
                count=count-1
                lifes.set(count)
                break
            else:
                reset()
                gameover()
        print (lifes.get())
def funcionhidalgo():
    global count
    if buscar2.get() == 12:
        resultado.configure(text="Correcto")
        eliminar.append(buscar2.get())
        count=count-1
        lifes.set(count)
    elif buscar3.get()== 12:
        resultado.configure(text="Correcto")
        informacion.configure(text="\nHidalgo: \n \nNombre Completo: Hidalgo \n \nCapital: Pachuca de Soto \n \nLocalización: Está ubicado en la región este del país, limitando al norte con San Luis Potosí y Veracruz, al este con Puebla, al sur con Tlaxcala y el estado de México, y al oeste con Querétaro.\n \nLugar Turístico: Grutas de Tolantongo, Prismas basálticos de Santa María Regla, Bosque de las Truchas, Zona Arqueológica de Tula, Parque Nacional El Chico y Hacienda de Santa María Regla \n \n Dato General:Se reconoce como oficial el escudo diseñado por Diego Rivera en 1922 en este estado.")
        eliminar2.append(buscar3.get())
    else:
        resultado.configure(text="Incorrecto")
        while True:
            if count>1:
                count=count-1
                lifes.set(count)
                break
            else:
                reset()
                gameover()
        print (lifes.get())
def funcionjalisco():
    global count
    if buscar2.get() == 13:
        resultado.configure(text="Correcto")
        eliminar.append(buscar2.get())
    elif buscar3.get()== 13:
        resultado.configure(text="Correcto")
        informacion.configure(text="\nJalisco: \n \nNombre Completo: Jalisco \n \nCapital: Guadalajara \n \nLocalización: En la región oeste del país, limitando al norte con Nayarit, Zacatecas y Aguascalientes, al noreste con San Luis Potosí, al este con Guanajuato, al sur con Michoacán y Colima, y al oeste con el océano Pacífico. \n \nLugar Turístico: Lago de Chapala \n \n Dato General:  Fue el punto de partida para la conquista de Filipinas, estuvo muy involucrado en la abolición de la esclavitud y fue estado clave en el desarrollo del federalismo mexicano.")
        eliminar2.append(buscar3.get())
    else:
        resultado.configure(text="Incorrecto")
        while True:
            if count>1:
                count=count-1
                lifes.set(count)
                break
            else:
                reset()
                gameover()
        print (lifes.get())
def funcionmichoa():
    global count
    if buscar2.get() == 14:
        resultado.configure(text="Correcto")
        eliminar.append(buscar2.get())
    elif buscar3.get()== 14:
        resultado.configure(text="Correcto")
        informacion.configure(text="\nMichoacan: \n \nNombre Completo: Michoacan \n \nCapital: Morelia \n \nLocalización: región oeste del país, limitando al norte con Jalisco y Guanajuato, al noreste con Querétaro, al este con el Estado de México, al suroeste con Colima y al sur con el río Balsas que lo separa de Guerrero, y al oeste con el océano Pacífico. \n \nLugar Turístico:  Santuarios de la Mariposa Monarca, Volcán Paricutín,  Pueblo Mágico de Pátzcuaro y  Lago de Camécuaro \n \n Dato General: La palabra Michoacán provienen del náhuatl michihuacán.Significa lugar de pescadores, esto debido a que las primeras poblaciones se construyeron alrededor de los lagos de Pátzcuaro, Zacapu, Cuitzeo y Zirahuén.")
        eliminar2.append(buscar3.get())
    else:
        resultado.configure(text="Incorrecto")
        while True:
            if count>1:
                count=count-1
                lifes.set(count)
                break
            else:
                reset()
                gameover()
        print (lifes.get())
def funcionmorelos():
    global count
    if buscar2.get() == 15:
        resultado.configure(text="Correcto")
        eliminar.append(buscar2.get())
    elif buscar3.get()== 15:
        resultado.configure(text="Correcto")
        informacion.configure(text="\nMorelos: \n \nNombre Completo: Morelos \n \nCapital: Cuernavaca\n \nLocalización:  región centrosur del país, limitando al norte con Ciudad de México, al este con Puebla, al sur con Guerrero y al oeste con el Estado de México. \n \nLugar Turístico: Tepoztlán,  Tequesquitengo, Jardines de Cuernavaca y Zoofari de Cuernavaca \n \n Dato General: La catedral de Morelos se fundó en 1869 por frailes que llegaron a México.")
        eliminar2.append(buscar3.get())
    else:
        resultado.configure(text="Incorrecto")
        while True:
            if count>1:
                count=count-1
                lifes.set(count)
                break
            else:
                reset()
                gameover()
        print (lifes.get())
def funcionnayarit():
    global count
    if buscar2.get() == 16:
        resultado.configure(text="Correcto")
        eliminar.append(buscar2.get())
    elif buscar3.get()== 16:
        resultado.configure(text="Correcto")
        informacion.configure(text="\nNayarit:  \n \nNombre Completo: Nayarit\n \nCapital: Tepic\n \nLocalización: Oeste de México, entre las montañas arboladas de la Sierra Madre Occidental y el océano Pacífico.\n \nLugar Turístico: Diversas playas del estado, Rincón de Guayabitos, Riviera Nayarit y Islas Marietas\n \n Dato General: La Riviera Nayarit ha sido la locación de algunas obras de creación audiovisual. Tal es el caso de las películas Limitless (2011) y The bachelor in Paradise (2016), el videoclip Un par de lugares de Café Tacvba (2016), el comercial Corona Extra (2014), entre otros.")
        eliminar2.append(buscar3.get())
    else:
        resultado.configure(text="Incorrecto")
        while True:
            if count>1:
                count=count-1
                lifes.set(count)
                break
            else:
                reset()
                gameover()
        print (lifes.get())
def funcionnuevleon():
    global count
    if buscar2.get() == 17:
        resultado.configure(text="Correcto")
        eliminar.append(buscar2.get())
    elif buscar3.get()== 17:
        resultado.configure(text="Correcto")
        informacion.configure(text="\nNuevo León: \n \nNombre Completo: Nuevo León \n \nCapital: Monterrey\n \nLocalización:  Noreste del país, limitando al norte con el río Bravo que lo separa de Estados Unidos, al este con Tamaulipas, al sur con San Luis Potosí y al oeste con Coahuila y Zacatecas. \n \nLugar Turístico: Cerro de la silla, Parque Fundidora, Grutas de Garcia, Nido de los Aguiluchos y Cascada Cola de Caballo \n \n Dato General:  La Macroplaza es más grande que la Plaza Roja de Moscú. Cuenta con una extensión de 40 hectáreas, que es 2 veces mayor al de la Plaza Roja de Moscú, 5 veces el tamaño de la Plaza de San Pedro en el Vaticano y 6 veces el del Zócalo de la Ciudad de México.")
        eliminar2.append(buscar3.get())
    else:
        resultado.configure(text="Incorrecto")
        while True:
            if count>1:
                count=count-1
                lifes.set(count)
                break
            else:
                reset()
                gameover()
        print (lifes.get())
def funcionoaxaca():
    global count
    if buscar2.get() == 18:
        resultado.configure(text="Correcto")
        eliminar.append(buscar2.get())
    elif buscar3.get()== 18:
        resultado.configure(text="Correcto")
        informacion.configure(text="\nOaxaca: \n \nNombre Completo: Oaxaca \n \nCapital: Oaxaca \n \nLocalización:  región suroeste del país.9​ Limita al norte con Puebla y Veracruz, al este con Chiapas, al sur con el océano Pacífico y al oeste con Guerrero. \n \nLugar Turístico: Zona Arqueologica Monte Alban, Pueblos Mancomunados, Jardín Etnobotánico y Museo Textil de Oaxaca \n \n Dato General: Es el estado de la república mexicana con más municipios.")
        eliminar2.append(buscar3.get())
    else:
        resultado.configure(text="Incorrecto")
        while True:
            if count>1:
                count=count-1
                lifes.set(count)
                break
            else:
                reset()
                gameover()
        print (lifes.get())
def funcionpuebla():
    global count
    if buscar2.get() == 19:
        resultado.configure(text="Correcto")
        eliminar.append(buscar2.get())
    elif buscar3.get()== 19:
        resultado.configure(text="Correcto")
        informacion.configure(text="\nPuebla: \n \nNombre Completo: Puebla \n \nCapital: Puebla de Zaragoza\n \nLocalización: Región sureste. Colinda en el noroeste con Tlaxcala e Hidalgo, en el oeste con el Estado de México y Morelos, en el noreste con Veracruz, en el suroeste con Guerrero y en el sureste con Oaxaca. \n \nLugar Turístico: Cuetzalan\n \n Dato General: Se fundó el 16 de abril de 1531, siendo la primera ciudad en América construida sólo para españoles, siguiendo la idea de una ciudad perfecta en su traza.")
        eliminar2.append(buscar3.get())
    else:
        resultado.configure(text="Incorrecto")
        while True:
            if count>1:
                count=count-1
                lifes.set(count)
                break
            else:
                reset()
                gameover()
        print (lifes.get())
def funcionqro():
    global count
    if buscar2.get() == 20:
        resultado.configure(text="Correcto")
        eliminar.append(buscar2.get())
    elif buscar3.get()== 20:
        resultado.configure(text="Correcto")
        informacion.configure(text="\nQuerétaro:  \n \nNombre Completo: Querétaro \n \nCapital: Santiago de Querétaro \n \nLocalización: Se encuentra en la región central de México. A su suroeste está Michoacán, a su sur el Estado de México, a su este Hidalgo, a su oeste Guanajuato y a su norte San Luis Potosí. \n \nLugar Turístico: Los Arcos\n \n Dato General: La Constitución de 1917 fue firmada aquí.")
        eliminar2.append(buscar3.get())
    else:
        resultado.configure(text="Incorrecto")
        while True:
            if count>1:
                count=count-1
                lifes.set(count)
                break
            else:
                reset()
                gameover()
        print (lifes.get())
def funcionquintana():
    global count
    if buscar2.get() == 21:
        resultado.configure(text="Correcto")
        eliminar.append(buscar2.get())
    elif buscar3.get()== 21:
        resultado.configure(text="Correcto")
        informacion.configure(text="\nQuintana Roo: \n\nNombre Completo: Quintana Roo \n \nCapital: Chetumal \n \nLocalización: Se encuentra en la región del este de México. A su noroeste está Yucatán y a su oeste Campeche. Está en la península \n \nLugar Turístico: Zona Arqueológica El Rey\n \n Dato General: Su nombre proviene del político, escritor, poeta y periodista yucateco, Andrés Quintana Roo, quien fue Diputado y uno de los firmantes del Acta de Independencia de México en 1821")
        eliminar2.append(buscar3.get())
    else:
        resultado.configure(text="Incorrecto")
        while True:
            if count>1:
                count=count-1
                lifes.set(count)
                break
            else:
                reset()
                gameover()
        print (lifes.get())
def funcionsl():
    global count
    if buscar2.get() == 22:
        resultado.configure(text="Correcto")
        eliminar.append(buscar2.get())
    elif buscar3.get()== 22:
        resultado.configure(text="Correcto")
        informacion.configure(text="\nSan Luis Potosí: \n \nNombre Completo: San Luis Potosí \n \nCapital: San Luis Potosí \n \nLocalización: Se encuentra en la región central de México. A su sur están Querétaro, Guanajuato e Hidalgo, a su norte Coahuila, Nuevo León y Tamaulipas, a su sureste Veracruz y a su este Zacatecas. \n \nLugar Turístico: Sótano de las Golondrinas\n \n Dato General: El compositor del himno nacional mexicano, Francisco González Bocanegra era potosino.")
        eliminar2.append(buscar3.get())
    else:
        resultado.configure(text="Incorrecto")
        while True:
            if count>1:
                count=count-1
                lifes.set(count)
                break
            else:
                reset()
                gameover()
        print (lifes.get())
def funcionsinaloa():
    global count
    if buscar2.get() == 23:
        resultado.configure(text="Correcto")
        eliminar.append(buscar2.get())
    elif buscar3.get()== 23:
        resultado.configure(text="Correcto")
        informacion.configure(text="\nSinaloa:  \n \nNombre Completo: Sinaloa \n \nCapital: Culiacán Rosales \n \nLocalización: Se encuentra en la región noroeste de México. A su oeste y suroeste se encuentra agua, a su norte Sonora y Chihuahua, a su este Durango y a su sur Nayarit. \n \nLugar Turístico: Bahía de Topolobampo\n \n Dato General: 40 días antes de semana santa se realiza el carnaval de Mazatlán.")
        eliminar2.append(buscar3.get())
    else:
        resultado.configure(text="Incorrecto")
        while True:
            if count>1:
                count=count-1
                lifes.set(count)
                break
            else:
                reset()
                gameover()
        print (lifes.get())
def funcionsonora():
    global count
    if buscar2.get() == 24:
        resultado.configure(text="Correcto")
        eliminar.append(buscar2.get())
    elif buscar3.get()== 24:
        resultado.configure(text="Correcto")
        informacion.configure(text="\nSonora: \n \nNombre Completo: Sonora \n \nCapital: Hermosillo \n \nLocalización: A su oeste se encuentra agua. A su oeste se encuentra Baja California, a su sur Sinaloa y a su este Chihuahua. \n \nLugar Turístico: Álamos\n \n Dato General: Sonora es el segundo estado más extenso del País con 179,503 km².")
        eliminar2.append(buscar3.get())
    else:
        resultado.configure(text="Incorrecto")
        while True:
            if count>1:
                count=count-1
                lifes.set(count)
                break
            else:
                reset()
                gameover()
        print (lifes.get())
def funciontabasco():
    global count
    if buscar2.get() == 25:
        resultado.configure(text="Correcto")
        eliminar.append(buscar2.get())
    elif buscar3.get()== 25:
        resultado.configure(text="Correcto")
        informacion.configure(text="\nTabasco:  \n \nNombre Completo: Tabasco \n \nCapital: Villahermosa \n \nLocalización: Se encuentra entre la península y el cuerpo principal de México. A su oeste se encuentra Veracruz, a su sur Chiapas y a su este Campeche. A su norte se encuentra agua.\n \nLugar Turístico: Paraíso\n \n Dato General: Fue uno de los puntos más importantes en los que habitó la cultura olmeca.")
        eliminar2.append(buscar3.get())
    else:
        resultado.configure(text="Incorrecto")
        while True:
            if count>1:
                count=count-1
                lifes.set(count)
                break
            else:
                reset()
                gameover()
        print (lifes.get())
def funciontamaulipas():
    global count
    if buscar2.get() == 26:
        resultado.configure(text="Correcto")
        eliminar.append(buscar2.get())
    elif buscar3.get()== 26:
        resultado.configure(text="Correcto")
        informacion.configure(text="\nTamaulipas:  \n \nNombre Completo: Tamaulipas \n \nCapital Ciudad Victoria:\n \nLocalización: Se encuentra en la región noreste de México. A su oeste se encuentra Coahuila y Nuevo León y a su sur San Luis Potosí y Veracruz. \n \nLugar Turístico: Reserva de la Biosfera El Cielo\n \n Dato General: Destacan las celebraciones de la Procesión del Silencio y el Viacrucis en el Pueblo Mágico de Tula, así como las representaciones que se llevarán a cabo en Soto la Marina y Matamoros.")
        eliminar2.append(buscar3.get())
    else:
        resultado.configure(text="Incorrecto")
        while True:
            if count>1:
                count=count-1
                lifes.set(count)
                break
            else:
                reset()
                gameover()
        print (lifes.get())
def funciontlaxcala():
    global count
    if buscar2.get() == 27:
        resultado.configure(text="Correcto")
        eliminar.append(buscar2.get())
    elif buscar3.get()== 27:
        resultado.configure(text="Correcto")
        informacion.configure(text="\nTlaxcala: \n \nNombre Completo:Tlaxcala \n \nCapital:Tlaxcala de Xicohténcatl\n \nLocalización: Se encuentra sureste de México. A su noroeste está Hidalgo y al este el Estado de México, el resto de territorio por colindar es cubierto por Puebla.\n \nLugar Turístico: Huamantla\n \n Dato General: Tlaxcala cuenta con el 1.1% de la población de México, de acuerdo con el último censo del Inegi, realizado en 2015")
        eliminar2.append(buscar3.get())
    else:
        resultado.configure(text="Incorrecto")
        while True:
            if count>1:
                count=count-1
                lifes.set(count)
                break
            else:
                reset()
                gameover()
        print (lifes.get())
def funcionveracruz():
    global count
    if buscar2.get() == 28:
        resultado.configure(text="Correcto")
        eliminar.append(buscar2.get())
    elif buscar3.get()== 28:
        resultado.configure(text="Correcto")
        informacion.configure(text="\nVeracruz: \n \nNombre Completo: Veracruz \n \nCapital:\n \nLocalización: Se encuentra en la región este de México. A su norte se encuentra Tamaulipas, a su este Tabasco y a su suroeste/oeste se encuentran San Luis Potosí, Hidalgo, Puebla y Oaxaca.\n \nLugar Turístico: San Juan de Ulúa\n \n Dato General:  El nombre de Veracruz se le dio a este lugar después de que Hernán Cortés desembarcó aquí el 22 de abril de 1519, fecha que coincidía con el Viernes Santo (el Viernes antes de Pascua), también conocido como Vera Cruz.")
        eliminar2.append(buscar3.get())
    else:
        resultado.configure(text="Incorrecto")
        while True:
            if count>1:
                count=count-1
                lifes.set(count)
                break
            else:
                reset()
                gameover()
        print (lifes.get())
def funcionyucatan():
    global count
    if buscar2.get() == 29:
        resultado.configure(text="Correcto")
        eliminar.append(buscar2.get())
    elif buscar3.get()== 29:
        resultado.configure(text="Correcto")
        informacion.configure(text="\nYucatán:  \n \nNombre Completo: Yucatán \n \nCapital: Xalapa-Enríquez Mérida \n \nLocalización: Se encuentra en la región este de México. A su suroeste se encuentra Campeche, mientras que Quintana Roo lo rodea por el este y sureste. El resto del territorio fronterizo colinda con agua.\n \nLugar Turístico: Celestún\n \n Dato General: En Yucatán cayó el meteorito que extinguió a los dinosaurios")
        eliminar2.append(buscar3.get())
    else:
        resultado.configure(text="Incorrecto")
        while True:
            if count>1:
                count=count-1
                lifes.set(count)
                break
            else:
                reset()
                gameover()
        print (lifes.get())
def funcionzacatecas():
    global count
    if buscar2.get() == 30:
        resultado.configure(text="Correcto")
        eliminar.append(buscar2.get())
    elif buscar3.get()== 30:
        resultado.configure(text="Correcto")
        informacion.configure(text="\nZacatecas: \n \nNombre Completo: Zacatecas \n \nCapital: Zacatecas\n \nLocalización: Se encuentra en la región central de México. En el norte se encuentra Coahuila, en el noroeste Durango, en el sur Aguascalientes y Jalisco, en el este San Luis Potosí y en el sureste Guanajuato. \n \nLugar Turístico: Cerro de la Bufa\n \n Dato General: La virgen de Guadalupe apareció en este estado")
        eliminar2.append(buscar3.get())
        
    else:
        resultado.configure(text="Incorrecto")
        while True:
            if count>1:
                count=count-1
                lifes.set(count)
                break
            else:
                reset()
                gameover()
        print (lifes.get())

def aguas_hover(e):
    botones.configure(text="Estado: Aguascalientes")
         
def cal_hover(e):
    botones.configure(text="Estado: Baja California")
def calsur_hover(e):
    botones.configure(text="Estado: Baja California Sur")
def camp_hover(e):
    botones.configure(text="Estado: Campeche")
def chiap_hover(e):
    botones.configure(text="Estado: Chiapas")
def chihua_hover(e):
    botones.configure(text="Estado: Chihuahua")
def coa_hover(e):
    botones.configure(text="Estado: Coahulia")
def colima_hover(e):
    botones.configure(text="Estado: Colima")
def duran_hover(e):
    botones.configure(text="Estado: Durango")
def edo_hover(e):
    botones.configure(text="Estado: Estado de México")
def guanajuato_hover(e):
    botones.configure(text="Estado: Guanajuato")
def guerrero_hover(e):
    botones.configure(text="Estado: Guerrero")
def hidalgo_hover(e):
    botones.configure(text="Estado: Hidalgo")
def jalisco_hover(e):
    botones.configure(text="Estado: Jalisco")
def michoa_hover(e):
    botones.configure(text="Estado: Michoacan")
def morelos_hover(e):
    botones.configure(text="Estado: Morelos")
def nayarit_hover(e):
    botones.configure(text="Estado: Nayarit")
def nuevleon_hover(e):
    botones.configure(text="Estado: Nuevo León")
def oaxaca_hover(e):
    botones.configure(text="Estado: Oaxaca")
def puebla_hover(e):
    botones.configure(text="Estado: Puebla")
def qro_hover(e):
    botones.configure(text="Estado: Querétaro")
def quintana_hover(e):
    botones.configure(text="Estado: Quintana Roo")
def slp_hover(e):
    botones.configure(text="Estado: San Luís Potosí")
def sinaloa_hover(e):
    botones.configure(text="Estado: Sinaloa")
def sonora_hover(e):
    botones.configure(text="Estado: Sonora")
def tabasco_hover(e):
    botones.configure(text="Estado: Tabasco")
def tamaulipas_hover(e):
    botones.configure(text="Estado: Tamaulipas")
def tlaxcala_hover(e):
    botones.configure(text="Estado: Tlaxcala")
def veracruz_hover(e):
    botones.configure(text="Estado: Veracruz")
def yucatan_hover(e):
    botones.configure(text="Estado: Yucatán")

def zacatecas_hover(e):
    botones.configure(text="Estado: Zacatecas")



def ventanacapitales():
    global mexico
    global cap
    global img_bt1
    global nombre
    global funcionqro
    global funcionsl
    global buscar2
    global continuar
    global resultado
    global informacion
    global vidas
    global botones
    
    menu.iconify()
    cap = Toplevel(menu)
    cap.resizable(0,0)
    cap["bg"]="#F0D973"


    mexico=PhotoImage(file="mapa_verde.png")
    mapa = Label(cap, image=mexico, bg = "#F0D973")
    mapa.pack()

    informacion=Label(cap,text="")

    vidas=Label(cap, text= "Vidas: ", font=("Georgia"),bg= "#F0D973")
    vidas.place(x=530,y=10)

    showlifes=Label(cap, textvariable=lifes,font=("Georgia"),bg= "#F0D973")
    showlifes.place(x=585,y=8)

    botones=Label(cap, text="Estado:", font=("Georgia",10),bg= "#F0D973")
    botones.place(x=470,y=100)
    
    img_bt1 = PhotoImage (file="botton.png")

    
    agua=Button(cap, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionaguas)
    agua.place(x=303, y = 255)
    mex=Button(cap, image = img_bt1, bg = "green", width = 5, height = 5, command = funcioncal)
    mex.place(x=60, y = 50)
    paz=Button(cap, image = img_bt1, bg = "green", width = 5, height = 5, command = funcioncalsur)
    paz.place(x=110, y = 150)
    camp=Button(cap, image = img_bt1, bg = "green", width = 5, height = 5, command = funcioncamp)
    camp.place(x=550, y = 310)
    chihua=Button(cap, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionchihua)
    chihua.place(x=225, y = 100)
    tuxt=Button(cap, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionchiap)
    tuxt.place(x=500, y = 370)
    salt=Button(cap, image = img_bt1, bg = "green", width = 5, height = 5, command = funcioncoa)
    salt.place(x=305, y = 140)
    col=Button(cap, image = img_bt1, bg = "green", width = 5, height = 5, command = funcioncolima)
    col.place(x=270, y = 318)
    dur=Button(cap, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionduran)
    dur.place(x=250, y = 200)
    gto=Button(cap, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionguanajuato)
    gto.place(x=325, y = 283)
    chil=Button(cap, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionguerrero)
    chil.place(x=350, y = 350)
    pach=Button(cap, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionhidalgo)
    pach.place(x=370, y = 285)
    glj=Button(cap, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionjalisco)
    glj.place(x=270, y = 290)
    tol=Button(cap, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionedo)
    tol.place(x=355, y = 310)
    morl=Button(cap, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionmichoa)
    morl.place(x=320, y = 315)
    cuer=Button(cap, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionmorelos)
    cuer.place(x=368, y = 328)
    tep=Button(cap, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionnayarit)
    tep.place(x=250, y = 255)
    mty=Button(cap, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionnuevleon)
    mty.place(x=350, y = 170)
    oax=Button(cap, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionoaxaca)
    oax.place(x=420, y = 360)
    pue=Button(cap, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionpuebla)
    pue.place(x=390, y = 325)
    #qro
    chet=Button(cap, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionquintana)
    chet.place(x=580, y = 310)
    #sanluis
    culia=Button(cap, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionsinaloa)
    culia.place(x=210, y = 200)
    herm=Button(cap, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionsonora)
    herm.place(x=150, y = 100)
    villa=Button(cap, image = img_bt1, bg = "green", width = 5, height = 5, command = funciontabasco)
    villa.place(x=500, y = 335)
    cdvic=Button(cap, image = img_bt1, bg = "green", width = 5, height = 5, command = funciontamaulipas)
    cdvic.place(x=375, y = 225)
    tlax=Button(cap, image = img_bt1, bg = "green", width = 5, height = 5, command = funciontlaxcala)
    tlax.place(x=388, y = 312)
    xal=Button(cap, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionveracruz)
    xal.place(x=415, y = 312)
    mer=Button(cap, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionyucatan)
    mer.place(x=570, y = 275)
    zac=Button(cap, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionzacatecas)
    zac.place(x=295, y = 220)
    
    qro=Button(cap, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionqro)
    qro.place(x=350, y= 283)
    sanluis=Button(cap, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionsl)
    sanluis.place(x= 345, y = 250)

    agua.bind("<Enter>",aguas_hover)
    
    mex.bind("<Enter>",cal_hover)
    paz.bind("<Enter>",calsur_hover)
    camp.bind("<Enter>",camp_hover)
    chihua.bind("<Enter>",chihua_hover)
    tuxt.bind("<Enter>",chiap_hover)
    salt.bind("<Enter>",coa_hover)
    col.bind("<Enter>",colima_hover)
    dur.bind("<Enter>",duran_hover)
    gto.bind("<Enter>",guanajuato_hover)
    chil.bind("<Enter>",guerrero_hover)
    pach.bind("<Enter>",hidalgo_hover)
    glj.bind("<Enter>",jalisco_hover)
    tol.bind("<Enter>",edo_hover)
    morl.bind("<Enter>",michoa_hover)
    cuer.bind("<Enter>",morelos_hover)
    tep.bind("<Enter>",nayarit_hover)
    mty.bind("<Enter>",nuevleon_hover)
    oax.bind("<Enter>",oaxaca_hover)
    pue.bind("<Enter>",puebla_hover)
    #qro
    chet.bind("<Enter>",quintana_hover)
    #sanluis
    culia.bind("<Enter>",sinaloa_hover)
    herm.bind("<Enter>",sonora_hover)
    villa.bind("<Enter>",tabasco_hover)
    cdvic.bind("<Enter>",tamaulipas_hover)
    tlax.bind("<Enter>",tlaxcala_hover)
    xal.bind("<Enter>",veracruz_hover)
    mer.bind("<Enter>",yucatan_hover)
    zac.bind("<Enter>",zacatecas_hover)
    qro.bind("<Enter>",qro_hover)
    sanluis.bind("<Enter>",slp_hover)
    
    
    nombre = Label (cap, textvariable = buscar, bg = "#F0D973", font=("Georgia","20", "bold"))
    nombre.pack()

    resultado = Label (cap, textvariable = "", bg = "#F0D973", font=("Georgia","20", "bold"))
    resultado.pack()

    
    regresar = Button(cap, text= "REGRESAR", bg = "#FA78BE", command = lambda:[menu.deiconify(),cap.iconify(), continuar1(), reset()])
    regresar.pack(side=BOTTOM)

    continuar = Button(cap, text= "CONTINUAR", bg = "#FA78BE", command = continuar1)
    continuar.pack(side=BOTTOM)

def ventanaestados():
    global mexico
    global img_bt1
    global nombre
    global funcionqro
    global funcionsl
    global buscar2
    global resultado
    global est
    global datos
    global informacion
    global lifes

    menu.iconify()
    est= Toplevel(menu)
    est["bg"]="#F0D973"
    mexico=PhotoImage(file="mapa_verde.png")
    est.resizable(0,0)
    mapa = Label(est, image=mexico,bg = "#F0D973")
    mapa.pack()


    datos=Toplevel(est)
    datos["bg"]="#F0D973"
    datos.iconify()
    informacion = Message(datos, text="\nContesta correctamente para ver información del estado", font=("Georgia"), bg= "#F0D973", width=300, justify=CENTER)
    informacion.pack()
    espacio=Label(datos,text="",bg= "#F0D973")
    espacio.pack()

    hide=Button(datos, text= "REGRESAR", bg = "#FA78BE", command = datos.iconify)
    hide.pack(side=BOTTOM)
    
    img_bt1 = PhotoImage (file="botton.png")

    vidas=Label(est, text= "Vidas: ", font=("Georgia"),bg= "#F0D973")
    vidas.place(x=530,y=10)

    showlifes=Label(est, textvariable=lifes,font=("Georgia"),bg= "#F0D973")
    showlifes.place(x=585,y=8)
    
    agua=Button(est, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionaguas)
    agua.place(x=303, y = 255)
    mex=Button(est, image = img_bt1, bg = "green", width = 5, height = 5, command = funcioncal)
    mex.place(x=60, y = 50)
    paz=Button(est, image = img_bt1, bg = "green", width = 5, height = 5, command = funcioncalsur)
    paz.place(x=110, y = 150)
    camp=Button(est, image = img_bt1, bg = "green", width = 5, height = 5, command = funcioncamp)
    camp.place(x=550, y = 310)
    chihua=Button(est, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionchihua)
    chihua.place(x=225, y = 100)
    tuxt=Button(est, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionchiap)
    tuxt.place(x=500, y = 370)
    salt=Button(est, image = img_bt1, bg = "green", width = 5, height = 5, command = funcioncoa)
    salt.place(x=305, y = 140)
    col=Button(est, image = img_bt1, bg = "green", width = 5, height = 5, command = funcioncolima)
    col.place(x=270, y = 318)
    dur=Button(est, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionduran)
    dur.place(x=250, y = 200)
    gto=Button(est, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionguanajuato)
    gto.place(x=325, y = 283)
    chil=Button(est, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionguerrero)
    chil.place(x=350, y = 350)
    pach=Button(est, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionhidalgo)
    pach.place(x=370, y = 285)
    glj=Button(est, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionjalisco)
    glj.place(x=270, y = 290)
    tol=Button(est, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionedo)
    tol.place(x=355, y = 310)
    morl=Button(est, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionmichoa)
    morl.place(x=320, y = 315)
    cuer=Button(est, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionmorelos)
    cuer.place(x=368, y = 328)
    tep=Button(est, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionnayarit)
    tep.place(x=250, y = 255)
    mty=Button(est, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionnuevleon)
    mty.place(x=350, y = 170)
    oax=Button(est, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionoaxaca)
    oax.place(x=420, y = 360)
    pue=Button(est, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionpuebla)
    pue.place(x=390, y = 325)
    #qro
    chet=Button(est, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionquintana)
    chet.place(x=580, y = 310)
    #sanluis
    culia=Button(est, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionsinaloa)
    culia.place(x=210, y = 200)
    herm=Button(est, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionsonora)
    herm.place(x=150, y = 100)
    villa=Button(est, image = img_bt1, bg = "green", width = 5, height = 5, command = funciontabasco)
    villa.place(x=500, y = 335)
    cdvic=Button(est, image = img_bt1, bg = "green", width = 5, height = 5, command = funciontamaulipas)
    cdvic.place(x=375, y = 225)
    tlax=Button(est, image = img_bt1, bg = "green", width = 5, height = 5, command = funciontlaxcala)
    tlax.place(x=388, y = 312)
    xal=Button(est, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionveracruz)
    xal.place(x=415, y = 312)
    mer=Button(est, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionyucatan)
    mer.place(x=570, y = 275)
    zac=Button(est, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionzacatecas)
    zac.place(x=295, y = 220)
    
    qro=Button(est, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionqro)
    qro.place(x=350, y= 283)
    sanluis=Button(est, image = img_bt1, bg = "green", width = 5, height = 5, command = funcionsl)
    sanluis.place(x= 345, y = 250)

    nombre = Label (est, textvariable = estado, bg = "#F0D973", font=("Georgia","20", "bold"))
    nombre.pack()

    resultado = Label (est, textvariable = "", bg = "#F0D973", font=("Georgia","20", "bold"))
    resultado.pack()

    info= Button(est, text= "INFO.", bg="#7DFFE0", command = datos.deiconify)
    info.place(x=360,y=521)

    regresar = Button(est, text= "REGRESAR", bg = "#FA78BE", command = lambda:[menu.deiconify(),est.iconify(), continuar1(),reset()])
    regresar.pack(side=BOTTOM)

    continuar = Button(est, text= "CONTINUAR", bg = "#FA78BE", command = continuar1)
    continuar.pack(side=BOTTOM)



def ventanapreguntas():
    global elegirpre
    global azar
    global opcion1
    global opcion2
    global opcion3
    global checkpre
    global pre
    global informacion
    global resultado
    global lifes
    global botones
    
    menu.iconify()
    botones= Label(text="")
    
    informacion=Label(text="")
    resultado=Label(text="")

    pre = Toplevel(menu)
    pre["bg"]="#F0D973"
    pre.geometry("600x400")
    pre.resizable(0,0)

    vidas=Label(pre, text= "Vidas: ", font=("Georgia"),bg= "#F0D973")
    vidas.pack()

    showlifes=Label(pre, textvariable=lifes,font=("Georgia"),bg= "#F0D973")
    showlifes.pack()

    espacio=Label(pre, text="\n",bg= "#F0D973")
    espacio.pack()


    question = Message(pre, textvariable=elegirpre, bg= "#F0D973",font = ("Georgia"), width=450, justify=CENTER)
    espacio=Label(pre,text="\n", bg= "#F0D973")



    correcta=IntVar()

    opcion1=Button(pre, textvariable=uno, font= ("Georgia"), bg="#FA78BE", command =check1)
    opcion2=Button(pre, textvariable=dos, font= ("Georgia"), bg="#FA78BE", command = check2)
    opcion3=Button(pre, textvariable=tres, font= ("Georgia"), bg="#FA78BE", command = check3)

    check=Button(pre, text="Continuar", font= ("Georgia"), bg="#7DFFE0",command=continuepre)

    checkpre= Label (pre, textvariable = "", bg = "#F0D973", font=("Georgia","20", "bold"))
    regresar = Button(pre, text= "REGRESAR", bg = "#FA78BE", command = lambda:[menu.deiconify(),pre.iconify(), continuar1(), reset()])
    regresar.pack(side=BOTTOM)

    question.pack()
    espacio.pack()
    opcion1.pack()
    opcion2.pack()
    opcion3.pack()
    checkpre.pack()
    check.pack()
    regresar.pack()



menu=Tk()
menu.title("")
menu.geometry("800x400")
menu.resizable(0,0)
menu["bg"]="#F0D973"



buscar = StringVar()
posicion = random.choice(capitales)
buscar.set(posicion)
num=capitales.index(posicion)
buscar2=IntVar()
buscar2.set(num)

estado = StringVar()
posicionesta=random.choice(estados)
estado.set(posicionesta)
num2=estados.index(posicionesta)
buscar3=IntVar()
buscar3.set(num2)

elegirpre=StringVar()
pregunta=random.choice(preguntas)
elegirpre.set(pregunta)

ranres1=IntVar()
ranres2=IntVar()
ranres3=IntVar()

position1=preguntas.index(pregunta)
azar1=respuestas[position1]

print(pregunta)
print (azar1)


while True:
        azar2=random.choice(respuestas)
        azar3=random.choice(respuestas)
        if azar1==azar2 or azar1==azar3 or azar1==azar2 or azar2==azar3:
            continue
        else:
            break

azar.append(azar2)
azar.append(azar3)
posazar=random.randrange(3)
print(posazar)
azar.insert(posazar, azar1)
print (azar)


uno=StringVar()
dos=StringVar()
tres=StringVar()
uno.set(azar[0])
dos.set(azar[1])
tres.set(azar[2])

search=IntVar()
search.set(azar.index(azar1))

searchpre=IntVar()
searchpre.set(preguntas.index(pregunta))

count=3
lifes=IntVar()
lifes.set(count)

    
    

titulo=Label(menu, text = "México Interactivo", fg = "#D98C5D", bg = "#F0D973", font=("Georgia","20", "bold"))
titulo.place(x=280, y=100)

capitales=Button(menu, text = "Capitales", font=("Georgia"), bg = "#88D95D", command=ventanacapitales)
capitales.place(x=300, y=150)

estados=Button(menu, text = "Estados", font=("Georgia"), bg = "#88D95D", command = ventanaestados)
estados.place(x=430, y=150)

preguntas=Button(menu, text = "Preguntas Generales", font=("Georgia"), bg = "#88D95D", command = ventanapreguntas)
preguntas.place(x=320, y=200)

global cap
cap =Toplevel(menu)
cap.iconify()
global est
est = Toplevel(menu)
est.iconify()
global pre
pre=Toplevel(menu)
pre.iconify()



menu.mainloop()
