# -*- coding: utf-8 -*-
# Génère les landing pages FR (racine) et DE (/de/) à partir des mêmes blocs.
import os

# ---------------- Icônes ----------------
I=dict(
PHONE='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.8 19.8 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
ARROW='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
CHECK='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>',
CK3='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>',
PIN='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
LOCK='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>',
MAIL='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 7L2 7"/></svg>',
SHIELD='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>',
SHIELD0='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
LEAF='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/></svg>',
DOC='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M16 13H8M16 17H8M10 9H8"/></svg>',
WARN='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/><path d="M12 9v4M12 17h.01"/></svg>',
TREE='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22v-6"/><path d="M8 16h8l-2-4h1l-3-5h.5L12 3l-.5 4H12l-3 5h1l-2 4z"/></svg>',
SCISS='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M20 4 8.12 15.88M14.47 14.48 20 20M8.12 8.12 12 12"/></svg>',
AXE='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m14 12-8.5 8.5a2.12 2.12 0 1 1-3-3L11 9"/><path d="M15 13 9 7l4-4 6 6h3a8 8 0 0 1-7 7z"/></svg>',
SEARCH='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>',
SPROUT='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 20h10M10 20c5.5-2.5.8-6.4 3-10"/><path d="M9.5 9.4c1.1.8 1.8 2.2 2.3 3.7-2 .4-3.5.4-4.8-.3-1.2-.6-2.3-1.9-3-4.2 2.8-.5 4.4 0 5.5.8z"/><path d="M14.1 6a7 7 0 0 0-1.1 4c1.9-.1 3.3-.6 4.3-1.4 1-1 1.6-2.3 1.7-4.6-2.7.1-4 1-4.9 2z"/></svg>',
LINK='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>',
STUMP='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="7" rx="8" ry="3"/><path d="M4 7v10c0 1.7 3.6 3 8 3s8-1.3 8-3V7"/><ellipse cx="12" cy="7" rx="3" ry="1.2"/></svg>',
CRANE='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21h18M6 21V8l12-5v18M6 8h12M14 8v6M14 14h3"/></svg>',
CUT='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3 3 6l3 3M18 3l3 3-3 3M3 6h18M12 6v15"/></svg>',
SHRINK='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 3 3 21M21 3h-6M21 3v6M3 21h6M3 21v-6"/></svg>',
LIFT='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22V8M5 12l7-7 7 7M4 22h16"/></svg>',
PLUS='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M2 12h20"/><circle cx="12" cy="12" r="9"/></svg>',
CABLE='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v18M6 9c0 3.3 2.7 6 6 6s6-2.7 6-6"/><path d="M4 6c0 4.4 3.6 8 8 8s8-3.6 8-8"/></svg>',
)

# ---------------- Textes d'interface par langue ----------------
UI={
'fr':dict(
  lang='fr-CH', base='', dir='', alt='de',
  phone_label='Appelez-nous', btn_quote='Devis gratuit', btn_quote_long='Demander un devis gratuit', btn_quote_mine='Demander mon devis gratuit',
  btn_call='Appeler', btn_send='Envoyer ma demande', choose='Choisir…',
  f_name='Nom et prénom', f_phone='Téléphone', f_mail='E-mail', f_city='Localité', f_need='Votre besoin', f_msg='Décrivez votre situation (facultatif)',
  f_msg_ph='Essence, hauteur approximative, accès, ce qui vous inquiète…', f_city_ph='Porrentruy, Delémont…', f_name_ph='Jean Dupont',
  f_note='Vos données restent confidentielles et servent uniquement à traiter votre demande. Aucune revente, aucun démarchage.',
  phone_note='', hero_phone_label='078 306 53 04',
  eyebrow_process='Comment ça se passe', eyebrow_gallery='Sur le terrain', eyebrow_faq='Questions fréquentes', h2_faq='Ce que nos clients nous demandent',
  eyebrow_cta='Parlons de votre arbre', cta_phone_sub='Robin Humbert, arboriste-grimpeur', cta_mail_sub='Réponse sous 48 h ouvrées',
  zone_eyebrow="Zone d'intervention", zone_h2='Jura, Neuchâtel et Berne',
  zone_lead='Basés à Courgenay, en Ajoie, nous intervenons chez les particuliers, les entreprises et les collectivités dans une grande partie de la Suisse romande.',
  zone_cols=[('Canton du Jura',['Porrentruy','Delémont','Courgenay','Alle','Bassecourt','Courrendlin','Moutier','Saignelégier','Le Noirmont',"Toute l'Ajoie"]),
             ('Canton de Neuchâtel',['Neuchâtel','La Chaux-de-Fonds','Le Locle','Val-de-Ruz','Val-de-Travers','Boudry','Littoral']),
             ('Berne',['Bienne','Tavannes','Saint-Imier','Tramelan','Reconvilier','La Neuveville'])],
  footer_role='Arboriste-grimpeur · Robin Humbert', footer_faq='FAQ', footer_quote='Devis',
  merci_title='Merci – Demande envoyée | Arboritaille', merci_h1='Merci, votre demande est bien reçue',
  merci_p="Nous vous recontactons sous 48 h ouvrées pour convenir d'une visite. Besoin d'une réponse plus rapide ? Appelez le ", merci_back='Retour au site',
  lang_switch='DE', lang_switch_title='Deutsche Version',
  src='Landing page Google Ads', lang_name='Français',
),
'de':dict(
  lang='de-CH', base='../', dir='de/', alt='fr',
  phone_label='Rufen Sie uns an', btn_quote='Gratis Offerte', btn_quote_long='Gratis Offerte anfordern', btn_quote_mine='Meine gratis Offerte anfordern',
  btn_call='Anrufen', btn_send='Anfrage senden', choose='Bitte wählen…',
  f_name='Name und Vorname', f_phone='Telefon', f_mail='E-Mail', f_city='Ort', f_need='Ihr Anliegen', f_msg='Beschreiben Sie Ihre Situation (optional)',
  f_msg_ph='Baumart, ungefähre Höhe, Zugang, was Ihnen Sorgen macht…', f_city_ph='Biel, Delsberg, Pruntrut…', f_name_ph='Hans Muster',
  f_note='Ihre Daten bleiben vertraulich und dienen ausschliesslich der Bearbeitung Ihrer Anfrage. Kein Weiterverkauf, keine Werbeanrufe.',
  phone_note='Wir kommunizieren gerne auf Deutsch per E-Mail und Kontaktformular. Telefonisch beraten wir Sie auf Französisch.',
  hero_phone_label='078 306 53 04 (Französisch)',
  eyebrow_process='So läuft es ab', eyebrow_gallery='Vor Ort', eyebrow_faq='Häufige Fragen', h2_faq='Was unsere Kunden uns fragen',
  eyebrow_cta='Sprechen wir über Ihren Baum', cta_phone_sub='Robin Humbert, Baumkletterer · Beratung auf Französisch', cta_mail_sub='Antwort auf Deutsch innert 48 Arbeitsstunden',
  zone_eyebrow='Einsatzgebiet', zone_h2='Jura, Neuenburg und Bern',
  zone_lead='Von Courgenay in der Ajoie aus sind wir für Privatpersonen, Unternehmen und Gemeinden in einem grossen Teil der Westschweiz und im Kanton Bern tätig.',
  zone_cols=[('Kanton Jura',['Pruntrut (Porrentruy)','Delsberg (Delémont)','Courgenay','Alle','Bassecourt','Courrendlin','Moutier','Saignelégier','Le Noirmont','ganze Ajoie']),
             ('Kanton Neuenburg',['Neuenburg (Neuchâtel)','La Chaux-de-Fonds','Le Locle','Val-de-Ruz','Val-de-Travers','Boudry','Seeufer']),
             ('Bern',['Biel/Bienne','Tavannes','Saint-Imier','Tramelan','Reconvilier','Neuenstadt (La Neuveville)'])],
  footer_role='Baumkletterer · Robin Humbert', footer_faq='FAQ', footer_quote='Offerte',
  merci_title='Danke – Anfrage gesendet | Arboritaille', merci_h1='Danke, Ihre Anfrage ist bei uns eingegangen',
  merci_p='Wir melden uns innert 48 Arbeitsstunden auf Deutsch per E-Mail, um einen Besichtigungstermin zu vereinbaren. Für eine schnellere Antwort erreichen Sie uns telefonisch auf Französisch unter ', merci_back='Zurück zur Seite',
  lang_switch='FR', lang_switch_title='Version française',
  src='Landing page Google Ads (DE)', lang_name='Deutsch',
),
}

# Correspondance des pages entre langues (nom de fichier)
PAGES={'index':{'fr':'index.html','de':'index.html'},
       'taille':{'fr':'taille.html','de':'baumpflege.html'},
       'abattage':{'fr':'abattage.html','de':'faellung.html'},
       'merci':{'fr':'merci.html','de':'danke.html'}}
SITE='https://page.arboritaille.ch/'
GTM_ID='GTM-WMF2BV3S'
GTM_HEAD=('<!-- Google Tag Manager -->\n<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({\'gtm.start\':new Date().getTime(),event:\'gtm.js\'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!=\'dataLayer\'?\'&l=\'+l:\'\';j.async=true;j.src=\'https://www.googletagmanager.com/gtm.js?id=\'+i+dl;f.parentNode.insertBefore(j,f);})(window,document,\'script\',\'dataLayer\',\''+GTM_ID+'\');</script>\n<!-- End Google Tag Manager -->') if GTM_ID else ''
GTM_BODY=('<!-- Google Tag Manager (noscript) -->\n<noscript><iframe src="https://www.googletagmanager.com/ns.html?id='+GTM_ID+'" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>\n<!-- End Google Tag Manager (noscript) -->') if GTM_ID else ''

def url(page,lang):
    return SITE+UI[lang]['dir']+PAGES[page][lang]

