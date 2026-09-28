# Assemble abattage.html and index.html from shared blocks of taille.html
import re
t=open('taille.html',encoding='utf-8').read()

def block(name):
    m=re.search(r'<!-- '+re.escape(name)+r' -->\n(.*?)(?=\n<!-- |\n</main>)',t,re.S)
    return m.group(1)

head_tpl=t.split('<body>')[0]
header=block('Header')
zone=block('Zone')
footer=t.split('</main>')[1]

PHONE_SVG='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.8 19.8 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
ARROW='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CHECK='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>'
CK3='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>'
PIN='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>'
LOCK='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>'
MAIL='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 7L2 7"/></svg>'
SHIELD='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>'
LEAF='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/></svg>'
DOC='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M16 13H8M16 17H8M10 9H8"/></svg>'
WARN='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/><path d="M12 9v4M12 17h.01"/></svg>'
TREE='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22v-6"/><path d="M8 16h8l-2-4h1l-3-5h.5L12 3l-.5 4H12l-3 5h1l-2 4z"/></svg>'
SCISS='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M20 4 8.12 15.88M14.47 14.48 20 20M8.12 8.12 12 12"/></svg>'
AXE='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m14 12-8.5 8.5a2.12 2.12 0 1 1-3-3L11 9"/><path d="M15 13 9 7l4-4 6 6h3a8 8 0 0 1-7 7z"/></svg>'
SEARCH='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>'
SPROUT='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 20h10M10 20c5.5-2.5.8-6.4 3-10"/><path d="M9.5 9.4c1.1.8 1.8 2.2 2.3 3.7-2 .4-3.5.4-4.8-.3-1.2-.6-2.3-1.9-3-4.2 2.8-.5 4.4 0 5.5.8z"/><path d="M14.1 6a7 7 0 0 0-1.1 4c1.9-.1 3.3-.6 4.3-1.4 1-1 1.6-2.3 1.7-4.6-2.7.1-4 1-4.9 2z"/></svg>'
LINK='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>'
STUMP='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="7" rx="8" ry="3"/><path d="M4 7v10c0 1.7 3.6 3 8 3s8-1.3 8-3V7"/><ellipse cx="12" cy="7" rx="3" ry="1.2"/></svg>'
CRANE='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21h18M6 21V8l12-5v18M6 8h12M14 8v6M14 14h3"/></svg>'
USERS='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/></svg>'
BUILD='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4M8 6h.01M16 6h.01M12 6h.01M12 10h.01M12 14h.01M16 10h.01M16 14h.01M8 10h.01M8 14h.01"/></svg>'
HOME='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V12h6v10"/></svg>'

def head(title,desc):
    h=head_tpl
    h=re.sub(r'<title>.*?</title>','<title>'+title+'</title>',h)
    h=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="'+desc+'">',h)
    return h+'<body>\n'

def form(title,sub,subject,source,options,lp):
    opts=''.join('<option>'+o+'</option>' for o in options)
    return f'''<div class="form-card" id="devis">
      <h2>{title}</h2>
      <p class="sub">{sub}</p>
      <form action="https://formsubmit.co/contact@arboritaille.ch" method="POST">
        <input type="hidden" name="_subject" value="{subject}">
        <input type="hidden" name="_template" value="table">
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="_next" value="https://page.arboritaille.ch/merci.html?lp={lp}">
        <input type="hidden" name="Source" value="{source}">
        <input type="text" name="_honey" class="honeypot" tabindex="-1" autocomplete="off">
        <div class="field-row">
          <div class="field"><label for="nom">Nom et prénom</label><input id="nom" name="Nom" type="text" required autocomplete="name" placeholder="Jean Dupont"></div>
          <div class="field"><label for="tel">Téléphone</label><input id="tel" name="Téléphone" type="tel" required autocomplete="tel" placeholder="078 000 00 00"></div>
        </div>
        <div class="field-row">
          <div class="field"><label for="email">E-mail</label><input id="email" name="Email" type="email" required autocomplete="email" placeholder="vous@exemple.ch"></div>
          <div class="field"><label for="localite">Localité</label><input id="localite" name="Localité" type="text" required autocomplete="address-level2" placeholder="Porrentruy, Delémont…"></div>
        </div>
        <div class="field"><label for="besoin">Votre besoin</label>
          <select id="besoin" name="Besoin" required><option value="" disabled selected>Choisir…</option>{opts}</select>
        </div>
        <div class="field"><label for="msg">Décrivez votre situation (facultatif)</label><textarea id="msg" name="Message" placeholder="Essence, hauteur approximative, accès, ce qui vous inquiète…"></textarea></div>
        <button class="btn btn-primary btn-block" type="submit">Envoyer ma demande</button>
        <p class="form-note">{LOCK} Vos données restent confidentielles et servent uniquement à traiter votre demande. Aucune revente, aucun démarchage.</p>
      </form>
    </div>'''

