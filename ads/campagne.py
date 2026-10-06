# -*- coding: utf-8 -*-
# Contenu de la campagne Google Ads Search Arboritaille (oct. 2026). Vérifie les limites de caractères.
import json
SITE="https://page.arboritaille.ch/"
C=dict(
 nom="Search · Arboritaille · Arc jurassien (FR)",
 budget_mensuel_chf=500, budget_jour_chf=round(500/30.4,2),
 encheres="Maximiser les conversions (sans CPA cible)",
 conversions=["Demande de devis","Appel téléphonique"],
 reseaux="Réseau de Recherche uniquement (partenaires et Display décochés)",
 langue="Français", ciblage="Présence : personnes situées dans la zone",
 diffusion="Tous les jours, 24h/24",
)
NEG_CAMPAGNE=["haie","haies","thuya","thuyas","laurier","taille de haie","bois de chauffage","bois de feu à vendre","pellets",
 "formation","cours","apprentissage","apprenti","cfc","emploi","job","jobs","offre d'emploi","salaire","stage","poste",
 "tronçonneuse","sécateur","échenilloir","perche élagage","location","louer","occasion","gratuit","diy","tuto","tutoriel","vidéo","youtube",
 "comment tailler","quand tailler","pdf","wikipedia","définition","france","belfort","montbéliard","mulhouse"]
G={
 "Élagage et taille":dict(url=SITE+"taille.html", chemins=("elagage","devis"),
  kw=["élagage arbre","élagage d'arbres","élagueur","élagage","taille d'arbre","taille arbre","taille des arbres","tailler un arbre",
      "entretien des arbres","entretien arbre","élaguer un arbre","réduction de couronne","élagage arbre prix","entreprise d'élagage","élagage de sécurité"],
  titres=["Élagage d'arbres Jura","Arboriste-grimpeur","Taille d'arbres raisonnée","Devis gratuit, sans engagement","Élagage Neuchâtel et Bienne",
          "Élagueur dans le Jura bernois","Réduction de couronne","Suppression du bois mort","Élagage de sécurité","Grimpe, nacelle ou grue",
          "Chantier propre, bois évacué","Réponse sous 48 h ouvrées","Arboritaille, Courgenay","Visite et devis offerts","Taille et entretien d'arbres"],
  desc=["Taille raisonnée, bois mort, réduction de couronne : arboriste-grimpeur. Devis gratuit.",
        "Nous intervenons dans le Jura, à Neuchâtel, Bienne et environs. Visite sur place offerte.",
        "Grimpe à la corde par défaut, nacelle ou grue si nécessaire. Chantier rendu propre.",
        "Arbre trop grand ou branches à risque ? Décrivez-nous votre arbre et recevez un devis."]),
 "Abattage et démontage":dict(url=SITE+"abattage.html", chemins=("abattage","devis"),
  kw=["abattage arbre","abattage d'arbre","abattre un arbre","faire abattre un arbre","abattage arbre prix","démontage arbre","démontage d'arbre",
      "faire couper un arbre","entreprise abattage arbre","arbre dangereux","arbre mort","rognage de souche","dessouchage","enlever une souche","abattage sapin"],
  titres=["Abattage d'arbres Jura","Démontage d'arbre à la corde","Abattage arbre dangereux","Devis gratuit, sans engagement","Abattage Neuchâtel et Bienne",
          "Rognage de souche","Démontage par rétention","Grimpe, nacelle ou grue","Intervention après tempête","Bois évacué, terrain propre",
          "Arbre près de la maison ?","Arboriste-grimpeur","Réponse sous 48 h ouvrées","Arboritaille, Courgenay","Abattage et démontage"],
  desc=["Abattage ou démontage pièce par pièce, même près des bâtiments. Devis gratuit sur place.",
        "Arbre mort, malade ou dangereux ? Nous évaluons la situation et proposons une méthode.",
        "Grimpe, nacelle, grue ou hélicoptère selon le cas. Bois de feu, broyé ou évacué.",
        "Jura, Neuchâtel, Bienne et environs. Rognage de souche possible. Réponse sous 48 h."]),
 "Généraliste arboriste":dict(url=SITE, chemins=("arboriste","jura"),
  kw=["arboriste","arboriste grimpeur","arboriste élagueur","soins aux arbres","entreprise arboriste","spécialiste des arbres","diagnostic arbre",
      "expertise arbre","arbre malade","plantation arbre","haubanage arbre","arboritaille"],
  titres=["Arboriste-grimpeur Jura","Soins aux arbres","Taille, abattage, plantation","Arboritaille, Courgenay","Devis gratuit, sans engagement",
          "Diagnostic d'arbre","Haubanage et consolidation","Plantation d'arbres","Arboriste Neuchâtel, Bienne","Particuliers et communes",
          "Grimpe, nacelle ou grue","Réponse sous 48 h ouvrées","Conseil sur mesure","Rognage de souche","Un seul interlocuteur"],
  desc=["Taille, abattage, diagnostic et plantation par un arboriste-grimpeur. Devis gratuit.",
        "Particuliers, entreprises et communes du Jura, de Neuchâtel et de la région de Bienne.",
        "L'objectif est de conserver vos arbres. Nous vous conseillons au cas par cas.",
        "Visite sur place et devis écrit gratuits, sans engagement. Réponse sous 48 h ouvrées."]),
}
LIENS=[("Taille et entretien",SITE+"taille.html","Taille raisonnée, bois mort","Réduction de couronne"),
       ("Abattage et démontage",SITE+"abattage.html","Même près des bâtiments","Rognage de souche"),
       ("Demander un devis",SITE+"#devis","Gratuit, sans engagement","Réponse sous 48 h ouvrées"),
       ("Questions fréquentes",SITE+"#faq","Prix, autorisations, accès","Ce que nos clients demandent")]
