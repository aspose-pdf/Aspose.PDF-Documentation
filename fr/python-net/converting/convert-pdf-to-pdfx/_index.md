---
title: Convertir PDF en PDF/A, PDF/E et PDF/X en Python
linktitle: Convertir le PDF en PDF/A, PDF/E et PDF/X
type: docs
weight: 120
url: /fr/python-net/convert-pdf-to-pdf_x/
lastmod: "2026-05-22"
description: Apprenez comment convertir des fichiers PDF en PDF/A, PDF/E et PDF/X en Python avec Aspose.PDF for Python via .NET pour l’archivage, l’accessibilité et les flux de travail d’impression.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Comment convertir PDF en formats PDF/x
Abstract: L'article propose un guide complet sur la conversion de PDF en formats PDF/A, PDF/E et PDF/X en utilisant Aspose.PDF pour Python.
---

**Le format PDF vers PDF/x signifie la capacité de convertir un PDF vers des formats supplémentaires, à savoir PDF/A, PDF/E et PDF/X.**

## Convertir le PDF en PDF/A

**Aspose.PDF for Python** vous permet de convertir un fichier PDF en <abbr title="Portable Document Format / A">PDF/A</abbr> fichier PDF conforme. Avant de le faire, le fichier doit être validé. Ce sujet explique comment.

{{% alert color="primary" %}}

Veuillez noter que nous suivons Adobe Preflight pour valider la conformité PDF/A. Tous les outils du marché ont leur propre “représentation” de la conformité PDF/A. Veuillez consulter cet article sur les outils de validation PDF/A pour référence. Nous avons choisi les produits Adobe pour vérifier comment Aspose.PDF génère les fichiers PDF, car Adobe est au centre de tout ce qui est lié au PDF.

{{% /alert %}}

Convertissez le fichier en utilisant la méthode Convert de la classe Document. Avant de convertir le PDF en fichier conforme PDF/A, validez le PDF à l'aide de la méthode Validate. Le résultat de la validation est stocké dans un fichier XML et ce résultat est également transmis à la méthode Convert. Vous pouvez également spécifier l'action pour les éléments qui ne peuvent pas être convertis en utilisant l'énumération ConvertErrorAction.

{{% alert color="success" %}}
**Essayez de convertir le PDF en PDF/A en ligne**

