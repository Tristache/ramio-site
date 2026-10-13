---
title: "Rami voleur : règles, joker, nombre de cartes"
mesure: true
description: >-
  Règles du rami voleur (ou rami chinois) : combien de cartes à 2, 3 ou 4,
  pas de défausse, tierce franche, joker. Cas concrets et questions
  fréquentes.
---

<style>
/* Cartes en texte, affichage simplifié en quatre couleurs (pique noir,
   cœur rouge, carreau bleu, trèfle vert). Fond et encre fixés ici : la
   carte reste lisible sur fond clair comme sur fond sombre. */
.k { display: inline-block; min-width: 1.6em; padding: 0 .3em; margin: 1px 0;
  border: 1px solid #8A93A3; border-radius: 5px; background: #fff; color: #111;
  font-weight: 700; line-height: 1.5; text-align: center; white-space: nowrap;
  font-variant-emoji: text; }
.k.kc { color: #C8102E; }
.k.kd { color: #0B5FB3; }
.k.kt { color: #1B7A33; }
.k.kj { border-style: dashed; }
</style>

# Les règles du rami voleur

Le rami voleur — aussi appelé **rami chinois** — est un jeu de cartes de
la famille du rami, qui se joue de
**2 à 4 joueurs** avec **deux jeux de 52 cartes** (et, au choix, 2 jokers).
Sa grande particularité : **on ne se défausse jamais**, et une fois sa
première pose faite, chacun peut **réorganiser librement toute la table**
pour caser ses cartes — comme au Rummikub, mais avec de vraies cartes.

Cette page décrit la règle telle qu'elle est jouée dans [Ramio](./),
application gratuite pour Android et iPhone. Le jeu est traditionnel et se
transmet de table en table : là où l'usage courant diffère, c'est signalé
au fil du texte. Vous pouvez aussi y jouer avec deux jeux de cartes
classiques : tout ce qu'il faut savoir est sur cette page.

L'essentiel, en cinq lignes :

- **13 cartes** par joueur, à 2, 3 ou 4 ;
- à son tour, on **pioche une carte**, puis on pose si on veut : **pas de
  défausse** ;
- pour poser la première fois, il faut une **tierce franche** (trois
  cartes qui se suivent, même couleur, sans joker) ;
- ensuite, **toute la table se recompose**, poses des adversaires
  comprises ;
- le premier qui **vide sa main** gagne la manche.

Pour voir tout cela joué carte après carte : [Rami voleur : la règle en
2 minutes](https://www.youtube.com/watch?v=5oETEAFIu_s) (vidéo, 2 min 13).

## Combien de cartes au rami voleur ?

Le matériel :

- **Deux jeux de 52 cartes** mélangés ensemble, soit 104 cartes.
- En option, **2 jokers** (106 cartes). Le jeu est plus tactique sans
  jokers, plus spectaculaire avec.
- De quoi noter les points si vous jouez une partie en plusieurs manches.

Chaque joueur reçoit **13 cartes**, quel que soit le nombre de joueurs.
Seule la pioche change :

| Joueurs | Cartes par joueur | Pioche au départ, sans joker | Pioche au départ, avec 2 jokers |
|---|---|---|---|
| 2 | 13 | 78 | 80 |
| 3 | 13 | 65 | 67 |
| 4 | 13 | 52 | 54 |

À table, on voit aussi des donnes plus courtes, de 10 ou 11 cartes. Dans
Ramio, la donne est de 13 cartes ; en salon privé, elle se règle de 7 à
15 cartes.

## Le but du jeu

Être le premier à **vider entièrement sa main** en posant ses cartes sur la
table, sous forme de combinaisons valides.

Les combinaisons admises :

- **La suite** : au moins trois cartes qui se suivent, de la même couleur
  (7-8-9 de cœur, par exemple). L'As peut se placer avant le 2 (As-2-3) ou
  après le Roi (Dame-Roi-As), mais la suite ne « tourne » jamais :
  Roi-As-2 est interdit.
- **Le brelan** (trois cartes) ou **le carré** (quatre cartes) de même
  valeur, de couleurs **toutes différentes** : deux 9 de pique dans le même
  brelan, c'est interdit.

En cartes (V = Valet, D = Dame, R = Roi) :

- une suite : <span class="k kc">7♥&#xFE0E;</span> <span class="k kc">8♥&#xFE0E;</span> <span class="k kc">9♥&#xFE0E;</span>
- un brelan : <span class="k">9♠&#xFE0E;</span> <span class="k kc">9♥&#xFE0E;</span> <span class="k kd">9♦&#xFE0E;</span>
- un carré : <span class="k">R♠&#xFE0E;</span> <span class="k kc">R♥&#xFE0E;</span> <span class="k kd">R♦&#xFE0E;</span> <span class="k kt">R♣&#xFE0E;</span>

## La donne

Chaque joueur reçoit **13 cartes**. Le reste forme la **pioche** (le
« sabot »), face cachée au centre. On ne retourne aucune carte : il n'y a
**pas de défausse** au rami chinois. Le premier joueur de la première
manche est tiré au sort ; ensuite, la main tourne à chaque manche.

## Le tour de jeu : y a-t-il une défausse ?

À son tour, un joueur :

1. **Pioche une carte** au sabot — c'est obligatoire, à chaque tour, même
   si l'on s'apprête à poser.
2. **Pose des combinaisons s'il le veut** (et s'il le peut). Poser est
   toujours facultatif : on peut piocher et passer.

Et c'est tout : **on ne se défausse jamais**. La main ne diminue qu'en
posant. C'est ce qui donne au jeu son tempo particulier : chaque tour sans
pose fait grossir la main — et les pénalités potentielles.

À table, on voit aussi des règles qui gardent une défausse en fin de
tour. Ce n'est pas le cas dans Ramio.

### La première pose : la tierce franche

Pour avoir le droit de poser, il faut ouvrir avec au moins une **tierce
franche** : trois cartes qui se suivent, de la même couleur, **sans
joker**. Pas de minimum de points (contrairement aux 51 points du rami
classique) : la tierce franche est la seule porte d'entrée. On peut poser
d'autres combinaisons dans le même tour, la tierce franche en fait partie.

Par exemple, <span class="k kt">4♣&#xFE0E;</span> <span class="k kt">5♣&#xFE0E;</span> <span class="k kt">6♣&#xFE0E;</span>
ouvre le jeu ; <span class="k kt">4♣&#xFE0E;</span> <span class="k kj">Joker</span> <span class="k kt">6♣&#xFE0E;</span>
ne l'ouvre pas, pas plus qu'un brelan. À table, on voit aussi une
ouverture à 30 ou 40 points.

### La réorganisation de la table

Une fois sa première pose faite, un joueur peut, pendant son tour,
**réorganiser librement toute la table** : déplacer des cartes d'une
combinaison à l'autre, découper une longue suite, emprunter le 4e cœur
d'un carré pour allonger sa suite… y compris dans les poses de ses
adversaires. Une seule contrainte : à la fin du tour, **toute la table doit
être valide** — chaque combinaison doit être une suite, un brelan ou un
carré corrects. Si ce n'est pas le cas, tout revient en place.

C'est le cœur du rami chinois : bien jouer, ce n'est pas seulement poser
ses cartes, c'est voir les recompositions que personne d'autre n'a vues.

Trois recompositions courantes :

- **Emprunter la quatrième carte d'un carré.**
  Sur la table : <span class="k">8♠&#xFE0E;</span> <span class="k kc">8♥&#xFE0E;</span> <span class="k kd">8♦&#xFE0E;</span> <span class="k kt">8♣&#xFE0E;</span>.
  En main : <span class="k kc">6♥&#xFE0E;</span> <span class="k kc">7♥&#xFE0E;</span>.
  Après le tour : <span class="k kc">6♥&#xFE0E;</span> <span class="k kc">7♥&#xFE0E;</span> <span class="k kc">8♥&#xFE0E;</span>
  et <span class="k">8♠&#xFE0E;</span> <span class="k kd">8♦&#xFE0E;</span> <span class="k kt">8♣&#xFE0E;</span>.
- **Couper une longue suite.**
  Sur la table : <span class="k kt">3♣&#xFE0E;</span> <span class="k kt">4♣&#xFE0E;</span> <span class="k kt">5♣&#xFE0E;</span> <span class="k kt">6♣&#xFE0E;</span> <span class="k kt">7♣&#xFE0E;</span>.
  En main : le second <span class="k kt">5♣&#xFE0E;</span> (on joue avec deux jeux).
  Après le tour : <span class="k kt">3♣&#xFE0E;</span> <span class="k kt">4♣&#xFE0E;</span> <span class="k kt">5♣&#xFE0E;</span>
  et <span class="k kt">5♣&#xFE0E;</span> <span class="k kt">6♣&#xFE0E;</span> <span class="k kt">7♣&#xFE0E;</span>.
- **Prendre le bout d'une suite.**
  Sur la table : <span class="k kd">9♦&#xFE0E;</span> <span class="k kd">10♦&#xFE0E;</span> <span class="k kd">V♦&#xFE0E;</span> <span class="k kd">D♦&#xFE0E;</span>.
  En main : <span class="k">D♠&#xFE0E;</span> <span class="k kc">D♥&#xFE0E;</span>.
  Après le tour : <span class="k kd">9♦&#xFE0E;</span> <span class="k kd">10♦&#xFE0E;</span> <span class="k kd">V♦&#xFE0E;</span>
  et <span class="k">D♠&#xFE0E;</span> <span class="k kc">D♥&#xFE0E;</span> <span class="k kd">D♦&#xFE0E;</span>.

Dans les trois cas, une carte au moins vient de la main : on ne recompose
pas la table sans rien y ajouter. Et une carte posée ne revient jamais en
main.

## Le joker au rami voleur : quatre cas concrets

La règle, d'abord :

- Le joker **remplace n'importe quelle carte**, dans une suite comme dans
  un brelan.
- Une combinaison peut contenir **plusieurs jokers**, tant qu'il lui reste
  au moins une vraie carte.
- Un joker posé sur la table peut être **déplacé et réutilisé** lors des
  réorganisations, à volonté — mais il **reste sur la table** : on ne le
  reprend jamais en main, même en apportant la carte qu'il remplace.

C'est le point sur lequel les tables divergent le plus. Voici ce que
Ramio applique, et ce que l'on voit ailleurs.

### 1. Vous avez la carte que le joker remplace

Sur la table : <span class="k kc">5♥&#xFE0E;</span> <span class="k kj">Joker</span> <span class="k kc">7♥&#xFE0E;</span>.
En main : <span class="k kc">6♥&#xFE0E;</span>.

Vous posez votre 6 à sa place. Le joker est libéré, mais il reste sur la
table : il glisse au bout de la suite,
<span class="k kc">5♥&#xFE0E;</span> <span class="k kc">6♥&#xFE0E;</span> <span class="k kc">7♥&#xFE0E;</span> <span class="k kj">Joker</span>
(il vaut alors le 8 de cœur), ou il part dans une autre combinaison
pendant le même tour.

À table, on voit aussi le joueur reprendre le joker en main contre la
carte qu'il remplace.

### 2. Le joker est dans un brelan

Sur la table : <span class="k">9♠&#xFE0E;</span> <span class="k kc">9♥&#xFE0E;</span> <span class="k kj">Joker</span>.
En main : <span class="k kd">9♦&#xFE0E;</span>.

Vous ajoutez votre 9 : le brelan devient un carré,
<span class="k">9♠&#xFE0E;</span> <span class="k kc">9♥&#xFE0E;</span> <span class="k kd">9♦&#xFE0E;</span> <span class="k kj">Joker</span>,
où le joker tient la place du 9 de trèfle. Vous pouvez aussi l'emmener
ailleurs, puisque les trois 9 tiennent seuls. Si quelqu'un apporte plus
tard le 9 de trèfle, le joker doit partir dans une autre combinaison : un
carré ne compte jamais plus de quatre cartes.

À table, on voit aussi une règle plus stricte : le joker d'un brelan ne se
libère qu'en apportant les deux cartes manquantes.

### 3. Vous déplacez un joker pour poser vos cartes

Sur la table : <span class="k">3♠&#xFE0E;</span> <span class="k">4♠&#xFE0E;</span> <span class="k">5♠&#xFE0E;</span> <span class="k kj">Joker</span>.
En main : <span class="k kd">D♦&#xFE0E;</span> <span class="k kd">R♦&#xFE0E;</span>.

La suite de pique tient sans son joker. Vous le prenez et vous posez
<span class="k kd">D♦&#xFE0E;</span> <span class="k kd">R♦&#xFE0E;</span> <span class="k kj">Joker</span> :
il vaut maintenant l'As ou le Valet de carreau. Aucune condition, sinon celles de
toute réorganisation : avoir déjà fait sa première pose, jouer au moins
une carte de sa main, laisser toute la table valide.

### 4. Deux jokers ensemble, et le joker gardé en main

La suite <span class="k kt">7♣&#xFE0E;</span> <span class="k kj">Joker</span> <span class="k kj">Joker</span>
est valide : il suffit d'une vraie carte. À table, on voit
aussi la limite d'un seul joker par combinaison.

Un joker encore en main à la fin de la manche coûte **50 points**, plus
que toute autre carte : mieux vaut le poser tôt. Selon les tables, on voit
aussi 15 à 25 points.

Dernier point : le joker ne compte pas dans la tierce franche de la
première pose. Une fois vos trois cartes franches réunies, rien n'empêche
de prolonger la suite avec un joker dans le même tour.

## Le rami voleur à deux joueurs

Le rami voleur se joue très bien à deux, avec la même règle qu'à trois ou
quatre : **13 cartes chacun**, la pioche obligatoire, la tierce franche
pour ouvrir, la table à recomposer.

Ce qui change, ce sont les proportions :

- 26 cartes sont distribuées, et la pioche en compte **78** (80 avec les
  jokers) : chacun peut piocher 39 fois avant qu'elle ne s'épuise ;
- la table se garnit moins vite, puisque deux mains seulement
  l'alimentent ;
- toute carte posée vient de votre unique adversaire, et tout ce que
  vous posez lui sert au tour suivant.

Le décompte est le même : partie à 100 points, ou partie simple en une
manche. Dans Ramio, on joue à deux en salon privé avec un ami, ou contre
l'ordinateur.

## La fin de manche et les points

La manche s'arrête dès qu'un joueur a **posé sa dernière carte**. Les
autres comptent alors les **pénalités** des cartes qui leur restent en
main :

| Cartes | Pénalité |
|---|---|
| 2 à 10 | valeur de la carte |
| Valet, Dame, Roi | 10 |
| As | 11 |
| Joker | 50 |

**Si la pioche s'épuise** avant qu'un joueur ait fini, la manche s'arrête
sans gagnant et **chaque joueur compte les pénalités de sa main** : celui
qui a bien posé est récompensé, celui qui a tout gardé paie.

## La partie

Les pénalités s'additionnent de manche en manche. La partie se termine dès
qu'un joueur atteint **100 points** : le joueur le **moins pénalisé**
gagne la partie.

Variante rapide, la **partie simple** : une seule manche, le premier à
vider sa main gagne. Si la pioche s'épuise, on rejoue la manche.

Dans Ramio, les parties publiques se jouent avec les jokers, en partie
simple, avec 120 secondes par tour. En salon privé, jokers, partie à
points ou partie simple se choisissent à la création.

## Rami voleur, rami classique, Rummikub : les différences

**Face au rami classique** (celui de la défausse et des 51 points) :

- pas de défausse — on pioche, on pose, c'est tout ;
- pas de seuil de 51 points — la tierce franche suffit pour ouvrir ;
- la table est **commune et recomposable** : on joue autant avec les
  cartes des autres qu'avec les siennes.

**Face au Rummikub** (qui appartient à la même famille) :

- des cartes au lieu de tuiles, avec les couleurs et figures classiques ;
- l'ouverture se fait à la tierce franche, pas à 30 points ;
- le joker resté sur la table est réutilisable sans condition ;
- un vrai décompte de pénalités (figures 10, As 11, joker 50), qui fait de
  chaque carte gardée un risque.

Les amateurs de jeux de cartes reconnaîtront la famille des ramis « de
manipulation » (Manipulation Rummy), dont font aussi partie le Machiavelli
italien et le Vatikan. Le rami chinois en est la variante française : 13
cartes, tierce franche, jokers à 50 points. Quant au nom ? Le rami descend
historiquement du khanhoo, un jeu chinois du XIIe siècle — la boucle est
bouclée.

## Rami chinois ou rami voleur ?

Deux noms, un seul jeu. Ce jeu est aussi largement connu sous le nom de
**rami voleur** — parce qu'on y « vole » les cartes déjà posées par ses
adversaires : emprunter le 4e cœur d'un carré, découper la suite du
voisin pour y caser les siennes, c'est tout le sel du jeu. Selon les
familles et les régions on dira rami voleur, rami chinois, ou simplement
« notre rami » ; les règles de cette page valent pour tous. Ramio est
donc aussi l'application du rami voleur.

## La règle du rami voleur en vidéo

[Rami voleur : la règle en 2 minutes](https://www.youtube.com/watch?v=5oETEAFIu_s)
(YouTube, chaîne Quintain Games, 2 min 13) montre la règle de Ramio,
chaque coup étant joué dans l'application : le but, les
combinaisons, le tour, la première pose, la table à défaire,
[le joker](https://www.youtube.com/watch?v=5oETEAFIu_s&t=91s) et la fin de
manche.

## Le même jeu dans d'autres pays

Le rami voleur porte d'autres noms ailleurs : en Allemagne, <a href="https://quintaingames.com/ramio/raeuber-romme/">Räuber-Rommé</a> ;
en Italie, <a href="https://quintaingames.com/ramio/machiavelli/">Machiavelli</a> ;
au Brésil et au Portugal, <a href="https://quintaingames.com/ramio/mexe-mexe/">mexe-mexe</a> ;
en Hongrie, rablórömi ; en Espagne, Maquiavelo ; en anglais, manipulation
rummy. L'idée est la même partout : la table est à tout le monde et, à son
tour, on peut recomposer les combinaisons déjà posées. Les pages liées
expliquent les règles dans la langue de chaque pays.

## Jouer au rami voleur en ligne

[Ramio](./) est l'application du rami voleur, ou rami chinois : salons
privés entre amis, parties publiques, mode solo contre l'ordinateur (même
hors ligne), et 1 000 casse-têtes à résoudre façon problèmes d'échecs.
L'application applique les règles de cette page : une pose qui ne tient
pas est refusée, et rien ne bouge sur la table. Gratuit, sur Android et
iPhone.

Installer Ramio : [Google Play](https://play.google.com/store/apps/details?id=com.ramio) · [App Store](https://apps.apple.com/fr/app/id6788317282)

## Questions fréquentes

### Combien de cartes au rami voleur ?

Chaque joueur reçoit 13 cartes, que l'on soit 2, 3 ou 4. On joue avec deux
jeux de 52 cartes, soit 104 cartes, ou 106 avec 2 jokers. À table, on voit
aussi des donnes de 10 ou 11 cartes.

### Y a-t-il une défausse au rami voleur ?

Non. À son tour, on pioche une carte, puis on pose si on le peut et si on
le veut. On ne se défausse jamais : la main ne diminue qu'en posant.
Certaines règles de table gardent une défausse en fin de tour ; ce n'est
pas le cas dans Ramio.

### Peut-on reprendre le joker au rami voleur ?

Dans Ramio, non : un joker posé reste sur la table. On peut le déplacer
d'une combinaison à l'autre pendant son tour, autant de fois qu'on veut,
mais jamais le remettre en main. À table, on voit aussi la reprise du
joker contre la carte qu'il remplace.

### Combien vaut le joker au rami voleur ?

Dans Ramio, un joker resté en main à la fin de la manche coûte 50 points
de pénalité. C'est la carte la plus chère, devant l'As (11 points) et les
figures (10 points). Selon les tables, on voit aussi 15 à 25 points.

### Peut-on jouer au rami voleur à deux ?

Oui. La règle est la même à 2, 3 ou 4 joueurs : 13 cartes chacun. À deux,
la pioche compte 78 cartes au départ, ou 80 avec les jokers.

### Rami voleur et rami chinois, est-ce le même jeu ?

Oui : deux noms pour un même jeu, dit « voleur » parce qu'on y prend les
cartes déjà posées par les autres. D'une table à l'autre, quelques règles
varient, surtout sur le joker et le nombre de cartes.

### Peut-on jouer au Rummikub avec des cartes ?

Le rami voleur en est très proche : deux jeux de 52 cartes remplacent les
tuiles, et la table se réorganise librement. Les différences tiennent à
l'ouverture, une tierce franche au lieu de 30 points, et au décompte des
pénalités.

### Où jouer au rami voleur en ligne ?

Ramio est une application gratuite pour Android et iPhone : parties en
ligne, salons privés entre amis, mode solo contre l'ordinateur et 1 000
casse-têtes.

Contact : contact@quintaingames.com

<p style="font-size:0.85em;color:#666;margin-top:2em;"><a href="mentions-legales.html">Mentions légales</a></p>

<!-- Données structurées (sans FAQPage, retiré volontairement).
     Vidéo : date et durée lues sur YouTube le 13/10/2026. -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "@id": "https://quintaingames.com/ramio/regles-rami-chinois.html#article",
      "headline": "Les règles du rami voleur",
      "description": "Règles du rami voleur (ou rami chinois) : combien de cartes à 2, 3 ou 4, pas de défausse, tierce franche, joker. Cas concrets et questions fréquentes.",
      "inLanguage": "fr",
      "mainEntityOfPage": "https://quintaingames.com/ramio/regles-rami-chinois.html",
      "image": "https://quintaingames.com/ramio/assets/ramio-partie-og.jpg",
      "datePublished": "2026-07-14",
      "dateModified": "2026-10-14",
      "author": {
        "@type": "Organization",
        "name": "Quintain Games",
        "url": "https://quintaingames.com/"
      },
      "publisher": {
        "@type": "Organization",
        "name": "Quintain Games",
        "url": "https://quintaingames.com/"
      }
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Quintain Games",
          "item": "https://quintaingames.com/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Ramio",
          "item": "https://quintaingames.com/ramio/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "Règles du rami voleur",
          "item": "https://quintaingames.com/ramio/regles-rami-chinois.html"
        }
      ]
    },
    {
      "@type": "VideoObject",
      "name": "Rami voleur : la règle en 2 minutes (Ramio)",
      "description": "Apprenez la règle du rami voleur telle qu'elle se joue dans Ramio : deux jeux de cartes, 13 cartes chacun, pas de défausse, et une table que l'on peut défaire et recomposer à chaque tour.",
      "thumbnailUrl": "https://i.ytimg.com/vi/5oETEAFIu_s/hqdefault.jpg",
      "uploadDate": "2026-10-07T22:00:32-07:00",
      "duration": "PT2M13S",
      "inLanguage": "fr",
      "url": "https://www.youtube.com/watch?v=5oETEAFIu_s",
      "embedUrl": "https://www.youtube.com/embed/5oETEAFIu_s"
    }
  ]
}
</script>

