---
title: Créer AcroForm - Créer un PDF remplissable en Python
linktitle: Créer AcroForm
type: docs
weight: 10
url: /fr/python-net/create-form/
description: Avec Aspose.PDF pour Python, vous pouvez créer un formulaire à partir de zéro dans votre fichier PDF
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment créer un AcroForm dans un PDF en utilisant Python
Abstract: L'article fournit un guide sur la façon de créer un champ de formulaire dans un document PDF en utilisant la bibliothèque Aspose.PDF pour Python. Il présente la classe `Document`, qui contient une collection `Form` pour gérer les champs de formulaire. Le processus d'ajout d'un champ de formulaire consiste à créer le champ souhaité et à utiliser la méthode `add` de la collection `Form`. Un exemple spécifique est fourni pour illustrer l'ajout d'un `TextBoxField` à un document PDF. L'exemple comprend un code détaillé démontrant la création d'un `TextBoxField`, la définition de ses propriétés telles que la position, le nom, la valeur, la bordure et la couleur, puis son ajout au document. Le PDF modifié est ensuite enregistré avec le champ de formulaire nouvellement ajouté.
---

## Créer un formulaire à partir de zéro

### Ajouter un champ de formulaire dans un document PDF

La classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) fournit une collection nommée [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/) qui vous aide à gérer les champs de formulaire dans un document PDF.

Pour ajouter un champ de formulaire :

1. Créez le champ de formulaire que vous souhaitez ajouter.
1. Appelez la méthode [add](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/#methods) de la collection Form.

### Ajout de TextBoxField

L'exemple ci-dessous montre comment ajouter un [TextBoxField](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/).

```python

    import aspose.pdf as ap

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    # Open document
    pdfDocument = ap.Document(path_infile)

    # Create a field
    textBoxField = ap.forms.TextBoxField(pdfDocument.pages[1], ap.Rectangle(100, 200, 300, 300, True))
    textBoxField.partial_name = "textbox1"
    textBoxField.value = "Text Box"

    border = ap.annotations.Border(textBoxField)
    border.width = 5
    border.dash = ap.annotations.Dash(1, 1)
    textBoxField.border = border

    textBoxField.color = ap.Color.green

    # Add field to the document
    pdfDocument.form.add(textBoxField, 1)

    # Save modified PDF
    pdfDocument.save(path_outfile)
```


