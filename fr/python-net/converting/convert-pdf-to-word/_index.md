---
title: Convertir PDF en Word en Python
linktitle: Convertir PDF en Word
type: docs
weight: 10
url: /fr/python-net/convert-pdf-to-word/
lastmod: "2026-04-14"
description: Apprenez comment convertir PDF en Word en Python, y compris PDF en DOC, PDF en DOCX, et la reconnaissance avancée de mise en page avec Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Convertir PDF en DOC et DOCX en Python
Abstract: Cet article montre comment convertir des fichiers PDF aux formats Microsoft Word avec Aspose.PDF for Python via .NET. Il couvre la conversion PDF vers DOC, PDF vers DOCX, ainsi que les options avancées de reconnaissance de mise en page pour créer des documents Word modifiables à partir du contenu PDF.
---

Cette page montre comment **convertir PDF en Word avec Python**. Utilisez ces exemples lorsque vous avez besoin d’une sortie DOC ou DOCX modifiable à partir d’un fichier PDF pour la révision, la réutilisation ou les flux de travail des documents de bureau.

## Convertir PDF en DOC avec Python

L’une des fonctionnalités les plus populaires est la conversion PDF vers Microsoft Word DOC, qui simplifie la gestion du contenu. **Aspose.PDF for Python via .NET** vous permet de convertir des fichiers PDF non seulement en DOC mais également en format DOCX, facilement et efficacement.

Utilisez la conversion Word lorsque vous devez réviser du texte, réutiliser le contenu dans les flux de travail bureautiques, ou déplacer le contenu PDF vers des documents DOC ou DOCX modifiables.

Le [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) classe fournit de nombreuses propriétés qui améliorent le processus de conversion des fichiers PDF au format DOC. Parmi ces propriétés, Mode vous permet de spécifier le mode de reconnaissance du contenu PDF. Vous pouvez spécifier n'importe quelle valeur de l'énumération RecognitionMode pour cette propriété. Chacune de ces valeurs possède des avantages et des limitations spécifiques :

Étapes : Convertir le PDF en DOC avec Python

1. Chargez le PDF dans un objet 'ap.Document'.
1. Créez une instance 'DocSaveOptions'.
1. Définissez la propriété format sur 'DocFormat.DOC' pour garantir que la sortie est au format .doc (format Word plus ancien).
1. Enregistrez le PDF en tant que document Word en utilisant les options d'enregistrement spécifiées.
1. Imprimez un message de confirmation.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_PDF_to_DOC(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Essayez de convertir PDF en DOC en ligne**

Aspose.PDF for Python vous présente une application en ligne [“PDF en DOC”](https://products.aspose.app/pdf/conversion/pdf-to-doc), où vous pouvez essayer d'examiner la fonctionnalité et la qualité avec lesquelles il fonctionne.

[![Convertir le PDF en DOC](/pdf/fr/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Convertir le PDF en DOCX en Python

L'API Aspose.PDF for Python vous permet de lire et de convertir des documents PDF en DOCX en utilisant Python via .NET. DOCX est un format bien connu pour les documents Microsoft Word dont la structure a été modifiée, passant d'un binaire simple à une combinaison de fichiers XML et binaires. Les fichiers DOCX peuvent être ouverts avec Word 2007 et les versions ultérieures, mais pas avec les versions antérieures de MS Word qui ne supportent que les extensions de fichiers DOC.

Le fragment de code Python suivant montre le processus de conversion d'un fichier PDF au format DOCX.

Étapes : Convertir le PDF en DOCX avec Python

1. Chargez le PDF source en utilisant 'ap.Document'.
1. Créez une instance de 'DocSaveOptions'.
1. Définissez la propriété format sur 'DocFormat.DOC_X' pour générer un fichier .docx (format Word moderne).
1. Enregistrez le PDF en tant que fichier DOCX avec les options d'enregistrement configurées.
1. Affichez un message de confirmation après la conversion.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_PDF_to_DOCX(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC_X
    document.save(outfile, save_options)
```

## Convertir le PDF en DOCX avec reconnaissance de mise en page avancée

Convertir un document PDF en fichier DOCX (Word) en utilisant Python et Aspose.PDF avec des paramètres de reconnaissance avancés. Il utilise un mode de flux amélioré pour préserver la structure du document, rendant la sortie plus modifiable et plus proche de la mise en page originale.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_PDF_to_DOCX_advanced(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC_X
    save_options.mode = ap.DocSaveOptions.RecognitionMode.ENHANCED_FLOW
    document.save(outfile, save_options)
```

Le [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) La classe possède une propriété nommée Format qui offre la capacité de spécifier le format du document résultant, c’est‑à‑dire DOC ou DOCX. Pour convertir un fichier PDF au format DOCX, veuillez passer la valeur Docx de l’énumération DocSaveOptions.DocFormat.

{{% alert color="warning" %}}
**Essayez de convertir le PDF en DOCX en ligne**

Aspose.PDF for Python vous présente une application en ligne ["PDF en Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), où vous pouvez essayer d'examiner la fonctionnalité et la qualité avec lesquelles il fonctionne.

[![Aspose.PDF Conversion PDF en Word App](/pdf/fr/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Conversions associées

- [Convertir le PDF en Excel](/pdf/fr/python-net/convert-pdf-to-excel/) pour les exportations orientées tableur.
- [Convertir le PDF en PowerPoint](/pdf/fr/python-net/convert-pdf-to-powerpoint/) lorsque vous avez besoin de diapositives de présentation au lieu d'une sortie de traitement de texte.
- [Convertir le PDF en HTML](/pdf/fr/python-net/convert-pdf-to-html/) pour la publication Web et les flux de travail de contenu basés sur le navigateur.