Aspose.PDF for Python vous présente une application en ligne ["PDF en PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), où vous pouvez essayer d'examiner le fonctionnement et la qualité.

[![Conversion PDF en PDF/A avec l'application Aspose.PDF](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

La méthode 'document.validate()' valide si un fichier PDF est conforme à la norme PDF/A-1B (une version du PDF normalisée par l'ISO conçue pour l'archivage à long terme). Les résultats de la validation sont enregistrés dans un fichier journal.

### Convertir le PDF en PDF/A-1B

L'extrait de code suivant montre comment convertir des fichiers PDF au format PDF/A-1B :

1. Chargez le document PDF en utilisant 'ap.Document'.
1. Appelez la méthode convert avec les paramètres suivants :
    - Chemin du fichier journal - stocke les détails du processus de conversion et des contrôles de conformité.
    - Format cible - 'ap.PdfFormat.PDF_A_1B' (norme d'archivage).
    - Action d'erreur - 'ap.ConvertErrorAction.DELETE' — supprime automatiquement les éléments qui empêchent la conformité.
1. Enregistrez le fichier PDF/A conforme converti dans le chemin de sortie.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA(infile, outfile):
    """Convert PDF to PDF/A-1B format."""

    document = ap.Document(infile)
    document.convert(
        outfile.replace(".pdf", "-log.xml"),
        ap.PdfFormat.PDF_A_1B,
        ap.ConvertErrorAction.DELETE,
    )
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

### Convertir le PDF en PDF 2.0 et PDF/A-4

Cet exemple montre comment convertir un document PDF en formats standardisés plus récents : PDF 2.0 et PDF/A-4.
Les deux conversions contribuent à garantir la conformité aux spécifications modernes et aux exigences d'archivage.

1. Chargez le document d\'entrée en utilisant ap.Document.
1. Effectuez la première conversion vers PDF 2.0 en appelant document.convert avec :
    - Chemin du fichier journal pour les détails de conversion.
    - Format cible - 'ap.PdfFormat.V_2_0'.
    - Action d'erreur - 'ap.ConvertErrorAction.DELETE' pour supprimer les éléments non conformes.
1. Effectuez une deuxième conversion vers PDF/A-4 en utilisant la même méthode, en vous assurant que le fichier soit également conforme aux normes d'archivage.
1. Enregistrez le document résultant dans le chemin de sortie spécifié.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA4(infile, outfile):
    logfile = outfile.replace(".pdf", "_log.xml")

    document = ap.Document(infile)
    document.convert(logfile, ap.PdfFormat.V_2_0, ap.ConvertErrorAction.DELETE)
    document.convert(logfile, ap.PdfFormat.PDF_A_4, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```

### Convertir le PDF en PDF/A-3A avec des fichiers incorporés

Le prochain extrait de code montre comment intégrer des fichiers externes dans un PDF, puis convertir le PDF au format PDF/A-3A, qui prend en charge les pièces jointes et convient à l'archivage à long terme avec du contenu intégré.

1. Chargez le PDF d'entrée en utilisant 'ap.Document'.
1. Créez un objet 'FileSpecification' pointant vers le fichier à intégrer (par exemple, "aspose-logo.jpg") avec une description.
1. Ajoutez la spécification de fichier à la collection « embedded_files » du PDF.
1. Convertir le document en PDF/A-3A en utilisant 'document.convert', en spécifiant :
    - Chemin du fichier journal.
    - Format cible - 'ap.PdfFormat.PDF_A_3A'.
    - Action d'erreur - 'ap.ConvertErrorAction.DELETE' pour supprimer les éléments non conformes.
1. Enregistrez le PDF converti dans le chemin de sortie.
1. Imprimez un message de confirmation.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA_with_attachment(infile, attachement_file, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")
    document = ap.Document(infile)

    fileSpecification = ap.FileSpecification(attachement_file, "Large Image file")
    document.embedded_files.add(fileSpecification)
    document.convert(
        logfile, ap.PdfFormat.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE
    )
    document.save(outfile)
```

### Convertir le PDF en PDF/A-1B avec substitution de police

Cette fonction convertit un PDF au format PDF/A-1B tout en gérant les polices manquantes en les remplaçant par des polices disponibles. Cela garantit que le PDF converti reste visuellement cohérent et conforme aux normes d'archivage.

1. Chargez le PDF en utilisant 'ap.Document'.
1. Convertissez le PDF en PDF/A-1B en utilisant 'document.convert', en spécifiant :
    - Chemin du fichier journal.
    - Format cible - 'ap.PdfFormat.PDF_A_1B'.
    - Action d'erreur - 'ap.ConvertErrorAction.DELETE' pour supprimer les éléments non conformes.
1. Enregistrez le PDF converti dans le chemin de sortie.
1. Imprimez un message de confirmation.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA_replace_missing_fonts(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")
    try:
        ap.text.FontRepository.find_font("AgencyFB")

    except ap.FontNotFoundException:
        font_substitution = ap.text.SimpleFontSubstitution("AgencyFB", "Arial")
        ap.text.FontRepository.Substitutions.append(font_substitution)

    document = ap.Document(infile)
    document.convert(logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```

### Convertir le PDF en PDF/A-1B avec étiquetage automatique

Cette fonction convertit un document PDF au format PDF/A-1B tout en balisant automatiquement le contenu pour l'accessibilité et la cohérence structurelle. Le balisage automatique améliore la convivialité du document pour les lecteurs d'écran et garantit une structure sémantique correcte.

1. Chargez le PDF en utilisant 'ap.Document'.
1. Créer 'PdfFormatConversionOptions' en spécifiant :
    - Chemin du fichier journal.
    - Format cible - 'ap.PdfFormat.PDF_A_1B'.
    - Action d'erreur - 'ap.ConvertErrorAction.DELETE' pour supprimer les éléments non conformes.
1. Configurer 'AutoTaggingSettings':
    - Activer 'enable_auto_tagging = True'.
    - Définissez 'heading_recognition_strategy = AUTO' pour détecter automatiquement les titres.
1. Attribuez les paramètres d'auto-étiquetage aux options de conversion.
1. Convertissez le PDF en utilisant 'document.convert(options)'.
1. Enregistrez le PDF converti dans le chemin de sortie.
1. Imprimez un message de confirmation.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA_with_automatic_tagging(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")

    document = ap.Document(infile)
    options = ap.PdfFormatConversionOptions(
        logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE
    )

    auto_tagging_settings = ap.AutoTaggingSettings()
    auto_tagging_settings.enable_auto_tagging = True

    auto_tagging_settings.heading_recognition_strategy = (
        ap.HeadingRecognitionStrategy.AUTO
    )

    options.auto_tagging_settings = auto_tagging_settings
    document.convert(options)
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## Convertir le PDF en PDF/E

Cet extrait de code montre comment convertir un document PDF au format PDF/E-1, qui est une norme ISO adaptée à la documentation d'ingénierie et technique. Ce format préserve la mise en page précise, les graphiques et les métadonnées nécessaires aux flux de travail d'ingénierie.

1. Chargez le PDF source en utilisant 'ap.Document'.
1. Créer 'PdfFormatConversionOptions' en spécifiant :
    - Chemin du fichier journal pour suivre les problèmes de conversion.
    - Format cible - 'ap.PdfFormat.PDF_E_1'.
    - Action d'erreur - 'ap.ConvertErrorAction.DELETE' pour supprimer les éléments non conformes.
1. Convertissez le PDF en utilisant 'document.convert(options)'.
1. Enregistrez le PDF converti à l'emplacement de sortie spécifié.
1. Imprimez un message de confirmation.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDF_E(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")

    document = ap.Document(infile)
    options = ap.PdfFormatConversionOptions(
        logfile, ap.PdfFormat.PDF_E_1, ap.ConvertErrorAction.DELETE
    )

    document.convert(options)

    # Save PDF document
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## Convertir le PDF en PDF/X

Le prochain extrait de code convertit un document PDF au format PDF/X-4, qui est une norme ISO couramment utilisée dans l'industrie de l'impression et de l'édition. PDF/X-4 garantit la précision des couleurs, maintient la transparence et intègre des profils ICC pour une sortie cohérente sur tous les appareils.

1. Chargez le PDF source en utilisant 'ap.Document'.
1. Créer 'PdfFormatConversionOptions' en spécifiant :
    - Chemin du fichier journal.
    - Format cible - 'ap.PdfFormat.PDF_X_4'.
    - Action d'erreur - 'ap.ConvertErrorAction.DELETE' pour supprimer les éléments non conformes.
1. Fournissez le **fichier de profil ICC** pour la gestion des couleurs via 'icc_profile_file_name'.
1. Spécifiez un **OutputIntent** avec un identifiant de condition (par exemple "FOGRA39") pour les exigences d'impression.
1. Convertissez le PDF en utilisant 'document.convert()'.
1. Enregistrez le PDF converti à l'emplacement de sortie spécifié.
1. Imprimez un message de confirmation.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDF_X(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")

    document = ap.Document(infile)
    options = ap.PdfFormatConversionOptions(
        logfile, ap.PdfFormat.PDF_X_4, ap.ConvertErrorAction.DELETE
    )

    # Provide the name of the external ICC profile file (optional)
    options.icc_profile_file_name = path.join(
        path.dirname(infile), "ISOcoated_v2_eci.icc"
    )
    # Provide an output condition identifier and other necessary OutputIntent properties (optional)
    options.output_intent = ap.OutputIntent("FOGRA39")

    document.convert(options)

    # Save PDF document
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## Conversions associées

- [Convertir le PDF en Word](/pdf/fr/python-net/convert-pdf-to-word/) pour les flux de travail de contenu éditable après la validation des normes.
- [Convertir le PDF en HTML](/pdf/fr/python-net/convert-pdf-to-html/) lorsque votre sortie cible est prête pour le web plutôt que PDF basé sur les normes.
