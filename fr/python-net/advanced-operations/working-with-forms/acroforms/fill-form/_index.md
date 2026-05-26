---
title: Remplir AcroForm - Remplir le formulaire PDF à l'aide de Python
linktitle: Remplir AcroForm
type: docs
weight: 20
url: /fr/python-net/fill-form/
description: Remplir les champs AcroForm dans un document PDF en utilisant Aspose.PDF for Python via .NET.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment remplir un champ de formulaire dans PDF à l'aide de Python
Abstract: Cet article explique comment remplir les champs AcroForm dans un document PDF en utilisant Aspose.PDF for Python via .NET. L'exemple utilise la façade Form, mappe les noms de champs à de nouvelles valeurs dans un dictionnaire, met à jour les champs correspondants et enregistre le PDF de sortie. Cette approche est utile pour les flux de travail automatisés de remplissage de documents et le traitement en masse des formulaires.
---

## Remplir le champ de formulaire dans un document PDF

L'exemple suivant remplit plusieurs champs dans un formulaire PDF existant en utilisant le [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) façade.

Utilisez les étapes suivantes :

1. Créez un dictionnaire avec les noms de champs et les valeurs.
1. Liez le PDF d'entrée à un objet Form.
1. Parcourez les champs de formulaire disponibles.
1. Remplissez les champs qui existent dans le dictionnaire.
1. Enregistrez le PDF mis à jour.

```python
import aspose.pdf as ap

def fill_form(input_file_name, output_file_name):
    new_field_values = {
        "First Name": "Alexander_New",
        "Last Name": "Greenfield_New",
        "City": "Yellowtown_New",
        "Country": "Redland_New",
    }

    form = ap.facades.Form(input_file_name)

    for field_name in form.field_names:
        if field_name in new_field_values:
            form.fill_field(field_name, new_field_values[field_name])

    form.save(output_file_name)
```

## Sujets associés

- [Créer AcroForm](/pdf/fr/python-net/create-form/)
- [Extraire AcroForm](/pdf/fr/python-net/extract-form/)
- [Importer et exporter les données du Form](/pdf/fr/python-net/import-export-form-data/)