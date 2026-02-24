---
title: Déplacer des pages PDF programmatiquement via Python
linktitle: Déplacer des pages PDF
type: docs
weight: 100
url: /fr/python-net/move-pages/
description: Essayez de déplacer des pages à l'emplacement souhaité ou à la fin d'un fichier PDF en utilisant Aspose.PDF pour Python via .NET.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Déplacer des pages entre des documents PDF en utilisant Python
Abstract: Cet article fournit un guide complet sur le déplacement de pages entre des documents PDF ou au sein d'un même document PDF à l'aide de Python, en utilisant spécifiquement la bibliothèque Aspose.PDF. Il décrit les processus étape par étape pour trois scénarios - déplacer une seule page d'un PDF à un autre, transférer plusieurs pages et repositionner une page dans le même document. Chaque scénario implique la création d'objets de classe `Document` pour les PDF source et destination, la manipulation des pages via la classe `PageCollection`, et l'utilisation des méthodes `add`, `delete` et `save` pour réaliser la réorganisation souhaitée des pages. Des extraits de code sont fournis pour une mise en œuvre pratique, démontrant comment déplacer les pages efficacement à l'aide de scripts Python.
---

## Déplacer une page d'un document PDF à un autre

Aspose.PDF pour Python vous permet de déplacer une page (pas seulement de la copier) d'un PDF à un autre. Elle supprime la page sélectionnée du document original puis l'ajoute à un nouveau fichier PDF.

Considérez cela comme couper une page d'un livre et la coller dans un autre — la page n'existe plus dans le fichier original après le déplacement.

1. Ouvrez le document PDF source en utilisant la classe [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Sélectionnez une page spécifique à déplacer (dans ce cas, la page 2) — cela fait référence à une [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Créez un nouveau document PDF (instanciez un autre [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Ajoutez la page sélectionnée au nouveau document PDF en utilisant la [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) du document de destination (par exemple, `another_document.pages.add(page)`).
1. Supprimez la page du document original via sa [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (par exemple, `document.pages.delete(index)`).
1. Enregistrez les deux documents.

Le fragment de code suivant montre comment déplacer une page.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def moving_page_from_one_document_to_another(input_file_name, output_file_name):
    """
    Move a single page from one PDF document to another.

    Parameters:
    - input_file_name (str): Path to the source PDF file.
    - output_file_name (str): Path to the destination PDF file after moving the page.
    """
    document = ap.Document(input_file_name)
    page = document.pages[2]
    another_document = ap.Document()
    another_document.pages.add(page)
    document.pages.delete(2)
    document.save(input_file_name.replace(".pdf","_new.pdf"))
    another_document.save(output_file_name)
```

## Déplacer un groupe de pages d'un document PDF à un autre

Contrairement à la copie, cette opération transfère les pages sélectionnées — les supprimant du fichier source et les enregistrant dans un nouveau PDF.

1. Créez un nouveau document de destination vide (`Document`).
1. Sélectionnez plusieurs pages (dans ce cas, les pages 1 et 3) à partir de la [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) du document source.
1. Parcourez les pages sélectionnées et ajoutez chacune à la [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) du document de destination.
1. Enregistrez le document de destination contenant les pages déplacées.
1. Supprimez les pages déplacées du document source en utilisant sa [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Enregistrez le document source modifié sous un nouveau nom de fichier pour préserver les deux versions.

Le fragment de code suivant montre comment insérer une page vide à la fin d'un fichier PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def moving_bunch_pages_from_one_document_to_another(input_file_name, output_file_name):
    """
    Move a set of pages from one PDF document to another.

    Parameters:
    - input_file_name (str): Path to the source PDF file.
    - output_file_name (str): Path to the destination PDF file where selected pages will be saved.
    """
    src_document = ap.Document(input_file_name)
    dst_document = ap.Document()
    pages = [1, 3]
    for page_index in pages:
        page = src_document.pages[page_index]
        dst_document.pages.add(page)
    # Save output files
    dst_document.save(output_file_name)
    src_document.pages.delete(pages)
    src_document.save(input_file_name.replace(".pdf","_new.pdf"))
```

## Déplacer une page à un nouvel emplacement dans le document PDF actuel

Cela montre comment déplacer une page spécifique à une position différente au sein du même document — un besoin courant lors de la réorganisation ou de la modification de mises en page PDF.

1. Chargez le document PDF d'entrée en utilisant la classe [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Sélectionnez la page que vous souhaitez déplacer (page 2) — il s'agit d'une [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Ajoutez‑la à la fin du document en utilisant la [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) du document.
1. Supprimez la page originale de son emplacement précédent via la [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Enregistrez le document modifié sous un nouveau fichier.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def moving_page_in_new_location_in_same_document(input_file_name, output_file_name):
    """
    Move a page to a new location within the same PDF document.

    Parameters:
    - input_file_name (str): Path to the source PDF file.
    - output_file_name (str): Path to the destination PDF file after moving the page.
    """
    srcDocument = ap.Document(input_file_name)

    page = srcDocument.pages[2]
    srcDocument.pages.add(page)
    srcDocument.pages.delete(2)

    # Save output file
    srcDocument.save(output_file_name)
```


