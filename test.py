import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

data = {0: [-1, 1, -1, -1, -1, -1]
        , 1: [-1, -1, 1, -1, -1, -1]
        , 2: [-1, -1, -1, 1, -1, -1]
        , 3: [1, 1, -1, 1, -1, -1]
        , 4: [1, -1, 1, 1, -1, -1]
        , 5: [-1, 1, 1, 1, -1, -1]
        , 6: [1, -1, -1, 1, 1, -1]
        , 7: [-1, 1, -1, 1, 1, -1]
        , 8: [-1, -1, 1, 1, 1, -1]
        , 9: [1, 1, 1, 1, 1, -1]
        }
fac = { 0: "Huile de brunissage"
        ,1 : "Loctite"
        ,2 : "Couple de serrage"
        ,3 : "Pièce Lien_boitier_tube"
        ,4 : "Joint torique"}
# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    label = "De quel facteur souhaitez-vous voir l'influence ?",
    options = (0, 1, 2, 3, 4),
    format_func = lambda x: fac.get(x)
)
n = add_selectbox
print(add_selectbox)
print(n)
n_bins = 1
colors = ['red', 'lime']
legend = ["Absence facteur", "Présence facteur"]
rup = 0 #rupture + absence facteur
nrup = 0 #rupture + presence facteur
abs = 0 #absence facteur
pres = 0 #presence facteur



print(add_selectbox)
fig, ax = plt.subplots()

for i in range(len(data)):
    if data[i][5] == -1 and data[i][n] == -1: #Si rupture ET absence facteur
        rup += 1
    if data[i][5] == -1 and data [i][n] == 1: #Si rupture ET presence facteur
        nrup += 1

for i in range(len(data)): #compteur présence // absence facteur
    if data [i][n] == -1:
        abs += 1
    if data [i][n] == 1:
        pres += 1
#Calcul rapport rupture et absence / absence en pourcent
rupabs = rup/abs
rupabs *= 100
#Calcul rapport rupture et présence / présence en pourcent
ruppres = nrup/pres
ruppres *= 100
x = ["En absence du facteur {}" .format(fac[n]), "En présence du facteur {}".format(fac[n])]
y = [rupabs, ruppres]
ax.bar(x, y, width = 0.5, color = colors)
plt.title("Pourcentage de coques cassées avec/sans le facteur {}".format(fac[n]), pad = 15)
ax.set_xticklabels(x, rotation=0, fontsize=8)
ax.bar_label(ax.containers[0], fmt = '%.2f%%' )

st.sidebar.write(add_selectbox)

ax.set_ylabel("% de coques cassées")



st.pyplot(fig)
#ax.hist(len(min), "r")
#ax.hist(len(max), "b")

#st.pyplot(fig)
