from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import io
import os
import requests

#CHeck for the right PATH!
driver = webdriver.Chrome(executable_path ="/Users/mikev/Google Drive/Py/bin/chromedriver")

main_window = driver.current_window_handle

def create_form(urls):
    team_names = []
    for url in urls:
        s=""
        i = 32
        while url[i]!="/":
            s+=url[i]
            i+=1
        team_names.append(s)

    forms = []
    for url in urls:
        #url = "https://www.flashscore.com/team/liverpool/lId4TMwf/"
        driver.get(url)

        html = driver.page_source

        driver.close()
        driver.switch_to_window(main_window)

        #soup = BeautifulSoup(html, 'lxml')
        soup = BeautifulSoup(html)

        d = soup.find('div', "leagues--static event--leagues summary-results")
        spans = d.find_all('span')

        lines = [span.get_text() for span in spans]

        form =[]
        for line in lines:
            if line in ['W', 'L', 'D']:
                form.append(line)
        form = form[:7]
        """
        form =""
        for line in lines:
            if line in ['W', 'L', 'D']:
                form+=line
        form = form[:7]
        """
        forms.append(form)
        driver.execute_script("window.open();")

        driver.switch_to_window(driver.window_handles[1])

    df = pd.DataFrame(list(zip(team_names, forms)),
                   columns =['Team', 'Form'])
    return df



#ext = ["ChL","En", "Ger", "It", "Nl", "Sp"]+ ["Fr"]
ext = ["En","Fr","Ger", "It", "Nl", "Sp", "Port", "ChL", "Eur"]

form = pd.DataFrame()



for ex in ext:
    #new driver window
    driver.execute_script("window.open();")
    driver.switch_to_window(driver.window_handles[1])
    #team url txt file
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    s = "urls"+ex+".txt"
    s = os.path.join(THIS_FOLDER, s)
    urls = [line.rstrip('\n') for line in open(s)]
    #df maker
    df = create_form(urls)
    form = form.append(df)


form = form.sort_values(by=['Team'])
form = form.reset_index(drop=True)



dfw = form['Team']
L=[]
#trim '-''!!!!!!!!!!!!!!!!!!!!!!!! important for the if below
for i in range(len(dfw)):
    s=''
    for char in dfw[i]:
        if char!="-":
                s+=char
    L.append(s)
    if L[i]=='rapidvienna':
        L[i] = 'rapidwien'
    if L[i]=='spartakmoscow':
        L[i] = 'spartakmoskva'
    if L[i]=='malmoff':
        L[i] = 'malmoe'
    if L[i]=='moreirense':
        L[i] = 'Moreirense'
    if L[i]=='ferreira':
        L[i] = 'PacosFerreira'
    if L[i]=='vitoriaguimaraes':
        L[i] = 'Guimaraes'
    if L[i]=='gaeagles':
        L[i] = 'GoAheadEagles'
    if L[i]=='greutherfurth':
        L[i] = 'fuerth'
    if L[i]=='krasnodar':
        L[i] = 'fckrasnodar'
    if L[i]=='lokomotivmoscow':
        L[i] = 'lokmoskva'
    if L[i]=='fcporto':
        L[i] = 'porto'
    if L[i]=='olympiacospiraeus':
        L[i] = 'olympiakos'
    if L[i]=='clubbrugge':
        L[i] = 'brugge'
    if L[i]=='basaksehir':
        L[i] = 'Bueyueksehir'
    if L[i]=='zenitstpetersburg':
        L[i] = 'zenit'
    if L[i]=='manchestercity':
        L[i] = 'ManCity'
    if L[i]=='sheffieldutd':
        L[i] = 'SheffieldUnited'
    if L[i]=='manchesterunited':
        L[i] = 'ManUnited'
    if L[i]=='newcastleutd':
        L[i] = 'newcastle'
    if L[i]=='stetienne':
        L[i] = 'Saint-Etienne'
    if L[i]=='amienssc':
        L[i] = 'amiens'
    if L[i]=='bayernmunich':
        L[i] = 'bayern'
    if L[i]=='bmonchengladbach':
        L[i] = 'Gladbach'
    if L[i]=='bayerleverkusen':
        L[i] = 'Leverkusen'
    if L[i]=='eintrachtfrankfurt':
        L[i] = 'frankfurt'
    if L[i]=='herthaberlin':
        L[i] = 'hertha'
    if L[i]=='1fckoln':
        L[i] = 'koeln'
    if L[i]=='werderbremen':
        L[i]='werder'
    if L[i]=='vfbstuttgart':
        L[i]='stuttgart'
    if L[i]=='arminiabielefeld':
        L[i]='bielefeld'
    if L[i]=='asroma':
        L[i]='roma'
    if L[i]=='acmilan':
        L[i]='milan'
    if L[i]=='azalkmaar':
        L[i]='alkmaar'
    if L[i]=='fcemmen':
        L[i]='emmen'
    if L[i]=='atlmadrid':
        L[i]='atletico'
    if L[i]=='realsociedad':
        L[i]='sociedad'
    if L[i]=='granadacf':
        L[i]='granada'
    if L[i]=='athbilbao':
        L[i]='bilbao'
    if L[i]=='celtavigo':
        L[i]='celta'
    if L[i]=='liberec':
        L[i]='slovanliberec'
    if L[i]=='dinzagreb':
        L[i]='dinamozagreb'
    if L[i]=='wolfsbergerac':
        L[i]='wolfsberg'
    if L[i]=='cskamoscow':
        L[i]='cskamoskva'
    if L[i]=='lasklinz':
        L[i]='lask'
    if L[i]=='maccabitelaviv':
        L[i]='mtelaviv'
    if L[i]=='ludogorets':
        L[i]='razgrad'
    if L[i]=='qarabagagdam':
        L[i]='KarabakhAgdam'
    if L[i]=='spartaprague':
        L[i]='spartapraha'
    if L[i]=='stliege':
        L[i]='standard'
    if L[i]=='lechpoznan':
        L[i]='lech'
    if L[i]=='hbeersheva':
        L[i]='beer-sheva'
    if L[i]=='slaviaprague':
        L[i]='slaviapraha'
    if L[i]=='rapidvienna':
        L[i]='rapidwien'


#elo TIME!
N = len(form)
for i in range(N):
    #print (L[i])
    url = "http://api.clubelo.com/"
    url2 = url+L[i]
    s = requests.get(url2).content
    elo = pd.read_csv(io.StringIO(s.decode('utf-8')))
    j=elo.index[-1]
    el = elo["Elo"][j]
    form.at[i, 'EloH'] = el #add in dataframe

#export to csv
path = r"C:\MAMP\htdocs\magic"
import os
form.to_csv(os.path.join(path,r'form.csv'))
