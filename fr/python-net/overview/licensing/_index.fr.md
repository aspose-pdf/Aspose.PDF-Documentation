---
title: Licence Aspose PDF
linktitle: Licences et limitations
type: docs
weight: 50
url: /python-net/licensing/
description: Aspose. PDF pour Python invite ses clients à obtenir une licence Classique. Ainsi qu'à utiliser une licence limitée pour mieux explorer le produit.
lastmod: "2022-12-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Limitation d'une version d'évaluation

Nous souhaitons que nos clients testent nos composants de manière exhaustive avant d'acheter, c'est pourquoi la version d'évaluation vous permet de l'utiliser comme vous le feriez normalement.

- **PDF créé avec un filigrane d'évaluation.** La version d'évaluation de Aspose.PDF pour Python offre toutes les fonctionnalités du produit, mais toutes les pages des documents PDF générés portent un filigrane avec "Évaluation uniquement. Créé avec Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" en haut.

>Si vous souhaitez tester Aspose.PDF sans les limitations de la version d'évaluation, vous pouvez également demander une Licence Temporaire de 30 jours.
 Veuillez vous référer à [Comment obtenir une licence temporaire ?](https://purchase.aspose.com/temporary-license)

## Licence classique

La licence peut être chargée à partir d'un fichier ou d'un objet flux. La manière la plus simple de configurer une licence est de placer le fichier de licence dans le même dossier que le fichier Aspose.PDF.dll et de spécifier le nom du fichier sans chemin, comme indiqué dans l'exemple ci-dessous.

Si vous utilisez un autre composant Aspose pour Python avec Aspose.PDF pour Python, veuillez spécifier l'espace de noms pour License comme la [classe Aspose.Pdf.License]().

```python

    license_file = LICENSE_FILE
    license = ap.License()
    license.set_license(license_file)
```