# ---------------- Blocs communs ----------------
def head(u,title,desc,page):
    b=u['base']; alt=u['alt']
    return f'''<!DOCTYPE html>
<html lang="{u['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, follow">
<link rel="alternate" hreflang="fr-CH" href="{url(page,'fr')}">
<link rel="alternate" hreflang="de-CH" href="{url(page,'de')}">
<link rel="icon" href="{b}img/logo-entreprise-icon-sans-fond.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{b}style.css">
{GTM_HEAD}
</head>
<body>
{GTM_BODY}
'''

def lang_link(u,page):
    alt=u['alt']; target=('../' if u['dir'] else 'de/')+PAGES[page][alt]
    return f'<a class="lang-switch" href="{target}" title="{u["lang_switch_title"]}" hreflang="{UI[alt]["lang"]}">{u["lang_switch"]}</a>'

def header(u,page):
    b=u['base']
    return f'''<header class="header">
  <div class="wrap">
    <a class="logo" href="#top" aria-label="Arboritaille">
      <img src="{b}img/logo-site-arboritaille-sans-ombre.svg" alt="Arboritaille" width="200" height="38">
    </a>
    <div class="header-cta">
      {lang_link(u,page)}
      <a class="header-phone" href="tel:+41783065304">{I['PHONE']}<span><small>{u['phone_label']}</small>078 306 53 04</span></a>
      <a class="btn btn-primary" href="#devis">{u['btn_quote']}</a>
    </div>
  </div>
</header>
'''

def form(u,page,title,sub,subject,options):
    opts=''.join('<option>'+o+'</option>' for o in options)
    note=f'<p class="form-note form-note-lang">{I["MAIL"]} {u["phone_note"]}</p>' if u['phone_note'] else ''
    return f'''<div class="form-card" id="devis">
      <h2>{title}</h2>
      <p class="sub">{sub}</p>
      <form action="{u['base']}contact.php" method="POST" id="devisForm">
        <input type="hidden" name="Sujet" value="{subject}">
        <input type="hidden" name="lp" value="{page}">
        <input type="hidden" name="lang" value="{'de' if u['dir'] else 'fr'}">
        <input type="hidden" name="Source" value="{u['src']} – {page}">
        <input type="hidden" name="Langue du client" value="{u['lang_name']}">
        <input type="text" name="_honey" class="honeypot" tabindex="-1" autocomplete="off">
        <div class="field-row">
          <div class="field"><label for="nom">{u['f_name']}</label><input id="nom" name="Nom" type="text" required autocomplete="name" placeholder="{u['f_name_ph']}"></div>
          <div class="field"><label for="tel">{u['f_phone']}</label><input id="tel" name="Téléphone" type="tel" required autocomplete="tel" placeholder="078 000 00 00"></div>
        </div>
        <div class="field-row">
          <div class="field"><label for="email">{u['f_mail']}</label><input id="email" name="Email" type="email" required autocomplete="email" placeholder="name@beispiel.ch"></div>
          <div class="field"><label for="localite">{u['f_city']}</label><input id="localite" name="Localité" type="text" required autocomplete="address-level2" placeholder="{u['f_city_ph']}"></div>
        </div>
        <div class="field"><label for="besoin">{u['f_need']}</label>
          <select id="besoin" name="Besoin" required><option value="" disabled selected>{u['choose']}</option>{opts}</select>
        </div>
        <div class="field"><label for="msg">{u['f_msg']}</label><textarea id="msg" name="Message" placeholder="{u['f_msg_ph']}"></textarea></div>
        <button class="btn btn-primary btn-block" type="submit">{u['btn_send']}</button>
        {note}
        <p class="form-note">{I['LOCK']} {u['f_note']}</p>
      </form>
    </div>'''

def hero(u,img,pos,eyebrow,h1,lead,points,formhtml):
    pts=''.join(f'<li>{I["CHECK"]}{p}</li>' for p in points)
    note=f'<p class="hero-note">{u["phone_note"]}</p>' if u['phone_note'] else ''
    return f'''<section class="hero">
  <img class="hero-bg" src="{u['base']}img/{img}" alt="" fetchpriority="high" style="object-position:{pos}">
  <div class="wrap">
    <div>
      <span class="eyebrow" style="color:var(--yellow)">{eyebrow}</span>
      <h1>{h1}</h1>
      <p class="lead">{lead}</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="#devis">{u['btn_quote_long']} {I['ARROW']}</a>
        <a class="btn btn-ghost" href="tel:+41783065304">{I['PHONE']} {u['hero_phone_label']}</a>
      </div>
      {note}
      <ul class="hero-points">{pts}</ul>
    </div>
    {formhtml}
  </div>
</section>
'''

def trust(items):
    inner=''.join(f'<div class="trust-item"><div class="ic">{I[ic]}</div><div>{a}<small>{b}</small></div></div>' for ic,a,b in items)
    return f'<section class="trust"><div class="wrap">{inner}</div></section>\n'

def cards(eyebrow,h2,lead,items):
    inner=''
    for ic,tag,h,p in items:
        tg=f'<span class="card-tag">{tag}</span>' if tag else ''
        inner+=f'<div class="card"><div class="ic">{I[ic]}</div>{tg}<h3>{h}</h3><p>{p}</p></div>'
    return f'''<section class="section" id="prestations"><div class="wrap">
  <div class="center"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2><p class="lead">{lead}</p></div>
  <div class="services-grid">{inner}</div>
</div></section>
'''

def why(eyebrow,h2,lead,items):
    inner=''.join(f'<div class="why-item"><div class="num">0{i+1}</div><h3>{h}</h3><p>{p}</p></div>' for i,(h,p) in enumerate(items))
    return f'''<section class="section why"><div class="wrap">
  <div class="center"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2><p class="lead">{lead}</p></div>
  <div class="why-grid">{inner}</div>
</div></section>
'''

def approach(u,img,alt,badge,eyebrow,h2,lead,items,cta):
    lis=''.join(f'<li><span class="ck">{I["CK3"]}</span><div><strong>{a}</strong><span>{b}</span></div></li>' for a,b in items)
    return f'''<section class="section"><div class="wrap split">
  <div class="split-img"><img src="{u['base']}img/{img}" alt="{alt}" loading="lazy"><div class="badge">{I['SHIELD0']} {badge}</div></div>
  <div><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2><p class="lead">{lead}</p>
    <ul class="check-list">{lis}</ul>
    <a class="btn btn-primary" href="#devis">{cta}</a>
  </div>
</div></section>
'''

def process(u,h2,steps,eyebrow=None):
    inner=''.join(f'<div class="step"><h3>{a}</h3><p>{b}</p></div>' for a,b in steps)
    return f'''<section class="section" style="padding-top:0"><div class="wrap">
  <div class="center"><span class="eyebrow">{eyebrow or u['eyebrow_process']}</span><h2>{h2}</h2></div>
  <div class="steps">{inner}</div>
</div></section>
'''

def gallery(u,h2,items):
    inner=''.join(f'<figure><img src="{u["base"]}img/{img}" alt="{alt}" loading="lazy"><figcaption>{cap}</figcaption></figure>' for img,alt,cap in items)
    return f'''<section class="section" style="padding-top:0"><div class="wrap">
  <div class="center"><span class="eyebrow">{u['eyebrow_gallery']}</span><h2>{h2}</h2></div>
  <div class="gallery">{inner}</div>
</div></section>
'''

def zone(u):
    cols=''
    for h,towns in u['zone_cols']:
        cols+=f'<div class="zone-col"><h3>{I["PIN"]}{h}</h3><ul>'+''.join(f'<li>{t}</li>' for t in towns)+'</ul></div>'
    return f'''<section class="section zone" id="zone"><div class="wrap">
  <div class="center"><span class="eyebrow">{u['zone_eyebrow']}</span><h2>{u['zone_h2']}</h2><p class="lead">{u['zone_lead']}</p></div>
  <div class="zone-grid">{cols}</div>
</div></section>
'''

def faq(u,items):
    inner=''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in items)
    return f'''<section class="section" id="faq"><div class="wrap">
  <div class="center"><span class="eyebrow">{u['eyebrow_faq']}</span><h2>{u['h2_faq']}</h2></div>
  <div class="faq">{inner}</div>
</div></section>
'''

def cta(u,img,h2,lead):
    return f'''<section class="section cta">
  <img class="cta-bg" src="{u['base']}img/{img}" alt="" loading="lazy">
  <div class="wrap">
    <div>
      <span class="eyebrow" style="color:var(--yellow)">{u['eyebrow_cta']}</span>
      <h2>{h2}</h2>
      <p class="lead">{lead}</p>
      <div class="cta-contact">
        <a href="tel:+41783065304"><span class="ic">{I['PHONE']}</span><span>078 306 53 04<small>{u['cta_phone_sub']}</small></span></a>
        <a href="mailto:contact@arboritaille.ch"><span class="ic">{I['MAIL']}</span><span>contact@arboritaille.ch<small>{u['cta_mail_sub']}</small></span></a>
      </div>
    </div>
    <div><a class="btn btn-primary" href="#devis" style="font-size:1.1rem;padding:1.1rem 2rem">{u['btn_quote_mine']} {I['ARROW']}</a></div>
  </div>
</section>
'''

def footer(u,page):
    b=u['base']; other=('../' if u['dir'] else 'de/')+PAGES[page][u['alt']]
    return f'''
<footer class="footer">
  <div class="wrap">
    <div class="footer-brand">
      <img src="{b}img/logo-entreprise-icon-sans-fond.svg" alt="" width="40" height="40">
      <div><strong>Arboritaille</strong>{u['footer_role']}</div>
    </div>
    <address>
      Derrière-Metthiez 13, 2950 Courgenay (JU)<br>
      <a href="tel:+41783065304">+41 78 306 53 04</a> · <a href="mailto:contact@arboritaille.ch">contact@arboritaille.ch</a>
    </address>
    <div class="footer-links">
      <a href="https://arboritaille.ch" rel="noopener">arboritaille.ch</a>
      <a href="#faq">{u['footer_faq']}</a>
      <a href="#devis">{u['footer_quote']}</a>
      <a href="{other}">{u['lang_switch_title']}</a>
    </div>
  </div>
</footer>

<div class="callbar">
  <a class="btn btn-outline" href="tel:+41783065304">{I['PHONE']} {u['btn_call']}</a>
  <a class="btn btn-primary" href="#devis">{u['btn_quote']}</a>
</div>

</body>
</html>
'''