ACCROCHES=["Devis gratuit","Arboriste-grimpeur","Chantier rendu propre","Réponse sous 48 h","Visite sur place offerte","Particuliers et communes"]
EXTRAITS=("Services",["Élagage","Taille d'arbres","Abattage","Démontage","Rognage de souche","Plantation","Haubanage","Diagnostic"])
APPEL="+41 78 306 53 04"

err=[]
for g,d in G.items():
    assert len(d["titres"])==15 and len(d["desc"])==4, g
    for t in d["titres"]:
        if len(t)>30: err.append((g,"titre",len(t),t))
    for t in d["desc"]:
        if len(t)>90: err.append((g,"desc",len(t),t))
    for p in d["chemins"]:
        if len(p)>15: err.append((g,"chemin",p))
    if len(set(d["titres"]))!=15: err.append((g,"doublon titre"))
for n,u,a,b in LIENS:
    for t,l in ((n,25),(a,35),(b,35)):
        if len(t)>l: err.append(("lien",len(t),t))
for a in ACCROCHES+EXTRAITS[1]:
    if len(a)>25: err.append(("accroche/extrait",len(a),a))
interdits=["honnête","fiable","meilleur","n°1","numéro 1","garanti","certifié","total","zéro","idéal","optimal","jamais"]
for g,d in G.items():
    for t in d["titres"]+d["desc"]:
        for w in interdits:
            if w in t.lower(): err.append((g,"mot interdit",w,t))
print("ERREURS:",err if err else "aucune")
print("Budget jour :",C["budget_jour_chf"],"CHF")
for g,d in G.items(): print(g,":",len(d["kw"]),"mots-clés, max titre",max(map(len,d["titres"])),", max desc",max(map(len,d["desc"])))
# Ajout du 6 oct. 2026 (volume de recherche trop faible en exact/expression) : mots clés en requête large
LARGE={
 "Abattage et démontage":["abattage arbre","couper un arbre","abattre un arbre","démontage arbre","abattage sapin","arbre dangereux","arbre mort","dessouchage","enlever souche arbre","bûcheron","abattage arbre prix"],
 "Élagage et taille":["élagage arbre","élagueur","taille arbre","tailler un arbre","entretien arbre","élaguer un arbre","couper branches arbre","réduction couronne arbre","taille arbre fruitier","élagage prix"],
 "Généraliste arboriste":["arboriste","arboriste grimpeur","élagueur grimpeur","entreprise arboriste","soins aux arbres","arbre malade","diagnostic arbre","planter un arbre","haubanage arbre","entreprise élagage abattage"],
}
json.dump(dict(requete_large=LARGE,campagne=C,negatifs=NEG_CAMPAGNE,groupes=G,liens=LIENS,accroches=ACCROCHES,extraits=EXTRAITS,appel=APPEL),open("campagne.json","w",encoding="utf-8"),ensure_ascii=False,indent=2)
