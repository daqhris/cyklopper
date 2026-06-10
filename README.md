# Cyklopper.be — Code source

Site web de l'atelier vélo participatif **Cyklopper**, situé à Zonneklopper (Forest, Bruxelles).

> Atelier de réparation vélo participatif ouvert tous les **jeudis de 16h à 20h**  
> 23 avenue de la Verrerie, 1190 Forest, Belgique  
> [cyklopper.be](https://cyklopper.be) · [Facebook](https://www.facebook.com/atelierCyklopper/) · [Instagram](https://www.instagram.com/cyklopper/)

---

## Structure du dépôt

```
cyklopper/
├── index.html              — Page d'accueil principale
├── sitemap.xml             — Sitemap pour les moteurs de recherche
├── llms.txt                — Métadonnées pour les agents IA
├── robots.txt
├── CNAME                   — Domaine personnalisé GitHub Pages
├── .htaccess               — Redirection HTTPS (hébergement OVH)
├── .ovhconfig              — Configuration serveur OVH
├── LICENSE                 — EUPL-1.2
├── images/                 — Images évènementielles 
├── images-bd/              — Illustrations vectorielles SVG du site
├── static/
│   ├── css/
│   │   ├── main.css        — Feuille de style principale
│   │   └── reset.css       — Reset CSS Meyer
│   ├── fonts/
│   │   └── hanken/         — Police Hanken (Book, Light, Bold)
│   └── images/             — Icônes et logo
├── cosmik-2025/            — Archive 1ère édition du Cosmik Bike Festival
│   ├── index.html          — Page d'accueil + galerie photos
│   └── photos/             — Photos de l'édition 2025
└── cosmik-2026/            — 2ème édition du Cosmik Bike Festival
    ├── index.html          — Page d'accueil + compte à rebours
    ├── poster.jpg          — Affiche officielle 2026
    └── photos/             — Photos de l'édition 2026 (à venir)
```

---

## Auteur·es

Ce site a été conçu et développé par :

- **Antoine Gelgon** — création du site, design graphique, identité visuelle, illustrations  
  [antoine-gelgon.fr](https://antoine-gelgon.fr/)

- **Chris-Armel Iradukunda (daqhris)** — développement web, maintenance du site, open-sourcing  
  [daqhris.com](https://daqhris.com/)

Avec l'assistance au code de **Claude Sonnet 4.6** (Anthropic).

---

## Droits et licences

### Code source

Le code source de ce site (HTML, CSS, JavaScript) est publié sous licence **EUPL-1.2** (European Union Public Licence v1.2).  
Voir le fichier [`LICENSE`](./LICENSE) pour le texte complet.

Vous êtes libre de réutiliser, modifier et redistribuer le code sous les termes de cette licence, à condition de conserver les mentions d'attribution et de redistribuer sous la même licence ou une licence compatible.

### Illustrations et dessins

Les illustrations vectorielles (`images-bd/`) sont des œuvres originales protégées par le droit d'auteur.  
**© Antoine Gelgon — Tous droits réservés.**  
Toute reproduction sans autorisation explicite est interdite.

### Photographies

Les photographies du Cosmik Bike Festival (`cosmik-2025/photos/`, `images/`) sont des œuvres protégées par le droit d'auteur.  
**© Leurs auteur·es respectif·ves — Tous droits réservés.**  
Toute reproduction sans autorisation explicite est interdite.

### Police de caractères

La police **Hanken** est utilisée conformément à sa licence d'origine.

---

## Développement local

Ce site est entièrement statique (HTML/CSS/JS pur). Aucune dépendance, aucun build requis.

```bash
# Cloner le dépôt
git clone https://github.com/daqhris/cyklopper.git
cd cyklopper

# Ouvrir directement dans un navigateur
open index.html

# Ou lancer un serveur local (recommandé pour éviter les problèmes CORS sur les polices)
python3 -m http.server 8000
# puis ouvrir http://localhost:8000
```

> **Note :** Le serveur local est recommandé car les polices `@font-face` locales peuvent être bloquées par les navigateurs en mode `file://` selon les paramètres de sécurité.

---

## Déploiement

Le site est hébergé sur **OVH** avec déploiement automatique via **GitHub Actions** à chaque push sur la branche `main`.

La redirection HTTP → HTTPS est gérée par `.htaccess`. La configuration serveur OVH (PHP 7.4, environnement stable64) est dans `.ovhconfig`.

---

## Cosmik Bike Festival

Festival annuel du vélo organisé à Zonneklopper, Forest (Bruxelles).

| Édition | Date | Statut |
|---------|------|--------|
| [1ère édition 2025](https://cyklopper.be/cosmik-2025/) | 30–31 mai & 1er juin 2025 | ✅ Terminée |
| [2ème édition 2026](https://cyklopper.be/cosmik-2026/) | 4–5 juillet 2026 | 🔜 À venir |

Pour participer en tant que bénévole ou proposer un projet vélo pour 2026 :  
👉 [Formulaire d'inscription bénévoles](https://lite.framacalc.org/3nnifnwayr-aliy)

---

## Contact

**Atelier Cyklopper**  
📧 [ateliercyklopper@protonmail.com](mailto:ateliercyklopper@protonmail.com)  
📘 [Facebook](https://www.facebook.com/atelierCyklopper/)  
📷 [Instagram](https://www.instagram.com/cyklopper/)
