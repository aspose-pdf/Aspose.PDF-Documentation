---
title: Création d'un PDF conforme PDF/3-A et ajout d'une facture ZUGFeRD en Python
linktitle: Attacher ZUGFeRD au PDF
type: docs
weight: 10
url: /fr/python-net/attach-zugferd/
description: Apprenez à générer un document PDF avec ZUGFeRD dans Aspose.PDF pour Python via .NET
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment attacher ZUGFeRD à un document PDF
Abstract: L'article fournit un guide étape par étape sur la façon d'attacher ZUGFeRD (un format de factures électroniques) à un document PDF en utilisant la bibliothèque Aspose.PDF. La procédure commence par l'importation de la bibliothèque nécessaire et la configuration des chemins des répertoires pour les fichiers d'entrée et de sortie. Elle implique le chargement du fichier PDF cible dans un objet Document, et la création d'un objet FileSpecification pour le fichier XML contenant les métadonnées de la facture. Des propriétés clés comme `mime_type` et `af_relationship` sont définies pour assurer une intégration correcte des métadonnées. Le fichier XML est ensuite ajouté à la collection de fichiers intégrés du PDF, le joignant ainsi comme métadonnées. Par la suite, le document PDF est converti au format PDF/A-3A, adapté à l'archivage des documents électroniques, avant d'enregistrer le PDF final avec le ZUGFeRD intégré. L'article se conclut par un extrait de code Python qui démontre la mise en œuvre de ces étapes, illustrant l'intégration de ZUGFeRD avec un PDF pour une meilleure gestion des documents.
---

## Attacher ZUGFeRD au PDF

Nous recommandons les étapes suivantes pour attacher ZUGFeRD au PDF :

1. Importez la bibliothèque Aspose.PDF et donnez‑lui l'alias ap par commodité.
1. Définissez le chemin du répertoire où se trouvent les fichiers PDF d'entrée et de sortie.
1. Définissez le chemin du fichier PDF qui sera traité.
1. Chargez le fichier PDF à partir de la variable de chemin et créez un objet Document.
1. Créez un objet FileSpecification pour le fichier XML contenant les métadonnées de la facture. Utilisez la variable de chemin et une chaîne de description pour créer l'objet FileSpecification.
1. Définissez les propriétés `mime_type` et `af_relationship` de l'objet FileSpecification à `text/xml` et `ALTERNATIVE`, respectivement.
1. Ajoutez l'objet fileSpecification à la collection de fichiers intégrés de l'objet document. Cela attache le fichier XML au document PDF en tant que fichier de métadonnées de facture.
1. Convertissez le document PDF au format PDF/A-3A. Utilisez le chemin du fichier journal, l'énumération `PdfFormat.PDF_A_3A` et l'énumération `ConvertErrorAction.DELETE` pour convertir l'objet document.
1. Enregistrez le document PDF avec le ZUGFeRD attaché.

```python
import aspose.pdf as ap

# Define the path to the directory where the input and output PDF files are located
_dataDir = "./"

# Load the PDF file that will be processed
path = _dataDir + "ZUGFeRD/ZUGFeRD-test.pdf"
document = ap.Document(path)

# Create a FileSpecification object for the XML file that contains the invoice metadata
description = "Invoice metadata conforming to ZUGFeRD standard"
path = _dataDir + "ZUGFeRD/factur-x.xml"
fileSpecification = ap.FileSpecification(path, description)

# Set the MIME type and the AFRelationship properties of the embedded file
fileSpecification.mime_type = "text/xml"
fileSpecification.af_relationship = ap.AFRelationship.ALTERNATIVE

# Add the embedded file to the PDF document's embedded files collection
document.embedded_files.add("factur",fileSpecification)

# Convert the PDF document to the PDF/A-3A format
path = _dataDir + "ZUGFeRD/log.xml"
document.convert(path, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)

# Save the PDF document with the attached ZUGFeRD
path = _dataDir + "ZUGFeRD/ZUGFeRD-res.pdf"
document.save(path)
```

