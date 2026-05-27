---
title: Extraire AcroForm - Extraire les données du formulaire du PDF en Python
linktitle: Extraire AcroForm
type: docs
weight: 30
url: /fr/python-net/extract-form/
description: Extraire les valeurs des champs AcroForm dans les documents PDF en utilisant Aspose.PDF for Python via .NET.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment obtenir les données du formulaire d'un PDF en utilisant Python
Abstract: Cet article montre comment extraire les données des champs AcroForm dans les documents PDF en utilisant Aspose.PDF for Python via .NET. L'exemple parcourt les noms des champs de formulaire, lit les valeurs en utilisant la façade Form, et renvoie un dictionnaire pour le traitement en aval. Ce flux de travail est utile pour le reporting, la validation et l'intégration avec des systèmes externes.
---

## Extraire les données du Form

### Obtenir les valeurs de tous les champs d'un document PDF

Pour lire les valeurs de tous les champs d'un document PDF, parcourez les noms des champs du formulaire et récupérez chaque valeur depuis le [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) façade.

Utilisez les étapes suivantes :

1. Lier le PDF d'entrée à un `Form` objet.
1. Parcourir `field_names`.
1. Lire chaque valeur avec `get_field()`.
1. Stocker les valeurs dans un dictionnaire.
1. Retourner ou traiter les valeurs extraites.

L'extrait de code Python suivant montre cette approche.

```python
import aspose.pdf as ap


def get_values_from_all_fields(input_file_name):
    form = ap.facades.Form(input_file_name)

    form_values = {}
    for field_name in form.field_names:
        form_values[field_name] = form.get_field(field_name)

    print(form_values)
    return form_values
```

## Sujets associés

- [Créer AcroForm](/pdf/fr/python-net/create-form/)
- [Remplir AcroForm](/pdf/fr/python-net/fill-form/)
- [Importer et exporter des données de formulaire](/pdf/fr/python-net/import-export-form-data/)
- [Modification d'AcroForm](/pdf/fr/python-net/modifying-form/)