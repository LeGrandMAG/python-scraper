from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import UnexpectedAlertPresentException
import time
import schedule
import csv
import pandas as pd
import random
import emoji





#--------------------------------------PARAMETERS-----------------------------------------------
#setting the different variables
df = pd.read_csv('es.csv')
df.columns = ["names"]
gname = df['names']
times = 0
rand = random.randrange
# setting up the link to use in the project

productList = [
    'https://mobile.facebook.com/story.php?story_fbid=163074876142690&id=101047079012137', 
    'https://mobile.facebook.com/story.php?story_fbid=163312619452249&id=101047079012137', 
    'https://mobile.facebook.com/story.php?story_fbid=163299339453577&id=101047079012137', 
    'https://mobile.facebook.com/story.php?story_fbid=163301649453346&id=101047079012137', 
    'https://mobile.facebook.com/story.php?story_fbid=163307819452729&id=101047079012137', 
    'https://mobile.facebook.com/story.php?story_fbid=163202182796626&id=101047079012137', 
    'https://mobile.facebook.com/story.php?story_fbid=163170099466501&id=101047079012137', 
    'https://mobile.facebook.com/story.php?story_fbid=163190889464422&id=101047079012137'
]

descp = [
    "Je suis chaud.Je vends a Kinshasa et le prix est discutable. @wearewepo",
    "Produits originaux et des prix discutables. Jettez un coup d'oeil sur notre page WEPO pour plus de produits",
    "Vous cherchez des phones d'occasions et des prix discutables? Visitez notre page WEPO",
    "En savoir plus sur notre page WEPO. Produits dispo à Kin",
    "Bonne qualité, bon prix. WEPO"
]

login = "https://mobile.facebook.com/"
productLis = []
h = "https://www."
for i in productList:
    productLis.append(h + i[15:])


username = 'info.sensmart@gmail.com'
password = 'yeswecan'
gname = df['names']


