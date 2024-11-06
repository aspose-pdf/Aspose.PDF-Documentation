---
title: Convertir PDF en HTML en Python 
linktitle: Convertir PDF en format HTML
type: docs
weight: 50
url: fr/python-java/convert-pdf-to-html/
lastmod: "2021-11-01"
description: Ce sujet vous montre comment convertir un fichier PDF en format HTML avec la bibliothèque Aspose.PDF pour Python Java.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Vue d'ensemble

Cet article explique comment **convertir un PDF en HTML en utilisant Python**. Il couvre ces sujets.

_Format_: **HTML**
- [Python PDF en HTML](#python-pdf-to-html)
- [Python Convertir PDF en HTML](#python-pdf-to-html)
- [Python Comment convertir un fichier PDF en HTML](#python-pdf-to-html)


## Convertir PDF en HTML

**Aspose.PDF pour Python via .NET** fournit de nombreuses fonctionnalités pour convertir divers formats de fichiers en documents PDF et convertir des fichiers PDF en divers formats de sortie.
 Cet article explique comment convertir un fichier PDF en <abbr title="HyperText Markup Language">HTML</abbr>. Vous pouvez utiliser seulement quelques lignes de code Python pour convertir un PDF en HTML. Vous pouvez avoir besoin de convertir un PDF en HTML si vous souhaitez créer un site Web ou ajouter du contenu à un forum en ligne. Une façon de convertir un PDF en HTML est d'utiliser Python de manière programmatique.

{{% alert color="success" %}}
**Essayez de convertir un PDF en HTML en ligne**

Aspose.PDF pour Python vous présente une application en ligne gratuite ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en HTML avec Application Gratuite](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

<a name="csharp-pdf-to-html"><strong>Étapes : Convertir un PDF en HTML en Python</strong></a>

1. Créez une instance de l'objet [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) avec le document PDF source.
2. Enregistrez-le dans [HtmlSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/htmlsaveoptions/) en appelant la méthode [Document.save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods).

```python
from asposepdf import Api

documentName = "../../testdata/source.pdf"
documentOutName = "../../testout/result.html"
# Ouvrir le document PDF
document = Api.Document(documentName)

# sauvegarder le document au format HTML
save_options = Api.HtmlSaveOptions()
document.save(documentOutName, save_options)
```

## Voir aussi

Cet article couvre également ces sujets. Les codes sont identiques à ceux ci-dessus.

_Format_: **HTML**
- [Code de conversion PDF en HTML avec Python](#python-pdf-to-html)
- [API de conversion PDF en HTML avec Python](#python-pdf-to-html)
- [Conversion PDF en HTML avec Python par programmation](#python-pdf-to-html)
- [Bibliothèque de conversion PDF en HTML avec Python](#python-pdf-to-html)
- [Sauvegarder PDF en HTML avec Python](#python-pdf-to-html)
- [Générer HTML à partir de PDF avec Python](#python-pdf-to-html)
- [Créer HTML à partir de PDF avec Python](#python-pdf-to-html)

- [Convertisseur PDF en HTML avec Python](#python-pdf-to-html)