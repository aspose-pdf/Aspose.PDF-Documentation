---
title: Créer un Document PDF N-Up
type: docs
weight: 10
url: /fr/python-net/create-n-up-pdf-document/
description: Apprenez comment créer un Document PDF N-Up tout en gérant en toute sécurité les erreurs potentielles à l'aide d'Aspose.PDF for Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Créer une mise en page PDF N-Up en Python
Abstract: Apprenez comment générer une mise en page PDF N-Up en utilisant Aspose.PDF for Python. Cet exemple montre comment combiner plusieurs pages d'un Document PDF sur une seule page en utilisant la méthode 'make_n_up' ou 'try_make_n_up' de la classe PdfFileEditor.
---

Une mise en page N-Up place plusieurs pages d'un Document PDF sur une seule page sous forme de grille. Cette mise en page est souvent utilisée pour imprimer des présentations, des notes de service ou des rapports où plusieurs pages peuvent être consultées en même temps.

En utilisant Aspose.PDF for Python, les développeurs peuvent rapidement créer un Document N-Up en spécifiant le nombre de lignes et de colonnes qui déterminent combien de pages originales apparaissent sur chaque page de sortie.

Dans cet extrait de code, la méthode 'make_n_up' de la [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) classe organise les pages du PDF d'entrée dans une grille 2 × 2, ce qui signifie que quatre pages d'origine apparaissent sur une page dans le document de sortie.

Dans l'exemple présenté, la mise en page utilise 2 lignes et 2 colonnes, produisant quatre pages par feuille :

1. Ouvrez le fichier PDF source.
1. Créez une instance PdfFileEditor.
1. Spécifiez le nombre de lignes et de colonnes pour la disposition N‑Up.
1. Générez un nouveau PDF avec les pages combinées.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Create N-Up PDF Document
def create_nup_pdf_document(infile, outfile):
    # Create NUpMaker object
    nup_maker = pdf_facades.PdfFileEditor()
    # Make N-Up layout from input PDF file and save to output PDF file
    nup_maker.make_n_up(
        FileIO(infile), FileIO(outfile, "w"), 2, 2
    )  # 2 rows and 2 columns for N-Up layout
```

Aspose.PDF for Python via .NET vous permet de générer des mises en page N-Up avec la classe PdfFileEditor. La méthode 'try_make_n_up' fonctionne de la même manière que make_n_up, mais au lieu de lever une exception lorsqu'une opération échoue, elle renvoie une valeur booléenne indiquant si le processus a réussi.

La disposition N-Up organise plusieurs pages PDF sur une seule page en utilisant une grille définie par des lignes et des colonnes.

La méthode \u0027try_make_n_up\u0027 offre une façon plus sûre d'effectuer cette opération parce que :

- Elle renvoie True si la disposition est créée avec succès
- Elle renvoie False si l'opération échoue
- Elle n'interrompt pas l'exécution du programme avec des exceptions

Dans l'exemple ci‑dessous, le document est organisé en utilisant une grille 2 \u00D7 2, qui place quatre pages originales sur chaque page de sortie.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Create N-Up PDF Document
def try_create_nup_pdf_document(infile, outfile):
    # Create NUpMaker object
    nup_maker = pdf_facades.PdfFileEditor()
    # Make N-Up layout from input PDF file and save to output PDF file
    if not nup_maker.try_make_n_up(FileIO(infile), FileIO(outfile, "w"), 2, 2):
        print("Failed to create N-Up PDF document.")
```
