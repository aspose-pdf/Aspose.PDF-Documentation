---
title: Extraire des données d'AcroForm avec Python
linktitle: Extraire des données d'AcroForm
type: docs
weight: 50
url: /fr/python-net/extract-data-from-acroform/
description: Aspose.PDF facilite l'extraction des données de champs de formulaire à partir de fichiers PDF. Apprenez comment extraire les données des AcroForms et les enregistrer au format JSON, XML ou FDF.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment extraire des données d'AcroForm via Python
Abstract: L'article fournit un guide complet sur l'utilisation d'Aspose.PDF for Python pour gérer les champs de formulaire dans les documents PDF. Il détaille diverses méthodes d'extraction, de manipulation et d'exportation des données de formulaire à partir de PDFs. L'article commence par démontrer comment extraire les valeurs des champs de formulaire et les stocker dans un dictionnaire, puis les sortir au format JSON. Il illustre également l'exportation directe des données de formulaire vers des fichiers JSON, améliorant les capacités de sérialisation des données. De plus, l'article couvre l'exportation des données de formulaire vers d'autres formats tels que XML, FDF (Forms Data Format) et XFDF, qui sont utiles pour l'échange de données et le stockage structuré. Chaque section comprend des extraits de code Python pour faciliter la compréhension et la mise en œuvre. Dans l'ensemble, l'article constitue une ressource pratique pour les développeurs souhaitant intégrer la manipulation de formulaires PDF dans leurs applications Python.
---

## Extraire les champs de formulaire du document PDF

[Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) de `aspose.pdf.facades` namespace fournit un moyen simple de lire les données des champs AcroForm sans ouvrir le modèle complet d’objet du document. Itérer sur `form.field_names` pour obtenir chaque nom de champ présent dans le formulaire, puis appeler `form.get_field(name)` pour récupérer sa valeur actuelle.

1. Construire un `Form` objet en passant le chemin du fichier d'entrée.
1. Itérer sur `form.field_names` pour énumérer tous les noms de champs.
1. Appeler `form.get_field(name)` pour chaque nom et stockez le résultat dans un dictionnaire.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = self.dataDir + infile
    form = apdf.facades.Form(path_infile)

    form_values = {}
    # Get values from all fields
    for formField in form.field_names:
        # Analyze names and values if needed
        form_values[formField] = form.get_field(formField)

    print(form_values)
```

## Récupérer la valeur du champ de formulaire par titre

Lorsque vous connaissez le nom exact du champ (title) défini dans le formulaire PDF, vous pouvez récupérer sa valeur directement avec `form.get_field(name)` sans parcourir l'intégralité de la collection de champs. C’est l'approche la plus rapide lorsque seuls des champs spécifiques sont nécessaires.

1. Construire un [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) objet contenant le chemin du fichier d'entrée.
1. Appeler `form.get_field("FieldName")` en utilisant le titre exact du champ tel qu'il apparaît dans le PDF.
1. Utilisez la valeur de chaîne retournée selon les besoins dans votre application.

```python

    import aspose.pdf as apdf

    form = apdf.facades.Form(path_infile)

    # Retrieve a single field value by its name
    value = form.get_field("FirstName")
    print(value)
```

## Extraire les champs de formulaire du document PDF vers JSON

Il existe deux façons d'exporter les données AcroForm en JSON. La première utilise la fonction intégrée `export_json` méthode sur [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form), qui sérialise toutes les données de champ directement vers un flux de fichier en un seul appel.

1. Construire un `Form` objet contenant le chemin du fichier d'entrée.
1. Ouvrez le fichier de sortie en tant que flux binaire en utilisant `FileIO`.
1. Appeler `form.export_json(stream, True)` écrire la sortie JSON.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    with FileIO(path_outfile, "w") as json_file:
        form.export_json(json_file, True)
```

La deuxième approche construit un dictionnaire Python à partir de `field_names` et `get_field`, puis le sérialise avec `json.dumps`. Utilisez ceci lorsque vous devez transformer ou filtrer les données avant de les écrire.

1. Itérer sur `form.field_names` et remplissez un dictionnaire avec les valeurs des champs.
1. Sérialiser le dictionnaire avec `json.dumps(form_data, indent=4)`.
1. Écrivez la chaîne JSON résultante dans le fichier de sortie.

```python

    import aspose.pdf as apdf
    from os import path
    import json

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    form_data = {}
    # Get values from all fields
    for formField in form.field_names:
        form_data[formField] = form.get_field(formField)

    # Serialize to JSON
    json_string = json.dumps(form_data, indent=4)
    print(json_string)

    with open(path_outfile, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

## Extraire des données au format XML à partir d'un fichier PDF

L'exportation XML est utile pour intégrer les données de formulaire PDF aux systèmes qui consomment des flux XML structurés ou des schémas. Le [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) classe fournit `export_xml` pour gérer la conversion en une seule étape.

1. Créer un `Form` instance et lier le PDF avec `form.bind_pdf(path)`.
1. Ouvrez le fichier de sortie en tant que flux binaire.
1. Appeler `form.export_xml(stream)` pour écrire toutes les données des champs au format XML.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Create Form object
    form = apdf.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export data to XML file
    with FileIO(path_outfile, "w") as f:
        form.export_xml(f)
```

## Exporter les données vers le format FDF à partir d'un fichier PDF

FDF (Forms Data Format) est le format d'échange standard pour les données AcroForm et est largement pris en charge par les visionneuses PDF et les outils de traitement. Utilisez `export_fdf` sur le [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) classe pour produire un fichier FDF autonome qui peut être importé de nouveau dans le PDF original ou dans un autre formulaire compatible.

1. Créer un `Form` instanciez et liez le PDF source avec `form.bind_pdf(path)`.
1. Ouvrez le fichier de sortie en tant que flux binaire.
1. Appeler `form.export_fdf(stream)` pour écrire les données FDF.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Create Form object
    form = apdf.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an FDF file
    with FileIO(path_outfile, "w") as f:
        form.export_fdf(f)
```

## Exporter les données vers XFDF à partir d'un fichier PDF

XFDF (XML Forms Data Format) est le successeur basé sur XML du FDF et est mieux adapté à une utilisation dans les services Web et les pipelines de données modernes. Comme le FDF, un fichier XFDF peut être importé de nouveau dans un formulaire PDF compatible. Utilisez `export_xfdf` sur le [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) classe pour générer la sortie.

1. Créer un `Form` instanciez et liez le PDF source avec `form.bind_pdf(path)`.
1. Ouvrez le fichier de sortie en tant que flux binaire.
1. Appeler `form.export_xfdf(stream)` écrire les données XFDF.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Create Form object
    form = apdf.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an XFDF file
    with FileIO(path_outfile, "w") as f:
        form.export_xfdf(f)
```
