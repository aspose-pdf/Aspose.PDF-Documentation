---
title: Création d'un PDF conforme à PDF/3-A et attachement de facture ZUGFeRD en Python
linktitle: Attacher ZUGFeRD au PDF
type: docs
weight: 10
url: /python-net/attach-zugferd/
description: Découvrez comment générer un document PDF avec ZUGFeRD dans Aspose.PDF pour Python via .NET
lastmod: "2024-01-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Attacher ZUGFeRD au PDF

Nous recommandons de suivre les étapes suivantes pour attacher ZUGFeRD au PDF :

1. Importez la bibliothèque Aspose.PDF et donnez-lui un alias ap pour plus de commodité.
2. Définissez le chemin vers le répertoire où se trouvent les fichiers PDF d'entrée et de sortie.
3. Définissez le chemin vers le fichier PDF qui sera traité.
4. Chargez le fichier PDF à partir de la variable de chemin et créez un objet Document.
5. Créez un objet FileSpecification pour le fichier XML contenant les métadonnées de la facture. Utilisez la variable de chemin et une chaîne de description pour créer l'objet FileSpecification.

1. Définissez les propriétés `mime_type` et `af_relationship` de l'objet FileSpecification à `text/xml` et `ALTERNATIVE`, respectivement.
1. Ajoutez l'objet fileSpecification à la collection de fichiers intégrés de l'objet document. Cela joint le fichier XML au document PDF en tant que fichier de métadonnées de facture.
1. Convertissez le document PDF au format PDF/A-3A. Utilisez le chemin d'accès au fichier journal, l'énumération `PdfFormat.PDF_A_3A` et l'énumération `ConvertErrorAction.DELETE` pour convertir l'objet document.
1. Enregistrez le document PDF avec le ZUGFeRD attaché.

```python
import aspose.pdf as ap

# Définir le chemin vers le répertoire où se trouvent les fichiers PDF d'entrée et de sortie
_dataDir = "./"

# Charger le fichier PDF qui sera traité
path = _dataDir + "ZUGFeRD/ZUGFeRD-test.pdf"
document = ap.Document(path)

# Créer un objet FileSpecification pour le fichier XML qui contient les métadonnées de la facture
description = "Métadonnées de facture conformes à la norme ZUGFeRD"
path = _dataDir + "ZUGFeRD/factur-x.xml"
fileSpecification = ap.FileSpecification(path, description)

# Définir le type MIME et les propriétés AFRelationship du fichier intégré
fileSpecification.mime_type = "text/xml"
fileSpecification.af_relationship = ap.AFRelationship.ALTERNATIVE

# Ajouter le fichier intégré à la collection de fichiers intégrés du document PDF
document.embedded_files.add("factur",fileSpecification)

# Convertir le document PDF au format PDF/A-3A
path = _dataDir + "ZUGFeRD/log.xml"
document.convert(path, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)

# Enregistrer le document PDF avec le ZUGFeRD attaché
path = _dataDir + "ZUGFeRD/ZUGFeRD-res.pdf"
document.save(path)
```