gr = [
    'Vendre-acheter Kinshasa', 
    "Les pro de l'informatique", 
    'Acheter,Louer,Vendre des produits à Kinshasa/Somba, Teka na Kinshasa', 
    'Teka somba voiture à Kinshasa', 
    'Teka somba na prix ya Bien', 
    'Teka somba na prix ya bien', 
    'TEKA ET SOMBA À KINSHASA (VAINQUEUR)', 
    'Teka somba en ligne', 
    'Teka Somba téléphone tou', 
    'SOMBA TEKA MOKILI MOBIMBA', 
    '�Teka-Somba 24/24�', 
    'Vente de iPhone à Kinshasa', 
    'Vente en ligne à Kinshasa', 
    'TEKA SOMBA NA WENZE KINSHASA', 
    'Bi Teka Teka', 
    'ZANDO ya KINSHASA', 
    'TEKA SOMBA NA PRIX YA Bien', 
    'Teka-Kakola-Somba 2éme bord (Kinshasa)', 
    'Occasion de Kinshasa', 
    'KIN VENTE/ACHAT', 
    'Kinshasa Expats Business Center', 
    'TEKA SOMBA RAPIDE KINSHASA🇨🇩', 
    'Acheter & Vendre à Kinshasa RDC', 
    'Ekiti talo (solde, vente, achat, troc, promotion, publicité,... )', 
    'Bon Coin', 
    'Teka - Kakola - Somba (kinshasa)', 
    'Vente à Kinshasa', 
    'VENTE EN LIGNE, EN RDC ET AILLEURS', 
    'KINSHASA MAGASIN', 
    'Le bon coin pour les congolais', 
    'TEKA SOMBA Drc 243📸📹🚕📱💻⌚️👗👠👖🥾', 
    'Kinshasa Expats', 'Cop & Business Congo Kinshasa', 
    "Découvrez les meilleurs vendeurs d'iPhone à kinshasa", 
    'Vente De Iphone Moins Cher( Markus Toutterrain💪🏿✨✌️)', 
    'TEKA-_SOMBA ( Coop en Ligne)', 
    'TEKA - SOMBA - Marché congolais', 
    'BILOKOS 💯 %⛸️🚔🛴🚲🚿🎹🎻', 
    'KINSHASA BUSINESS (ACHATS ET VENTES)', 
    'Vente des iPhone 📱', 
    "A chercher d'un téléphone deal lushi ��", 
    'teka na congo', 
    'Undersky Group Vente Partout à Kinshasa', 
    'TEKA PE SOMBA NYONSO MOKILI MOBIMBA 📷☎️🚘🏠💻🖨️', 
    'Kinshasa � � vente de console', 
    'Teka /Somba/Vente et Achat/ Kinshasa +243', 
    'VENTE et TROC DE TÉLÉPHONE IPHONE et ANDROID à Kinshasa', 
    'Vente des véhicules toute sorte a Kinshasa', 
    'Vente et Achat Ordinateur Portable Kinshasa RDC', 
    'kin-Achat, - Vente et location', 'Teka Nyioso', 
    'Kinshasa Vente/Achat', 'Global Kinshasa Market', 
    'Allô teka na kin', 'TEKA SOMBA NA PRIX YA BIEN', 
    'Kps teka somba na prix ya bien', 
    "D.Law's Business women's. �Somba,Teka, pe Kakola en ligne na prix tokos�", 'TEKA, SOMBA TSHOMBO NA PRIX MANGONDO �����', 'Vente en ligne Kinshasa', 'TOZO TEKA PE TOZO SOMBA (vente et achat en ligne)���pour les Matadien', 'vente à Kinshasa', 'Vente en ligne filles, garçons +243891356043 chz davido', 'Teka pe Somba Nionso', 'RDC BUSINESS VENTE ET ACHAT EN LIGNE', 'Bon coin de vente et achat à Kinshasa iPhone, Samsung, itel, techno ....', "Teka'ngo Market", 'Business Avenue Kennedy (Achetez - Vendez & Troquez En Ligne)', 'TEKA KAKOLA SOMBA NA WENZE YA KINSHASA TSHANGU', 'teka somba na Kinshasa', 'VENTE DE TOUT A KINSHASA', 'Marché en ligne, Vente de tous KINSHASA', '📲Teka Somba✨na✨Prix ya bien!📲', 'TEKA SOMBA & BALI MOBILE', 'Kinshasa Members', 'Achats et ventes en ligne Tout Kinshasa', 'Teka somba na talo ya bien(Kinshasa)', 'Kinshasa Buy And Sell', 'Kinshasa 🇨🇩 achat et vente', 'Teka pe somba na kinshasa', 'Somba Tshombo', 'TEKA SOMBA NA PRIX YA BIEN', 'TEKA SOMBA NA PRIX YA BIEN', 'Libre échange ( TEKA SOMBA )�', 'Teka somba📱📲 achat et vente', '100 % Kinshasa business somba_pe_teka_kakola en ligne', '📱Teka-Somba✨En ligne!📱', "Teka somba na prix y'a bien", 'TEKA SOMBA NA CONGO avec LAMA SHOPPING', 'ANNONCE CONGO - Achats et Ventes des articles', 'TEKA SOMBA NA KINSHASA', 'VENTE EN LIGNE', 'Habits, Sacs, Chaussures et tous en vente/RDC', 'Teka Somba Iphone', 'VENTE ET ACHAT DES ORDINATEURS', 'KIN APPLE 🍏', 'BONNES AFFAIRES TEKA ,SOMBA Na KINSHASA-LUANDA', 'Teka chaud', 'Kinshasa Vente et Achat', 'Wenze Na Poche', 'Teka somba en ligne', 'Amazon Vents tout à Kinshasa', 'KINSHASA MAKAMBO DE PAPA MOLIERE', 'Acheter & Vendre des Biens et services en RDCongo', 'KINSHASA, AFFAIRES TEKA , SOMBA', 'TOUT TEKA NGO ( commerce en ligne)', 'Marché ya Kin (achat, vente, expertise, location, gestion immobilière...)', 'Congo Ventes', 'Vente et Achat facile', 'Vente et Achat a Kinshasa', 'ZandoNet (vente et achat de tout type de produit légal)', 'KINSHASA BUSINESS et MARKETING (vente, achat et pub)', 'Kinshasa somba teka eloko nayo', 'Brands Bazar Kinshasa', 'RDC 🇨🇩 Teka pé Somba', 'Bilokos (Achat/Vente/Troc/Offres. Je deal - Tu deal - On deal)', 'Congo Speed! VENDEZ ET TROQUER', 'À VENDRE, À ACHETER OU À DONNER À KINSHASA ET SES ENVIRONS']


#setting up the environment to use in the project

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
#chrome_options.add_argument('headless')



#========================================LAUNCH THE BROWSER======================================================
#Launch the browser
driver = webdriver.Chrome('C:/Users/maglo/OneDrive/Documents/chromedriver.exe',options=chrome_options)

#=============================================FUNCTIONS===============================================================


#=====LOGIN========
def Log(driver):
    driver.get(login)
    time.sleep(2)
    driver.find_element(By.TAG_NAME, "input[id='m_login_email']").send_keys(username)
    driver.find_element(By.TAG_NAME, "input[id='m_login_password']").send_keys(password)
    time.sleep(5)
    driver.find_element(By.TAG_NAME, "button[name='login']").click()
    
#==========CHECK LINK==============
link ="https://mobile.facebook.com/login/save-device/?login_source=login#_=_"


def checklink(link):
    d = WebDriverWait(driver, 30).until(EC.url_to_be(link))
    time.sleep(3)
    return d