def hero(img,pos,eyebrow,h1,lead,points,formhtml):
    pts=''.join(f'<li>{CHECK}{p}</li>' for p in points)
    return f'''<!-- Hero -->
<section class="hero">
  <img class="hero-bg" src="img/{img}" alt="" fetchpriority="high" style="object-position:{pos}">
  <div class="wrap">
    <div>
      <span class="eyebrow" style="color:var(--yellow)">{eyebrow}</span>
      <h1>{h1}</h1>
      <p class="lead">{lead}</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="#devis">Demander un devis gratuit {ARROW}</a>
        <a class="btn btn-ghost" href="tel:+41783065304">{PHONE_SVG} 078 306 53 04</a>
      </div>
      <ul class="hero-points">{pts}</ul>
    </div>
    {formhtml}
  </div>
</section>
'''

def trust(items):
    inner=''.join(f'<div class="trust-item"><div class="ic">{ic}</div><div>{a}<small>{b}</small></div></div>' for ic,a,b in items)
    return f'<!-- Trust bar -->\n<section class="trust"><div class="wrap">{inner}</div></section>\n'

def cards(eyebrow,h2,lead,items,sid='prestations'):
    inner=''
    for ic,tag,h,p in items:
        tg=f'<span class="card-tag">{tag}</span>' if tag else ''
        inner+=f'<div class="card"><div class="ic">{ic}</div>{tg}<h3>{h}</h3><p>{p}</p></div>'
    return f'''<!-- Services -->
<section class="section" id="{sid}"><div class="wrap">
  <div class="center"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2><p class="lead">{lead}</p></div>
  <div class="services-grid">{inner}</div>
</div></section>
'''

def why(eyebrow,h2,lead,items):
    inner=''.join(f'<div class="why-item"><div class="num">0{i+1}</div><h3>{h}</h3><p>{p}</p></div>' for i,(h,p) in enumerate(items))
    return f'''<!-- Why -->
<section class="section why"><div class="wrap">
  <div class="center"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2><p class="lead">{lead}</p></div>
  <div class="why-grid">{inner}</div>
</div></section>
'''

def approach(img,alt,badge,eyebrow,h2,lead,items,cta):
    lis=''.join(f'<li><span class="ck">{CK3}</span><div><strong>{a}</strong><span>{b}</span></div></li>' for a,b in items)
    return f'''<!-- Approach -->
<section class="section"><div class="wrap split">
  <div class="split-img"><img src="img/{img}" alt="{alt}" loading="lazy"><div class="badge">{SHIELD.replace('<path d="m9 12 2 2 4-4"/>','')} {badge}</div></div>
  <div><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2><p class="lead">{lead}</p>
    <ul class="check-list">{lis}</ul>
    <a class="btn btn-primary" href="#devis">{cta}</a>
  </div>
</div></section>
'''

