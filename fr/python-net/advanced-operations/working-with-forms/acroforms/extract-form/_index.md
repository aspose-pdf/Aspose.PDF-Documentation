---
title: Extract AcroForm - Extraire les données de formulaire PDF en Python
linktitle: Extraire AcroForm
type: docs
weight: 30
url: /fr/python-net/extract-form/
description: Extrayez le formulaire de votre document PDF avec la bibliothèque Aspose.PDF pour Python. Obtenez la valeur d'un champ individuel du fichier PDF.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment obtenir les données de formulaire à partir d'un PDF avec Python
Abstract: Cet article fournit un guide sur l'extraction des données des champs de formulaire dans un document PDF à l'aide de Python. Il décrit comment parcourir tous les champs en utilisant la bibliothèque Aspose.PDF, notamment en accédant à la collection `Form` et en utilisant le type `Field` ainsi que sa propriété `value`. Un extrait de code Python est inclus, montrant comment ouvrir un document PDF, itérer sur ses champs de formulaire et afficher le nom et la valeur de chaque champ. Cette méthode est utile pour récupérer programmatiquement les données de formulaire des fichiers PDF.
---

## Extraire les données du formulaire

### Obtenir les valeurs de tous les champs du document PDF

Pour obtenir les valeurs de tous les champs d'un document PDF, vous devez parcourir tous les champs de formulaire puis récupérer la valeur à l'aide de la propriété Value. Récupérez chaque champ de la collection Form, dans le type de champ de base appelé [Field](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/) et accédez à sa propriété [value](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/#properties).

Les extraits de code Python suivants montrent comment obtenir les valeurs de tous les champs d'un document PDF.

```python

    import aspose.pdf as ap

    # Construct the full path to the input PDF file
    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)

    # Create a Form object from the PDF file
    form = ap.facades.Form(path_infile)

    # Initialize an empty dictionary to store form values
    form_values = {}

    # Iterate through all form fields in the PDF
    for formField in form.field_names:
        # Retrieve the value for each form field and store in the dictionary
        form_values[formField] = form.get_field(formField)

    # Print and return the extracted form values
    print(form_values)
```

