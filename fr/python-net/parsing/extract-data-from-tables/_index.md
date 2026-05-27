---
title: Extraire des données d'un tableau dans un PDF avec Python
linktitle: Extraire des données d'un tableau
type: docs
weight: 40
url: /fr/python-net/extract-data-from-table-in-pdf/
description: Apprenez comment extraire les données d'un tableau à partir de fichiers PDF avec Aspose.PDF for Python et exporter les résultats pour un traitement ultérieur.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment extraire des données d'un tableau dans un PDF via Python
Abstract: Cet article explique comment extraire et traiter les données de tableau à partir de documents PDF avec Aspose.PDF for Python. Il montre comment analyser chaque page avec TableAbsorber, lire les lignes et les cellules des tableaux détectés, limiter l'extraction à une région annotée spécifique, et exporter le contenu PDF au format CSV pour une utilisation dans des outils de tableur et un traitement en aval.
---

## Extraire des tables d'un PDF de manière programmatique

Utiliser [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) pour détecter les tableaux sur chaque page d'un [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Après avoir visité une page, parcourir `table_list`, puis parcourez chaque ligne et chaque cellule pour reconstruire le contenu du tableau sous un format de texte lisible.

1. Ouvrez le PDF en tant que `Document`.
1. Parcourir les pages de `document.pages`.
1. Créer un `TableAbsorber` pour chaque page et appeler `visit(page)`.
1. Parcourir les tables, les lignes et les cellules détectées.
1. Lire les fragments de texte de chaque cellule et assembler la sortie de ligne extraite.

```python
import aspose.pdf as apdf
from os import path

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
                    cell_text.append("".join(seg.text for seg in fragment.segments))
                row_text.append("|".join(cell_text))
            print("|".join(row_text))
```

## Extraire le tableau dans une zone spécifique de la page PDF

Si vous devez extraire uniquement les tableaux situés à l'intérieur d'une région marquée, combinez [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) avec un [SquareAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation/). Dans cet exemple, le rectangle d'annotation est utilisé comme limite, et seules les tables entièrement contenues dans cette région sont traitées.

1. Ouvrez le PDF en tant que `Document`.
1. Sélectionnez la page cible.
1. Trouvez l'annotation carrée qui marque la région d'intérêt.
1. Créer un `TableAbsorber` et visitez la page.
1. Comparez chaque rectangle de table détecté avec le rectangle d'annotation.
1. Traitez uniquement les tables qui se trouvent entièrement à l'intérieur de la zone marquée.

```python
import aspose.pdf as apdf
from os import path

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
                    cell_text.append("".join(seg.text for seg in fragment.segments))
                row_text.append("|".join(cell_text))
            print("|".join(row_text))
```

## Exporter les données du tableau du PDF en CSV

Lorsque vous avez besoin des données extraites dans un format convivial pour les feuilles de calcul, enregistrez le PDF en utilisant [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) et définissez le format de sortie sur CSV. Le fichier résultant peut être ouvert dans Excel, Google Sheets ou importé dans des flux de travail analytiques.

1. Ouvrez le PDF source en tant que [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Créer un `ExcelSaveOptions` instance.
1. Définir `excel_save.format` à `ExcelSaveOptions.ExcelFormat.CSV`.
1. Enregistrez le document vers le chemin CSV cible.

```python
import aspose.pdf as apdf
from os import path

path_infile = path.join(self.dataDir, infile)
path_outfile = path.join(self.dataDir, outfile)

document = apdf.Document(path_infile)
excel_save = apdf.ExcelSaveOptions()
excel_save.format = apdf.ExcelSaveOptions.ExcelFormat.CSV
document.save(path_outfile, excel_save)
```