def write(lang,page,title,desc,body):
    u=UI[lang]
    path=u['dir']+PAGES[page][lang]
    os.makedirs(os.path.dirname(path) or '.',exist_ok=True)
    open(path,'w',encoding='utf-8').write(head(u,title,desc,page)+header(u,page)+'\n<main id="top">\n\n'+body+'\n</main>'+footer(u,page))

def merci(lang):
    u=UI[lang]; b=u['base']; back=PAGES['index'][lang]
    html=f'''<!DOCTYPE html>
<html lang="{u['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{u['merci_title']}</title>
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="{b}img/logo-entreprise-icon-sans-fond.svg" type="image/svg+xml">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600&family=Inter:wght@400;600&display=swap" rel="stylesheet">
{GTM_HEAD}
<style>
body{{margin:0;font-family:"Inter",system-ui,sans-serif;background:#f5f1e8;color:#151a16;min-height:100vh;display:grid;place-items:center;padding:1.5rem}}
.box{{background:#fff;border-radius:18px;padding:2.5rem;max-width:520px;text-align:center;box-shadow:0 24px 60px rgba(15,32,23,.15)}}
.box img{{height:64px;margin:0 auto 1rem}}
h1{{font-family:"Fraunces",Georgia,serif;font-size:2rem;margin:0 0 .5rem;color:#163223}}
p{{color:#5d685f;line-height:1.6}}
.btn{{display:inline-block;margin-top:1rem;padding:.9rem 1.5rem;border-radius:999px;background:#d56626;color:#fff;font-weight:600;text-decoration:none}}
a.tel{{color:#163223;font-weight:600}}
</style>
</head>
<body>
{GTM_BODY}
<div class="box">
  <img src="{b}img/logo-entreprise-icon-sans-fond.svg" alt="Arboritaille">
  <h1>{u['merci_h1']}</h1>
  <p>{u['merci_p']}<a class="tel" href="tel:+41783065304">078 306 53 04</a>.</p>
  <a class="btn" href="{back}">{u['merci_back']}</a>
</div>
</body>
</html>
'''
    path=u['dir']+PAGES['merci'][lang]
    os.makedirs(os.path.dirname(path) or '.',exist_ok=True)
    open(path,'w',encoding='utf-8').write(html)

