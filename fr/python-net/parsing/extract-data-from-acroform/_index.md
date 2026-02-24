---
title: Extraire des données d'AcroForm avec Python
linktitle: Extraire des données d'AcroForm
type: docs
weight: 50
url: /fr/python-net/extract-data-from-acroform/
description: Aspose.PDF facilite l'extraction des données des champs de formulaire à partir de fichiers PDF. Apprenez comment extraire les données des AcroForms et les enregistrer au format JSON, XML ou FDF.
lastmod: "2025-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment extraire des données d'AcroForm via Python
Abstract: L'article fournit un guide complet sur l'utilisation d'Aspose.PDF pour Python afin de gérer les champs de formulaire dans les documents PDF. Il détaille différentes méthodes d'extraction, de manipulation et d'exportation des données de formulaire à partir des PDF. L'article commence par démontrer comment extraire les valeurs des champs de formulaire et les stocker dans un dictionnaire, puis restituer les données au format JSON. Il illustre également l'exportation directe des données de formulaire vers des fichiers JSON, renforçant les capacités de sérialisation des données. De plus, l'article couvre l'exportation des données de formulaire vers d'autres formats tels que XML, FDF (Formats de données de formulaire) et XFDF, utiles pour l'échange de données et le stockage structuré. Chaque section comprend des extraits de code Python pour faciliter la compréhension et la mise en œuvre. Dans l'ensemble, l'article constitue une ressource pratique pour les développeurs souhaitant intégrer la gestion des formulaires PDF dans leurs applications Python.
---

## Extraire les champs de formulaire du document PDF

En plus de vous permettre de générer et de remplir des champs de formulaire, Aspose.PDF pour Python facilite l'extraction des données des champs de formulaire ou des informations sur les champs de formulaire à partir de fichiers PDF.

L'extrait de code crée un dictionnaire pour stocker les valeurs de tous les champs du formulaire PDF. Il parcourt les noms des champs du formulaire, récupère leurs valeurs et remplit le dictionnaire avec ces données. Enfin, il affiche les valeurs de formulaire collectées.

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

## Récupérer la valeur du champ de formulaire par le titre

## Extraire les champs de formulaire du document PDF vers JSON

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    with FileIO(path_outfile, "w") as json_file:
        form.export_json(json_file, True)
```

L'extrait de code Python fourni extrait les valeurs de ses champs et sérialise ces données au format JSON. Il importe les modules nécessaires, construit les chemins des fichiers d'entrée et de sortie, récupère les noms et les valeurs des champs du formulaire PDF, puis écrit la chaîne JSON sérialisée dans un fichier de sortie spécifié.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    form_data = {}
    # Get values from all fields
    for formField in form.field_names:
        # Analyze names and values if need
        form_data[formField] = form.get_field(formField)

    # Serialize to JSON
    json_string = json.dumps(form_data, indent=4)

    # Output the JSON string
    print(json_string)

    with open(path_outfile, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

## Extraire les données au format XML à partir d'un fichier PDF

L'extrait de code Python suivant crée un objet formulaire, associe un document PDF à cet objet et exporte les données du formulaire vers un fichier XML. Le code extrait automatiquement les données d'un formulaire PDF et les enregistre dans un format XML structuré.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

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

## Exporter les données au format FDF depuis un fichier PDF

L'extrait de code suivant crée un objet formulaire, associe un document PDF à ce formulaire, puis exporte les données du formulaire vers un fichier FDF (Formats de données de formulaire). Le fichier FDF est un format utilisé pour stocker les données de formulaire provenant de documents PDF, permettant un échange de données facilité.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

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

## Exporter les données au format XFDF depuis un fichier PDF

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

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

