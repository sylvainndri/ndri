# impoter les packages
import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import multivariate_normal
from PIL import Image
from streamlit_option_menu import option_menu
import json
import requests
from streamlit_lottie import st_lottie
import os
import emoji
import time
import base64
from io import StringIO, BytesIO
from pptx import Presentation
from pptx.util import Inches
import sqlite3
import hashlib
# ---------------------- Importer les images -----------------------
image = Image.open('Y3.png')
st.set_page_config(page_title="Mon App de Risk Management",
                   page_icon="🧊",
                   initial_sidebar_state="expanded",
                   layout="wide" # utilise la largeur maximale,
                   )
# Supprimer l'option de menu de streamlit
hide_menu = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu, unsafe_allow_html=True)

# definition les fonctions
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False

# DB Management
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
    conn.commit()

def login_user(username,password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
    data = c.fetchall()
    return data


def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data


def main():
    # Créer un expander dans la barre latérale
    options_expander = st.sidebar.expander("Connexion")
    with options_expander:
        choice=st.selectbox("",["S'inscrire","Se connecter"],index=1)
    if choice=="Se connecter":
        with options_expander:
            username = st.text_input("Identifiant")
            password = st.text_input("Mot de passe",type='password')
        if username and password is not None:
            if st.sidebar.checkbox("Se connecter"):
                create_usertable()
                hashed_pswd = make_hashes(password)

                result = login_user(username,check_hashes(password,hashed_pswd))
                if result:
                    with st.spinner("Conexion en cours..."):
                        time.sleep(1)
                        result = st.success("Connxion effectuée avec succès")
                        # Attendre 3 secondes avant de masquer l'alerte
                        for i in range(1):
                            time.sleep(1)

                        # Effacer l'alerte de succès
                        result.empty()

                    # ---------------------Option de déconnexion
                    if st.button("Déconnexion"):
                        st.success("Déconnecté avec succès !.")
                        st.stop()

                    test_a_faire= option_menu(
                        menu_title=None,
                        options=["Home","Stress Tests","Reverses Tests","IFRS 9","Contact"],
                        icons=["house","list-task","list-task","list-task",'envelope'],
                        menu_icon="cast",
                        default_index=0,
                        orientation="horizontal",

                        styles={
                            "container": {"padding": "0!important","background-color": "#cccccc"},
                            "icon": {"color": "white", "font-size": "16px"},
                            "nav-link": {"font-size": "16px", "text-align": "center", "margin":"0px"},
                            "nav-link-selected": {"background-color": "#0E6655"},
                        }
                    )

                    if test_a_faire=="Home":
                        st.cache(allow_output_mutation=True,show_spinner=True,suppress_st_warning=True)
                        def load_lottiefile(filepath: str):
                            with open(filepath, "r") as f:
                                return json.load(f)
                        def load_lottieurl(url: str):
                            r = requests.get(url)
                            if r.status_code != 200:
                                return None
                            return r.json()
                        z1,sep,z2=st.columns([8,0.2,8])
                        st.markdown("***")
                        with z1:
                            st.markdown("""
                                  ***
                                 ### Bienvenue sur l'application de Risk Management
                                  
                                  ***
                                  """)

                        with z2:
                            st.image(image, caption="Audits & Conseils")
                            st.write(emoji.emojize("""# App de Risk Management """))
                        lottie_hello = load_lottiefile("110031-welcome.json")
                        # lottie_hello = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_d8cmv6qa.json")
                        with z1:
                            st_lottie(
                                lottie_hello,
                                speed=1,
                                reverse=False,
                                loop=True,
                                quality="low", # medium ; high
                                #renderer="svg", # canvas
                                height=None,
                                width=None,
                                key=None,
                            )
                            st.balloons()


                    elif test_a_faire == "Contact":

                        st.cache(allow_output_mutation=True,show_spinner=True,suppress_st_warning=True)
                        e1, sep,e2=st.columns([8,0.2,8])
                        with e1:
                            """
                            ## Departement Risk Management
                            ### Etude Statistique et modélisation
                            ***
                            #### Sylvain N'DRI
                            * Economiste | Economètre Financier | Data Analyst & Machine Learning Consultant Junior
                            * Contact :+225 0778804983/0140015896
                            * Email: sylvain.ngoran.ndri@gmail.com
                            * Vous pouvez accéder à mon [linkedin](https://www.linkedin.com/in/n-goran-sylvain-n-dri-1b778b1a1/) en cliquant sur ce lien.
                            ***
                            """
                        with e2 :
                            def load_lottiefile(filepath: str):
                                with open(filepath, "r") as f:
                                    return json.load(f)
                            def load_lottieurl(url: str):
                                r = requests.get(url)
                                if r.status_code != 200:
                                    return None
                                return r.json()

                            lottie_hello = load_lottiefile("h.json")
                            #lottie_hello = load_lottieurl("https://assets1.lottiefiles.com/private_files/lf30_TBKozE.json")
                            # st.markdown("***")
                            st_lottie(
                                lottie_hello,
                                speed=1,
                                reverse=False,
                                loop=True,
                                quality="low", # medium ; high
                                #renderer=
                                height=None,
                                width=None,
                                key=None,
                            )



                    elif test_a_faire== "Stress Tests":

                        st.write("Hello stress test")





                    elif test_a_faire=="IFRS 9":
                        st.cache(allow_output_mutation=True,show_spinner=True,suppress_st_warning=True)
                        with open('style.css') as f:
                            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
                            st.markdown("---")
                        options_expander = st.sidebar.expander("J'importe les données")
                        with options_expander:
                            st.header("Nom de la banque")
                            nom_utilisateur=st.text_input("")
                            date=st.date_input("Date")

                        choice= option_menu(
                            menu_title=None,
                            options=["PD","LGD","EAD","ECL"],
                            icons=["reception-4","snow3","speedometer","list-task"],
                            menu_icon="cast",
                            default_index=0,
                            orientation="horizontal",


                            styles={
                                "container": {"padding": "0!important"},
                                "icon": {"color": "green", "font-size": "25px"},
                                "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px"},
                                "nav-link-selected": {"background-color": "#008080"},
                            }
                        )
                        global  df_lgd, df_lgd_s1_ens, df_pd, df_ead
                        with options_expander:
                            data_frame_import = st.file_uploader("Télécharger xlsx",type=["xlsx"])
                        if data_frame_import is not None:
                            with options_expander:
                                st.sidebar.success('Téléchargement reussi!', icon="✅")
                            try:
                                df_all=pd.read_excel(data_frame_import,sheet_name="LGD")
                                df_pd=pd.read_excel(data_frame_import,sheet_name="PD")
                                # df_ead=pd.read_excel(data_frame_import,sheet_name="EAD")


                                # ------------Marque de saisir ---Enter values--------------------
                                a,s,b=st.sidebar.columns([8,0.2,8])
                                with a:
                                    value_one=st.number_input("Valeur Minimale",90)
                                    value_two=st.number_input("Valeur Maximale",180)

                                options_expander = st.sidebar.expander("Notes")
                                with options_expander:
                                    st.markdown("""
                                        #### Notes :
                                        * Les valeurs saisies désignent les bornes pour la classification des stages.
                                        * 90 et 180 sont les valeurs par défaut.
                                        * S1 est inférieur ou égal à la valeur minimale.
                                        * S2 est supérieur à la valeur minimale et inférieure à la valeur maximale
                                        * S3 est strictement supérieur à la valeur maximale                              
                                        """)
                                def bucket1(bucket):
                                    if bucket <= value_one:
                                        return 1
                                    elif bucket > value_one and bucket <= value_two:
                                        return 2
                                    else:
                                        return 3
                                df_all["Bucket"]=df_all["Nombre Jours Impayés"].apply(bucket1)
                                df_all["Bucket"]=df_all["Nombre Jours Impayés"].apply(bucket1)
                                df_lgd=df_all[["Bucket","Catégorie","Date d'entrée","Date de defaut","Encours"]]
                                df_ead=df_all[["Bucket","Catégorie","Montant de prêt","Montant reçu","Exposition Bilan","Exposition HB"]]
                                with b:
                                    choix_radio_stage=st.radio("",["Strate 1","Strate 2","Strate 3"],
                                                               horizontal=False,index=0)


                            except Exception as e:
                                st.write("Télécharger les données")
                        try:
                            # --------------PD----------
                            def rating_classe(Nombre):
                                if Nombre <=30:
                                    return "AAA"
                                elif Nombre>30 and Nombre<= 60:
                                    return "AA"
                                elif Nombre >60 and Nombre <= 90:
                                    return "A"
                                elif Nombre >90 and Nombre <= 120:
                                    return "BB"
                                elif Nombre > 120 and Nombre <=150:
                                    return "B"
                                elif Nombre >150 and Nombre <=180:
                                    return "CCC"
                                else:
                                    return "DDD"
                            def fois_100(valeur):
                                return valeur*100
                            def matrice(df):
                                df_pd=df.copy()
                                df_pd["Notation Initiale"]=df_pd["NBJ1"].apply(rating_classe)
                                df_pd["Notation Suivante"]=df_pd["NBJ2"].apply(rating_classe)
                                # matrice de transition
                                transition_matrix=pd.crosstab(df_pd["Notation Initiale"], df_pd["Notation Suivante"])
                                transition_matrix= transition_matrix.div(transition_matrix.sum(axis = 1), axis = 0)
                                transition_matrix=transition_matrix.apply(lambda x: round(x,4))
                                # transition_matrix=transition_matrix.apply(lambda x: fois_100(x))
                                return transition_matrix

                            # ----------Par catégorie ------------------------
                            df_pd_ens=df_pd.copy()
                            df_pd_partucilier=df_pd[df_pd["Catégorie"]=="Particulier"]
                            df_pd_Grande_Entreprise=df_pd[df_pd["Catégorie"]=="Grande Entreprise"]
                            df_pd_pme=df_pd[df_pd["Catégorie"]=="PME"]
                            df_pd_salarie=df_pd[df_pd["Catégorie"]=="Salarié"]
                            # -------Appliquer la fonction -----

                            df_pd_ens=matrice(df_pd_ens).copy()
                            df_pd_partucilier=matrice(df_pd_partucilier).copy()
                            df_pd_Grande_Entreprise=matrice(df_pd_Grande_Entreprise).copy()
                            df_pd_pme=matrice(df_pd_pme).copy()
                            df_pd_salarie=matrice(df_pd_salarie).copy()
                        #-------------------------Produit matriciel  si nécessaire-----------
                            index, colonne=df_pd_ens.index,df_pd_ens.columns
                            # les produits ---------------------*
                            df_pd_ens=np.dot(df_pd_ens.values,df_pd_ens.values)
                            # df_pd_partucilier=np.dot(df_pd_partucilier.values,df_pd_partucilier.values)
                            # df_pd_Grande_Entreprise=np.dot(df_pd_Grande_Entreprise.values, df_pd_Grande_Entreprise.values)
                            # df_pd_pme=np.dot(df_pd_pme.values,df_pd_pme.values)
                            # df_pd_salarie=np.dot(df_pd_salarie.values, df_pd_salarie.values)

                            def matpro(df):
                                df=df.copy()
                                df=pd.DataFrame(data=df, index=index, columns=colonne)
                                df=df.apply(lambda x: fois_100(x))
                                return df
                            df_pd_ens=matpro(df_pd_ens)
                            # df_pd_partucilier=matpro(df_pd_partucilier)
                            # df_pd_Grande_Entreprise=matpro(df_pd_Grande_Entreprise)
                            # df_pd_pme=matpro(df_pd_pme)
                            # df_pd_salarie=matpro(df_pd_salarie)


                    # ----------------------LGD ----------------------------------------------
                            def difference(value_one,value_two):

                                value=int(value_one-value_two)
                                if value >= 0:
                                    return value
                                elif value < 0:
                                    return -value

                            # filtrer
                            df_lgd_s=df_lgd.copy()
                            df_lgd_s1=df_lgd_s[df_lgd_s["Bucket"]==1]
                            df_lgd_s2=df_lgd_s[df_lgd_s["Bucket"]==2]
                            df_lgd_s3=df_lgd_s[df_lgd_s["Bucket"]==3]

                            #--------------------------LGD-------------------------
                            #--------------------stage 1 -----------------------------
                            df_lgd_s1_ens=df_lgd_s1.copy()
                            df_lgd_s1_partucilier=df_lgd_s1[df_lgd_s1["Catégorie"]=="Particulier"]
                            df_lgd_s1_grande_entreprise=df_lgd_s1[df_lgd_s1["Catégorie"]=="Grande Entreprise"]
                            df_lgd_s1_pme=df_lgd_s1[df_lgd_s1["Catégorie"]=="PME"]
                            df_lgd_s1_salarie=df_lgd_s1[df_lgd_s1["Catégorie"]=="Salarié"]

                            #----------------------------Stage 2-------------------------
                            df_lgd_s2_ens=df_lgd_s2.copy()
                            df_lgd_s2_partucilier=df_lgd_s2[df_lgd_s2["Catégorie"]=="Particulier"]
                            df_lgd_s2_grande_entreprise=df_lgd_s2[df_lgd_s2["Catégorie"]=="Grande Entreprise"]
                            df_lgd_s2_pme=df_lgd_s2[df_lgd_s2["Catégorie"]=="PME"]
                            df_lgd_s2_salarie=df_lgd_s2[df_lgd_s2["Catégorie"]=="Salarié"]

                            #----------------------------Stage 3-------------------------
                            df_lgd_s3_ens=df_lgd_s3.copy()
                            df_lgd_s3_partucilier=df_lgd_s3[df_lgd_s3["Catégorie"]=="Particulier"]
                            df_lgd_s3_grande_entreprise=df_lgd_s3[df_lgd_s3["Catégorie"]=="Grande Entreprise"]
                            df_lgd_s3_pme=df_lgd_s3[df_lgd_s3["Catégorie"]=="PME"]
                            df_lgd_s3_salarie=df_lgd_s3[df_lgd_s3["Catégorie"]=="Salarié"]



                            ## ----------------------------------------- Calcul de la LGD--------------------------------------------------------------

                            def calcul_lgd(data):
                                global final_output
                                df_lgd=data

                                df_lgd["colonne"]=df_lgd[["Date d'entrée","Date de defaut"]].apply(lambda df_lgd:difference(df_lgd["Date d'entrée"],
                                                                                                                            df_lgd["Date de defaut"]),axis=1)
                                triangle=pd.pivot_table(df_lgd, index="Date d'entrée",aggfunc="sum",columns="colonne",values="Encours")

                                #--------------------------------------------------------------------------------------------------------------
                                # ----------------------ETAPE DE CALCUL LGD---------------------------------
                                # données
                                df_lgd=triangle.copy()
                                data_copy=df_lgd.copy()
                                columns_number=len(data_copy.columns)
                                data_copy_lgd=df_lgd.copy()
                                df_soustration=data_copy_lgd
                                #  Soustration faire la difference
                                for i in range(len(df_soustration.columns)-1):
                                    df_soustration["diff{}-{}".format(i+1, i+2)] = df_soustration.iloc[:, i]-df_soustration.iloc[:, i+1]
                                # recuperer la premiere colonne
                                df_soustration.columns._values[0]="Enter"
                                premiere_colonne=df_soustration.iloc[:,0]
                                # recuperer les dernières colonnes
                                derniere_colonne=df_soustration.iloc[:,-(len(data_copy.columns)-1):]
                                # # calculer le cumul par ligne de chaque des colonnes
                                df_copy_0=derniere_colonne.copy()
                                derniere_colonne_cumul = pd.DataFrame()
                                n = len(df_copy_0.columns)
                                for i in range(1, n+1):
                                    derniere_colonne_cumul[f'cumul_{i}'] = df_copy_0.iloc[:, :i].sum(axis=1)
                                # récuperer le trianlge de Chain Ladder
                                l = list(derniere_colonne_cumul.keys())
                                for idx, key in enumerate(l[::-1]):
                                    derniere_colonne_cumul[key] = derniere_colonne_cumul[key].iloc[:idx+1]

                                # # combiner les data
                                combiner=pd.concat([premiere_colonne,derniere_colonne_cumul],axis=1)
                                # combiner=pd.concat([premiere_colonne,derniere_colonne],axis=1)
                                # remplacer les valeurs négatives par des zeros
                                for col in combiner.columns:
                                    combiner[col] = combiner[col].apply(lambda x: 0 if x<0 else x)
                                # calculer les rapports.
                                for i in range(len(combiner.columns)-1):
                                    combiner['T {}'.format(i+1)] = combiner.iloc[:, i+1] / combiner.iloc[:, 0]
                                # récupérer les rapports
                                rapport=combiner.iloc[:,-(len(data_copy.columns)-1):]
                                # la moyenne
                                moy_rapport= rapport.mean(axis=0)
                                # le taux de recuperation
                                taux_recuperation=pd.DataFrame(moy_rapport,columns=["Taux de récupération"])
                                # taux_recuperation["Taux de recupération"] = taux_recuperation["Valeur"].cumsum()
                                taux_recuperation["Taux LGD"]=1-taux_recuperation["Taux de récupération"]
                                # taux_recuperation["Taux LGD cumulé"]=taux_recuperation["Taux LGD"].cumsum()
                                # Calculez la variation de la colonne taux de recuperation
                                variation = taux_recuperation["Taux de récupération"].diff()
                                # Calculer le taux de croissance
                                taux_croissance = variation / taux_recuperation["Taux de récupération"].shift(1)
                                taux_croissance=pd.DataFrame(taux_croissance)
                                taux_croissance.columns = ['Taux de croissance']
                                taux_recuperation["Taux de croissance"]=taux_croissance['Taux de croissance']
                                final_output=taux_recuperation.copy()
                                return final_output


                            #---------------------------APPLIQUER LA FONCTION DE LGD  AUX CATEGOIRES----------------------------------------
                            # -------------------------Stage 1----------------------------------------------
                            df_lgd_s1_ens=calcul_lgd(df_lgd_s1_ens).copy()
                            df_lgd_s1_particulier=calcul_lgd(df_lgd_s1_partucilier).copy()
                            df_lgd_s1_grande_entreprise=calcul_lgd(df_lgd_s1_grande_entreprise).copy()
                            df_lgd_s1_pme=calcul_lgd(df_lgd_s1_pme).copy()
                            df_lgd_s1_salarie=calcul_lgd(df_lgd_s1_salarie).copy()


                            # -------------------------Stage 2----------------------------------------------
                            df_lgd_s2_ens=calcul_lgd(df_lgd_s2_ens).copy()
                            df_lgd_s2_particulier=calcul_lgd(df_lgd_s2_partucilier).copy()
                            df_lgd_s2_grande_entreprise=calcul_lgd(df_lgd_s2_grande_entreprise).copy()
                            df_lgd_s2_pme=calcul_lgd(df_lgd_s2_pme).copy()
                            df_lgd_s2_salarie=calcul_lgd(df_lgd_s2_salarie).copy()

                            # -------------------------Stage 3----------------------------------------------
                            df_lgd_s3_ens=calcul_lgd(df_lgd_s3_ens).copy()
                            df_lgd_s3_particulier=calcul_lgd(df_lgd_s3_partucilier).copy()
                            df_lgd_s3_grande_entreprise=calcul_lgd(df_lgd_s3_grande_entreprise).copy()
                            df_lgd_s3_pme=calcul_lgd(df_lgd_s3_pme).copy()
                            df_lgd_s3_salarie=calcul_lgd(df_lgd_s3_salarie).copy()

                    ## -----------------------EAD -------------------------

                            df_ead_s=df_ead.copy()
                            df_ead_s1=df_ead_s[df_ead_s["Bucket"]==1]
                            df_ead_s2=df_ead_s[df_ead_s["Bucket"]==2]
                            df_ead_s3=df_ead_s[df_ead_s["Bucket"]==3]

                            #---------------------------EAD-------------------------------------
                                                        # -------------------Stage 1 --------------------------------------
                            df_ead_s1_ens=df_ead_s1.copy()
                            df_ead_s1_particulier=df_ead_s1[df_ead_s1["Catégorie"]=="Particulier"]
                            df_ead_s1_grande_entreprise=df_ead_s1[df_ead_s1["Catégorie"]=="Grande Entreprise"]
                            df_ead_s1_pme=df_ead_s1[df_ead_s1["Catégorie"]=="PME"]
                            df_ead_s1_salarie=df_ead_s1[df_ead_s1["Catégorie"]=="Salarié"]

                                                         # -------------------Stage 2 --------------------------------------
                            df_ead_s2_ens=df_ead_s2.copy()
                            df_ead_s2_particulier=df_ead_s2[df_ead_s2["Catégorie"]=="Particulier"]
                            df_ead_s2_grande_entreprise=df_ead_s2[df_ead_s2["Catégorie"]=="Grande Entreprise"]
                            df_ead_s2_pme=df_ead_s2[df_ead_s2["Catégorie"]=="PME"]
                            df_ead_s2_salarie=df_ead_s2[df_ead_s2["Catégorie"]=="Salarié"]

                                                         # -------------------Stage 3 --------------------------------------
                            df_ead_s3_ens=df_ead_s3.copy()
                            df_ead_s3_particulier=df_ead_s3[df_ead_s3["Catégorie"]=="Particulier"]
                            df_ead_s3_grande_entreprise=df_ead_s3[df_ead_s3["Catégorie"]=="Grande Entreprise"]
                            df_ead_s3_pme=df_ead_s3[df_ead_s3["Catégorie"]=="PME"]
                            df_ead_s3_salarie=df_ead_s3[df_ead_s3["Catégorie"]=="Salarié"]

                            # ---------------Fonction ----
                            def calcul_ead(df):
                                df=df.copy()
                                # calculer le ccf
                                ccf=(df["Montant de prêt"]-df["Montant reçu"])/df["Montant de prêt"]
                                ccf=ccf.mean()
                                montant=df["Montant de prêt"]
                                montant=montant.mean()
                                ead=montant*ccf
                                ead=pd.DataFrame({"Montant":[montant],"CCF":[ccf],"EAD":[ead]})

                                # ead=df["Exposition Bilan"]+ccf*df["Exposition HB"]
                                return ead




                    #---------------------------APPLIQUER LA FONCTION DE EAD  AUX CATEGOIRES----------------------------------------

                                            #----------------------------Stage 1---------------------------------
                            df_ead_s1_ens=calcul_ead(df_ead_s1_ens).copy()
                            df_ead_s1_particulier=calcul_ead(df_ead_s1_particulier).copy()
                            df_ead_s1_grande_entreprise=calcul_ead(df_ead_s1_grande_entreprise).copy()
                            df_ead_s1_pme=calcul_ead(df_ead_s1_pme).copy()
                            df_ead_s1_salarie=calcul_ead(df_ead_s1_salarie).copy()

                                                #----------------------------Stage 2---------------------------------
                            df_ead_s2_ens=calcul_ead(df_ead_s2_ens).copy()
                            df_ead_s2_particulier=calcul_ead(df_ead_s2_particulier).copy()
                            df_ead_s2_grande_entreprise=calcul_ead(df_ead_s2_grande_entreprise).copy()
                            df_ead_s2_pme=calcul_ead(df_ead_s2_pme).copy()
                            df_ead_s2_salarie=calcul_ead(df_ead_s2_salarie).copy()

                                                #-------------------------  Stage 3-------------------------------
                            df_ead_s3_ens=calcul_ead(df_ead_s3_ens).copy()
                            df_ead_s3_particulier=calcul_ead(df_ead_s3_particulier).copy()
                            df_ead_s3_grande_entreprise=calcul_ead(df_ead_s3_grande_entreprise).copy()
                            df_ead_s3_pme=calcul_ead(df_ead_s3_pme).copy()
                            df_ead_s3_salarie=calcul_ead(df_ead_s3_salarie).copy()


                            # --------------------les EAD -----------------
                            index=["Ensemble","Particulier","Grande Entreprise","PME","Salarié"]
                            df_ead_s1=pd.concat([df_ead_s1_ens,df_ead_s1_particulier,df_ead_s1_grande_entreprise,df_ead_s1_pme,df_ead_s1_salarie],axis=0)
                            df_ead_s2=pd.concat([df_ead_s2_ens,df_ead_s2_particulier,df_ead_s2_grande_entreprise,df_ead_s2_pme,df_ead_s2_salarie],axis=0)
                            df_ead_s3=pd.concat([df_ead_s3_ens,df_ead_s3_particulier,df_ead_s3_grande_entreprise,df_ead_s3_pme,df_ead_s3_salarie],axis=0)

                            df_ead_s1["index"]=index
                            df_ead_s2["index"]=index
                            df_ead_s3["index"]=index
                            df_ead_s1=df_ead_s3.set_index("index")
                            df_ead_s2=df_ead_s3.set_index("index")
                            df_ead_s3=df_ead_s3.set_index("index")


                            if choice=="PD":
                                col1,sep,col2,sep,col3=st.columns([2,0.2,8,0.2,2])
                                with col2:

                                    st.markdown("""
                                        ####  Probabilité de défaut 
                                        """)
                                    choix_radio=st.radio("",["Ensemble","Particulier","Grande Entreprise","PME","Salarié"],
                                                             horizontal=True,index=0)
                                st.markdown("***")
                                if choix_radio=="Ensemble":
                                    st.table(df_pd_ens)
                                    st.write(df_pd_ens.iloc[:,-1].iloc[0])
                                    #df_pd_ens.iloc[:,-1]).iloc[0]
                                elif choix_radio=="Particulier":
                                    st.table(df_pd_partucilier)
                                elif choix_radio=="Grande Entreprise":
                                    st.table(df_pd_Grande_Entreprise)
                                elif choix_radio=="PME":
                                    st.table(df_pd_pme)
                                elif choix_radio=="Salarié":
                                    st.table(df_pd_salarie)

                            # afficher les résultats de LGD

                            elif choice=="LGD":
                                col1,sep,col2,sep,col3=st.columns([2,0.2,8,0.2,2])
                                with col2:

                                    st.markdown("""
                                        ####  Perte en cas de défaut : Loss Given Default
                                        """)
                                    choix_radio=st.radio("",["Ensemble","Particulier","Grande Entreprise","PME","Salarié"],
                                                             horizontal=True,index=0)

                                st.markdown("***")

                                # ----------------Stage 1----------------------------------
                                if choix_radio_stage=="Strate 1":
                                    if choix_radio=="Ensemble":
                                        st.table(df_lgd_s1_ens)
                                        st.write(df_ead_s1.iloc[:,-1].iloc[0])
                                        #df_ead_s1.iloc[:,-1]).iloc[0]
                                    elif choix_radio=="Particulier":
                                        st.table(df_lgd_s1_particulier)
                                    elif choix_radio=="Grande Entreprise":
                                        st.table(df_lgd_s1_grande_entreprise)
                                    elif choix_radio=="PME":
                                        st.table(df_lgd_s1_pme)

                                    elif choix_radio=="Salarié":
                                        st.table(df_lgd_s1_salarie)

                                    else:
                                        st.write("Veuillez choisir une option")

                                #--------------------Stage 2---------------------------------------------
                                elif choix_radio_stage=="Strate 2":
                                    if choix_radio=="Ensemble":
                                        st.table(df_lgd_s2_ens)
                                    elif choix_radio=="Particulier":
                                        st.table(df_lgd_s2_particulier)
                                    elif choix_radio=="Grande Entreprise":
                                        st.table(df_lgd_s2_grande_entreprise)
                                    elif choix_radio=="PME":
                                        st.table(df_lgd_s2_pme)

                                    elif choix_radio=="Salarié":
                                        st.table(df_lgd_s2_salarie)
                                    else:
                                        st.write("Veuillez choisir une option")

                                #---------------------Stage 3-----------------------------------------------
                                elif choix_radio_stage=="Strate 3":
                                    if choix_radio=="Ensemble":
                                        st.table(df_lgd_s3_ens)
                                    elif choix_radio=="Particulier":
                                        st.table(df_lgd_s3_particulier)
                                    elif choix_radio=="Grande Entreprise":
                                        st.table(df_lgd_s3_grande_entreprise)
                                    elif choix_radio=="PME":
                                        st.table(df_lgd_s3_pme)

                                    elif choix_radio=="Salarié":
                                        st.table(df_lgd_s3_salarie)

                                    else:
                                        st.write("Veuillez choisir une option")


                            elif choice=="EAD":
                                col1,sep,col2,sep,col3=st.columns([2,0.2,8,0.2,2])
                                with col2:
                                    # st.markdown("***")
                                    st.markdown("""
                                        ####  Exposition en cas de defaut: Expositon at default
                                        """)
                                    # choix_radio_ead=st.radio("",["Ensemble","Particulier","Grande Entreprise","PME","Salarié"],
                                    #                          horizontal=True,index=0)

                                st.markdown("***")
                                if choix_radio_stage=="Strate 1":
                                    st.header("Stage 1")
                                    st.table(df_ead_s1)
                                elif choix_radio_stage=="Strate 2":
                                    st.header("Stage 2")
                                    st.table(df_ead_s2)
                                elif choix_radio_stage=="Strate 3":
                                    st.header("Stage 3")
                                    st.table(df_ead_s3)
                                else:
                                    st.write("Veuillez choisir une option")

                            elif choice=="ECL":
                                col1,sep,col2,sep,col3=st.columns([2,0.2,8,0.2,2])
                                with col2:

                                    # st.markdown("***")
                                    st.markdown("""
                                            ####  Perte attendues de crédits : Expected credit loss
                                            """)
                                    choix=st.radio("",["Ensemble","Particulier","Grande Entreprise","PME","Salarié"],
                                                             horizontal=True,index=0)
                                st.markdown("***")

                                if choix_radio_stage=="Strate 1":
                                    # st.write((df_ead_s1.iloc[:,-1]).iloc[0])
                                    # calcul de PD* LGD
                                    index_pd=(df_pd_ens.iloc[:,-1]).iloc[0]/100*((df_ead_s1.iloc[:,-1]).iloc[0])
                                    index_pd_p=(df_pd_partucilier.iloc[:,-1]).iloc[0]/100*((df_ead_s1.iloc[:,-1]).iloc[1])
                                    index_pd_g=(df_pd_Grande_Entreprise.iloc[:,-1]).iloc[0]/100*((df_ead_s1.iloc[:,-1]).iloc[2])
                                    index_pd_pme=(df_pd_pme.iloc[:,-1]).iloc[0]/100*((df_ead_s1.iloc[:,-1]).iloc[3])
                                    index_pd_s=(df_pd_salarie.iloc[:,-1]).iloc[0]/100*((df_ead_s1.iloc[:,-1]).iloc[4])

                                    df_ecl=df_lgd_s1_ens["Taux LGD"].reset_index()
                                    df1=df_lgd_s1_particulier["Taux LGD"].reset_index()
                                    df_ecl["LGD P"]=df1["Taux LGD"]
                                    df1=df_lgd_s1_grande_entreprise["Taux LGD"].reset_index()
                                    df_ecl["LGD G"]=df1["Taux LGD"]
                                    df1=df_lgd_s1_pme["Taux LGD"].reset_index()
                                    df_ecl["LGD PM"]=df1["Taux LGD"]
                                    df1=df_lgd_s1_salarie["Taux LGD"].reset_index()
                                    df_ecl["LGD S"]=df1["Taux LGD"]

                                    df_ecl["PD EAD E"]=index_pd
                                    df_ecl["PD EAD P"]=index_pd_p
                                    df_ecl["PD EAD G"]=index_pd_g
                                    df_ecl["PD EAD PM"]=index_pd_pme
                                    df_ecl["PD EAD S"]=index_pd_s
                                    # le ecl
                                    df_ecl["ECL E"]=df_ecl["Taux LGD"]*df_ecl["PD EAD E"]
                                    df_ecl["ECL P"]=df_ecl["LGD P"]*df_ecl["PD EAD P"]
                                    df_ecl["ECL G"]=df_ecl["LGD G"]*df_ecl["PD EAD G"]
                                    df_ecl["ECL PME"]=df_ecl["LGD PM"]*df_ecl["PD EAD PM"]
                                    df_ecl["ECL S"]=df_ecl["LGD S"]*df_ecl["PD EAD S"]
                                    df_ecl=df_ecl[["ECL E","ECL P","ECL G","ECL PME","ECL S","index"]]
                                    df_ecl=df_ecl.set_index("index")
                                    st.table(df_ecl)

                                elif choix_radio_stage=="Strate 2":
                                    pass


                            else:
                                st.write("Veuillez choisir une option")


                        except Exception as e:
                            st.write("Veuillez saisir les données")