#============COLLECT GROUP NAME ===============

#THIS FUNCTION WILL COLLECT ALL THE NAME OF THE GROUP I AM FOLLOWING
def grouploop(driver,gr):
    
    pp = driver.find_element(By.CSS_SELECTOR, "div[class ='b20td4e0 muag1w35']>div>div")
    for j in range(6):
        pp.send_keys(Keys.END)
        time.sleep(2)

    love = driver.find_elements(By.CSS_SELECTOR, "div[class ='b20td4e0 muag1w35']>div")

    for i in range(len(love)-1):
        ol = love[i].find_element(By.CSS_SELECTOR, "span").text
        if ol not in gr:
            gr.append(ol)
            time.sleep(2)
        else:
            time.sleep(2)
    
    return gr

#======= changing the user before posting =============
def changeuser(driver):
    time.sleep(3)
    try:
        v = driver.find_element(By.TAG_NAME, "html")
        v.send_keys(Keys.END)
    except UnexpectedAlertPresentException:
        time.sleep(10)
        print("Alert was seen, let's wait at least 10 seconds")
        v = driver.find_element(By.TAG_NAME, "html")
        v.send_keys(Keys.END)
    d = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[aria-label='Sélection du profil à utiliser']")))
    driver.find_element(By.CSS_SELECTOR,"button[aria-label='Sélection du profil à utiliser']").click()
    #d.find_element(By.CSS_SELECTOR, "button[aria-label='Sélection du profil à utiliser']").click()
    time.sleep(5)
    driver.find_element(By. CSS_SELECTOR,  "div[ class ='l9j0dhe7 ama3r5zh']>div>div>div>div>div>div:nth-child(3)").click()
    time.sleep(2)
    #driver.find_element(By.CSS_SELECTOR, "div[aria-label='Envoyez ceci à vos amis ou publiez-le sur votre journal.']").click()

#=====share in other group============

#For clicking on the sharing button
def share(driver):
    time.sleep(2)
    driver.find_element(By. CSS_SELECTOR,  "div[class ='tvfksri0 ozuftl9m']>div>div:nth-child(3)").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "div[ class = 'o36gj0jk eg9m0zos d76ob5m9']>div>div>div>div:nth-child(4)").click()


#===========SEARCH A GROUP WHERE TO PSOT AT============


#THI FUNCTION WILL TYPE THE GROUP NAME AND CHOOSE IT

def tsearch(driver, gr, n):
    time.sleep(2)
    v = driver.find_element(By.TAG_NAME, "html")

    search = driver.find_element(By.CSS_SELECTOR, "input[aria-label='Rechercher des groupes']")
    if (search.get_attribute('value') !=''):
        search.send_keys(Keys.CONTROL, 'a')
        time.sleep(1)
        search.send_keys(Keys.DELETE)
        time.sleep(1)
    try:
        search.send_keys(gr[n][:30])
        time.sleep(3)
        lo = driver.find_element(By.CSS_SELECTOR, "div[class='b20td4e0 muag1w35']>div>div")
        lo.click()
    except WebDriverException:
        pass
    

#========write the post description =======================

def createpost(driver, descp):

    time.sleep(2)
    content = driver.find_element(By.CSS_SELECTOR, "div[class = 'taijpn5t j83agx80']")
    ub = content.find_element(By.CSS_SELECTOR, "br[data-text='true']")
    z = descp[random.randrange(0,len(descp)-1)]

    if (ub.text != ""):
        z = descp[random.randrange(0,len(descp)-1)]
        print(z)
        time.sleep(3)
        ub.send_keys(z)
        #webdriver.ActionChains(driver).send_keys(descp[random.randrange(0,len(descp))])
    else:
        time.sleep(2)
        ub.send_keys(z)
        #webdriver.ActionChains(driver).send_keys(descp[random.randrange(0,len(descp))])
        ##content.send_keys(descp[random.randrange(0,len(descp))])






    


#================click the publish button=====================
def publish(driver):
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "div[aria-label='Publier'").click()
    time.sleep(5)

times = 0
def productpost(driver, gname, descp, prod,times):
    stock = []
    numg = 0
    while(True):
        group = random.randint(1,len(gname)-1)

        #number of groups
        
        driver.refresh()
        time.sleep(5)
        changeuser(driver)
        
        share(driver)
        if (group in stock):
            print("This group already exist")
        else:
            try:
                tsearch(driver, gname, group)
                createpost(driver,descp)
                publish(driver)
                time.sleep(3)
            except WebDriverException:
                print("could not print the file")
                driver.refresh()
                time.sleep(3)
            numg += 1
            times +=1
            stock.append(group)
            print("------------------------------")
            
            print(f"Product {prod} was posted in {numg} groups far...")
        
        
        if (len(stock) >= 100):
            break
    prod += 1
        
