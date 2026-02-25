---
title: Importer et exporter des données de formulaire
type: docs
weight: 80
url: /fr/python-net/import-export-form-data/
description: Cette section explique comment importer et exporter des données de formulaire.
lastmod: "2025-08-05"
TechArticle: true
AlternativeHeadline: Techniques d'importation et d'exportation utilisant Aspose.PDF pour Python via .NET.
Abstract: Cette compilation présente une suite complète de techniques d'importation et d'exportation de données de formulaire utilisant Aspose.PDF pour Python via .NET. Elle couvre les flux de travail pour intégrer les formulaires PDF à des formats de données externes, notamment XML, FDF, XFDF et JSON. Les utilisateurs peuvent automatiser le remplissage massif de formulaires en important des données structurées dans les champs interactifs, ou extraire les valeurs des champs pour l'analyse, la sauvegarde ou l'intégration avec d'autres systèmes. Les exemples montrent comment lier les formulaires PDF, transférer les données entre les formats et enregistrer les documents mis à jour, permettant un traitement de documents évolutif et cohérent dans diverses applications.
---

## Importer des données de formulaire à partir d'un fichier XML

Le prochain exemple montre comment importer des données de formulaire à partir d'un fichier XML dans un formulaire PDF existant à l'aide d'Aspose.PDF pour Python. En liant un formulaire PDF, en chargeant les données XML et en enregistrant le fichier mis à jour, vous pouvez rapidement remplir les champs interactifs sans modifier manuellement chaque page. Cette méthode est idéale pour automatiser le remplissage massif de formulaires, traiter de grands ensembles de données et garantir la cohérence des données à travers plusieurs documents.

Utilisez les étapes suivantes :

1. Créez un objet Form en utilisant Aspose.PDF.
1. Liez le formulaire PDF.
1. Chargez les données XML.
1. Importez le XML dans le PDF.
1. Enregistrez le PDF mis à jour.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    # Define the working directory path
    workdir_path = "/path/to/working/directory"

    # Construct full file paths using the working directory
    path_infile = path.join(workdir_path, infile)
    path_datafile = path.join(workdir_path, datafile)
    path_outfile = path.join(workdir_path, outfile)

    # Create a Form object from Aspose.PDF
    form = ap.facades.Form()

    # Bind the input PDF form
    form.bind_pdf(path_infile)

    # Import XML data into the form
    with FileIO(path_datafile, "r") as f:
        form.import_xml(f)

    # Save the form with imported data to a new PDF file
    form.save(path_outfile)
```

## Exporter les données de champ de formulaire d'un document PDF vers un fichier XML

La bibliothèque Python montre comment exporter les données de champ de formulaire d'un document PDF vers un fichier XML à l'aide d'Aspose.PDF pour Python. En liant un formulaire PDF et en enregistrant ses valeurs de champ au format XML, vous pouvez facilement stocker, traiter ou réutiliser les données du formulaire dans d'autres applications ou flux de travail. Cette approche est idéale pour la sauvegarde des données, l'analyse et l'intégration avec des systèmes externes.

Utilisez les étapes suivantes :

1. Créez un objet Form en utilisant Aspose.PDF.
1. Liez le formulaire PDF
1. Exportez les données de formulaire
1. Enregistrez les valeurs des champs en XML

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    # Combine the working directory path with the input PDF file name
    path_infile = path.join(self.workdir_path, infile)

    # Combine the working directory path with the output XML file name
    path_outfile = path.join(self.workdir_path, datafile)

    # Create a Form object to work with PDF form fields
    form = ap.facades.Form()

    # Bind the PDF document containing the form
    form.bind_pdf(path_infile)

    # Open the XML file in write mode to store exported form data
    with FileIO(path_outfile, "w") as f:
        # Export form field data from the PDF to the XML file
        form.export_xml(f)
```

## Importer les données de champ de formulaire à partir d'un FDF

La méthode 'import_data_from_fdf' importe les données de champ de formulaire à partir d'un fichier FDF (Formats de données de formulaires) dans un formulaire PDF existant et enregistre le document mis à jour. Cette approche est utile pour pré-remplir ou mettre à jour des formulaires PDF de manière programmatique sans modifier la structure du document.

Utilisez les étapes suivantes :