##
                    #  ----------REVERSE STRESS TEST ---------------------------------------------------------------------
                    # #

                    elif test_a_faire=="Reverses Tests":
                        st.cache(allow_output_mutation=True,show_spinner=True,suppress_st_warning=True)
                        # Créer un expander dans la barre latérale
                        options_expander = st.sidebar.expander("Cliquez ici")
                        with options_expander:
                            st.subheader("Paramètre de données")
                        # ajouter untitre et une image le logo de y3
                        st.title("REVERSE STRESS TEST : RISK MANAGEMENT TOOL ")
                        st.markdown("***")
                        # methode 2
                        a1, sep, a2,sep,a3=st.columns([8,0.2,8,0.2,8])
                        with a1:
                            pnp=st.slider("Valeur de perte", min_value=4.00, max_value=30.00)

                        with a2:
                            credittotal=st.number_input("Crédit total", min_value=100000.00, max_value=1000000000000.00)
                            pret_a_risque=pnp * credittotal/100
                            st.write("Crédit à risque", pret_a_risque)
                        with a3:
                            fp=st.number_input("Fonds propres", min_value=1000.00)
                            rs=np.round(fp/pret_a_risque*100,2)
                            st.write("Ratio de solvabilité",rs,"%")
                        st.markdown("***")
                        L=pnp
                        with options_expander:
                        ### se connecter au données"""
                            data_file = st.file_uploader("Télécharger CSV ou xlsx",type=["csv","xlsx"])
                        d1,sep,d2,sep,d3=st.columns([8,0.2,8,0.2,8])
                        c1, sep, c2=st.columns([8,0.5,8,])
                        global df
                        global cov_matrix
                        global scenarios
                        if data_file is not None:
                            with options_expander:
                                st.success("Téléchargement reussi")
                            try:
                                df=pd.read_csv(data_file)
                            except Exception as e:
                                df=pd.read_excel(data_file)


                        try:
                            # st.sidebar.write("Les 5 premières colonnes",df.head(5))
                            with d1:
                                colomns=st.multiselect("Selectionner les variables pour créer les scénarios", df.columns)
                                st.markdown("***")
                            df=df[colomns]


                            st.sidebar.write("Données historiques pour les scénarios",df)
                        except Exception as e:
                            st.write("Veuillez télécharger les données")


                        try:
                            cov_matrix = pd.DataFrame.cov(df)
                        except Exception as e:
                            st.write("!!!")
                        ### Definition des fonctions"""
                        def gram_schmidt_columns(x):
                            q, r = np.linalg.qr(x)   # caclul de la factorisation de matrice # decomposition
                            return q

                        def gram_schmidt_rows(x):
                            """ row-wise Gram Schmidt procedure """
                            q, r = np.linalg.qr(x.T)
                            return q.T

                        def p_from_w(w):
                            """ étant donné le vecteur de poids w, calculé la matrice de transformation p,
                            comme decrite à l'annexe  A du livre
                            """
                            w = np.array(w) # table de w
                            n = len(w) # la longueur de w
                            p = np.zeros((n, n)) # une matrice carrée nulle de n*n dimension
                            p[0, :] = w / np.linalg.norm(w) # norme de matrice ou vectorielle
                            j0 = (np.abs(w) > 0.00001).nonzero()[0][0]
                            for j in range(j0):
                                p[j + 1, j] = 1
                            for j in range(j0 + 1, n):
                                p[j, j] = 1
                            gs = gram_schmidt_rows(p)
                            for j in range(gs.shape[1]):
                                if gs[0, j] < 0:
                                    gs[:, j] = -gs[:, j]
                            return gs

                        def standard_simplex_vertices(M):
                            """ just that """
                            z = np.eye(M) - 1 / M
                            a = np.eye(M)
                            a[0, :] = 1
                            p = gram_schmidt_rows(a)
                            cls = np.append(range(1, M), 0)
                            gs = np.delete(p.dot(z), 0, axis=0)[:, cls]
                            if gs[0, 0] < 0:
                                gs = -gs
                            return gs * np.sqrt(M / (M - 1))


                        def quadratic_form_inv(a, x):
                            """ x * a^(-1) * x """
                            ax = np.linalg.solve(a, x)
                            return x.T.dot(ax)

                        ### procedure principale"""

                        def comp_scenarios(c, w, L, q, M, printIt=False):
                            """ matrice de covariance  c, vectur poids (paramètre) w,
                            perte L, vraissemblance relative q,
                            nombre de scénario non-central M,
                            calcul de stress scenarios, et de vraissemblance relative;

                            """
                            # scenario central
                            cw = c.dot(w)
                            ah = L * cw / w.dot(cw)
                            if printIt:
                                print('------------   ah   ------------')
                                print(ah.round(3))

                            # préparer la matrice de transformation
                            p = p_from_w(w)
                            n = len(w)
                            if printIt:
                                print('------------   p   ------------')
                                print(p.round(3))

                            ahy_full = p.dot(ah)
                            first_comp = ahy_full[0]
                            if printIt:
                                print('------------   ahy_full   ------------')
                                print(ahy_full.round(3))

                            # asset names
                            ass = c.columns

                            # compute covariance matrix in the transformed space
                            dy = p.dot(c.dot(p.T))
                            if printIt:
                                print('------------   dy   ------------')
                                print(dy.round(3))

                            # extract decomposition parts
                            d11 = dy[0, 0]
                            # d1I = dy[0, 1:]
                            dI1 = dy[1:, 0]
                            dII = dy[1:, 1:]

                            # compute center and conditional distribution in transformed space
                            wn = np.linalg.norm(w)
                            ahy = L * dI1 / d11 / wn
                            i_m = np.matrix(dI1).reshape(n - 1, 1) * np.matrix(dI1).reshape(1, n - 1)
                            dyh = dII - i_m / d11
                            if printIt:
                                print('------------   ahy   ------------')
                                print(ahy.round(3))
                                print('------------   dyh   ------------')
                                print(dyh.round(3))

                            # egenvalues in ascending order and eigenvectors
                            vals, vect = np.linalg.eig(dyh)
                            ind = vals.argsort()[::-1]
                            V = vect[:, ind]

                            # place the eigenvectors in opposite order
                            # V = vect[:, ::-1]
                            if printIt:
                                print('------------   V   ------------')
                                print(V.round(3))
                                print('------------   Vals   ------------')
                                print(vals.round(3))

                            # compute vertices of the regular M-simplex
                            t = standard_simplex_vertices(M)
                            if printIt:
                                print('------------   t   ------------')
                                print(t.round(3))

                            # rotation to principle components space
                            z = V[:, :(M - 1)].dot(t)
                            if printIt:
                                print('------------   z   ------------')
                                print(z.round(3))

                            # compute the sphere radius
                            z_last = z[:, -1]
                            denom = quadratic_form_inv(dyh, np.array(z_last))
                            r = np.sqrt(-2 * np.log(q) / denom)[0, 0]
                            ahyr = ahy.repeat(M).reshape(n - 1, M)
                            rz = r * z + ahyr
                            if printIt:
                                print('------------   r   ------------')
                                print(r.round(3))

                            # unite central scenario with sphere scenarios
                            df = pd.DataFrame(ahy, columns=['aa']).join(pd.DataFrame(rz))
                            cls = ['Scenario_{0}'.format(i) for i in range(M + 1)]
                            df.columns = cls

                            # append first_comp row at the beginning
                            df0 = first_comp * pd.DataFrame(np.ones((1, M + 1)), columns=cls)
                            df = df0.append(df.set_index(np.array(range(1, n))))
                            if printIt:
                                print('------------   df0   ------------')
                                print(df0.round(3))
                                print('------------   df   ------------')
                                print(df.round(3))

                            # rotating back to initial space
                            ar = p.T.dot(df)

                            # turning to dataframe
                            scenarios = pd.DataFrame(ar, columns=cls).set_index(ass)
                            if printIt:
                                print('------------   scenarios  ------------')
                                print(scenarios.round(3))

                            lik = np.array([multivariate_normal.pdf(scenarios[cls[j]],
                                                                    mean=np.zeros((n,)),
                                                                    cov=c)
                                            for j in range(M + 1)])
                            lik = pd.DataFrame((lik / lik[0]).reshape(1, M + 1), columns=cls)
                            lik.index = ['Likelihood']
                            if printIt:
                                print('------------   lik  ------------')
                                print(lik.round(3))

                            return scenarios, lik

                        try:
                            c =cov_matrix
                            w = np.ones((len(cov_matrix),))
                            M =df.columns.nunique()
                            q = 0.01
                            scenarios, lik = comp_scenarios(c, w, L, q, M)
                            d=df
                            d.tail()
                            #print(lik.round(3))
                            with c2:
                                st.markdown("***")
                                st.header("La probabilité de vraissemble")
                                st.table(lik.round(3)) # la vraissemblance relative
                                st.markdown("***")
                            with c1:
                                st.markdown("***")
                                st.header("Scénarios Générés")
                                st.table(scenarios) # scénarios

                                def convert_df(df):
                                    return df.to_csv().encode('utf-8')
                                telech=convert_df(scenarios)
                                st.download_button(label="Télécharger ici", data=telech,file_name='scenario.csv',mime='text/csv')
                                #telecharger=st.download_button("Télécharger le résultat",data=telech,file_name="Résultats des scenario.xlsx")
                                st.markdown("***")

                            distance=np.array([np.linalg.norm(scenarios.iloc[:, i] - scenarios.iloc[:, j]) for i in range(M) for j in range(i+1, M+1)]).round(3) # la distance

                        except Exception as e:
                            print("Veuillez télécharger les données")

                        # no necessary, mais permet d'avoir plus de controle sur l'app
                    else:
                        try:
                            st.write("Veuillez selectionner une option")
                        except Exception as e:
                            st.write("Veuillez selectionner une option")

                else:
                    with st.spinner("Conexion en cours..."):
                        time.sleep(1)
                        st.warning("l'identifiant ou le mot de passe est incorrect")


    elif choice=="S'inscrire":
        st.subheader("Création d'un nouveau compte")
        new_user = st.text_input("Nom d'utilisateur")
        new_password = st.text_input("Mot de passe",type='password')
        if st.button("S'inscrire"):
            if new_password and new_user is not None:
                create_usertable()
                add_userdata(new_user,make_hashes(new_password))
                with st.spinner("Traitement en cours..."):
                    time.sleep(2)
                    r1=st.success("Votre compte a été crée avec succès !")
                    r2=st.info("Vous pouvez vous connecter maintenant")
                    for i in range(2):
                        time.sleep(1)
                    r1.empty()
                    r2.empty()


            else:

                # Afficher une alerte de succès pendant 3 secondes
                with st.spinner("Traitement en cours..."):
                    time.sleep(2)
                    result = st.warning("Veuillez remplir toutes les options")

                    # Attendre 3 secondes avant de masquer l'alerte
                    for i in range(2):
                        time.sleep(1)

                    # Effacer l'alerte de succès
                    result.empty()


if __name__ == '__main__':
    main()