def process(h2,steps,eyebrow="Comment ça se passe"):
    inner=''.join(f'<div class="step"><h3>{a}</h3><p>{b}</p></div>' for a,b in steps)
    return f'''<!-- Process -->
<section class="section" style="padding-top:0"><div class="wrap">
  <div class="center"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2></div>
  <div class="steps">{inner}</div>
</div></section>
'''

def gallery(h2,items):
    inner=''.join(f'<figure><img src="img/{img}" alt="{alt}" loading="lazy"><figcaption>{cap}</figcaption></figure>' for img,alt,cap in items)
    return f'''<!-- Gallery -->
<section class="section" style="padding-top:0"><div class="wrap">
  <div class="center"><span class="eyebrow">Sur le terrain</span><h2>{h2}</h2></div>
  <div class="gallery">{inner}</div>
</div></section>
'''

def faq(items):
    inner=''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in items)
    return f'''<!-- FAQ -->
<section class="section" id="faq"><div class="wrap">
  <div class="center"><span class="eyebrow">Questions fréquentes</span><h2>Ce que nos clients nous demandent</h2></div>
  <div class="faq">{inner}</div>
</div></section>
'''

def cta(img,h2,lead):
    return f'''<!-- CTA final -->
<section class="section cta">
  <img class="cta-bg" src="img/{img}" alt="" loading="lazy">
  <div class="wrap">
    <div>
      <span class="eyebrow" style="color:var(--yellow)">Parlons de votre arbre</span>
      <h2>{h2}</h2>
      <p class="lead">{lead}</p>
      <div class="cta-contact">
        <a href="tel:+41783065304"><span class="ic">{PHONE_SVG}</span><span>078 306 53 04<small>Robin Humbert, arboriste-grimpeur</small></span></a>
        <a href="mailto:contact@arboritaille.ch"><span class="ic">{MAIL}</span><span>contact@arboritaille.ch<small>Réponse sous 48 h ouvrées</small></span></a>
      </div>
    </div>
    <div><a class="btn btn-primary" href="#devis" style="font-size:1.1rem;padding:1.1rem 2rem">Demander mon devis gratuit {ARROW}</a></div>
  </div>
</section>
'''

def page(fname,title,desc,body):
    open(fname,'w',encoding='utf-8').write(head(title,desc)+header+'\n<main id="top">\n\n'+body+'\n</main>'+footer)

# ---------------- ABATTAGE ----------------
ab_form=form("Devis abattage gratuit","Décrivez l'arbre et son emplacement. Nous venons l'évaluer sur place, sans engagement.",
  "Nouvelle demande de devis – Abattage / démontage d'arbre","Landing page Google Ads – Abattage",
  ["Abattage d'un arbre","Démontage d'un arbre en zone contrainte","Arbre dangereux / urgence après tempête","Arbre mort ou malade","Rognage de souche","Plusieurs arbres à abattre","Autre"],"abattage")
ab=hero("demontage_arbre_porrentruy.jpg","55% 35%","Abattage et démontage · Jura · Neuchâtel · Berne",
  "Abattage d'arbres <em>en toute sécurité</em>, même en espace restreint",
  "Arbre dangereux, mort, malade ou trop proche de la maison ? Un arboriste-grimpeur professionnel l'abat ou le démonte pièce par pièce, en préservant votre propriété, et laisse le terrain propre.",
  ["Devis gratuit et sans engagement","Intervention rapide en cas d'urgence","Grimpe, nacelle, grue ou hélicoptère selon le cas","Bois évacué, terrain nettoyé"],ab_form)
