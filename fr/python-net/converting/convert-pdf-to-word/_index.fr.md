---
title: Convertir des PDF en Documents Microsoft Word en Python
linktitle: Convertir PDF en Word 2003/2019
type: docs
weight: 10
url: /python-net/convert-pdf-to-word/
lastmod: "2022-12-23"
description: Apprenez à écrire du code Python pour la conversion de formats PDF en Microsoft Word avec Aspose.PDF pour Python via .NET et optimisez la conversion PDF en DOC(DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Vue d'ensemble

Cet article explique comment **convertir des PDF en documents Microsoft Word en utilisant Python**. Il couvre ces sujets.

_Format_: **DOC**
- [PDF à DOC en Python](#python-pdf-to-doc)
- [Convertir PDF en DOC en Python](#python-pdf-to-doc)
- [Comment convertir un fichier PDF en DOC en Python](#python-pdf-to-doc)

_Format_: **DOCX**
- [PDF à DOCX en Python](#python-pdf-to-docx)
- [Convertir PDF en DOCX en Python](#python-pdf-to-docx)
- [Comment convertir un fichier PDF en DOCX en Python](#python-pdf-to-docx)

_Format_: **Word**
- [PDF à Word en Python](#python-pdf-to-docx)
- [Convertir PDF en Word en Python](#python-pdf-to-doc)
- [Comment convertir un fichier PDF en Word en Python](#python-pdf-to-docx)

## Conversion de PDF à DOC et DOCX en Python

L'une des fonctionnalités les plus populaires est la conversion de PDF en DOC de Microsoft Word, ce qui facilite la gestion du contenu. **Aspose.PDF pour Python** vous permet de convertir des fichiers PDF non seulement en DOC mais aussi en format DOCX, facilement et efficacement.

## Convertir un PDF en fichier DOC (Word 97-2003)

Convertissez un fichier PDF en format DOC avec aisance et contrôle total. Aspose.PDF pour Python est flexible et prend en charge une grande variété de conversions. Par exemple, la conversion de pages de documents PDF en images est une fonctionnalité très populaire.

Une conversion que beaucoup de nos clients ont demandée est la conversion de PDF à DOC : convertir un fichier PDF en document Microsoft Word. Les clients veulent cela parce que les fichiers PDF ne peuvent pas être facilement modifiés, tandis que les documents Word le peuvent. Certaines entreprises souhaitent que leurs utilisateurs puissent manipuler le texte, les tableaux et les images dans des fichiers qui ont commencé comme des PDF.

En gardant vivante la tradition de rendre les choses simples et compréhensibles, Aspose.PDF pour Python vous permet de transformer un fichier PDF source en fichier DOC avec deux lignes de code.
 Pour accomplir cette fonctionnalité, nous avons introduit une énumération nommée SaveFormat et sa valeur .Doc vous permet de sauvegarder le fichier source au format Microsoft Word.

Le snippet de code Python suivant montre le processus de conversion d'un fichier PDF en format DOC.

<a name="csharp-pdf-to-doc"><strong>Étapes : Convertir PDF en DOC en Python</strong></a>

1. Créez une instance de l'objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) avec le document PDF source.
2. Enregistrez-le au format [SaveFormat](https://reference.aspose.com/pdf/python-net/aspose.pdf/saveformat/) en appelant la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_doc.doc"
    # Ouvrir le document PDF
    document = ap.Document(input_pdf)
    # Enregistrer le fichier au format document MS Word
    document.save(output_pdf, ap.SaveFormat.DOC)
```

### Utilisation de la classe DocSaveOptions

La classe [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) fournit de nombreuses propriétés qui améliorent le processus de conversion des fichiers PDF en format DOC. Parmi ces propriétés, Mode vous permet de spécifier le mode de reconnaissance pour le contenu PDF. Vous pouvez spécifier n'importe quelle valeur de l'énumération RecognitionMode pour cette propriété. Chacune de ces valeurs a des avantages et des limitations spécifiques :

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_doc_with_options.doc"
    # Ouvrir le document PDF
    document = ap.Document(input_pdf)

    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC
    # Définir le mode de reconnaissance comme Flow
    save_options.mode = ap.DocSaveOptions.RecognitionMode.FLOW
    # Définir la proximité horizontale à 2.5
    save_options.relative_horizontal_proximity = 2.5
    # Activer la reconnaissance des puces lors du processus de conversion
    save_options.recognize_bullets = True

    # Enregistrer le fichier au format document MS Word
    document.save(output_pdf, save_options)
```

{{% alert color="success" %}}
**Essayez de convertir PDF en DOC en ligne**

Aspose.PDF pour Python vous présente l'application en ligne gratuite ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.
[![Convert PDF to DOC](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc) {{% /alert %}}

## Convertir PDF en DOCX

Aspose.PDF pour Python API vous permet de lire et de convertir des documents PDF en DOCX à l'aide de Python via .NET. DOCX est un format bien connu pour les documents Microsoft Word dont la structure est passée d'un binaire simple à une combinaison de fichiers XML et binaires. Les fichiers DOCX peuvent être ouverts avec Word 2007 et les versions ultérieures, mais pas avec les versions antérieures de MS Word qui prennent en charge les extensions de fichiers DOC.

Le fragment de code Python suivant montre le processus de conversion d'un fichier PDF en format DOCX.

<a name="csharp-pdf-to-docx"><strong>Étapes : Convertir PDF en DOCX en Python</strong></a>

1. Créez une instance de l'objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) avec le document PDF source.

2. Enregistrez-le au format [SaveFormat](https://reference.aspose.com/pdf/python-net/aspose.pdf/saveformat/) en appelant la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_docx_options.docx"
    # Ouvrir le document PDF
    document = ap.Document(input_pdf)

    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC_X
    # Définir le mode de reconnaissance comme Flow
    save_options.mode = ap.DocSaveOptions.RecognitionMode.FLOW
    # Définir la proximité horizontale à 2.5
    save_options.relative_horizontal_proximity = 2.5
    # Activer la valeur pour reconnaître les puces pendant le processus de conversion
    save_options.recognize_bullets = True

    # Enregistrer le fichier au format document MS Word
    document.save(output_pdf, save_options)
```

La classe [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) a une propriété nommée Format qui offre la possibilité de spécifier le format du document résultant, c'est-à-dire, DOC ou DOCX.
 Afin de convertir un fichier PDF au format DOCX, veuillez passer la valeur Docx de l'énumération DocSaveOptions.DocFormat.

{{% alert color="warning" %}}
**Essayez de convertir un PDF en DOCX en ligne**

Aspose.PDF pour Python vous présente l'application en ligne gratuite ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en Word Application Gratuite](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Voir Aussi

Cet article couvre également ces sujets. Les codes sont les mêmes que ci-dessus.

_Format_: **Word**
- [Python PDF en Code Word](#python-pdf-to-docx)
- [Python PDF en API Word](#python-pdf-to-docx)
- [Python PDF en Word Programmatiquement](#python-pdf-to-docx)
- [Python PDF en Bibliothèque Word](#python-pdf-to-docx)
- [Python Enregistrer PDF en Word](#python-pdf-to-docx)
- [Python Générer Word à partir de PDF](#python-pdf-to-docx)
- [Python Créer Word à partir de PDF](#python-pdf-to-docx)

- [Python PDF en Convertisseur Word](#python-pdf-to-docx)
_Format_: **DOC**
- [Code Python PDF vers DOC](#python-pdf-to-doc)
- [API Python PDF vers DOC](#python-pdf-to-doc)
- [Python PDF vers DOC Programmatiquement](#python-pdf-to-doc)
- [Bibliothèque Python PDF vers DOC](#python-pdf-to-doc)
- [Python Enregistrer PDF en tant que DOC](#python-pdf-to-doc)
- [Python Générer DOC à partir de PDF](#python-pdf-to-doc)
- [Python Créer DOC à partir de PDF](#python-pdf-to-doc)
- [Convertisseur Python PDF vers DOC](#python-pdf-to-doc)

_Format_: **DOCX**
- [Code Python PDF vers DOCX](#python-pdf-to-docx)
- [API Python PDF vers DOCX](#python-pdf-to-docx)
- [Python PDF vers DOCX Programmatiquement](#python-pdf-to-docx)
- [Bibliothèque Python PDF vers DOCX](#python-pdf-to-docx)
- [Python Enregistrer PDF en tant que DOCX](#python-pdf-to-docx)
- [Python Générer DOCX à partir de PDF](#python-pdf-to-docx)
- [Python Créer DOCX à partir de PDF](#python-pdf-to-docx)
- [Convertisseur Python PDF vers DOCX](#python-pdf-to-docx)