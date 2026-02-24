---
title: Extraire des données d'un tableau dans un PDF avec Python
linktitle: Extraire des données du tableau
type: docs
weight: 40
url: /fr/python-net/extract-data-from-table-in-pdf/
description: Apprenez comment extraire des tableaux d'un PDF à l'aide d'Aspose.PDF pour Python
lastmod: "2025-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment extraire des données d'un tableau dans un PDF via Python
Abstract: Cet article fournit un guide complet sur l'extraction et le traitement programmés de tableaux à partir de documents PDF à l'aide d'Aspose.PDF, une bibliothèque Python. L'article présente un script Python qui ouvre un document PDF, parcourt chaque page et extrait les tableaux en utilisant la classe `TableAbsorber`. Les données de tableau extraites sont ensuite structurées et affichées pour une analyse supplémentaire. Cette section décrit comment extraire des tableaux de zones spécifiquement marquées dans un PDF, comme des zones délimitées par des annotations carrées. Le script identifie ces annotations, initialise le `TableAbsorber` et vérifie si les tableaux se trouvent à l'intérieur des régions annotées avant d'extraire et d'afficher les données. La section finale détaille une méthode pour convertir les données tabulaires extraites d'un PDF en format de fichier CSV.
---

## Extraire des tableaux d'un PDF par programme

Ce code extrait les tableaux d'un PDF et convertit les données tabulaires d'un fichier PDF en un format lisible et structuré pour un traitement ou une analyse ultérieure.

1. Ouverture du document PDF
1. Parcourir les pages du PDF
1. Extraction des données du tableau

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    # Iterate through each page in the document
    for page in document.pages:
        absorber = apdf.text.TableAbsorber()
        absorber.visit(page)

        for table in absorber.table_list:
            print("Table")
            for row in table.row_list:
                row_text = []
                for cell in row.cell_list:
                    cell_text = []
                    for fragment in cell.text_fragments:
                        cell_text.append(
                            "".join(seg.text for seg in fragment.segments)
                        )
                    row_text.append("|".join(cell_text))
                print("|".join(row_text))
```

## Extraire le tableau dans une zone spécifique d'une page PDF

Cet extrait de code extrait les données tabulaires de régions marquées spécifiques dans un PDF, comme des données à l'intérieur d'une zone surlignée ou d'une annotation spécifique.

1. Ouvrir le document PDF
1. Obtenir la première page
1. Trouver la première annotation carrée
1. Initialiser le TableAbsorber
1. Parcourir les tableaux sur la page
1. Vérifier si le tableau se trouve à l'intérieur de la région d'annotation

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    # The path to the documents directory
    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    # Get the first page (index starts from 1 in Aspose.PDF)
    page = document.pages[1]

    # Find the first square annotation
    square_annotation = next(
        (
            ann
            for ann in page.annotations
            if ann.annotation_type == apdf.annotations.AnnotationType.SQUARE
        ),
        None,
    )

    if square_annotation is None:
        print("No square annotation found.")
        return

    # Initialize the TableAbsorber
    absorber = apdf.text.TableAbsorber()
    absorber.visit(page)

    # Iterate through tables on the page
    for table in absorber.table_list:
        table_rect = table.rectangle
        annotation_rect = square_annotation.rect

        # Check if the table is inside the annotation region
        is_in_region = (
            annotation_rect.llx < table_rect.llx
            and annotation_rect.lly < table_rect.lly
            and annotation_rect.urx > table_rect.urx
            and annotation_rect.ury > table_rect.ury
        )

        if is_in_region:
            for row in table.row_list:
                row_text = []
                for cell in row.cell_list:
                    cell_text = []
                    for fragment in cell.text_fragments:
                        cell_text.append(
                            "".join(seg.text for seg in fragment.segments)
                        )
                    row_text.append("|".join(cell_text))
                print("|".join(row_text))
```

## Extraire les données du tableau d'un PDF et les enregistrer dans un fichier Excel

Le fragment de code suivant extrait les données tabulaires d'un PDF et les exporte sous forme de fichier CSV pour une analyse ou une manipulation supplémentaire dans des applications de tableur comme Excel ou Google Sheets.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    excel_save = apdf.ExcelSaveOptions()
    excel_save.format = apdf.ExcelSaveOptions.ExcelFormat.CSV
    document.save(path_outfile, excel_save)
```

