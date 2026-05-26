---
title: Création d'un PDF conforme PDF/3-A et attachement d'une facture ZUGFeRD en Python
linktitle: Attacher ZUGFeRD au PDF
type: docs
weight: 10
url: /fr/python-net/attach-zugferd/
description: Apprenez comment générer un document PDF avec ZUGFeRD dans Aspose.PDF for Python via .NET
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment attacher ZUGFeRD à un document PDF
Abstract: L'article fournit un guide étape par étape sur la façon d'attacher ZUGFeRD (un format de factures électroniques) à un document PDF en utilisant la bibliothèque Aspose.PDF. La procédure commence par l'importation de la bibliothèque nécessaire et la configuration des chemins de répertoires pour les fichiers d'entrée et de sortie. Elle consiste à charger le fichier PDF cible dans un objet Document, et à créer un objet FileSpecification pour le fichier XML contenant les métadonnées de la facture. Des propriétés clés comme `mime_type` et `af_relationship` sont définies pour garantir une intégration correcte des métadonnées. Le fichier XML est ensuite ajouté à la collection des fichiers incorporés du PDF, le joignant ainsi comme métadonnées. Ensuite, le document PDF est converti au format PDF/A-3A, qui convient à l'archivage des documents électroniques, avant d'enregistrer le PDF final avec le ZUGFeRD incorporé. L'article se conclut par un extrait de code Python qui montre la mise en œuvre de ces étapes, illustrant l'intégration de ZUGFeRD avec un PDF pour une meilleure gestion des documents.
---

## Attacher ZUGFeRD au PDF

Nous recommandons les étapes suivantes pour joindre ZUGFeRD au PDF :

1. Importez la bibliothèque Aspose.PDF et donnez‑lui un alias ap pour plus de commodité.
1. Définissez le chemin du répertoire où se trouvent les fichiers PDF d’entrée et de sortie.
1. Définissez le chemin du fichier PDF qui sera traité.
1. Chargez le fichier PDF à partir de la variable de chemin et créez un objet Document.
1. Créez un objet FileSpecification pour le fichier XML contenant les métadonnées de la facture. Utilisez la variable de chemin et une chaîne de description pour créer l’objet FileSpecification.
1. Définir le `mime_type` et le `af_relationship` propriétés de l'objet FileSpecification à `text/xml` et `ALTERNATIVE`, respectivement.
1. Ajoutez l'objet fileSpecification à la collection de fichiers intégrés de l'objet document. Cela attache le fichier XML au document PDF en tant que fichier de métadonnées de facture.
1. Convertir le document PDF au format PDF/A-3A. Utilisez le chemin vers le fichier journal, le `PdfFormat.PDF_A_3A` énumération, et le `ConvertErrorAction.DELETE` énumération pour convertir l'objet Document.
1. Enregistrez le document PDF avec le ZUGFeRD attaché.

```python
import sys
import os
import aspose.pdf as ap

def attach_invoice_zugferd_format(infile, invoice, outfile):
    document = ap.Document(infile)

    # Create a FileSpecification object for the XML file that contains the invoice metadata
    description = "Invoice metadata conforming to ZUGFeRD standard"
    file_specification = ap.FileSpecification(invoice, description)

    # Set the MIME type and the AFRelationship properties of the embedded file
    file_specification.mime_type = "text/xml"
    file_specification.af_relationship = ap.AFRelationship.ALTERNATIVE

    # Add the embedded file to the PDF document's embedded files collection
    document.embedded_files.add("factur", file_specification)

    # Convert the PDF document to the PDF/A-3A format
    log_path = outfile.replace(".pdf", "_log.xml")
    document.convert(log_path, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```
