---
title: Politique de confidentialité
---

# Politique de confidentialité — Ramio

Dernière mise à jour : 16 juillet 2026

Cette politique décrit les données traitées par l'application mobile
« Ramio » (jeu de rami chinois, ci-après « l'application ») et les droits
des joueurs.

## Qui est responsable des données ?

L'application est éditée par Tristan Hurel.
Contact : ramio.contact@gmail.com

## Quelles données sont collectées ?

L'application collecte le strict nécessaire au fonctionnement du jeu :

- **Adresse e-mail et mot de passe** : pour créer le compte et se connecter.
  Le mot de passe n'est jamais stocké en clair (il est haché par notre
  prestataire d'authentification). Si vous choisissez la **connexion via
  Google ou Apple**, l'application reçoit uniquement l'adresse e-mail du
  compte choisi (aucun accès à vos autres données Google ou Apple).
- **Compte invité** : vous pouvez essayer le jeu sans créer de compte. Un
  compte technique anonyme (sans adresse e-mail) est alors créé pour
  conserver votre progression ; vous pouvez le convertir en compte complet
  à tout moment, ou le supprimer comme n'importe quel compte.
- **Pseudo** : le nom affiché aux autres joueurs pendant une partie. Il est
  unique et visible des joueurs connectés (ajout d'amis par pseudo).
- **Liste d'amis et invitations** : les relations d'amitié que vous créez
  dans le jeu et les invitations de salon échangées entre amis.
- **Messages entre amis** : les messages privés que vous échangez avec vos
  amis depuis l'écran « Mes amis » sont stockés pour que la conversation
  reste consultable. Ils ne sont visibles que de vous et de votre
  correspondant, et sont supprimés avec le compte.
- **Résultats de parties** : score, classement, date et mode de jeu de chaque
  partie terminée, pour alimenter l'écran « Mon profil » (statistiques,
  historique personnels et classement Elo).
- **Jeton de notification** : un identifiant technique de l'appareil, fourni
  par le service de notifications, pour recevoir les invitations d'amis en
  notification « push ». Supprimé à la déconnexion.
- **Signalements** : si vous signalez un joueur (pseudo ou propos déplacés),
  nous conservons le pseudo signalé, le motif que vous indiquez et la date,
  afin de modérer le jeu. Les messages du salon de discussion ne sont
  jamais stockés ; les mots injurieux y sont masqués automatiquement.
- **Joueurs bloqués** : si vous bloquez un joueur, nous conservons ce lien
  (votre compte, le compte bloqué, la date) pour empêcher ce joueur de vous
  contacter (demandes d'ami, messages, invitations, discussion en partie).
  Le joueur bloqué n'en est pas informé ; vous pouvez le débloquer à tout
  moment depuis l'écran « Mes amis ». Ces liens sont supprimés avec le
  compte.
- **Données techniques de connexion** : adresse IP et journaux techniques,
  traités transitoirement pour acheminer les parties en ligne et assurer la
  sécurité du service.
- **Mesure d'audience anonyme** : pour savoir si le jeu plaît et
  l'améliorer, l'application envoie un identifiant d'appareil **aléatoire**
  (jamais rattaché à votre compte ni à votre adresse e-mail), la date de
  première ouverture, les jours d'utilisation et deux jalons de découverte
  (didacticiel terminé, première partie lancée). Ces mesures ne permettent
  pas de vous identifier.
- **Rapports de plantage** : en cas d'erreur technique, un rapport anonyme
  (modèle d'appareil, versions du système et de l'application, trace
  technique de l'erreur) est envoyé à notre prestataire **Sentry**
  (ingestion en Union européenne) pour corriger les bogues. Il n'est pas
  rattaché à votre compte.

L'application ne collecte **aucune** donnée de localisation, aucune photo,
et ne contient **ni publicité ni traceur publicitaire**.

## Contacts du téléphone (fonctionnalité facultative)

L'application propose de **retrouver vos amis dans vos contacts**. Cette
fonctionnalité ne s'active jamais seule : elle demande votre accord dans
l'application, puis la permission du système.

Si vous l'utilisez :

- seules des **empreintes chiffrées** (hachage SHA-256) des adresses e-mail
  de vos contacts sont envoyées à nos serveurs — jamais les noms, jamais
  les adresses en clair, jamais les numéros de téléphone ;
- ces empreintes sont comparées à la volée à celles des comptes existants
  pour vous proposer les joueurs correspondants, puis **oubliées : rien
  n'est conservé** de votre carnet d'adresses ;
- vous pouvez refuser ou révoquer la permission à tout moment dans les
  réglages du téléphone, sans perdre aucune autre fonction du jeu.

## Où sont stockées les données ?

- Les comptes et les résultats de parties sont stockés chez
  **Supabase** (prestataire d'hébergement de base de données), dans un
  centre de données situé dans l'Union européenne.
- Le serveur de jeu (parties en temps réel) est hébergé chez **Fly.io** ;
  l'état d'une partie en cours n'est conservé qu'en mémoire, le temps de
  la partie.

Les échanges entre l'application et les serveurs sont chiffrés (HTTPS/WSS).

## Combien de temps les données sont-elles conservées ?

- Compte et historique de parties : tant que le compte existe.
- À la suppression du compte, les données personnelles associées sont
  supprimées ou anonymisées sans délai injustifié.

## Qui a accès aux données ?

Personne d'autre que l'éditeur et ses prestataires techniques (Supabase,
Fly.io, Google Firebase pour l'acheminement des notifications, et Sentry
pour les rapports de plantage), dans la seule mesure nécessaire au
fonctionnement du service.
Les données ne sont **ni vendues, ni louées, ni partagées** à des fins
publicitaires ou commerciales. Les autres joueurs d'une partie ne voient
que votre pseudo et vos actions de jeu.

## Vos droits (RGPD)

Conformément au Règlement général sur la protection des données, vous
disposez d'un droit d'accès, de rectification, d'effacement, de limitation
et de portabilité de vos données.

Vous pouvez **supprimer votre compte directement dans l'application** :
écran « Mon profil », bouton « Supprimer mon compte » (voir la page
[Suppression de compte](suppression-compte)). La suppression est immédiate
et efface le compte, les statistiques et l'historique de parties.

Pour exercer vos autres droits, ou demander la suppression sans accès à
l'application, écrivez à ramio.contact@gmail.com. Vous pouvez aussi saisir
la CNIL (www.cnil.fr).

## Mineurs

L'application est un jeu de cartes sans mise d'argent, sans achat intégré
à ce jour et sans contenu inapproprié. La création de compte requiert une
adresse e-mail valide.

## Évolutions

Cette politique pourra évoluer (par exemple à l'ajout de nouvelles
fonctionnalités). La version en vigueur est publiée à l'adresse indiquée
sur les fiches App Store et Google Play, avec sa date de mise à jour.
