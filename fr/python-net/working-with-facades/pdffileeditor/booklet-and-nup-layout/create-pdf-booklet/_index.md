---
title: Créer un livret PDF
type: docs
weight: 20
url: /fr/python-net/create-pdf-booklet/
description: Générer un PDF au format livret à partir d'un document existant en utilisant Aspose.PDF for Python
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Créer un livret PDF à partir d'un PDF existant en utilisant Python
Abstract: Apprenez comment générer un PDF au format livret à partir d'un document existant en utilisant Aspose.PDF for Python. Cet exemple montre comment utiliser la classe PdfFileEditor pour réorganiser les pages afin qu'elles puissent être imprimées et pliées en livret. La méthode ordonne automatiquement les pages pour produire une mise en page de livret correcte.
---

Créer des documents au format livret est une exigence courante lors de la préparation de PDF pour l'impression. Dans une mise en page de livret, les pages sont réorganisées de sorte que, une fois imprimées et pliées, elles apparaissent dans le bon ordre.

En utilisant Aspose.PDF for Python, les développeurs peuvent facilement convertir un PDF standard en livret en utilisant le [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) classe. La méthode ‘make_booklet’ réorganise automatiquement les pages du document d'entrée et génère un nouveau PDF optimisé pour l'impression en livret.

1. Ouvrez un document PDF existant.
1. Créez une instance PdfFileEditor.
1. Utilisez la méthode make_booklet pour réorganiser les pages.
1. Enregistrez la sortie sous forme de fichier PDF prêt pour le livret.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Create PDF Booklet
def create_pdf_booklet(infile, outfile):
    # Create BookletMaker object
    booklet_maker = pdf_facades.PdfFileEditor()
    # Make booklet from input PDF file and save to output PDF file
    booklet_maker.make_booklet(FileIO(infile), FileIO(outfile, "w"))
```

Cet extrait de code montre comment utiliser la méthode 'try_make_booklet' de [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) classe pour réorganiser les pages en vue d'une impression en livret sans déclencher d'exceptions si l'opération échoue.

Une mise en page de livret réorganise les pages de sorte que, lorsqu'elles sont imprimées et pliées, le document se lise dans le bon ordre. L'automatisation de ce processus garantit des résultats cohérents et élimine le besoin de réarranger manuellement les pages.

La méthode 'try_make_booklet' fonctionne de manière similaire à 'make_booklet', mais avec une différence importante :

- 'make_booklet' génère une exception si l'opération échoue.
- 'try_make_booklet' renvoie True ou False, permettant aux développeurs de gérer les erreurs plus sûrement.

1. Ouvrez un document PDF existant.
1. Créez une instance PdfFileEditor.
1. Tentative de création du livret.
1. Gérer le résultat.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def try_create_pdf_booklet(infile, outfile):
    # Create BookletMaker object
    booklet_maker = pdf_facades.PdfFileEditor()
    # Make booklet from input PDF file and save to output PDF file
    # The try_make_booklet method is like the make_booklet method,
    # except the try_make_booklet method does not throw an exception if the operation fails.
    if not booklet_maker.try_make_booklet(FileIO(infile), FileIO(outfile, "w")):
        print("Failed to create booklet.")
```
