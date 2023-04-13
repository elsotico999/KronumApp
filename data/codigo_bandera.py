from tkinter import *
from PIL import Image, ImageTk

size = (30, 30)

# lista de banderas de los países
banderas = {
    "Afghanistan": "af.png",
  "Albania": "al.png",
  "Algeria": "dz.png",
  "Andorra": "ad.png",
  "Angola": "ao.png",
  "Antigua and Barbuda": "ag.png",
  "Argentina": "ar.png",
  "Armenia": "am.png",
  "Australia": "au.png",
  "Austria": "at.png",
  "Azerbaijan": "az.png",
  "Bahamas": "bs.png",
  "Bahrain": "bh.png",
  "Bangladesh": "bd.png",
  "Barbados": "bb.png",
  "Belarus": "by.png",
  "Belgium": "be.png",
  "Belize": "bz.png",
  "Benin": "bj.png",
  "Bhutan": "bt.png",
  "Bolivia": "bo.png",
  "Bosnia and Herzegovina": "ba.png",
  "Botswana": "bw.png",
  "Brazil": "br.png",
  "Brunei": "bn.png",
  "Bulgaria": "bg.png",
  "Burkina Faso": "bf.png",
  "Burundi": "bi.png",
  "Cabo Verde": "cv.png",
  "Cambodia": "kh.png",
  "Cameroon": "cm.png",
  "Canada": "ca.png",
  "Central African Republic": "cf.png",
  "Chad": "td.png",
  "Chile": "cl.png",
  "China": "cn.png",
  "Colombia": "co.png",
  "Comoros": "km.png",
  "Congo, Democratic Republic of the": "cd.png",
  "Congo, Republic of the": "cg.png",
  "Costa Rica": "cr.png",
  "Côte d'Ivoire": "ci.png",
  "Croatia": "hr.png",
  "Cuba": "cu.png",
  "Cyprus": "cy.png",
  "Czech Republic": "cz.png",
  "Denmark": "dk.png",
  "Djibouti": "dj.png",
  "Dominica": "dm.png",
  "Dominican Republic": "do.png",
  "Ecuador": "ec.png",
  "Egypt": "eg.png",
  "El Salvador": "sv.png",
  "Equatorial Guinea": "gq.png",
  "Eritrea": "er.png",
  "Estonia": "ee.png",
  "Eswatini": "sz.png",
  "Ethiopia": "et.png",
  "Fiji": "fj.png",
  "Finland": "fi.png",
  "France": "fr.png",
  "Gabon": "ga.png",
  "Gambia": "gm.png",
  "Georgia": "ge.png",
  "Germany": "de.png",
  "Ghana": "gh.png",
  "Greece": "gr.png",
  "Grenada": "gd.png",
  "Guatemala": "gt.png",
  "Guinea": "gn.png",
  "Guinea-Bissau": "gw.png",
  "Guyana": "gy.png",
  "Haiti": "ht.png",
  "Honduras": "hn.png",
  "Hungary": "hu.png",
  "Iceland": "is.png",
  "India": "in.png",
  "Indonesia": "id.png",
  "Iran": "ir.png",
  "Iraq": "iq.png",
  "Ireland": "ie.png",
  "Israel": "il.png",
  "Italy": "it.png",
  "Jamaica": "jm.png",
  "Japan": "jp.png",
  "Jordan": "jo.png",
  "Kazakhstan": "kz.png",
  "Kenya": "ke.png",
  "Kiribati": "ki.png",
  "Kosovo": "xk.png",
  "Kuwait": "kw.png",
  "Kyrgyzstan": "kg.png",
  "Laos": "la.png",
  "Latvia": "lv.png",
  "Lebanon": "lb.png",
  "Lesotho": "ls.png",
  "Liberia": "lr.png",
  "Libya": "ly.png",
  "Liechtenstein": "li.png",
  "Lithuania": "lt.png",
  "Luxembourg": "lu.png",
  "Madagascar": "mg.png",
  "Malawi": "mw.png",
  "Malaysia": "my.png",
  "Maldives": "mv.png",
  "Mali": "ml.png",
  "Malta": "mt.png",
  "Marshall Islands": "mh.png",
  "Mauritania": "mr.png",
  "Mauritius": "mu.png",
  "Mexico": "mx.png",
  "Micronesia": "fm.png",
  "Moldova": "md.png",
  "Monaco": "mc.png",
  "Mongolia": "mn.png",
  "Montenegro": "me.png",
  "Morocco": "ma.png",
  "Mozambique": "mz.png",
  "Myanmar": "mm.png",
  "Namibia": "na.png",
  "Nauru": "nr.png",
  "Nepal": "np.png",
  "Netherlands": "nl.png",
  "New Zealand": "nz.png",
  "Nicaragua": "ni.png",
  "Niger": "ne.png",
  "Nigeria": "ng.png",
  "North Korea": "kp.png",
  "North Macedonia": "mk.png",
  "Norway": "no.png",
  "Oman": "om.png",
  "Pakistan": "pk.png",
  "Palau": "pw.png",
  "Palestine": "ps.png",
  "Panama": "pa.png",
  "Papua New Guinea": "pg.png",
  "Paraguay": "py.png",
  "Peru": "pe.png",
  "Philippines": "ph.png",
  "Poland": "pl.png",
  "Portugal": "pt.png",
  "Qatar": "qa.png",
  "Romania": "ro.png",
  "Russia": "ru.png",
  "Rwanda": "rw.png",
  "Saint Kitts and Nevis": "kn.png",
  "Saint Lucia": "lc.png",
  "Saint Vincent and the Grenadines": "vc.png",
  "Samoa": "ws.png",
  "San Marino": "sm.png",
  "Sao Tome and Principe": "st.png",
  "Saudi Arabia": "sa.png",
  "Senegal": "sn.png",
  "Serbia": "rs.png",
  "Seychelles": "sc.png",
  "Sierra Leone": "sl.png",
  "Singapore": "sg.png",
  "Slovakia": "sk.png",
  "Slovenia": "si.png",
  "Solomon Islands": "sb.png",
  "Somalia": "so.png",
  "South Africa": "za.png",
  "South Korea": "kr.png",
  "South Sudan": "ss.png",
  "Spain": "es.png",
  "Sri Lanka": "lk.png",
  "Sudan": "sd.png",
  "Suriname": "sr.png",
  "Sweden": "se.png",
  "Switzerland": "ch.png",
  "Syria": "sy.png",
  "Taiwan": "tw.png",
  "Tajikistan": "tj.png",
  "Tanzania": "tz.png",
  "Thailand": "th.png",
  "Timor-Leste": "tl.png",
  "Togo": "tg.png",
  "Tonga": "to.png",
  "Trinidad and Tobago": "tt.png",
  "Tunisia": "tn.png",
  "Turkey": "tr.png",
  "Turkmenistan": "tm.png",
  "Tuvalu": "tv.png",
  "Uganda": "ug.png",
  "Ukraine": "ua.png",
  "United Arab Emirates": "ae.png",
  "United Kingdom": "gb.png",
  "United States of America": "us.png",
  "Uruguay": "uy.png",
  "Uzbekistan": "uz.png",
  "Vanuatu": "vu.png",
  "Vatican City": "va.png",
  "Venezuela": "ve.png",
  "Vietnam": "vn.png",
  "Yemen": "ye.png",
  "Zambia": "zm.png",
  "Zimbabwe": "zw.png"
}