ab+=trust([(SHIELD,"Arboriste-grimpeur","Démontage à la corde, techniques de rétention"),(WARN,"Urgences tempête","Mise en sécurité rapide"),(DOC,"Devis écrit et détaillé","Gratuit, sans engagement")])
ab+=cards("Nos prestations d'abattage","La bonne technique pour chaque situation",
  "Un arbre isolé dans un pré ne s'abat pas comme un sapin collé à une façade. Nous choisissons la méthode adaptée à votre terrain, vos bâtiments et vos voisins.",
  [(AXE,"","Abattage classique","Quand l'espace le permet, l'arbre est abattu en une pièce, avec une direction de chute maîtrisée. La solution la plus rapide et la plus économique."),
   (SCISS,"Le plus courant","Démontage par morceaux","Le grimpeur monte dans l'arbre et le démonte branche par branche, puis tronçon par tronçon. Adapté en jardin, près d'une maison ou d'une ligne électrique."),
   (LINK,"Zone contrainte","Démontage par rétention","Chaque pièce est attachée et descendue en douceur avec un système de freinage. Aucun morceau ne touche le sol sans contrôle : toitures, serres et massifs sont préservés."),
   (CRANE,"","Nacelle, grue et moyens spéciaux","Quand la grimpe ne suffit pas, nous intervenons en nacelle ou faisons lever les sections à la grue. Dans les cas les plus rares, un hélicoptère peut être mobilisé. Nous organisons toute la logistique."),
   (STUMP,"","Rognage de souche","Après l'abattage, la souche est rognée sous le niveau du sol. Vous pouvez replanter, semer du gazon ou reconstruire sans obstacle."),
   (TREE,"","Évacuation et valorisation du bois","Branches broyées, bois de feu pour votre chauffage ou évacué. Le terrain est rendu propre, à vous de choisir.")])
ab+=why("Quand faut-il abattre un arbre","Certains arbres doivent être abattus. Nous vous conseillons au cas par cas.",
  "Abattre n'est pas notre première option : si une taille ou un haubanage peut sauver l'arbre, nous vous le proposons. Mais dans certains cas, l'abattage est la seule option raisonnable.",
  [("Arbre dangereux","Tronc fissuré, racines soulevées, penchant vers la maison ou la route : le risque de chute est réel, surtout par vent fort."),
   ("Arbre mort ou malade","Champignons au pied, écorce qui se détache, houppier sec : un arbre dépérissant devient cassant et imprévisible."),
   ("Trop proche des bâtiments","Racines qui soulèvent les dalles, branches sur la toiture, ombre permanente : l'arbre n'a plus sa place là où il a poussé."),
   ("Projet de construction","Extension, piscine, nouvel accès : nous libérons l'emprise proprement, souche comprise, avant les travaux.")])
ab+=approach("demontage_d-arbre_retention.jpg","Démontage d'arbre par rétention, tronçon retenu par cordes","Chaque pièce est retenue et contrôlée",
  "Notre méthode","Un abattage propre, c'est d'abord un abattage préparé",
  "La sécurité de vos biens et des personnes dépend de la préparation. Chaque intervention est planifiée avant que la tronçonneuse ne démarre.",
  [("Visite et évaluation sur place","Nous mesurons l'arbre, repérons les obstacles, les accès et les points d'ancrage, puis nous choisissons la technique et les moyens adaptés : grimpe, nacelle, grue ou, exceptionnellement, hélicoptère."),
   ("Zone sécurisée pendant les travaux","Périmètre balisé, protection des surfaces sensibles, coordination avec vous et vos voisins si nécessaire."),
   ("Descente contrôlée des pièces","En démontage, rien ne tombe au hasard : chaque tronçon est guidé ou freiné jusqu'au sol."),
   ("Terrain rendu propre","Bois évacué ou débité, branches broyées, sciure ramassée. Vous retrouvez votre jardin, sans la corvée.")],
  "Demander une évaluation gratuite")
ab+=process("Quatre étapes, du premier appel au terrain propre",
  [("Vous nous contactez","Décrivez l'arbre en quelques mots. En cas de danger immédiat, appelez-nous directement."),
   ("Visite et diagnostic","Nous évaluons l'arbre et son environnement, et vous conseillons sur la méthode et sur une éventuelle autorisation communale."),
   ("Devis clair et gratuit","Un devis écrit, avec ou sans rognage de souche et évacuation du bois."),
   ("Abattage et nettoyage","Intervention à la date convenue, en sécurité. Le terrain est nettoyé avant notre départ.")],eyebrow="Le planning des travaux")
