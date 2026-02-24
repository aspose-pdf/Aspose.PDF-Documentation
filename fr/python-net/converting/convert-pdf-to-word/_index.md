---
title: Convertir des PDF en documents Microsoft Word en Python
linktitle: Convertir PDF en Word
type: docs
weight: 10
url: /fr/python-net/convert-pdf-to-word/
lastmod: "2025-09-27"
description: Apprenez à convertir des documents PDF au format Word en Python en utilisant Aspose.PDF pour une édition facile des documents.
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment convertir un PDF en Word avec Python
Abstract: Cet article fournit un guide complet sur la conversion de fichiers PDF vers les formats Microsoft Word (DOC et DOCX) en Python, en utilisant spécifiquement la bibliothèque Aspose.PDF. Il décrit les avantages de convertir les PDF en documents Word modifiables, permettant une manipulation plus facile du contenu tel que le texte, les tableaux et les images. L'article détaille le processus de conversion de PDF en DOC (format Word 97-2003) et en DOCX, avec des extraits de code démontrant ces conversions en Python. Le processus consiste à créer un objet `Document` à partir du PDF et à l'enregistrer dans le format souhaité à l'aide de la méthode `save()` et de l'énumération `SaveFormat`. De plus, il présente la classe `DocSaveOptions`, qui permet une personnalisation supplémentaire du processus de conversion, comme la spécification des modes de reconnaissance. L'article met également en avant les applications en ligne fournies par Aspose.PDF pour tester la qualité et la fonctionnalité de la conversion. Le contenu comprend un aperçu structuré et des liens vers les sections correspondantes pour chaque format.
---

## Convertir PDF en DOC

L'une des fonctionnalités les plus populaires est la conversion de PDF en DOC Microsoft Word, ce qui facilite la gestion du contenu. **Aspose.PDF for Python via .NET** vous permet de convertir des fichiers PDF non seulement en DOC mais aussi en format DOCX, facilement et efficacement.

La classe [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) offre de nombreuses propriétés qui améliorent le processus de conversion de fichiers PDF en format DOC. Parmi ces propriétés, Mode vous permet de spécifier le mode de reconnaissance du contenu PDF. Vous pouvez spécifier n'importe quelle valeur de l'énumération RecognitionMode pour cette propriété. Chacune de ces valeurs possède des avantages et des limites spécifiques :

Étapes : Convertir PDF en DOC avec Python

1. Chargez le PDF dans un objet 'ap.Document'.
1. Créez une instance de 'DocSaveOptions'.
1. Définissez la propriété format sur 'DocFormat.DOC' pour garantir que la sortie est au format .doc (format Word ancien).
1. Enregistrez le PDF en tant que document Word en utilisant les options d'enregistrement spécifiées.
1. Affichez un message de confirmation.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.DocSaveOptions()
    save_options.format = apdf.DocSaveOptions.DocFormat.DOC
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Essayez de convertir PDF en DOC en ligne**

Aspose.PDF pour Python vous propose une application en ligne gratuite ["PDF en DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), où vous pouvez tester la fonctionnalité et la qualité du service.

[![Convertir PDF en DOC](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Convertir PDF en DOCX

L'API Aspose.PDF pour Python vous permet de lire et de convertir des documents PDF en DOCX en utilisant Python via .NET. DOCX est un format bien connu pour les documents Microsoft Word dont la structure a évolué d'un binaire simple à une combinaison de fichiers XML et binaires. Les fichiers docx peuvent être ouverts avec Word 2007 et les versions ultérieures, mais pas avec les versions antérieures de MS Word qui ne prennent en charge que les extensions de fichier DOC.

Le fragment de code Python suivant montre le processus de conversion d'un fichier PDF au format DOCX.

Étapes : Convertir PDF en DOCX avec Python

1. Chargez le PDF source en utilisant 'ap.Document'.
1. Créez une instance de 'DocSaveOptions'.
1. Définissez la propriété format sur 'DocFormat.DOC_X' pour générer un fichier .docx (format Word moderne).
1. Enregistrez le PDF en fichier DOCX avec les options d'enregistrement configurées.
1. Affichez un message de confirmation après la conversion.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.DocSaveOptions()
    save_options.format = apdf.DocSaveOptions.DocFormat.DOC_X
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

La classe [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) possède une propriété nommée Format qui permet de spécifier le format du document résultant, c’est‑à‑dire DOC ou DOCX. Pour convertir un fichier PDF au format DOCX, veuillez fournir la valeur Docx de l'énumération DocSaveOptions.DocFormat.

{{% alert color="warning" %}}
**Essayez de convertir PDF en DOCX en ligne**

Aspose.PDF pour Python vous propose une application en ligne gratuite ["PDF en Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), où vous pouvez tester la fonctionnalité et la qualité du service.

[![Aspose.PDF Conversion PDF en Word Application gratuite](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