# ======================================================================
#                              FRANÇAIS
# ======================================================================
def build_fr():
    u=UI['fr']
    # ---------- TAILLE ----------
    f=form(u,'taille',"Recevez votre devis gratuit","Décrivez-nous votre arbre en 30 secondes. Nous vous rappelons pour fixer une visite.",
      "Nouvelle demande de devis – Taille et entretien d'arbres",
      ["Taille d'entretien","Réduction ou allègement de couronne","Élagage de sécurité (bois mort, branches dangereuses)","Taille de fruitiers","Diagnostic / conseil sur un arbre","Abattage ou démontage","Autre"])
    p=hero(u,"arboriste_grimpeur-19.jpg","62% 30%","Arboriste-grimpeur · Jura · Neuchâtel · Berne",
      "Taille et entretien d'arbres <em>dans les règles de l'art</em>",
      "Un arboriste-grimpeur professionnel prend soin de vos arbres : taille raisonnée, mise en sécurité, allègement de couronne, bois mort. En grimpe, en nacelle ou avec les machines adaptées, avec un devis clair et gratuit.",
      ["Devis gratuit et sans engagement","Réponse sous 48 h ouvrées","Taille raisonnée, respectueuse de l'arbre","Chantier propre, branches évacuées"],f)
    p+=trust([('SHIELD',"Arboriste-grimpeur","Techniques de grimpe et cordes"),('LEAF',"Taille raisonnée","Respect de la physiologie de l'arbre"),('DOC',"Devis écrit et détaillé","Gratuit, sans engagement")])
    p+=cards("Nos prestations de taille","Chaque arbre mérite la taille qui lui convient",
      "Il n'existe pas de taille standard. Nous observons l'arbre, son essence, son âge et son environnement avant de choisir l'intervention adaptée.",
      [('CUT',"Le plus demandé","Taille d'entretien","Suppression du bois mort et des branches qui se croisent ou frottent, pour laisser passer la lumière et l'air. L'arbre garde sa silhouette naturelle."),
       ('SHRINK',"","Réduction et allègement de couronne","Pour un arbre devenu trop volumineux, trop proche d'une toiture ou d'une ligne. Nous réduisons de manière ciblée en limitant la taille des coupes pour impacter le moins possible la structure de l'arbre."),
       ('LIFT',"","Rehaussement de couronne","Remontée des branches basses pour dégager un passage, une façade, un accès véhicule ou une vue, tout en respectant les besoins de l'arbre."),
       ('WARN',"Urgence possible","Élagage de sécurité","Branches fissurées, bois mort au-dessus d'une zone de passage, arbre fragilisé après une tempête. Nous sécurisons rapidement et proprement."),
       ('PLUS',"","Taille de formation","Pour les jeunes arbres et les plantations récentes : guider la structure dès les premières années évite les gros travaux plus tard."),
       ('CABLE',"","Haubanage et consolidation","Quand une fourche ou une charpentière présente une faiblesse, un haubanage dynamique permet souvent de conserver l'arbre plutôt que de l'abattre.")])
    p+=why("Pourquoi faire tailler ses arbres","Une taille bien faite protège vos arbres, vos biens ainsi que votre sécurité.",
      "Faire suivre vos arbres par un professionnel permet de prévenir les risques, de les adapter au mieux à leur environnement et ainsi de réduire au minimum les impacts subis, dans le but de les conserver le plus longtemps possible.",
      [("Sécurité","Élimination du bois mort et des branches à risque au-dessus des toitures, terrasses, routes et aires de jeux."),
       ("Santé de l'arbre","Des coupes propres, au bon endroit et de la plus petite taille possible, limitent champignons et parasites."),
       ("Lumière et espace","Retrouvez de la clarté dans le jardin et la maison, dégagez une vue ou un passage sans sacrifier l'arbre."),
       ("Valeur du bien","Des arbres sains et bien conduits valorisent votre propriété et vous évitent un abattage coûteux dans quelques années.")])
    p+=approach(u,"arboriste_grimpeur-2.jpg","Arboriste-grimpeur en intervention dans la couronne d'un grand arbre","Grimpe, nacelle ou grue selon le cas",
      "Notre approche","La taille raisonnée : intervenir ni trop, ni trop peu",
      "Un arbre étêté ou taillé trop sévèrement s'affaiblit, produit des rejets fragiles et devient plus dangereux qu'avant. Nous faisons l'inverse.",
      [("Diagnostic avant de couper","Essence, vigueur, défauts mécaniques, contraintes du terrain : chaque intervention commence par une lecture de l'arbre."),
       ("Des coupes propres, au bon endroit","Respect du col de la branche et des proportions : l'arbre tolère mieux ce type de coupe."),
       ("Le bon moyen d'accès pour chaque arbre","Grimpe à la corde par défaut, pour préserver votre jardin. Nacelle, grue ou autres machines quand la situation l'exige, et même hélicoptère dans les cas exceptionnels."),
       ("Chantier rendu propre","Branches broyées ou évacuées, terrain nettoyé. Vous ne vous occupez de rien.")],
      "Planifier une visite gratuite")
    p+=process(u,"Quatre étapes, du premier contact au terrain propre",
      [("Vous nous contactez","Par le formulaire ou par téléphone. Quelques mots sur votre arbre suffisent pour démarrer."),
       ("Visite et diagnostic","Nous venons voir l'arbre sur place, écoutons vos attentes et vous conseillons sur ce qu'il faut faire, ou ne pas faire."),
       ("Devis clair et gratuit","Vous recevez un devis écrit et détaillé. Vous décidez en toute liberté."),
       ("Intervention et nettoyage","Nous intervenons à la date convenue, sécurisons la zone et laissons votre jardin propre.")])
    p+=gallery(u,"Nos interventions",
      [("arboriste_grimpeur-3.jpg","Arboriste-grimpeur au sommet d'un cèdre","Taille en hauteur, accès en grimpe"),
       ("grand_tilleul.jpg","Grand tilleul sain après entretien","Un tilleul entretenu, équilibré et vigoureux"),
       ("arbre_porrentruy.jpg","Arbre de jardin à Porrentruy","Arbre de jardin, Porrentruy"),
       ("demontage_d-arbre_retention.jpg","Démontage d'arbre par rétention","Démontage par rétention en zone contrainte"),
       ("arboriste_grimpeur-15.jpg","Arboriste-grimpeur dans le feuillage","Travail dans la couronne, à la corde"),
       ("plantation_arbre.jpg","Jeune arbre planté avec tuteurage tripode","Plantation et tuteurage tripode")])
    p+=zone(u)
    p+=faq(u,[("Quelle est la meilleure période pour tailler un arbre ?","Cela dépend de l'essence et de l'objectif. La taille d'entretien se pratique souvent en hiver, hors gel, ou en été après la pousse. Certaines essences supportent mal la taille en période de montée de sève. Nous vous conseillons la période la plus favorable lors de la visite."),
      ("Combien coûte une taille d'arbre ?","Le prix dépend de la taille de l'arbre, de son accessibilité, du type d'intervention et de l'évacuation des branches. C'est pourquoi nous nous déplaçons gratuitement pour établir un devis précis et écrit. Aucun engagement de votre part."),
      ("Faut-il une autorisation pour tailler ou abattre un arbre ?","Une simple taille d'entretien ne nécessite en général aucune démarche. L'abattage, ou l'intervention sur un arbre protégé ou situé en zone particulière, peut être soumis à autorisation communale. Nous vous indiquons la marche à suivre selon votre commune."),
      ("Mon arbre est très grand ou difficile d'accès. Est-ce possible ?","Oui. En tant qu'arboriste-grimpeur, nous accédons à la couronne à la corde, ce qui convient à la plupart des jardins, cours intérieures et terrains en pente. Quand c'est nécessaire, nous mobilisons une nacelle, une grue ou d'autres machines, et dans des cas très particuliers un hélicoptère."),
      ("Que deviennent les branches coupées ?","Selon votre souhait et le devis, les branches sont broyées sur place, évacuées, ou le bois est laissé débité pour votre chauffage. Le terrain est nettoyé avant notre départ."),
      ("Intervenez-vous aussi pour les entreprises et les communes ?","Oui. Nous accompagnons les entreprises sur leurs chantiers, ainsi que les collectivités pour le suivi de groupes d'arbres, la gestion des sujets dangereux et les projets de plantation.")])
    p+=cta(u,"grand_tilleul.jpg","Un doute sur un arbre ? Demandez l'avis d'un professionnel.","Visite et devis gratuits, sans engagement. Nous vous répondons sous 48 h ouvrées.")
    write('fr','taille',"Taille et entretien d'arbres – Arboriste-grimpeur Jura, Neuchâtel, Berne | Arboritaille",
      "Taille raisonnée, élagage et entretien de vos arbres par un arboriste-grimpeur professionnel. Devis gratuit sous 48 h dans le Jura, Neuchâtel et Berne.",p)

    # ---------- ABATTAGE ----------
    f=form(u,'abattage',"Devis abattage gratuit","Décrivez l'arbre et son emplacement. Nous venons l'évaluer sur place, sans engagement.",
      "Nouvelle demande de devis – Abattage / démontage d'arbre",
      ["Abattage d'un arbre","Démontage d'un arbre en zone contrainte","Arbre dangereux / urgence après tempête","Arbre mort ou malade","Rognage de souche","Plusieurs arbres à abattre","Autre"])
    p=hero(u,"demontage_arbre_porrentruy.jpg","55% 35%","Abattage et démontage · Jura · Neuchâtel · Berne",
      "Abattage d'arbres <em>en toute sécurité</em>, même en espace restreint",
      "Arbre dangereux, mort, malade ou trop proche de la maison ? Un arboriste-grimpeur professionnel l'abat ou le démonte pièce par pièce, en préservant votre propriété, et laisse le terrain propre.",
      ["Devis gratuit et sans engagement","Intervention rapide en cas d'urgence","Grimpe, nacelle, grue ou hélicoptère selon le cas","Bois évacué, terrain nettoyé"],f)
    p+=trust([('SHIELD',"Arboriste-grimpeur","Démontage à la corde, techniques de rétention"),('WARN',"Urgences tempête","Mise en sécurité rapide"),('DOC',"Devis écrit et détaillé","Gratuit, sans engagement")])
    p+=cards("Nos prestations d'abattage","La bonne technique pour chaque situation",
      "Un arbre isolé dans un pré ne s'abat pas comme un sapin collé à une façade. Nous choisissons la méthode adaptée à votre terrain, vos bâtiments et vos voisins.",
      [('AXE',"","Abattage classique","Quand l'espace le permet, l'arbre est abattu en une pièce, avec une direction de chute maîtrisée. La solution la plus rapide et la plus économique."),
       ('SCISS',"Le plus courant","Démontage par morceaux","Le grimpeur monte dans l'arbre et le démonte branche par branche, puis tronçon par tronçon. Adapté en jardin, près d'une maison ou d'une ligne électrique."),
       ('LINK',"Zone contrainte","Démontage par rétention","Chaque pièce est attachée et descendue en douceur avec un système de freinage. Aucun morceau ne touche le sol sans contrôle : toitures, serres et massifs sont préservés."),
       ('CRANE',"","Nacelle, grue et moyens spéciaux","Quand la grimpe ne suffit pas, nous intervenons en nacelle ou faisons lever les sections à la grue. Dans les cas les plus rares, un hélicoptère peut être mobilisé. Nous organisons toute la logistique."),
       ('STUMP',"","Rognage de souche","Après l'abattage, la souche est rognée sous le niveau du sol. Vous pouvez replanter, semer du gazon ou reconstruire sans obstacle."),
       ('TREE',"","Évacuation et valorisation du bois","Branches broyées, bois de feu pour votre chauffage ou évacué. Le terrain est rendu propre, à vous de choisir.")])
    p+=why("Quand faut-il abattre un arbre","Certains arbres doivent être abattus. Nous vous conseillons au cas par cas.",
      "Abattre n'est pas notre première option : si une taille ou un haubanage peut sauver l'arbre, nous vous le proposons. Mais dans certains cas, l'abattage est la seule option raisonnable.",
      [("Arbre dangereux","Tronc fissuré, racines soulevées, penchant vers la maison ou la route : le risque de chute est réel, surtout par vent fort."),
       ("Arbre mort ou malade","Champignons au pied, écorce qui se détache, houppier sec : un arbre dépérissant devient cassant et imprévisible."),
       ("Trop proche des bâtiments","Racines qui soulèvent les dalles, branches sur la toiture, ombre permanente : l'arbre n'a plus sa place là où il a poussé."),
       ("Projet de construction","Extension, piscine, nouvel accès : nous libérons l'emprise proprement, souche comprise, avant les travaux.")])
    p+=approach(u,"demontage_d-arbre_retention.jpg","Démontage d'arbre par rétention, tronçon retenu par cordes","Chaque pièce est retenue et contrôlée",
      "Notre méthode","Un abattage propre, c'est d'abord un abattage préparé",
      "La sécurité de vos biens et des personnes dépend de la préparation. Chaque intervention est planifiée avant que la tronçonneuse ne démarre.",
      [("Visite et évaluation sur place","Nous mesurons l'arbre, repérons les obstacles, les accès et les points d'ancrage, puis nous choisissons la technique et les moyens adaptés : grimpe, nacelle, grue ou, exceptionnellement, hélicoptère."),
       ("Zone sécurisée pendant les travaux","Périmètre balisé, protection des surfaces sensibles, coordination avec vous et vos voisins si nécessaire."),
       ("Descente contrôlée des pièces","En démontage, rien ne tombe au hasard : chaque tronçon est guidé ou freiné jusqu'au sol."),
       ("Terrain rendu propre","Bois évacué ou débité, branches broyées, sciure ramassée. Vous retrouvez votre jardin, sans la corvée.")],
      "Demander une évaluation gratuite")
    p+=process(u,"Quatre étapes, du premier appel au terrain propre",
      [("Vous nous contactez","Décrivez l'arbre en quelques mots. En cas de danger immédiat, appelez-nous directement."),
       ("Visite et diagnostic","Nous évaluons l'arbre et son environnement, et vous conseillons sur la méthode et sur une éventuelle autorisation communale."),
       ("Devis clair et gratuit","Un devis écrit, avec ou sans rognage de souche et évacuation du bois."),
       ("Abattage et nettoyage","Intervention à la date convenue, en sécurité. Le terrain est nettoyé avant notre départ.")],eyebrow="Le planning des travaux")
    p+=gallery(u,"Nos abattages et démontages",
      [("demontage_arbre_porrentruy.jpg","Démontage d'un grand arbre à Porrentruy","Démontage tronçon par tronçon, Porrentruy"),
       ("abattage_arbre_porrentruy-6.jpg","Grue et camion lors d'un abattage","Levage à la grue en zone urbaine"),
       ("abattage_sequoia.jpg","Souche d'un séquoia abattu","Abattage d'un séquoia"),
       ("abattage_arbre_porrentruy-3.jpg","Tronc débité après abattage","Bois débité, prêt à être évacué"),
       ("demontage_d-arbre_retention.jpg","Démontage par rétention","Descente par rétention, sans impact au sol"),
       ("arboriste_grimpeur-3.jpg","Arboriste-grimpeur au sommet d'un arbre","Accès en grimpe, à la corde")])
    p+=zone(u)
    p+=faq(u,[("Faut-il une autorisation pour abattre un arbre ?","Dans de nombreuses communes du Jura, de Neuchâtel et de Berne, l'abattage d'un arbre peut être soumis à autorisation, selon son essence, sa taille ou sa situation (zone protégée, alignement, arbre remarquable). Nous vous indiquons la démarche à suivre auprès de votre commune et pouvons vous fournir les éléments techniques nécessaires."),
      ("Combien coûte l'abattage d'un arbre ?","Le prix dépend de la hauteur et du diamètre de l'arbre, de son accessibilité, de la technique nécessaire (abattage direct, démontage, rétention, grue) et de l'évacuation du bois. Un démontage en zone contrainte demande plus de temps qu'un abattage en plein champ. Nous établissons un devis précis et gratuit après visite."),
      ("Pouvez-vous abattre un arbre collé à ma maison ?","Oui, c'est justement le cœur de notre métier. Par démontage à la corde et rétention, chaque pièce est descendue de manière contrôlée, sans toucher la toiture, la façade ou les aménagements."),
      ("Mon arbre est-il vraiment à abattre ?","Pas forcément. Lors de la visite, nous examinons l'arbre avec attention. Si une taille de sécurité, un allègement ou un haubanage suffit à le conserver sans risque, nous vous le proposons en priorité."),
      ("Que faites-vous du bois et de la souche ?","Selon le devis, le bois est débité en bûches pour votre chauffage, broyé ou évacué. La souche peut être laissée, coupée au ras du sol ou rognée pour permettre une replantation ou un engazonnement."),
      ("Intervenez-vous en urgence après une tempête ?","Oui. Un arbre tombé sur un toit, une branche cassée qui menace de chuter ou un sujet déraciné : appelez-nous, nous intervenons au plus vite pour sécuriser les lieux.")])
    p+=cta(u,"abattage_arbre_porrentruy-6.jpg","Un arbre vous inquiète ? Faites-le évaluer gratuitement.","Visite et devis gratuits, sans engagement. En cas de danger immédiat, appelez-nous directement.")
    write('fr','abattage',"Abattage et démontage d'arbres – Arboriste-grimpeur Jura, Neuchâtel, Berne | Arboritaille",
      "Abattage, démontage et rognage de souche par un arboriste-grimpeur professionnel. Intervention sécurisée, même près des bâtiments. Devis gratuit dans le Jura, Neuchâtel et Berne.",p)

    # ---------- INDEX ----------
    f=form(u,'index',"Recevez votre devis gratuit","Dites-nous ce dont votre arbre a besoin. Nous vous rappelons pour fixer une visite.",
      "Nouvelle demande de devis – Arboritaille",
      ["Taille et entretien","Abattage ou démontage","Diagnostic / expertise d'un arbre","Plantation","Haubanage / consolidation","Rognage de souche","Je ne sais pas encore, j'ai besoin d'un conseil"])
    p=hero(u,"arboriste_grimpeur-19.jpg","62% 30%","Arboriste-grimpeur · Jura · Neuchâtel · Berne",
      "Votre arboriste-grimpeur <em>pour tous les soins</em> de vos arbres",
      "Taille, élagage, abattage, démontage, diagnostic, plantation : Arboritaille prend soin de vos arbres avec les techniques de grimpe, les moyens adaptés à chaque situation et le respect du vivant. Pour les particuliers, les entreprises et les collectivités.",
      ["Devis gratuit et sans engagement","Réponse sous 48 h ouvrées","Un seul interlocuteur, du conseil au chantier","Chantier propre, branches évacuées"],f)
    p+=trust([('SHIELD',"Arboriste-grimpeur","Techniques de grimpe et cordes"),('LEAF',"Respect de l'arbre","Taille raisonnée, conseil sur mesure"),('DOC',"Devis écrit et détaillé","Gratuit, sans engagement")])
    p+=cards("Nos services","Tout ce dont un arbre a besoin, de la plantation à l'abattage",
      "Un seul spécialiste pour l'ensemble de la vie de vos arbres. Nous vous conseillons la bonne intervention, au bon moment.",
      [('SCISS',"Le plus demandé","Taille et entretien","Taille d'entretien, réduction ou rehaussement de couronne, suppression du bois mort. Une taille raisonnée qui respecte la forme et la santé de l'arbre. <a href=\"taille.html\">En savoir plus</a>"),
       ('AXE',"","Abattage et démontage","Abattage classique, démontage à la corde ou par rétention en zone contrainte, levage à la grue. Y compris près des bâtiments. <a href=\"abattage.html\">En savoir plus</a>"),
       ('SEARCH',"","Diagnostic et expertise","Analyse de la vigueur, des défauts mécaniques et des pathologies. Un avis clair pour décider : conserver, soigner ou abattre."),
       ('SPROUT',"","Plantation","Choix de l'essence adaptée au lieu, plantation dans les règles et tuteurage tripode pour une bonne reprise."),
       ('LINK',"","Haubanage","Consolidation d'une fourche ou d'une charpentière fragile par haubanage dynamique ou statique, pour conserver l'arbre en sécurité."),
       ('STUMP',"","Rognage de souche","Élimination des souches sous le niveau du sol pour replanter, engazonner ou construire sans obstacle.")])
    p+=why("Pour qui","Particuliers, entreprises, collectivités : le même soin, adapté à vos enjeux",
      "Que vous ayez un arbre dans votre jardin ou un parc d'arbres à gérer, vous avez le même besoin : un professionnel qui vous conseille selon votre situation.",
      [("Particuliers","Entretien de vos arbres de jardin, mise en sécurité, abattage d'un sujet gênant. Devis gratuit et conseils personnalisés."),
       ("Entreprises","Un arbre gêne votre chantier ou nécessite des soins ? Nous évaluons rapidement et intervenons dans les meilleurs délais."),
       ("Collectivités","Suivi de groupes d'arbres, gestion des sujets dangereux, projets de plantation. Un partenaire pour l'entretien arboricole communal."),
       ("Gérances et régies","Entretien régulier du patrimoine arboré de vos immeubles, avec un interlocuteur unique et des devis clairs.")])
    p+=approach(u,"arboriste_grimpeur-2.jpg","Arboriste-grimpeur dans la couronne d'un grand arbre","Grimpe, nacelle ou grue selon le cas",
      "Notre approche","La passion du métier, le respect du vivant",
      "Chaque arbre est un cas particulier. Avant d'intervenir, nous prenons le temps de le comprendre : son essence, sa vigueur, son environnement et ce que vous en attendez.",
      [("Un conseil sur mesure","L'objectif est d'embellir et de conserver les arbres. Chaque situation est différente, parfois l'abattage est nécessaire. Nous sommes là pour vous conseiller."),
       ("Les bons moyens pour chaque arbre","Grimpe à la corde par défaut, pour préserver votre jardin. Nacelle, grue ou autres machines quand la situation l'exige, et hélicoptère dans les cas exceptionnels."),
       ("Des coupes propres et raisonnées","Taille raisonnée et respect de la physiologie de l'arbre pour un résultat durable."),
       ("Un chantier rendu propre","Branches broyées ou évacuées, bois débité si vous le souhaitez, terrain nettoyé.")],
      "Demander un devis gratuit")
    p+=process(u,"Quatre étapes, du premier contact au terrain propre",
      [("Vous nous contactez","Par le formulaire ou par téléphone. Quelques mots sur votre arbre suffisent."),
       ("Visite et diagnostic","Nous venons voir l'arbre, écoutons vos attentes et vous conseillons la bonne intervention."),
       ("Devis clair et gratuit","Un devis écrit et détaillé. Vous décidez librement."),
       ("Intervention et nettoyage","Nous intervenons à la date convenue et laissons votre terrain propre.")])
    p+=gallery(u,"Nos interventions",
      [("arboriste_grimpeur-3.jpg","Arboriste-grimpeur au sommet d'un cèdre","Taille en hauteur, accès en grimpe"),
       ("grand_tilleul.jpg","Grand tilleul sain après entretien","Un tilleul entretenu, équilibré et vigoureux"),
       ("demontage_arbre_porrentruy.jpg","Démontage d'un grand arbre à Porrentruy","Démontage tronçon par tronçon, Porrentruy"),
       ("demontage_d-arbre_retention.jpg","Démontage par rétention","Descente par rétention en zone contrainte"),
       ("plantation_arbre.jpg","Jeune arbre planté avec tuteurage tripode","Plantation et tuteurage tripode"),
       ("abattage_arbre_porrentruy-6.jpg","Grue lors d'un abattage","Levage à la grue en zone urbaine")])
    p+=zone(u)
    p+=faq(u,[("Comment savoir si mon arbre a besoin d'une intervention ?","Bois mort dans la couronne, branches qui touchent une toiture, champignons au pied, tronc penché ou fissuré, feuillage clairsemé : autant de signes à ne pas ignorer. Une visite gratuite permet de trancher."),
      ("Combien coûtent vos prestations ?","Chaque arbre est différent : hauteur, essence, accès, type d'intervention et évacuation du bois font varier le prix. C'est pourquoi nous nous déplaçons gratuitement pour établir un devis écrit et précis."),
      ("Faut-il une autorisation pour tailler ou abattre un arbre ?","Une taille d'entretien ne nécessite en général aucune démarche. L'abattage, ou une intervention sur un arbre protégé, peut être soumis à autorisation communale. Nous vous guidons dans la démarche."),
      ("Mon arbre est difficile d'accès. Est-ce un problème ?","Non. Nous travaillons en grimpe, à la corde, ce qui permet d'accéder aux jardins clos, terrains en pente et cours intérieures. Quand c'est nécessaire, nous mobilisons une nacelle, une grue ou d'autres machines, et dans des cas très particuliers un hélicoptère."),
      ("Dans quelle zone intervenez-vous ?","Dans tout le canton du Jura, le canton de Neuchâtel et Berne."),
      ("Travaillez-vous avec les entreprises et les communes ?","Oui. Nous accompagnons les entreprises sur leurs chantiers et les collectivités pour la gestion de leur patrimoine arboré : suivi, sécurité, plantations.")])
    p+=cta(u,"grand_tilleul.jpg","Un doute sur un arbre ? Demandez l'avis d'un professionnel.","Visite et devis gratuits, sans engagement. Nous vous répondons sous 48 h ouvrées.")
    write('fr','index',"Arboriste-grimpeur Jura, Neuchâtel, Berne – Taille, abattage, soins aux arbres | Arboritaille",
      "Arboritaille, arboriste-grimpeur à Courgenay : taille, élagage, abattage, démontage, diagnostic et plantation d'arbres. Devis gratuit dans le Jura, Neuchâtel et Berne.",p)
    merci('fr')