1. Créez un objet Form en utilisant Aspose.PDF.
1. Liez le PDF d'entrée.
1. Importez les données du formulaire avec import_fdf().
1. Enregistrez le PDF avec les données importées vers le chemin de fichier de sortie spécifié.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_datafile = path.join(self.workdir_path, datafile)
    path_outfile = path.join(self.workdir_path, outfile)

    form = ap.facades.Form()
    form.bind_pdf(path_infile)

    with FileIO(path_datafile, "r") as f:
        form.import_fdf(f)
        form.save(path_outfile)
```

## Exporter les données de champ de formulaire vers FDF

Cet exemple montre comment exporter les données de formulaire d'un document PDF vers un fichier FDF (Formats de données de formulaires) en utilisant Aspose.PDF pour Python via .NET.

1. Créez un objet Form en utilisant Aspose.PDF.
1. Liez le document PDF.
1. Exportez les données du formulaire avec export_fdf().

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form = ap.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an FDF file
    with FileIO(path_outfile, "w") as f:
        form.export_fdf(f)
```

## Importer les données de champ de formulaire à partir d'un XFDF

Cet exemple exporte les données de champ de formulaire d'un document PDF vers un fichier XFDF (XML Forms Data Format) puis enregistre le PDF mis à jour en utilisant Aspose.PDF pour Python via .NET.

1. Créez un objet Form en utilisant Aspose.PDF.
1. Liez le document PDF au formulaire.
1. Exportez les données du formulaire vers un fichier XFDF.
1. Enregistrez le formulaire traité.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_datafile = path.join(self.workdir_path, datafile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form = ap.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an XFDF file
    with FileIO(path_datafile, "w") as f:
        form.export_xfdf(f)
        form.save(path_outfile)
```

## Exporter les données de champ de formulaire vers XFDF

Ce code extrait les données de champ de formulaire d'un document PDF et les exporte dans un fichier XFDF (XML Forms Data Format) en utilisant Aspose.PDF pour Python.

1. Créez un objet Form en utilisant Aspose.PDF.
1. Liez le document PDF au formulaire.
1. Exportez les données du formulaire vers un fichier FDF.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form = ap.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an FDF file
    with FileIO(path_outfile, "w") as f:
        form.export_xfdf(f)
```

## Importer des données d'un autre PDF

Cet extrait de code montre comment transférer les données de champ de formulaire d'un PDF source vers un PDF cible. Les données du formulaire sont exportées vers un flux XFDF depuis le PDF source puis importées dans le PDF cible en utilisant Aspose.PDF pour Python via .NET.

1. Créez un objet Form en utilisant Aspose.PDF.
1. Liez le document PDF au formulaire.
1. Exportez les données du formulaire du PDF source.
1. Importez les données du formulaire dans le PDF de destination.
1. Enregistrez le PDF de destination mis à jour.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form_source = ap.facades.Form()
    form_dest = ap.facades.Form()

    # Bind PDF document
    form_source.bind_pdf(path_infile)
    form_dest.bind_pdf(path_outfile)

    # Export form data to an FDF file
    with StringIO() as f:
        form_source.export_xfdf(f)
        form_dest.import_xfdf(f)
        form_dest.save()
```

## Extraire les champs de formulaire en Json

Cette méthode extrait les champs de formulaire d'un fichier d'entrée et les exporte vers un fichier JSON.

1. Créez un objet Form en utilisant Aspose.PDF.
1. Ouvrez le fichier de sortie en mode écriture en utilisant FileIO().
1. Exportez les champs du formulaire vers le fichier JSON en utilisant la méthode form.export_json().

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    form = ap.facades.Form(path_infile)
    with FileIO(path_outfile, "w") as json_file:
        form.export_json(json_file, True)
```

## Extraire les champs de formulaire vers le document JSON

1. Créez un objet Form à partir du fichier d'entrée.
1. Initialise un dictionnaire vide pour stocker les données des champs du formulaire.
1. Parcourez tous les champs du formulaire et extrayez leurs valeurs.
1. Sérialisez le dictionnaire de données du formulaire en une chaîne JSON avec une indentation de 4 espaces.
1. Écrivez la chaîne JSON dans le fichier de sortie avec l'encodage UTF-8.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    form = ap.facades.Form(path_infile)
    form_data = {}
    # Get values from all fields
    for formField in form.field_names:
        # Analyze names and values if needed
        form_data[formField] = form.get_field(formField)

    # Serialize to JSON
    json_string = json.dumps(form_data, indent=4)

    with open(path_outfile, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

