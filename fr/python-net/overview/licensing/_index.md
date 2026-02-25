---
title: Licence Aspose PDF
linktitle: Licence et limitations
type: docs
weight: 50
url: /fr/python-net/licensing/
description: Aspose.PDF pour Python invite ses clients à obtenir une licence Classique. Vous pouvez également utiliser une licence limitée pour explorer davantage le produit.
lastmod: "2025-02-21"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Licence d'Aspose.PDF pour Python
Abstract: L'article traite des limitations et des options de licence pour Aspose.PDF pour Python. Il souligne que la version d'évaluation permet de tester l'ensemble des fonctionnalités mais ajoute un filigrane aux PDF générés, affichant "Evaluation Only" ainsi que les informations de droit d'auteur. Pour les utilisateurs souhaitant tester sans ces limitations, une licence temporaire de 30 jours est disponible. L'article explique également comment mettre en œuvre une licence classique en la chargeant depuis un fichier ou un flux, en recommandant de placer le fichier de licence dans le même répertoire que le fichier Aspose.PDF.dll et de définir la licence à l'aide de la classe `Aspose.Pdf.License`. Des extraits de code sont fournis pour illustrer le processus de licence.
---

## Limitation d'une version d'évaluation

Nous voulons que nos clients testent nos composants minutieusement avant d'acheter, c'est pourquoi la version d'évaluation vous permet de l'utiliser comme vous le feriez normalement.

- **PDF créé avec un filigrane d'évaluation.** La version d'évaluation d'Aspose.PDF pour Python offre toutes les fonctionnalités du produit, mais toutes les pages des documents PDF générés sont filigranées avec "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" en haut.

>Si vous souhaitez tester Aspose.PDF sans les limitations de la version d'évaluation, vous pouvez également demander une licence temporaire de 30 jours. Veuillez vous référer à [Comment obtenir une licence temporaire ?](https://purchase.aspose.com/temporary-license)

## Licence classique

La licence peut être chargée depuis un fichier ou un objet flux. La façon la plus simple de définir une licence est de placer le fichier de licence dans le même dossier que le fichier Aspose.PDF.dll et de spécifier le nom du fichier sans chemin, comme le montre l'exemple ci-dessous.

Si vous utilisez un autre composant Aspose pour Python avec Aspose.PDF pour Python, veuillez spécifier l'espace de noms pour la licence comme [classe Aspose.Pdf.License]().

```python

    license_file = LICENSE_FILE
    license = ap.License()
    license.set_license(license_file)
```