# Iterar sobre todas las banderas en la lista
for country, flag_path in banderas.items():
    # Abrir la imagen
    img = Image.open("banderas/" + flag_path)
    #img = Image.open("banderas/" + flag_path).resize(size, resample=0)
    # Redimensionar la imagen
    img_resized = img.resize(size)
    # Guardar la imagen redimensionada
    img_resized.save(f'resized_{flag_path}')

def mostrar_banderas():
    # obtener los nombres de los dos países seleccionados por el usuario
    pais1 = var_pais1.get()
    pais2 = var_pais2.get()

    # cargar las imágenes de las banderas correspondientes
    img1 = Image.open("resized_" + banderas[pais1])
    img2 = Image.open("resized_" + banderas[pais2])

    # crear objetos ImageTk a partir de las imágenes cargadas
    img_tk1 = ImageTk.PhotoImage(img1)
    img_tk2 = ImageTk.PhotoImage(img2)

    # mostrar las imágenes en widgets de imagen de Tkinter
    label_banderas1.config(image=img_tk1)
    label_banderas2.config(image=img_tk2)

    # actualizar la interfaz
    label_banderas1.image = img_tk1
    label_banderas2.image = img_tk2
    label_banderas1.pack()
    label_banderas2.pack()


# crear la interfaz de usuario
root = Tk()

# crear variables de control para los nombres de los países seleccionados por el usuario
var_pais1 = StringVar(root)
var_pais2 = StringVar(root)

# crear una lista desplegable para seleccionar el primer país
label_pais1 = Label(root, text="País 1:")
label_pais1.pack()
dropdown_pais1 = OptionMenu(root, var_pais1, *banderas.keys())
dropdown_pais1.pack()

# crear una lista desplegable para seleccionar el segundo país
label_pais2 = Label(root, text="País 2:")
label_pais2.pack()
dropdown_pais2 = OptionMenu(root, var_pais2, *banderas.keys())
dropdown_pais2.pack()

# crear widgets de imagen de Tkinter para mostrar las banderas
label_banderas1 = Label(root)
label_banderas2 = Label(root)

label_banderas1.configure(width=50, height=50)
label_banderas2.configure(width=100, height=100)

# crear un botón para mostrar las banderas seleccionadas
boton_mostrar = Button(root, text="Mostrar banderas", command=mostrar_banderas)
boton_mostrar.pack()

# iniciar la aplicación
root.mainloop()

