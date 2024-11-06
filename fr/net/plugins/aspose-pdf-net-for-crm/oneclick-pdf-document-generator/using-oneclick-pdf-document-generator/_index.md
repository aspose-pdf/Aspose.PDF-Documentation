---
title: Utilisation du générateur de documents PDF OneClick
type: docs
weight: 10
url: fr/net/using-oneclick-pdf-document-generator/
description: Apprenez à utiliser le générateur de documents PDF OneClick Aspose.PDF dans Microsoft Dynamics
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Créer un modèle et l'ajouter dans CRM

- Ouvrez Word et créez un modèle.
- Insérez des champs de publipostage pour les données provenant du CRM.

![Insérer des champs de fusion](using-oneclick-pdf-document-generator_1.png)

- Assurez-vous que le nom du champ correspond exactement au champ du CRM.
- Les modèles sont spécifiques à l'utilisation avec une entité individuelle.

![Modèle de démonstration](using-oneclick-pdf-document-generator_2.png)

- Une fois le modèle créé, ouvrez l'entité de configuration PDF OneClick dans CRM et créez un nouvel enregistrement.
- Donnez le nom du modèle, sélectionnez l'entité pour laquelle le modèle est défini et attachez le document créé en pièce jointe.

![Sélectionner le modèle](using-oneclick-pdf-document-generator_3.png)

## Générer un document à partir du bouton Ruban

- Ouvrez l'enregistrement où vous souhaitez générer le document.
- Ouvrez l'enregistrement où vous souhaitez générer le document.
- Cliquez sur le bouton OneClick PDF dans le ruban.

![Cliquez sur OneClick PDF](using-oneclick-pdf-document-generator_4.png)

- Dans le Popup : Sélectionnez le modèle, le Nom du fichier et l'Action puis cliquez sur Générer.
- Vérifiez le fichier téléchargé ou les Notes, selon la sélection.

## Configurer les boutons OneClick et les utiliser

- Pour utiliser un bouton OneClick directement depuis un formulaire, ouvrez la personnalisation du formulaire.
- Insérez une WebResource où vous souhaitez ajouter des boutons OneClick.
- Sélectionnez OpenButtonPage dans Webresource et donnez-lui un Nom.
- Configurez les boutons dans le champ Données selon l'exemple suivant.

![Propriétés de WebResource](using-oneclick-pdf-document-generator_5.png)

- Utilisez une ligne séparée pour chaque bouton et utilisez la syntaxe suivante :
  - Syntaxe : Nom du modèle |<Action : Télécharger/Note>|Nom du fichier de sortie
  - Exemple : Demo|Télécharger|Mon fichier téléchargé
- Sauvegardez et publiez la personnalisation.
- Le bouton est disponible sur le formulaire.

![Le bouton est disponible sur le formulaire](using-oneclick-pdf-document-generator_6.png)
![Le bouton est disponible sur le formulaire](using-oneclick-pdf-document-generator_6.png)
