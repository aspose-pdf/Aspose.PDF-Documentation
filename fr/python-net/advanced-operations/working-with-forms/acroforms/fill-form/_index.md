---
title: Remplir AcroForm - Remplir un formulaire PDF en Python
linktitle: Remplir AcroForm
type: docs
weight: 20
url: /fr/python-net/fill-form/
description: Vous pouvez remplir des formulaires dans votre document PDF avec la bibliothèque Aspose.PDF pour Python.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment remplir un champ de formulaire dans un PDF avec Python
Abstract: L'article fournit un guide sur la façon de remplir un champ de formulaire dans un document PDF en utilisant la bibliothèque Aspose.PDF pour Python. Il explique le processus d'accès à un champ de formulaire depuis la collection de formulaires du document et la définition de sa valeur via la propriété Value du champ. Le code d'exemple montre comment ouvrir un document PDF, parcourir ses champs de formulaire pour trouver un champ spécifique par son nom partiel (dans ce cas, "Field 1"), et modifier la valeur d'un TextBoxField en "777". Enfin, le document mis à jour est enregistré dans un fichier de sortie. Des liens vers la documentation pertinente d'Aspose sont fournis pour référence supplémentaire.
---

## Remplir un champ de formulaire dans un document PDF

Le prochain exemple remplit les champs de formulaire PDF avec de nouvelles valeurs en utilisant Aspose.PDF pour Python via .NET et enregistre le document mis à jour. Il prend en charge la mise à jour de plusieurs champs en spécifiant un dictionnaire de noms de champs et de valeurs.

```python

    import aspose.pdf as ap

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    # Define the new field values
    new_field_values = {
        "First Name": "Alexander_New",
        "Last Name": "Greenfield_New",
        "City": "Yellowtown_New",
        "Country": "Redland_New"
    }

    # Create a Form object from the input PDF file
    form = ap.facades.Form(path_infile)

    # Fill out the form fields with the new values
    for formField in form.field_names:
        if formField in new_field_values:
            form.fill_field(formField, new_field_values[formField])

    # Save the modified form to the output PDF file
    form.save(path_outfile)
```