ab+=gallery("Nos abattages et démontages",
  [("demontage_arbre_porrentruy.jpg","Démontage d'un grand arbre à Porrentruy","Démontage tronçon par tronçon, Porrentruy"),
   ("abattage_arbre_porrentruy-6.jpg","Grue et camion lors d'un abattage","Levage à la grue en zone urbaine"),
   ("abattage_sequoia.jpg","Souche d'un séquoia abattu","Abattage d'un séquoia"),
   ("abattage_arbre_porrentruy-3.jpg","Tronc débité après abattage","Bois débité, prêt à être évacué"),
   ("demontage_d-arbre_retention.jpg","Démontage par rétention","Descente par rétention, sans impact au sol"),
   ("arboriste_grimpeur-3.jpg","Arboriste-grimpeur au sommet d'un arbre","Accès en grimpe, à la corde")])
ab+=zone+'\n'
ab+=faq([("Faut-il une autorisation pour abattre un arbre ?","Dans de nombreuses communes du Jura, de Neuchâtel et de Berne, l'abattage d'un arbre peut être soumis à autorisation, selon son essence, sa taille ou sa situation (zone protégée, alignement, arbre remarquable). Nous vous indiquons la démarche à suivre auprès de votre commune et pouvons vous fournir les éléments techniques nécessaires."),
  ("Combien coûte l'abattage d'un arbre ?","Le prix dépend de la hauteur et du diamètre de l'arbre, de son accessibilité, de la technique nécessaire (abattage direct, démontage, rétention, grue) et de l'évacuation du bois. Un démontage en zone contrainte demande plus de temps qu'un abattage en plein champ. Nous établissons un devis précis et gratuit après visite."),
  ("Pouvez-vous abattre un arbre collé à ma maison ?","Oui, c'est justement le cœur de notre métier. Par démontage à la corde et rétention, chaque pièce est descendue de manière contrôlée, sans toucher la toiture, la façade ou les aménagements."),
  ("Mon arbre est-il vraiment à abattre ?","Pas forcément. Lors de la visite, nous examinons l'arbre avec attention. Si une taille de sécurité, un allègement ou un haubanage suffit à le conserver sans risque, nous vous le proposons en priorité."),
  ("Que faites-vous du bois et de la souche ?","Selon le devis, le bois est débité en bûches pour votre chauffage, broyé ou évacué. La souche peut être laissée, coupée au ras du sol ou rognée pour permettre une replantation ou un engazonnement."),
  ("Intervenez-vous en urgence après une tempête ?","Oui. Un arbre tombé sur un toit, une branche cassée qui menace de chuter ou un sujet déraciné : appelez-nous, nous intervenons au plus vite pour sécuriser les lieux.")])
ab+=cta("abattage_arbre_porrentruy-6.jpg","Un arbre vous inquiète ? Faites-le évaluer gratuitement.","Visite et devis gratuits, sans engagement. En cas de danger immédiat, appelez-nous directement.")
page('abattage.html',"Abattage et démontage d'arbres – Arboriste-grimpeur Jura, Neuchâtel, Berne | Arboritaille",
  "Abattage, démontage et rognage de souche par un arboriste-grimpeur professionnel. Intervention sécurisée, même près des bâtiments. Devis gratuit dans le Jura, Neuchâtel et Berne.",ab)

# ---------------- INDEX (généraliste) ----------------
ix_form=form("Recevez votre devis gratuit","Dites-nous ce dont votre arbre a besoin. Nous vous rappelons pour fixer une visite.",
  "Nouvelle demande de devis – Arboritaille","Landing page Google Ads – Généraliste",
  ["Taille et entretien","Abattage ou démontage","Diagnostic / expertise d'un arbre","Plantation","Haubanage / consolidation","Rognage de souche","Je ne sais pas encore, j'ai besoin d'un conseil"],"general")
