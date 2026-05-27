---
title: Manipuler les tables dans les documents PDF existants
linktitle: Manipuler des tables
type: docs
weight: 40
url: /fr/python-net/manipulating-tables/
description: Apprenez comment inspecter et modifier les tables dans les documents PDF existants à l'aide de Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Inspectez et modifiez les tables PDF existantes avec Python
Abstract: Cet article explique comment manipuler les tables déjà présentes dans les documents PDF à l'aide d'Aspose.PDF for Python via .NET. Apprenez à localiser les tables avec TableAbsorber, à accéder aux lignes et cellules spécifiques, à mettre à jour le contenu texte des tables et à enregistrer le PDF modifié en Python.
---

## Manipuler les tables dans le PDF existant

Aspose.PDF for Python via .NET vous permet de mettre à jour les tables qui existent déjà dans un document PDF. Vous pouvez utiliser le [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) classe pour trouver les tables sur une page, accéder aux lignes et aux cellules, modifier le contenu texte et enregistrer le fichier mis à jour.

Utilisez cette page lorsque vous devez mettre à jour le contenu des tables existantes dans les PDF sans recréer la mise en page complète du document.

## Trouver et remplacer le texte dans les cellules de tables PDF

Cet exemple trouve la première table de la page 1, accède à la première cellule, remplace son texte et enregistre le PDF de sortie.

1. Ouvrez le PDF d'entrée.
1. Créez un TableAbsorber et visitez la page 1.
1. Assurez-vous qu'au moins une table est détectée.
1. Accédez à la première cellule de la première ligne de la première table.
1. Assurez-vous que la cellule contient des fragments de texte, puis mettez à jour le premier fragment.
1. Enregistrez le PDF modifié.

```python
import aspose.pdf as ap

def replace_cell_text(infile: str, outfile: str) -> None:
    """Replace text in the first cell of the first detected table."""
    # Open PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    if len(absorber.table_list) == 0:
        raise ValueError("No tables were found on page 1.")

    first_cell = absorber.table_list[0].row_list[0].cell_list[0]
    if len(first_cell.text_fragments) == 0:
        raise ValueError("The target cell has no text fragments.")

    # Change text of the first text fragment in the cell
    first_cell.text_fragments[0].text = "New Value"

    # Save PDF document
    document.save(outfile)
```

## Remplacer un tableau existant par un nouveau tableau

Vous pouvez également remplacer un tableau détecté par un tableau nouvellement créé. Cette approche est utile lorsque la structure et le contenu doivent tous les deux changer.

Le code ci-dessous ouvre un PDF, trouve le premier tableau à la page 1, crée un tableau de remplacement, échange l’ancien tableau avec le nouveau, puis enregistre le résultat.

```python
import aspose.pdf as ap

def replace_table(infile: str, outfile: str) -> None:
    """Replace an entire table with a new one."""
    # Open PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    if len(absorber.table_list) == 0:
        raise ValueError("No tables were found on page 1.")

    # Get first table on the page
    old_table = absorber.table_list[0]

    # Create new table
    new_table = ap.Table()
    new_table.column_widths = "100 100 100"
    new_table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 1.0)

    row = new_table.rows.add()
    row.cells.add("Col 1")
    row.cells.add("Col 2")
    row.cells.add("Col 3")
    row = new_table.rows.add()
    row.cells.add("Col 12")
    row.cells.add("Col 22")
    row.cells.add("Col 32")

    # Replace the old table with the new one
    absorber.replace(document.pages[1], old_table, new_table)

    # Save PDF document
    document.save(outfile)
```

## Sujets liés à la table

- [Travailler avec des tableaux dans les PDF en Python](/pdf/fr/python-net/working-with-tables/)
- [Ajouter des tables au PDF avec Python](/pdf/fr/python-net/adding-tables/)
- [Extraire les tableaux des documents PDF](/pdf/fr/python-net/extracting-table/)
- [Supprimer les tables des PDF existants](/pdf/fr/python-net/removing-tables/)
