---
title: Supprimer les tableaux des documents PDF existants
linktitle: Supprimer les tableaux
description: Apprenez comment supprimer un ou plusieurs tableaux des documents PDF existants en Python.
lastmod: "2026-05-22"
type: docs
weight: 50
url: /fr/python-net/removing-tables/
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimez un ou plusieurs tableaux des fichiers PDF avec Python
Abstract: Cet article explique comment supprimer des tableaux des documents PDF existants à l'aide d'Aspose.PDF for Python via .NET. Il présente `TableAbsorber` pour localiser les tableaux et montre comment supprimer un tableau unique ou supprimer tous les tableaux détectés d'une page.
---

## Supprimer le tableau d'un document PDF

Aspose.PDF for Python vous permet de supprimer un tableau d’un PDF. Il ouvre un PDF existant, détecte le premier tableau de la première page avec `TableAbsorber`, supprime cette table en utilisant `remove()`, et enregistre le PDF mis à jour dans un nouveau fichier.

Utilisez cette page lorsque vous devez nettoyer des PDF contenant beaucoup de tableaux, supprimer du contenu tabulaire obsolète ou simplifier les documents avant redistribution.

```python
import aspose.pdf as ap
from os import path
import sys

def remove_one_table(infile: str, outfile: str) -> None:
    # Load existing PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(document.pages[1])
    # Get first table on the page
    table = absorber.table_list[0]
    # Remove the table
    absorber.remove(table)
    # Save PDF
    document.save(outfile)
```

## Supprimer toutes les tables du document PDF

Avec notre bibliothèque, vous pouvez supprimer toutes les tables d'une page spécifique d'un PDF. Le code ouvre un PDF existant, détecte toutes les tables de la deuxième page avec TableAbsorber, parcourt les tables détectées, supprime chacune d'elles, puis enregistre le PDF modifié dans un nouveau fichier. Cela est utile lorsque vous devez supprimer en masse les tables d'une page tout en conservant le reste du contenu du PDF intact.

```python
import aspose.pdf as ap
from os import path
import sys

def remove_all_tables(infile: str, outfile: str) -> None:
    # Load existing PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(document.pages[1])
    #  Loop through the copy of collection and removing tables
    tables = list(absorber.table_list)
    for table in tables:
        absorber.remove(table)

    # Save document
    document.save(outfile)
```

## Sujets liés à la table

- [Travailler avec des tableaux dans les PDF en Python](/pdf/fr/python-net/working-with-tables/)
- [Ajouter des tables au PDF avec Python](/pdf/fr/python-net/adding-tables/)
- [Extraire les tableaux des documents PDF](/pdf/fr/python-net/extracting-table/)
- [Manipuler les tableaux dans des PDF existants](/pdf/fr/python-net/manipulating-tables/)