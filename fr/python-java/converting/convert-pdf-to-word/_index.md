---
title: Convertir des PDF en documents Microsoft Word en Python
linktitle: Convertir PDF en Word 2003/2019
type: docs
weight: 10
url: fr/python-java/convert-pdf-to-word/
lastmod: "2023-04-06"
description: Apprenez à écrire du code Python pour la conversion de PDF en formats Microsoft Word avec Aspose.PDF pour Python via .NET et améliorez la conversion PDF en DOC(DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Aperçu

Cet article explique comment **convertir des PDF en documents Microsoft Word en utilisant Python**. Il couvre les sujets suivants.

_Format_: **DOC**
- [Python PDF en DOC](#python-pdf-to-doc)
- [Python Convertir PDF en DOC](#python-pdf-to-doc)
- [Python Comment convertir un fichier PDF en DOC](#python-pdf-to-doc)

_Format_: **DOCX**
- [Python PDF en DOCX](#python-pdf-to-docx)
- [Python Convertir PDF en DOCX](#python-pdf-to-docx)
- [Python Comment convertir un fichier PDF en DOCX](#python-pdf-to-docx)

_Format_: **Word**
- [Python PDF en Word](#python-pdf-to-docx)
- [Python Convertir PDF en Word](#python-pdf-to-doc)

- [Python Comment convertir un fichier PDF en Word](#python-pdf-to-docx)

## Conversion de PDF à DOC et DOCX en Python

L'une des fonctionnalités les plus populaires est la conversion de PDF en DOC de Microsoft Word, ce qui facilite la gestion du contenu. **Aspose.PDF pour Python** vous permet de convertir des fichiers PDF non seulement au format DOC mais aussi au format DOCX, facilement et efficacement.

## Convertir un PDF en fichier DOC (Word 97-2003)

Convertissez un fichier PDF au format DOC avec facilité et contrôle total. Aspose.PDF pour Python est flexible et prend en charge une grande variété de conversions. La conversion de pages de documents PDF en images, par exemple, est une fonctionnalité très populaire.

Une conversion que beaucoup de nos clients ont demandée est le PDF en DOC : convertir un fichier PDF en document Microsoft Word. Les clients le souhaitent car les fichiers PDF ne peuvent pas être facilement modifiés, tandis que les documents Word le peuvent. Certaines entreprises veulent que leurs utilisateurs puissent manipuler le texte, les tableaux et les images dans des fichiers qui ont commencé comme des PDF.

En gardant vivante la tradition de rendre les choses simples et compréhensibles, Aspose.PDF pour Python vous permet de transformer un fichier PDF source en un fichier DOC avec deux lignes de code.
 Pour réaliser cette fonctionnalité, nous avons introduit une énumération nommée SaveFormat et sa valeur .Doc vous permet de sauvegarder le fichier source au format Microsoft Word.

Le fragment de code Python suivant montre le processus de conversion d'un fichier PDF au format DOC.

<a name="csharp-pdf-to-doc"><strong>Étapes : Convertir PDF en DOC en Python</strong></a>

1. Créez une instance de l'objet [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) avec le document PDF source.
2. Enregistrez-le au format [SaveFormat.Doc](https://reference.aspose.com/pdf/python-java/aspose.pdf/saveformat/) en appelant la méthode [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods).

```python

from asposepdf import Api

documentName = "testdata/Hello.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/out.doc"
doc.save(documentOutName, Api.SaveFormat.Doc)
```

### Utilisation de la classe DocSaveOptions

La classe [DocSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/docsaveoptions/) fournit de nombreuses propriétés qui améliorent le processus de conversion des fichiers PDF au format DOC. Parmi ces propriétés, Mode vous permet de spécifier le mode de reconnaissance pour le contenu PDF. Vous pouvez spécifier n'importe quelle valeur de l'énumération RecognitionMode pour cette propriété. Chacune de ces valeurs a des avantages et des limites spécifiques :

```python

from asposepdf import Api

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_doc_with_options.doc"
# Ouvrir le document PDF
document = Api.Document(input_pdf)

save_options = Api.DocSaveOptions()
save_options.format = Api.DocSaveOptions.DocFormat.Doc
# Définir le mode de reconnaissance en tant que Flow
save_options.mode = Api.DocSaveOptions.RecognitionMode.Flow
# Définir la proximité horizontale à 2.5
save_options.relative_horizontal_proximity = 2.5
# Activer la valeur pour reconnaître les puces pendant le processus de conversion
save_options.recognize_bullets = True

# Enregistrer le fichier au format document MS Word
document.save(output_pdf, save_options)

```

{{% alert color="success" %}}
**Essayez de convertir PDF en DOC en ligne**

Aspose.PDF pour Python vous présente l'application gratuite en ligne ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.
[![Convert PDF to DOC](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Convertir PDF en DOCX

Aspose.PDF pour l'API Python vous permet de lire et de convertir des documents PDF en DOCX en utilisant Python via .NET. DOCX est un format bien connu pour les documents Microsoft Word dont la structure a été modifiée d'un binaire simple à une combinaison de fichiers XML et binaires. Les fichiers Docx peuvent être ouverts avec Word 2007 et les versions ultérieures, mais pas avec les versions antérieures de MS Word qui supportent les extensions de fichiers DOC.

Le snippet de code Python suivant montre le processus de conversion d'un fichier PDF en format DOCX.

<a name="csharp-pdf-to-docx"><strong>Étapes : Convertir PDF en DOCX en Python</strong></a>

1. Créez une instance de l'objet [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) avec le document PDF source.

2. Enregistrez-le au format [SaveFormat.DocX](https://reference.aspose.com/pdf/python-java/aspose.pdf/saveformat/) en appelant la méthode [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods).

```python


from asposepdf import Api

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_doc_with_options.docx"
# Ouvrir le document PDF
document = Api.Document(input_pdf)

save_options = Api.DocSaveOptions()
save_options.format = Api.DocSaveOptions.DocFormat.Docx
# Définir le mode de reconnaissance comme Flow
save_options.mode = Api.DocSaveOptions.RecognitionMode.Flow
# Définir la proximité horizontale comme 2.5
save_options.relative_horizontal_proximity = 2.5
# Activer la valeur pour reconnaître les puces lors du processus de conversion
save_options.recognize_bullets = True

# Enregistrer le fichier au format document MS Word
document.save(output_pdf, save_options)
```

La classe [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) a une propriété nommée Format qui offre la possibilité de spécifier le format du document résultant, c'est-à-dire DOC ou DOCX.
 Afin de convertir un fichier PDF au format DOCX, veuillez passer la valeur Docx de l'énumération DocSaveOptions.DocFormat.

{{% alert color="warning" %}}
**Essayez de convertir un PDF en DOCX en ligne**

Aspose.PDF pour Python vous présente l'application en ligne gratuite ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en Word Application Gratuite](/pdf/java/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Voir Aussi 

Cet article couvre également ces sujets. Les codes sont les mêmes que ci-dessus.

_Format_: **Word**
- [Code Python PDF en Word](#python-pdf-to-docx)
- [API Python PDF en Word](#python-pdf-to-docx)
- [Conversion Programmée Python PDF en Word](#python-pdf-to-docx)
- [Bibliothèque Python PDF en Word](#python-pdf-to-docx)
- [Enregistrer un PDF en tant que Word avec Python](#python-pdf-to-docx)
- [Générer un Word à partir d'un PDF avec Python](#python-pdf-to-docx)
- [Créer un Word à partir d'un PDF avec Python](#python-pdf-to-docx)

- [Convertisseur Python PDF en Word](#python-pdf-to-docx)
_Format_: **DOC**
- [Code Python PDF en DOC](#python-pdf-to-doc)
- [API Python PDF en DOC](#python-pdf-to-doc)
- [Programmation Python PDF en DOC](#python-pdf-to-doc)
- [Bibliothèque Python PDF en DOC](#python-pdf-to-doc)
- [Enregistrer PDF en DOC avec Python](#python-pdf-to-doc)
- [Générer DOC à partir de PDF avec Python](#python-pdf-to-doc)
- [Créer DOC à partir de PDF avec Python](#python-pdf-to-doc)
- [Convertisseur Python PDF en DOC](#python-pdf-to-doc)

_Format_: **DOCX**
- [Code Python PDF en DOCX](#python-pdf-to-docx)
- [API Python PDF en DOCX](#python-pdf-to-docx)
- [Programmation Python PDF en DOCX](#python-pdf-to-docx)
- [Bibliothèque Python PDF en DOCX](#python-pdf-to-docx)
- [Enregistrer PDF en DOCX avec Python](#python-pdf-to-docx)
- [Générer DOCX à partir de PDF avec Python](#python-pdf-to-docx)
- [Créer DOCX à partir de PDF avec Python](#python-pdf-to-docx)
- [Convertisseur Python PDF en DOCX](#python-pdf-to-docx)