---
title: Manipuler les tableaux dans un PDF existant
linktitle: Manipuler les tableaux
type: docs
weight: 40
url: /fr/python-net/manipulating-tables/
description: Apprenez à travailler avec les tableaux dans des PDF existants en utilisant Aspose.PDF pour Python via .NET, offrant une flexibilité dans la modification de documents.
lastmod: "2025-09-27"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## Manipuler les tableaux dans un PDF existant

Aspose.PDF pour Python montre comment modifier le contenu d’une cellule spécifique au sein d’un tableau dans un document PDF. Il utilise la classe TableAbsorber pour localiser les tableaux sur la première page, accède à un fragment de texte particulier dans la première cellule du premier tableau, met à jour son texte, et enregistre le PDF modifié dans un nouveau fichier.

1. Ouvrez le fichier PDF en utilisant 'ap.Document()'.
1. Créez un objet TableAbsorber pour détecter les tableaux dans le PDF.
1. Appelez absorber.visit() pour trouver tous les tableaux sur la première page.
1. Accédez à un fragment de texte spécifique :
- Récupère le premier tableau.
- Obtient la première ligne du tableau.
- Sélectionne le deuxième fragment de texte dans la cellule.
1. Modifiez le texte.
1. Enregistrez le PDF mis à jour.
1. Imprimez la confirmation du fichier enregistré.

```python

    import aspose.pdf as ap
    from os import path

    # Define file names and data directory
    data_dir = "."  # or specify your data directory
    infile = "input.pdf"   # replace with your input PDF file name
    outfile = "output.pdf" # replace with your desired output PDF file name

    # Open PDF document
    path_infile = path.join(data_dir, infile)
    path_outfile = path.join(data_dir, outfile)
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    # Get access to first table on page, their first cell and text fragments in it
    fragment = absorber.table_list[0].row_list[0].cell_list[0].text_fragments[1]

    # Change text of the first text fragment in the cell
    fragment.text = "hi world"

    # Save PDF document

    document.save(path_outfile)
    print(f"File saved at: {path_outfile}")
```

## Remplacer l'ancien tableau par un nouveau dans le document PDF

Aspose.PDF permet de remplacer un tableau existant dans un PDF par un nouveau tableau. Le fragment de code ouvre un PDF, identifie le premier tableau de la première page à l’aide de TableAbsorber, crée un nouveau tableau avec des largeurs de colonne personnalisées et du contenu, puis remplace le tableau original par le nouveau. Enfin, il enregistre le PDF mis à jour dans un nouveau fichier.

Il montre comment modifier la structure et le contenu d’un tableau dans un PDF sans altérer le reste du document.

```python

    import aspose.pdf as ap
    from os import path

    # Open PDF document
    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    # Get first table on the page
    table = absorber.table_list[0]

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

    # Replace the table with new one
    absorber.replace(document.pages[1], table, new_table)

    # Save PDF document
    document.save(path_outfile)
    print(f"File saved at: {path_outfile}")
```