# ======================================================================
#                              DEUTSCH (Schweiz)
# ======================================================================
def build_de():
    u=UI['de']
    DE_NOTE_FAQ=("Sprechen Sie Deutsch?","Ja, schriftlich. Wir beantworten Ihre Anfragen gerne auf Deutsch per E-Mail und Kontaktformular, und die Offerte erhalten Sie ebenfalls auf Deutsch. Telefonisch beraten wir Sie auf Französisch. Am einfachsten beschreiben Sie uns Ihren Baum über das Formular, wir melden uns schriftlich zurück.")
    # ---------- BAUMPFLEGE (taille) ----------
    f=form(u,'taille',"Ihre gratis Offerte","Beschreiben Sie uns Ihren Baum in 30 Sekunden. Wir melden uns schriftlich, um einen Besichtigungstermin zu vereinbaren.",
      "Neue Offertanfrage (DE) – Baumschnitt und Baumpflege",
      ["Pflegeschnitt","Kroneneinkürzung oder Kronenentlastung","Sicherheitsschnitt (Totholz, gefährliche Äste)","Obstbaumschnitt","Baumdiagnose / Beratung","Fällung oder Abtragen","Anderes"])
    p=hero(u,"arboriste_grimpeur-19.jpg","62% 30%","Baumkletterer · Jura · Neuenburg · Bern",
      "Baumschnitt und Baumpflege <em>nach den Regeln der Fachkunde</em>",
      "Ein professioneller Baumkletterer kümmert sich um Ihre Bäume: baumschonender Schnitt, Sicherung, Kronenentlastung, Totholzentfernung. In Klettertechnik, mit Hebebühne oder den passenden Maschinen, mit einer klaren und kostenlosen Offerte.",
      ["Gratis Offerte, unverbindlich","Antwort innert 48 Arbeitsstunden","Baumschonender Schnitt","Sauberer Arbeitsplatz, Äste abtransportiert"],f)
    p+=trust([('SHIELD',"Baumkletterer","Seilklettertechnik"),('LEAF',"Baumschonender Schnitt","Respekt vor der Physiologie des Baums"),('DOC',"Schriftliche, detaillierte Offerte","Gratis und unverbindlich")])
    p+=cards("Unsere Schnittarbeiten","Jeder Baum verdient den Schnitt, der zu ihm passt",
      "Es gibt keinen Standardschnitt. Wir beobachten den Baum, seine Art, sein Alter und sein Umfeld, bevor wir den passenden Eingriff wählen.",
      [('CUT',"Am häufigsten","Pflegeschnitt","Entfernen von Totholz und von Ästen, die sich kreuzen oder reiben, damit Licht und Luft in die Krone gelangen. Der Baum behält seine natürliche Form."),
       ('SHRINK',"","Kroneneinkürzung und Kronenentlastung","Für Bäume, die zu gross geworden sind oder einem Dach oder einer Leitung zu nahe kommen. Wir kürzen gezielt ein und halten die Schnittstellen klein, um die Struktur des Baums so wenig wie möglich zu beeinträchtigen."),
       ('LIFT',"","Kronenaufastung","Entfernen der unteren Äste, um einen Durchgang, eine Fassade, eine Zufahrt oder eine Aussicht freizustellen, unter Berücksichtigung der Bedürfnisse des Baums."),
       ('WARN',"Notfall möglich","Sicherheitsschnitt","Gerissene Äste, Totholz über einem Durchgang, ein durch Sturm geschwächter Baum: wir sichern rasch und sauber."),
       ('PLUS',"","Erziehungsschnitt","Für junge Bäume und Neupflanzungen: wer die Struktur in den ersten Jahren lenkt, vermeidet später grosse Eingriffe."),
       ('CABLE',"","Kronensicherung","Zeigt eine Zwiesel oder ein Starkast eine Schwachstelle, erlaubt eine dynamische Kronensicherung oft, den Baum zu erhalten, statt ihn zu fällen.")])
    p+=why("Warum Bäume schneiden lassen","Ein fachgerechter Schnitt schützt Ihre Bäume, Ihr Eigentum und Ihre Sicherheit.",
      "Wer seine Bäume von einer Fachperson betreuen lässt, beugt Risiken vor, passt sie bestmöglich an ihr Umfeld an und hält die Eingriffe so gering wie möglich, mit dem Ziel, die Bäume so lange wie möglich zu erhalten.",
      [("Sicherheit","Entfernen von Totholz und Risikoästen über Dächern, Terrassen, Strassen und Spielplätzen."),
       ("Gesundheit des Baums","Saubere Schnitte an der richtigen Stelle und so klein wie möglich begrenzen Pilze und Schädlinge."),
       ("Licht und Raum","Mehr Helligkeit in Garten und Haus, eine freie Aussicht oder ein freier Durchgang, ohne den Baum zu opfern."),
       ("Wert der Liegenschaft","Gesunde, gut geführte Bäume werten Ihr Grundstück auf und ersparen Ihnen in einigen Jahren eine teure Fällung.")])
    p+=approach(u,"arboriste_grimpeur-2.jpg","Baumkletterer bei der Arbeit in der Krone eines grossen Baums","Klettern, Hebebühne oder Kran je nach Fall",
      "Unsere Arbeitsweise","Baumschonender Schnitt: nicht zu viel, nicht zu wenig",
      "Ein gekappter oder zu stark geschnittener Baum wird geschwächt, bildet brüchige Wasserreiser und wird gefährlicher als zuvor. Wir machen das Gegenteil.",
      [("Diagnose vor dem Schnitt","Baumart, Vitalität, mechanische Schwachstellen, Gegebenheiten vor Ort: jeder Eingriff beginnt mit dem Lesen des Baums."),
       ("Saubere Schnitte an der richtigen Stelle","Respekt vor Astkragen und Proportionen: der Baum verträgt diese Art von Schnitt besser."),
       ("Der passende Zugang für jeden Baum","Standardmässig Seilklettertechnik, um Ihren Garten zu schonen. Hebebühne, Kran oder andere Maschinen, wenn es die Situation verlangt, in Ausnahmefällen sogar Helikopter."),
       ("Sauber hinterlassener Arbeitsplatz","Äste gehäckselt oder abtransportiert, Gelände gereinigt. Sie müssen sich um nichts kümmern.")],
      "Gratis Besichtigung vereinbaren")
    p+=process(u,"Vier Schritte, vom ersten Kontakt bis zum sauberen Gelände",
      [("Sie kontaktieren uns","Über das Formular oder per E-Mail, gerne auf Deutsch. Ein paar Worte zu Ihrem Baum genügen."),
       ("Besichtigung und Diagnose","Wir schauen uns den Baum vor Ort an, hören Ihre Wünsche und beraten Sie, was zu tun ist, und was nicht."),
       ("Klare, kostenlose Offerte","Sie erhalten eine schriftliche, detaillierte Offerte auf Deutsch. Sie entscheiden frei."),
       ("Ausführung und Reinigung","Wir arbeiten am vereinbarten Termin, sichern den Bereich und hinterlassen Ihren Garten sauber.")])
    p+=gallery(u,"Unsere Einsätze",
      [("arboriste_grimpeur-3.jpg","Baumkletterer in der Spitze einer Zeder","Schnitt in der Höhe, Zugang per Seil"),
       ("grand_tilleul.jpg","Gesunde grosse Linde nach der Pflege","Eine gepflegte, ausgeglichene und vitale Linde"),
       ("arbre_porrentruy.jpg","Gartenbaum in Pruntrut","Gartenbaum, Pruntrut"),
       ("demontage_d-arbre_retention.jpg","Abtragen eines Baums mit Abseiltechnik","Abtragen mit Abseiltechnik auf engem Raum"),
       ("arboriste_grimpeur-15.jpg","Baumkletterer im Laub","Arbeit in der Krone, am Seil"),
       ("plantation_arbre.jpg","Junger Baum mit Dreibock-Pfahlung","Pflanzung mit Dreibock-Pfahlung")])
    p+=zone(u)
    p+=faq(u,[DE_NOTE_FAQ,
      ("Wann ist die beste Zeit, um einen Baum zu schneiden?","Das hängt von der Baumart und vom Ziel ab. Der Pflegeschnitt erfolgt oft im Winter bei frostfreiem Wetter oder im Sommer nach dem Austrieb. Manche Arten vertragen den Schnitt während des Saftaufstiegs schlecht. Bei der Besichtigung empfehlen wir Ihnen den günstigsten Zeitpunkt."),
      ("Was kostet ein Baumschnitt?","Der Preis hängt von der Grösse des Baums, seiner Zugänglichkeit, der Art des Eingriffs und dem Abtransport der Äste ab. Deshalb kommen wir kostenlos vorbei, um eine genaue, schriftliche Offerte zu erstellen. Für Sie unverbindlich."),
      ("Braucht es eine Bewilligung, um einen Baum zu schneiden oder zu fällen?","Ein einfacher Pflegeschnitt erfordert in der Regel keine Schritte. Eine Fällung oder ein Eingriff an einem geschützten Baum oder in einer besonderen Zone kann eine Bewilligung der Gemeinde erfordern. Wir sagen Ihnen, wie Sie in Ihrer Gemeinde vorgehen."),
      ("Mein Baum ist sehr gross oder schwer zugänglich. Geht das trotzdem?","Ja. Als Baumkletterer erreichen wir die Krone am Seil, was für die meisten Gärten, Innenhöfe und Hanglagen passt. Wenn nötig, setzen wir eine Hebebühne, einen Kran oder andere Maschinen ein, in sehr besonderen Fällen einen Helikopter."),
      ("Was passiert mit den geschnittenen Ästen?","Je nach Wunsch und Offerte werden die Äste vor Ort gehäckselt oder abtransportiert, oder das Holz wird für Ihre Heizung zugeschnitten belassen. Das Gelände wird vor unserer Abfahrt gereinigt."),
      ("Arbeiten Sie auch für Unternehmen und Gemeinden?","Ja. Wir unterstützen Unternehmen auf ihren Baustellen sowie Gemeinden bei der Betreuung von Baumgruppen, dem Umgang mit gefährlichen Bäumen und bei Pflanzprojekten.")])
    p+=cta(u,"grand_tilleul.jpg","Zweifel an einem Baum? Holen Sie die Meinung einer Fachperson ein.","Besichtigung und Offerte gratis und unverbindlich. Wir antworten Ihnen auf Deutsch innert 48 Arbeitsstunden.")
    write('de','taille',"Baumschnitt und Baumpflege – Baumkletterer Jura, Neuenburg, Bern | Arboritaille",
      "Baumschonender Schnitt und Baumpflege durch einen professionellen Baumkletterer. Gratis Offerte innert 48 Stunden im Jura, in Neuenburg und Bern. Beratung auf Deutsch per E-Mail.",p)

    # ---------- FÄLLUNG (abattage) ----------
    f=form(u,'abattage',"Gratis Offerte für die Fällung","Beschreiben Sie den Baum und seinen Standort. Wir beurteilen ihn vor Ort, unverbindlich.",
      "Neue Offertanfrage (DE) – Baumfällung / Abtragen",
      ["Fällung eines Baums","Abtragen eines Baums auf engem Raum","Gefährlicher Baum / Notfall nach Sturm","Toter oder kranker Baum","Stockfräsen","Mehrere Bäume zu fällen","Anderes"])
    p=hero(u,"demontage_arbre_porrentruy.jpg","55% 35%","Baumfällung und Abtragen · Jura · Neuenburg · Bern",
      "Baumfällung <em>in aller Sicherheit</em>, auch auf engem Raum",
      "Ein gefährlicher, toter, kranker oder dem Haus zu naher Baum? Ein professioneller Baumkletterer fällt ihn oder trägt ihn Stück für Stück ab, schont dabei Ihr Eigentum und hinterlässt das Gelände sauber.",
      ["Gratis Offerte, unverbindlich","Rascher Einsatz im Notfall","Klettern, Hebebühne, Kran oder Helikopter je nach Fall","Holz abtransportiert, Gelände gereinigt"],f)
    p+=trust([('SHIELD',"Baumkletterer","Abtragen am Seil, Abseiltechnik"),('WARN',"Sturmnotfälle","Rasche Sicherung"),('DOC',"Schriftliche, detaillierte Offerte","Gratis und unverbindlich")])
    p+=cards("Unsere Fällarbeiten","Die richtige Technik für jede Situation",
      "Ein freistehender Baum auf einer Wiese wird nicht wie eine Tanne direkt an einer Fassade gefällt. Wir wählen die Methode, die zu Ihrem Gelände, Ihren Gebäuden und Ihren Nachbarn passt.",
      [('AXE',"","Klassische Fällung","Wo der Platz es erlaubt, wird der Baum in einem Stück gefällt, mit kontrollierter Fallrichtung. Die schnellste und günstigste Lösung."),
       ('SCISS',"Am häufigsten","Stückweises Abtragen","Der Kletterer steigt in den Baum und trägt ihn Ast für Ast, dann Stammstück für Stammstück ab. Geeignet im Garten, nahe an Häusern oder Stromleitungen."),
       ('LINK',"Enger Raum","Abtragen mit Abseiltechnik","Jedes Stück wird angeseilt und mit einem Bremssystem sanft abgelassen. Nichts berührt unkontrolliert den Boden: Dächer, Gewächshäuser und Beete bleiben geschont."),
       ('CRANE',"","Hebebühne, Kran und Spezialmittel","Reicht das Klettern nicht aus, arbeiten wir mit Hebebühne oder lassen die Teile per Kran heben. In seltenen Fällen kann ein Helikopter eingesetzt werden. Wir organisieren die gesamte Logistik."),
       ('STUMP',"","Stockfräsen","Nach der Fällung wird der Wurzelstock unter das Bodenniveau gefräst. Sie können neu pflanzen, Rasen säen oder bauen, ohne Hindernis."),
       ('TREE',"","Abtransport und Verwertung des Holzes","Äste gehäckselt, Brennholz für Ihre Heizung oder abtransportiert. Das Gelände wird sauber übergeben, Sie entscheiden.")])
    p+=why("Wann muss ein Baum gefällt werden","Manche Bäume müssen gefällt werden. Wir beraten Sie von Fall zu Fall.",
      "Fällen ist nicht unsere erste Wahl: kann ein Schnitt oder eine Kronensicherung den Baum retten, schlagen wir Ihnen das vor. In gewissen Fällen ist die Fällung jedoch die einzige vernünftige Option.",
      [("Gefährlicher Baum","Gerissener Stamm, angehobene Wurzeln, Neigung zum Haus oder zur Strasse: das Risiko eines Umsturzes ist real, vor allem bei starkem Wind."),
       ("Toter oder kranker Baum","Pilze am Stammfuss, sich lösende Rinde, dürre Krone: ein absterbender Baum wird brüchig und unberechenbar."),
       ("Zu nahe an Gebäuden","Wurzeln, die Platten anheben, Äste auf dem Dach, dauerhafter Schatten: der Baum hat dort, wo er gewachsen ist, keinen Platz mehr."),
       ("Bauprojekt","Anbau, Pool, neue Zufahrt: wir räumen die Fläche sauber frei, Wurzelstock inklusive, bevor die Arbeiten beginnen.")])
    p+=approach(u,"demontage_d-arbre_retention.jpg","Abtragen eines Baums mit Abseiltechnik, Stammstück am Seil","Jedes Stück wird gehalten und kontrolliert",
      "Unsere Methode","Eine saubere Fällung ist zuerst eine gut vorbereitete Fällung",
      "Die Sicherheit von Personen und Eigentum hängt von der Vorbereitung ab. Jeder Einsatz wird geplant, bevor die Motorsäge läuft.",
      [("Besichtigung und Beurteilung vor Ort","Wir messen den Baum, erfassen Hindernisse, Zugänge und Ankerpunkte und wählen dann Technik und Mittel: Klettern, Hebebühne, Kran oder ausnahmsweise Helikopter."),
       ("Gesicherter Bereich während der Arbeiten","Abgesperrter Perimeter, Schutz empfindlicher Flächen, Absprache mit Ihnen und bei Bedarf mit den Nachbarn."),
       ("Kontrolliertes Ablassen der Teile","Beim Abtragen fällt nichts zufällig: jedes Stück wird bis zum Boden geführt oder gebremst."),
       ("Sauber übergebenes Gelände","Holz abtransportiert oder zugeschnitten, Äste gehäckselt, Sägemehl aufgenommen. Sie erhalten Ihren Garten zurück, ohne die Arbeit.")],
      "Gratis Beurteilung anfordern")
    p+=process(u,"Vier Schritte, vom ersten Kontakt bis zum sauberen Gelände",
      [("Sie kontaktieren uns","Beschreiben Sie den Baum in wenigen Worten, gerne auf Deutsch über das Formular. Bei akuter Gefahr rufen Sie uns direkt an (Französisch)."),
       ("Besichtigung und Diagnose","Wir beurteilen den Baum und sein Umfeld und beraten Sie zur Methode und zu einer allfälligen Bewilligung der Gemeinde."),
       ("Klare, kostenlose Offerte","Eine schriftliche Offerte auf Deutsch, mit oder ohne Stockfräsen und Holzabtransport."),
       ("Fällung und Reinigung","Einsatz am vereinbarten Termin, in aller Sicherheit. Das Gelände wird vor unserer Abfahrt gereinigt.")],eyebrow="Ablauf der Arbeiten")
    p+=gallery(u,"Unsere Fällungen und Abtragungen",
      [("demontage_arbre_porrentruy.jpg","Abtragen eines grossen Baums in Pruntrut","Stückweises Abtragen, Pruntrut"),
       ("abattage_arbre_porrentruy-6.jpg","Kran und Lastwagen bei einer Fällung","Kranhub im Siedlungsgebiet"),
       ("abattage_sequoia.jpg","Wurzelstock eines gefällten Mammutbaums","Fällung eines Mammutbaums"),
       ("abattage_arbre_porrentruy-3.jpg","Zugeschnittener Stamm nach der Fällung","Zugeschnittenes Holz, bereit zum Abtransport"),
       ("demontage_d-arbre_retention.jpg","Abtragen mit Abseiltechnik","Abseilen ohne Bodenkontakt"),
       ("arboriste_grimpeur-3.jpg","Baumkletterer in der Baumspitze","Zugang per Seil")])
    p+=zone(u)
    p+=faq(u,[DE_NOTE_FAQ,
      ("Braucht es eine Bewilligung, um einen Baum zu fällen?","In vielen Gemeinden im Jura, in Neuenburg und Bern kann die Fällung eines Baums bewilligungspflichtig sein, je nach Art, Grösse oder Standort (Schutzzone, Allee, markanter Baum). Wir erklären Ihnen das Vorgehen bei Ihrer Gemeinde und können die nötigen technischen Angaben liefern."),
      ("Was kostet eine Baumfällung?","Der Preis hängt von Höhe und Durchmesser des Baums, seiner Zugänglichkeit, der nötigen Technik (direkte Fällung, Abtragen, Abseilen, Kran) und dem Holzabtransport ab. Ein Abtragen auf engem Raum braucht mehr Zeit als eine Fällung im offenen Feld. Nach der Besichtigung erstellen wir eine genaue, kostenlose Offerte."),
      ("Können Sie einen Baum direkt an meinem Haus fällen?","Ja, genau das ist der Kern unseres Berufs. Durch Abtragen am Seil und Abseiltechnik wird jedes Stück kontrolliert abgelassen, ohne Dach, Fassade oder Umgebung zu berühren."),
      ("Muss mein Baum wirklich gefällt werden?","Nicht unbedingt. Bei der Besichtigung prüfen wir den Baum sorgfältig. Reicht ein Sicherheitsschnitt, eine Entlastung oder eine Kronensicherung, um ihn ohne Risiko zu erhalten, schlagen wir Ihnen das zuerst vor."),
      ("Was machen Sie mit dem Holz und dem Wurzelstock?","Je nach Offerte wird das Holz als Brennholz für Ihre Heizung zugeschnitten, gehäckselt oder abtransportiert. Der Wurzelstock kann belassen, bodeneben abgesägt oder gefräst werden, damit Sie neu pflanzen oder Rasen ansäen können."),
      ("Kommen Sie nach einem Sturm im Notfall?","Ja. Ein Baum auf dem Dach, ein gebrochener Ast, der abzustürzen droht, oder ein entwurzelter Baum: kontaktieren Sie uns, wir sichern die Lage so rasch wie möglich. Bei akuter Gefahr rufen Sie bitte direkt an (auf Französisch).")])
    p+=cta(u,"abattage_arbre_porrentruy-6.jpg","Ein Baum macht Ihnen Sorgen? Lassen Sie ihn gratis beurteilen.","Besichtigung und Offerte gratis und unverbindlich. Antwort auf Deutsch per E-Mail, bei akuter Gefahr telefonisch auf Französisch.")
    write('de','abattage',"Baumfällung und Abtragen – Baumkletterer Jura, Neuenburg, Bern | Arboritaille",
      "Baumfällung, Abtragen und Stockfräsen durch einen professionellen Baumkletterer. Sicherer Einsatz, auch nahe an Gebäuden. Gratis Offerte im Jura, in Neuenburg und Bern. Beratung auf Deutsch per E-Mail.",p)

    # ---------- INDEX ----------
    f=form(u,'index',"Ihre gratis Offerte","Sagen Sie uns, was Ihr Baum braucht. Wir melden uns schriftlich, um einen Besichtigungstermin zu vereinbaren.",
      "Neue Offertanfrage (DE) – Arboritaille",
      ["Baumschnitt und Baumpflege","Fällung oder Abtragen","Diagnose / Gutachten","Pflanzung","Kronensicherung","Stockfräsen","Ich weiss es noch nicht, ich brauche eine Beratung"])
    p=hero(u,"arboriste_grimpeur-19.jpg","62% 30%","Baumkletterer · Jura · Neuenburg · Bern",
      "Ihr Baumkletterer <em>für alle Baumarbeiten</em>",
      "Schnitt, Pflege, Fällung, Abtragen, Diagnose, Pflanzung: Arboritaille kümmert sich um Ihre Bäume mit Seilklettertechnik, den passenden Mitteln für jede Situation und Respekt vor dem Lebendigen. Für Privatpersonen, Unternehmen und Gemeinden.",
      ["Gratis Offerte, unverbindlich","Antwort innert 48 Arbeitsstunden","Eine Ansprechperson, von der Beratung bis zur Ausführung","Sauberer Arbeitsplatz, Äste abtransportiert"],f)
    p+=trust([('SHIELD',"Baumkletterer","Seilklettertechnik"),('LEAF',"Respekt vor dem Baum","Baumschonender Schnitt, individuelle Beratung"),('DOC',"Schriftliche, detaillierte Offerte","Gratis und unverbindlich")])
    p+=cards("Unsere Leistungen","Alles, was ein Baum braucht, von der Pflanzung bis zur Fällung",
      "Eine Fachperson für das ganze Leben Ihrer Bäume. Wir empfehlen Ihnen den richtigen Eingriff zum richtigen Zeitpunkt.",
      [('SCISS',"Am häufigsten","Baumschnitt und Baumpflege","Pflegeschnitt, Kroneneinkürzung oder Kronenaufastung, Totholzentfernung. Ein baumschonender Schnitt, der Form und Gesundheit des Baums respektiert. <a href=\"baumpflege.html\">Mehr erfahren</a>"),
       ('AXE',"","Fällung und Abtragen","Klassische Fällung, Abtragen am Seil oder mit Abseiltechnik auf engem Raum, Kranhub. Auch nahe an Gebäuden. <a href=\"faellung.html\">Mehr erfahren</a>"),
       ('SEARCH',"","Diagnose und Gutachten","Beurteilung von Vitalität, mechanischen Schwachstellen und Krankheiten. Eine klare Einschätzung als Entscheidungsgrundlage: erhalten, pflegen oder fällen."),
       ('SPROUT',"","Pflanzung","Wahl der zum Standort passenden Baumart, fachgerechte Pflanzung und Dreibock-Pfahlung für ein gutes Anwachsen."),
       ('LINK',"","Kronensicherung","Sicherung einer schwachen Zwiesel oder eines Starkastes mit dynamischer oder statischer Kronensicherung, um den Baum sicher zu erhalten."),
       ('STUMP',"","Stockfräsen","Entfernen von Wurzelstöcken unter das Bodenniveau, um ohne Hindernis neu zu pflanzen, Rasen anzusäen oder zu bauen.")])
    p+=why("Für wen","Privatpersonen, Unternehmen, Gemeinden: dieselbe Sorgfalt, angepasst an Ihre Anliegen",
      "Ob Sie einen Baum im Garten oder einen ganzen Baumbestand zu betreuen haben, das Bedürfnis ist dasselbe: eine Fachperson, die Sie nach Ihrer Situation berät.",
      [("Privatpersonen","Pflege Ihrer Gartenbäume, Sicherung, Fällung eines störenden Baums. Gratis Offerte und individuelle Beratung."),
       ("Unternehmen","Ein Baum behindert Ihre Baustelle oder braucht Pflege? Wir beurteilen rasch und handeln so bald wie möglich."),
       ("Gemeinden","Betreuung von Baumgruppen, Umgang mit gefährlichen Bäumen, Pflanzprojekte. Ein Partner für die kommunale Baumpflege."),
       ("Liegenschaftsverwaltungen","Regelmässige Pflege des Baumbestands Ihrer Liegenschaften, mit einer Ansprechperson und klaren Offerten.")])
    p+=approach(u,"arboriste_grimpeur-2.jpg","Baumkletterer in der Krone eines grossen Baums","Klettern, Hebebühne oder Kran je nach Fall",
      "Unsere Arbeitsweise","Leidenschaft für den Beruf, Respekt vor dem Lebendigen",
      "Jeder Baum ist ein Einzelfall. Bevor wir eingreifen, nehmen wir uns Zeit, ihn zu verstehen: seine Art, seine Vitalität, sein Umfeld und Ihre Erwartungen.",
      [("Individuelle Beratung","Das Ziel ist, Bäume zu verschönern und zu erhalten. Jede Situation ist anders, manchmal ist eine Fällung nötig. Wir sind da, um Sie zu beraten."),
       ("Die passenden Mittel für jeden Baum","Standardmässig Seilklettertechnik, um Ihren Garten zu schonen. Hebebühne, Kran oder andere Maschinen, wenn es die Situation verlangt, in Ausnahmefällen Helikopter."),
       ("Saubere, überlegte Schnitte","Baumschonender Schnitt und Respekt vor der Physiologie des Baums für ein dauerhaftes Ergebnis."),
       ("Sauber hinterlassener Arbeitsplatz","Äste gehäckselt oder abtransportiert, Holz auf Wunsch zugeschnitten, Gelände gereinigt.")],
      "Gratis Offerte anfordern")
    p+=process(u,"Vier Schritte, vom ersten Kontakt bis zum sauberen Gelände",
      [("Sie kontaktieren uns","Über das Formular oder per E-Mail, gerne auf Deutsch. Ein paar Worte zu Ihrem Baum genügen."),
       ("Besichtigung und Diagnose","Wir schauen uns den Baum an, hören Ihre Wünsche und empfehlen den richtigen Eingriff."),
       ("Klare, kostenlose Offerte","Eine schriftliche, detaillierte Offerte auf Deutsch. Sie entscheiden frei."),
       ("Ausführung und Reinigung","Wir arbeiten am vereinbarten Termin und hinterlassen Ihr Gelände sauber.")])
    p+=gallery(u,"Unsere Einsätze",
      [("arboriste_grimpeur-3.jpg","Baumkletterer in der Spitze einer Zeder","Schnitt in der Höhe, Zugang per Seil"),
       ("grand_tilleul.jpg","Gesunde grosse Linde nach der Pflege","Eine gepflegte, ausgeglichene und vitale Linde"),
       ("demontage_arbre_porrentruy.jpg","Abtragen eines grossen Baums in Pruntrut","Stückweises Abtragen, Pruntrut"),
       ("demontage_d-arbre_retention.jpg","Abtragen mit Abseiltechnik","Abseilen auf engem Raum"),
       ("plantation_arbre.jpg","Junger Baum mit Dreibock-Pfahlung","Pflanzung mit Dreibock-Pfahlung"),
       ("abattage_arbre_porrentruy-6.jpg","Kran bei einer Fällung","Kranhub im Siedlungsgebiet")])
    p+=zone(u)
    p+=faq(u,[DE_NOTE_FAQ,
      ("Woran erkenne ich, dass mein Baum einen Eingriff braucht?","Totholz in der Krone, Äste, die ein Dach berühren, Pilze am Stammfuss, ein geneigter oder gerissener Stamm, schütteres Laub: Zeichen, die man nicht ignorieren sollte. Eine kostenlose Besichtigung schafft Klarheit."),
      ("Was kosten Ihre Leistungen?","Jeder Baum ist anders: Höhe, Art, Zugang, Art des Eingriffs und Holzabtransport beeinflussen den Preis. Deshalb kommen wir kostenlos vorbei, um eine schriftliche, genaue Offerte zu erstellen."),
      ("Braucht es eine Bewilligung, um einen Baum zu schneiden oder zu fällen?","Ein Pflegeschnitt erfordert in der Regel keine Schritte. Eine Fällung oder ein Eingriff an einem geschützten Baum kann eine Bewilligung der Gemeinde erfordern. Wir begleiten Sie beim Vorgehen."),
      ("Mein Baum ist schwer zugänglich. Ist das ein Problem?","Nein. Wir arbeiten in Seilklettertechnik, womit wir eingezäunte Gärten, Hanglagen und Innenhöfe erreichen. Wenn nötig, setzen wir eine Hebebühne, einen Kran oder andere Maschinen ein, in sehr besonderen Fällen einen Helikopter."),
      ("In welchem Gebiet sind Sie tätig?","Im ganzen Kanton Jura, im Kanton Neuenburg und in Bern."),
      ("Arbeiten Sie mit Unternehmen und Gemeinden?","Ja. Wir unterstützen Unternehmen auf ihren Baustellen und Gemeinden bei der Betreuung ihres Baumbestands: Kontrolle, Sicherheit, Pflanzungen.")])
    p+=cta(u,"grand_tilleul.jpg","Zweifel an einem Baum? Holen Sie die Meinung einer Fachperson ein.","Besichtigung und Offerte gratis und unverbindlich. Wir antworten Ihnen auf Deutsch innert 48 Arbeitsstunden.")
    write('de','index',"Baumkletterer Jura, Neuenburg, Bern – Baumschnitt, Fällung, Baumpflege | Arboritaille",
      "Arboritaille, Baumkletterer in Courgenay: Baumschnitt, Baumpflege, Fällung, Abtragen, Diagnose und Pflanzung. Gratis Offerte im Jura, in Neuenburg und Bern. Beratung auf Deutsch per E-Mail.",p)
    merci('de')

build_fr(); build_de()
print("built FR + DE")
