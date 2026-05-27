---
title: Importer et exporter des données de formulaire
linktitle: Importer et exporter des données de formulaire
type: docs
weight: 80
url: /fr/python-net/import-export-form-data/
description: Importez et exportez les données de champs AcroForm au format XML, FDF, XFDF et JSON en utilisant Aspose.PDF for Python via .NET.
lastmod: "2026-05-22"
TechArticle: true
AlternativeHeadline: Techniques d'importation et d'exportation utilisant Aspose.PDF for Python via .NET.
Abstract: Cette compilation présente une suite complète de techniques d'importation et d'exportation de données de formulaire utilisant Aspose.PDF for Python via .NET. Elle couvre les flux de travail pour l'intégration des formulaires PDF avec des formats de données externes tels que XML, FDF, XFDF et JSON. Les utilisateurs peuvent automatiser le remplissage en masse des formulaires en important des données structurées dans des champs interactifs, ou extraire les valeurs des champs pour l'analyse, la sauvegarde ou l'intégration avec d'autres systèmes. Les exemples montrent comment lier les formulaires PDF, transférer les données entre les formats et enregistrer les documents mis à jour, permettant un traitement de documents évolutif et cohérent dans diverses applications.
---

Cette page montre les flux de travail courants pour l'importation et l'exportation des données AcroForm avec Aspose.PDF for Python via .NET. Toutes les opérations utilisent le [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) façade.

## Importer les données des champs de formulaire depuis XML

Utilisez cette approche pour remplir un formulaire PDF à partir de données XML externes.

1. Créer un `Form` objet.
1. Lier le PDF d'entrée.
1. Ouvrez le fichier de données XML.
1. Importer des données XML dans le formulaire.
1. Enregistrez le PDF mis à jour.

```python
from io import FileIO
import aspose.pdf as ap

def import_data_from_xml(input_file_name, data_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_xml(f)

    form.save(output_file_name)
```

## Exporter les données de FormField vers XML

Cette méthode exporte les valeurs des champs de formulaire d'un document PDF vers XML.

1. Créer un `Form` objet.
1. Lier le PDF d'entrée.
1. Ouvrez le fichier de sortie XML.
1. Exporter les données du formulaire au format XML.

```python
from io import FileIO
import aspose.pdf as ap

def export_data_to_xml(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)
    with FileIO(output_file_name, "w") as f:
        form.export_xml(f)
```

## Importer les données de champs de formulaire à partir du FDF

Le `import_data_from_fdf` Cette méthode importe les données des champs de formulaire depuis un fichier FDF (Formats de données de formulaire) dans un formulaire PDF.

1. Créer un `Form` objet.
1. Lier le PDF d'entrée.
1. Importer les données du formulaire avec `import_fdf()`.
1. Enregistrez le PDF mis à jour.

```python
from io import FileIO
import aspose.pdf as ap

def import_data_from_fdf(input_file_name, data_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_fdf(f)
        form.save(output_file_name)
```

## Exporter les données du FormField vers FDF

Cet exemple exporte les données de formulaire d'un document PDF vers un fichier FDF.

1. Créer un `Form` objet.
1. Lier le document PDF.
1. Exporter les données du formulaire avec `export_fdf()`.

```python
from io import FileIO
import aspose.pdf as ap

def export_data_to_fdf(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(output_file_name, "w") as f:
        form.export_fdf(f)
```

## Importer les données de champ de formulaire depuis XFDF

Utilisez cette méthode pour importer les données des champs de formulaire à partir d'un fichier XFDF (XML Forms Data Format) dans un formulaire PDF.

1. Créer un `Form` objet.
1. Lier le PDF d'entrée.
1. Importer les données de formulaire à partir d’un fichier XFDF.
1. Enregistrez le PDF mis à jour.

```python
from io import FileIO
import aspose.pdf as ap

def import_data_from_xfdf(input_file_name, data_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_xfdf(f)
        form.save(output_file_name)
```

## Exporter les données de champ de formulaire vers XFDF

Ce code exporte les données des champs de formulaire d'un document PDF vers un fichier XFDF.

1. Créer un `Form` objet.
1. Lier le PDF d'entrée.
1. Exporter les données du formulaire vers XFDF.

```python
from io import FileIO
import aspose.pdf as ap

def export_data_to_xfdf(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(output_file_name, "w") as f:
        form.export_xfdf(f)
```

## Importer des données d'un autre PDF

Cet exemple transfère les données de champs de formulaire d'un PDF source vers un PDF de destination en exportant le XFDF vers un flux en mémoire et en l'important dans le formulaire cible.

1. Créer la source et la destination `Form` objets.
1. Liez les PDF source et destination.
1. Exporter les données du formulaire du PDF source.
1. Importer les données du formulaire dans le PDF de destination.
1. Enregistrez le PDF de destination mis à jour.

```python
from io import StringIO
import aspose.pdf as ap

def import_data_from_another_pdf(source_pdf_name, destination_pdf_name, output_file_name):
    form_source = ap.facades.Form()
    form_dest = ap.facades.Form()

    form_source.bind_pdf(source_pdf_name)
    form_dest.bind_pdf(destination_pdf_name)

    with StringIO() as xfdf_stream:
        form_source.export_xfdf(xfdf_stream)
        xfdf_stream.seek(0)
        form_dest.import_xfdf(xfdf_stream)

    form_dest.save(output_file_name)
```

## Extraire les champs de formulaire au format JSON

Cette méthode exporte les champs de formulaire vers un fichier JSON en utilisant `export_json()`.

1. Créer un `Form` objet.
1. Ouvrez le fichier de sortie JSON.
1. Exporter les champs de formulaire en utilisant `export_json()`.

```python
from io import FileIO
import aspose.pdf as ap

def extract_form_fields_to_json(input_file_name, output_file_name):
    form = ap.facades.Form(input_file_name)
    with FileIO(output_file_name, "w") as json_file:
        form.export_json(json_file, True)
```

## Extraire les champs de formulaire vers un document JSON

Cet exemple crée un document JSON personnalisé à partir des noms et valeurs des champs de formulaire.

1. Créez un objet Form à partir du fichier d'entrée.
1. Initialisez un dictionnaire vide pour stocker les données des champs de formulaire.
1. Parcourir tous les champs de formulaire et extraire leurs valeurs.
1. Sérialisez le dictionnaire de données du formulaire en une chaîne JSON avec une indentation de 4 espaces.
1. Écrivez la chaîne JSON dans le fichier de sortie avec l'encodage UTF-8.

```python
import json
import aspose.pdf as ap

def extract_form_fields_to_json_doc(input_file_name, output_file_name):
    form = ap.facades.Form(input_file_name)
    form_data = {}
    for field_name in form.field_names:
        form_data[field_name] = form.get_field(field_name)

    json_string = json.dumps(form_data, indent=4)

    with open(output_file_name, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

## Sujets associés (approche des façades)

- [Importer des données XML](/pdf/fr/python-net/import-xml-data/)
- [Importer les données FDF](/pdf/fr/python-net/import-fdf-data/)
- [Importer les données XFDF](/pdf/fr/python-net/import-xfdf-data/)
- [Importer des données JSON](/pdf/fr/python-net/import-json-data/)
- [Exporter vers XML](/pdf/fr/python-net/export-to-xml/)
- [Exporter vers FDF](/pdf/fr/python-net/export-to-fdf/)
- [Exporter vers XFDF](/pdf/fr/python-net/export-to-xfdf/)
- [Exporter vers JSON](/pdf/fr/python-net/export-to-json/)
