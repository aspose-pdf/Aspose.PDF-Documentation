---
title: Extraire des tables d'un PDF en Python
linktitle: Extraire une table
type: docs
weight: 20
url: /fr/python-net/extracting-table/
description: Apprenez comment extraire les données d'une table à partir de documents PDF existants en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraire les données d'une table des fichiers PDF avec Python
Abstract: Cet article explique comment extraire des tables de documents PDF en utilisant Aspose.PDF for Python via .NET. Il montre comment utiliser `TableAbsorber` pour détecter les tables par page, parcourir les lignes et les cellules, et récupérer le texte des cellules pour l'analyse et le traitement des données en aval.
---

## Extraire une table d'un PDF

L'extraction de tableaux à partir de PDF est utile pour les rapports, la migration de données et les flux de travail d'analyse. Avec Aspose.PDF for Python via .NET, vous pouvez détecter et lire le contenu des tableaux à partir de documents PDF existants de manière efficace.

Cet extrait de code ouvre un fichier PDF existant, parcourt chaque page à la recherche de tableaux et extrait le contenu texte des cellules. Il utilise `TableAbsorber` détecter les tableaux, puis parcourir les lignes et les cellules pour afficher le texte extrait.

1. Charge le PDF dans un objet ap.Document.
1. Boucle à travers les pages.
1. Crée un objet TableAbsorber.
1. Parcourt les tableaux.
1. Parcourir les lignes et les cellules.
1. Extraire et imprimer le texte des cellules.

Cet exemple lit un PDF, trouve toutes les tables et affiche le contenu des cellules ligne par ligne.

```python
import aspose.pdf as ap
from os import path
import sys

def extract(infile: str) -> None:
    """Extract and print all tables from a PDF file."""
    document = ap.Document(infile)
    for page in document.pages:
        absorber = ap.text.TableAbsorber()
        absorber.visit(page)
        for table in absorber.table_list:
            print("Table ----")
            for row in table.row_list:
                print("Row:")
                row_txt = ""
                for cell in row.cell_list:
                    cell_txt = ""
                    text_fragment_collection = cell.text_fragments
                    for fragment in text_fragment_collection:
                        for seg in fragment.segments:
                            cell_txt += seg.text
                    row_txt += " | "
                    row_txt += cell_txt
                print(row_txt)
```

## Sujets liés à la table

- [Travailler avec des tableaux dans les PDF en Python](/pdf/fr/python-net/working-with-tables/)
- [Ajouter des tables au PDF avec Python](/pdf/fr/python-net/adding-tables/)
- [Intégrer les tableaux PDF avec des sources de données](/pdf/fr/python-net/integrate-table/)
- [Supprimer les tables des PDF existants](/pdf/fr/python-net/removing-tables/)