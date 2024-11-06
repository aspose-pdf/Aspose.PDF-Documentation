---
title: Convertir HTML en PDF avec Python
linktitle: Convertir un fichier HTML en PDF
type: docs
weight: 40
url: fr/python-java/convert-html-to-pdf/
lastmod: "2023-04-06"
description: Ce sujet vous montre comment convertir HTML en PDF et MHTML en PDF en utilisant Aspose.PDF pour Python.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Aperçu

Aspose.PDF pour Python via Java est une solution professionnelle qui vous permet de créer des fichiers PDF à partir de pages web et de code HTML brut dans vos applications.

Cet article explique comment **convertir HTML en PDF en utilisant Python**. Il couvre les sujets suivants.

_Format_: **HTML**
- [Python HTML en PDF](#python-html-to-pdf)
- [Python Convertir HTML en PDF](#python-html-to-pdf)
- [Python Comment convertir HTML en PDF](#python-html-to-pdf)

## Conversion de HTML en PDF avec Python

**Aspose.PDF pour Python** est une API de manipulation de PDF qui vous permet de convertir facilement n'importe quel document HTML existant en PDF. Le processus de conversion de HTML en PDF peut être personnalisé de manière flexible.

## Convertir HTML en PDF

L'exemple de code Python suivant montre comment convertir un document HTML en PDF.

1. Créez une instance de la classe [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/).
2. Initialisez l'objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
3. Enregistrez le document PDF de sortie en appelant la méthode **Document.Save()**.

```python

from asposepdf import Api


# initier la licence
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# conversion à partir d'un tableau d'octets
documentName = "input.html"
with open(documentName, "rb") as file:
    byte_array = file.read()
doc = Api.Document(byte_array, Api.LoadFormat.HTML)
documentOutName = "result_fromHtml.pdf"
doc.save(documentOutName)

# conversion à partir d'un fichier
documentName = "input.html"
doc = Api.Document(documentName, Api.LoadFormat.HTML)
documentOutName = "result2_fromHtml.pdf"
doc.save(documentOutName)
```

{{% alert color="success" %}}
**Essayez de convertir HTML en PDF en ligne**


Aspose vous présente l'application en ligne gratuite ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion HTML to PDF using Free App](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}