ix=hero("arboriste_grimpeur-19.jpg","62% 30%","Arboriste-grimpeur · Jura · Neuchâtel · Berne",
  "Votre arboriste-grimpeur <em>pour tous les soins</em> de vos arbres",
  "Taille, élagage, abattage, démontage, diagnostic, plantation : Arboritaille prend soin de vos arbres avec les techniques de grimpe, les moyens adaptés à chaque situation et le respect du vivant. Pour les particuliers, les entreprises et les collectivités.",
  ["Devis gratuit et sans engagement","Réponse sous 48 h ouvrées","Un seul interlocuteur, du conseil au chantier","Chantier propre, branches évacuées"],ix_form)
ix+=trust([(SHIELD,"Arboriste-grimpeur","Techniques de grimpe et cordes"),(LEAF,"Respect de l'arbre","Taille raisonnée, conseil sur mesure"),(DOC,"Devis écrit et détaillé","Gratuit, sans engagement")])
ix+=cards("Nos services","Tout ce dont un arbre a besoin, de la plantation à l'abattage",
  "Un seul spécialiste pour l'ensemble de la vie de vos arbres. Nous vous conseillons la bonne intervention, au bon moment.",
  [(SCISS,"Le plus demandé","Taille et entretien","Taille d'entretien, réduction ou rehaussement de couronne, suppression du bois mort. Une taille raisonnée qui respecte la forme et la santé de l'arbre. <a href=\"taille.html\">En savoir plus</a>"),
   (AXE,"","Abattage et démontage","Abattage classique, démontage à la corde ou par rétention en zone contrainte, levage à la grue. Y compris près des bâtiments. <a href=\"abattage.html\">En savoir plus</a>"),
   (SEARCH,"","Diagnostic et expertise","Analyse de la vigueur, des défauts mécaniques et des pathologies. Un avis clair pour décider : conserver, soigner ou abattre."),
   (SPROUT,"","Plantation","Choix de l'essence adaptée au lieu, plantation dans les règles et tuteurage tripode pour une bonne reprise."),
   (LINK,"","Haubanage","Consolidation d'une fourche ou d'une charpentière fragile par haubanage dynamique ou statique, pour conserver l'arbre en sécurité."),
   (STUMP,"","Rognage de souche","Élimination des souches sous le niveau du sol pour replanter, engazonner ou construire sans obstacle.")])
ix+=why("Pour qui","Particuliers, entreprises, collectivités : le même soin, adapté à vos enjeux",
  "Que vous ayez un arbre dans votre jardin ou un parc d'arbres à gérer, vous avez le même besoin : un professionnel qui vous conseille selon votre situation.",
  [("Particuliers","Entretien de vos arbres de jardin, mise en sécurité, abattage d'un sujet gênant. Devis gratuit et conseils personnalisés."),
   ("Entreprises","Un arbre gêne votre chantier ou nécessite des soins ? Nous évaluons rapidement et intervenons dans les meilleurs délais."),
   ("Collectivités","Suivi de groupes d'arbres, gestion des sujets dangereux, projets de plantation. Un partenaire pour l'entretien arboricole communal."),
   ("Gérances et régies","Entretien régulier du patrimoine arboré de vos immeubles, avec un interlocuteur unique et des devis clairs.")])
ix+=approach("arboriste_grimpeur-2.jpg","Arboriste-grimpeur dans la couronne d'un grand arbre","Grimpe, nacelle ou grue selon le cas",
  "Notre approche","La passion du métier, le respect du vivant",
  "Chaque arbre est un cas particulier. Avant d'intervenir, nous prenons le temps de le comprendre : son essence, sa vigueur, son environnement et ce que vous en attendez.",
  [("Un conseil sur mesure","L'objectif est d'embellir et de conserver les arbres. Chaque situation est différente, parfois l'abattage est nécessaire. Nous sommes là pour vous conseiller."),
   ("Les bons moyens pour chaque arbre","Grimpe à la corde par défaut, pour préserver votre jardin. Nacelle, grue ou autres machines quand la situation l'exige, et hélicoptère dans les cas exceptionnels."),
   ("Des coupes propres et raisonnées","Taille raisonnée et respect de la physiologie de l'arbre pour un résultat durable."),
   ("Un chantier rendu propre","Branches broyées ou évacuées, bois débité si vous le souhaitez, terrain nettoyé.")],
  "Demander un devis gratuit")
