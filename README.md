# Arboritaille – Landing pages Google Ads

Pages d'atterrissage statiques pour les campagnes Google Ads d'Arboritaille (arboriste-grimpeur, Jura / Neuchâtel / Berne).

- `index.html` – LP généraliste (tous les services)
- `taille.html` – LP « Taille et entretien d'arbres »
- `abattage.html` – LP « Abattage et démontage »
- `de/index.html`, `de/baumpflege.html`, `de/faellung.html`, `de/danke.html` – versions en allemand (Suisse), sélecteur de langue dans l'en-tête
- `merci.html` – page de remerciement (à utiliser comme conversion Google Ads)
- `style.css` – styles communs
- `build.py` – génère toutes les pages FR et DE (ne pas éditer les .html à la main, modifier `build.py` puis lancer `python3 build.py`)
- `img/` – photos et logos repris du site arboritaille.ch

Déploiement : chaque push sur `main` est synchronisé automatiquement vers Hostinger (page.arboritaille.ch) par GitHub Actions via SSH/rsync.

Le formulaire est traité par `contact.php` sur Hostinger : e-mail à contact@arboritaille.ch (copie aymeric@cleanibat.fr), sauvegarde de chaque lead dans `~/leads_arboritaille.csv` hors docroot, puis redirection vers la page merci.
