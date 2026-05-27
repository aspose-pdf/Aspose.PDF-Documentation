---
title: Convertir PDF en Word en Python
linktitle: Convertir le PDF en Word
type: docs
weight: 10
url: /fr/python-net/convert-pdf-to-word/
lastmod: "2026-05-22"
description: Apprenez comment convertir des fichiers PDF en DOC et DOCX en Python avec Aspose.PDF for Python via .NET pour faciliter la modification et la réutilisation des documents.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment convertir PDF en Word en Python
Abstract: Cet article fournit un guide complet sur la conversion de fichiers PDF en formats Microsoft Word (DOC et DOCX) en utilisant Python, en particulier la bibliothèque Aspose.PDF. Il décrit les avantages de convertir les PDF en documents Word modifiables, permettant une manipulation plus facile du contenu comme le texte, les tableaux et les images. L'article détaille le processus de conversion de PDF en DOC (format Word 97-2003) et DOCX, avec des extraits de code montrant ces conversions en Python. Le processus consiste à créer un objet `Document` à partir du PDF et à l'enregistrer au format souhaité en utilisant la méthode `save()` et l'énumération `SaveFormat`. De plus, il introduit la classe `DocSaveOptions`, qui permet une personnalisation supplémentaire du processus de conversion, comme la spécification des modes de reconnaissance. L'article met également en avant les applications en ligne fournies par Aspose.PDF pour tester la qualité et la fonctionnalité de la conversion. Le contenu comprend une vue d'ensemble structurée et des liens vers les sections correspondantes pour chaque format.
---

## Convertir le PDF en DOC

L'une des fonctionnalités les plus populaires est la conversion de PDF en DOC Microsoft Word, ce qui facilite la gestion du contenu. **Aspose.PDF for Python via .NET** vous permet de convertir les fichiers PDF non seulement en DOC mais aussi au format DOCX, facilement et efficacement.

Utilisez la conversion Word lorsque vous devez réviser le texte, réutiliser le contenu dans les flux de travail de bureau ou déplacer le contenu PDF vers des documents DOC ou DOCX modifiables.

Le [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) la classe fournit de nombreuses propriétés qui améliorent le processus de conversion des fichiers PDF en format DOC. Parmi ces propriétés, Mode vous permet de spécifier le mode de reconnaissance du contenu PDF. Vous pouvez spécifier n'importe quelle valeur de l'énumération RecognitionMode pour cette propriété. Chacune de ces valeurs présente des avantages et des limitations spécifiques :

Étapes : Convertir PDF en DOC avec Python

1. Chargez le PDF dans un objet 'ap.Document'.
1. Créez une instance de 'DocSaveOptions'.
1. Définissez la propriété format sur 'DocFormat.DOC' pour garantir que la sortie soit au format .doc (format Word plus ancien).
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

Aspose.PDF for Python vous présente une application en ligne ["PDF en DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), où vous pouvez essayer d'examiner le fonctionnement et la qualité.

[![Convertir le PDF en DOC](/pdf/fr/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Convertir PDF en DOCX

Aspose.PDF for Python API vous permet de lire et de convertir des documents PDF en DOCX en utilisant Python via .NET. DOCX est un format bien connu pour les documents Microsoft Word dont la structure est passée d’un binaire simple à une combinaison de fichiers XML et binaires. Les fichiers DOCX peuvent être ouverts avec Word 2007 et les versions ultérieures, mais pas avec les versions antérieures de MS Word qui ne prennent en charge que les extensions de fichiers DOC.

L'extrait de code Python suivant montre le processus de conversion d'un fichier PDF en format DOCX.

Étapes : Convertir PDF en DOCX avec Python

1. Chargez le PDF source en utilisant 'ap.Document'.
1. Créez une instance de 'DocSaveOptions'.
1. Définissez la propriété format sur 'DocFormat.DOC_X' pour générer un fichier .docx (format Word moderne).
1. Enregistrez le PDF en tant que fichier DOCX avec les options d'enregistrement configurées.
1. Imprimer un message de confirmation après la conversion.

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

## Convertir le PDF en DOCX avec reconnaissance avancée de mise en page

Convertir un document PDF en fichier DOCX (Word) en utilisant Python et Aspose.PDF avec des paramètres de reconnaissance avancés. Il utilise le mode flux amélioré pour préserver la structure du document, rendant la sortie plus modifiable et plus proche de la mise en page originale.

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

Le [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) La classe possède une propriété nommée Format qui permet de spécifier le format du document résultant, c’est‑à‑dire DOC ou DOCX. Pour convertir un fichier PDF au format DOCX, veuillez passer la valeur Docx de l’énumération DocSaveOptions.DocFormat.

{{% alert color="warning" %}}
**Essayez de convertir PDF en DOCX en ligne**

Aspose.PDF for Python vous présente une application en ligne ["PDF vers Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), où vous pouvez essayer d'examiner le fonctionnement et la qualité.

[![Application Aspose.PDF de conversion PDF en Word](/pdf/fr/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Conversions associées

- [Convertir le PDF en Excel](/pdf/fr/python-net/convert-pdf-to-excel/) pour les exportations orientées feuille de calcul.
- [Convertir PDF en PowerPoint](/pdf/fr/python-net/convert-pdf-to-powerpoint/) lorsque vous avez besoin de diapositives de présentation au lieu d’une sortie de traitement de texte.
- [Convertir le PDF en HTML](/pdf/fr/python-net/convert-pdf-to-html/) pour la publication web et les flux de travail de contenu basés sur le navigateur.