ix+=process("Quatre étapes, du premier contact au terrain propre",
  [("Vous nous contactez","Par le formulaire ou par téléphone. Quelques mots sur votre arbre suffisent."),
   ("Visite et diagnostic","Nous venons voir l'arbre, écoutons vos attentes et vous conseillons la bonne intervention."),
   ("Devis clair et gratuit","Un devis écrit et détaillé. Vous décidez librement."),
   ("Intervention et nettoyage","Nous intervenons à la date convenue et laissons votre terrain propre.")])
ix+=gallery("Nos interventions",
  [("arboriste_grimpeur-3.jpg","Arboriste-grimpeur au sommet d'un cèdre","Taille en hauteur, accès en grimpe"),
   ("grand_tilleul.jpg","Grand tilleul sain après entretien","Un tilleul entretenu, équilibré et vigoureux"),
   ("demontage_arbre_porrentruy.jpg","Démontage d'un grand arbre à Porrentruy","Démontage tronçon par tronçon, Porrentruy"),
   ("demontage_d-arbre_retention.jpg","Démontage par rétention","Descente par rétention en zone contrainte"),
   ("plantation_arbre.jpg","Jeune arbre planté avec tuteurage tripode","Plantation et tuteurage tripode"),
   ("abattage_arbre_porrentruy-6.jpg","Grue lors d'un abattage","Levage à la grue en zone urbaine")])
ix+=zone+'\n'
ix+=faq([("Comment savoir si mon arbre a besoin d'une intervention ?","Bois mort dans la couronne, branches qui touchent une toiture, champignons au pied, tronc penché ou fissuré, feuillage clairsemé : autant de signes à ne pas ignorer. Une visite gratuite permet de trancher."),
  ("Combien coûtent vos prestations ?","Chaque arbre est différent : hauteur, essence, accès, type d'intervention et évacuation du bois font varier le prix. C'est pourquoi nous nous déplaçons gratuitement pour établir un devis écrit et précis."),
  ("Faut-il une autorisation pour tailler ou abattre un arbre ?","Une taille d'entretien ne nécessite en général aucune démarche. L'abattage, ou une intervention sur un arbre protégé, peut être soumis à autorisation communale. Nous vous guidons dans la démarche."),
  ("Mon arbre est difficile d'accès. Est-ce un problème ?","Non. Nous travaillons en grimpe, à la corde, ce qui permet d'accéder aux jardins clos, terrains en pente et cours intérieures. Quand c'est nécessaire, nous mobilisons une nacelle, une grue ou d'autres machines, et dans des cas très particuliers un hélicoptère."),
  ("Dans quelle zone intervenez-vous ?","Dans tout le canton du Jura, le canton de Neuchâtel et Berne."),
  ("Travaillez-vous avec les entreprises et les communes ?","Oui. Nous accompagnons les entreprises sur leurs chantiers et les collectivités pour la gestion de leur patrimoine arboré : suivi, sécurité, plantations.")])
ix+=cta("grand_tilleul.jpg","Un doute sur un arbre ? Demandez l'avis d'un professionnel.","Visite et devis gratuits, sans engagement. Nous vous répondons sous 48 h ouvrées.")
page('index.html',"Arboriste-grimpeur Jura, Neuchâtel, Berne – Taille, abattage, soins aux arbres | Arboritaille",
  "Arboritaille, arboriste-grimpeur à Courgenay : taille, élagage, abattage, démontage, diagnostic et plantation d'arbres. Devis gratuit dans le Jura, Neuchâtel et Berne.",ix)
print("built")
