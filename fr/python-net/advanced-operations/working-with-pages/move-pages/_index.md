---
title: Déplacer les pages PDF en Python
linktitle: Déplacement des pages PDF
type: docs
weight: 100
url: /fr/python-net/move-pages/
description: Apprenez comment déplacer des pages PDF au sein d'un document ou entre des documents en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Déplacer les pages PDF entre des documents en Python
Abstract: Cet article explique comment déplacer des pages dans les PDF en utilisant Aspose.PDF for Python via .NET. Découvrez comment déplacer une seule page ou plusieurs pages vers un autre document, et comment repositionner une page dans le même PDF en utilisant les API Document et PageCollection.
---

## Déplacer une page d'un document PDF à un autre

Aspose.PDF for Python vous permet de déplacer une page (pas seulement de la copier) d'un PDF à un autre. Il supprime la page sélectionnée du document original, puis l'ajoute à un nouveau fichier PDF.

Considérez cela comme couper une page d'un livre et la coller dans un autre — la page n'existe plus dans le fichier original après le déplacement.

1. Ouvrez le document PDF source en utilisant le [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe.
1. Sélectionnez une page spécifique à déplacer (dans ce cas, la page 2) — cela fait référence à un [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Créez un nouveau document PDF (instanciez un autre [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Ajoutez la page sélectionnée au nouveau document PDF en utilisant le document de destination [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (par exemple, `another_document.pages.add(page)`).
1. Supprimez la page du document original via son [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (par exemple, `document.pages.delete(index)`).
1. Enregistrez les deux documents.

L'extrait de code suivant vous montre comment déplacer une page.

```python
import aspose.pdf as ap

def move_page_from_one_document_to_another(
    input_file_name: str, output_file_name: str
) -> None:

    document = ap.Document(input_file_name)
    page = document.pages[2]
    another_document = ap.Document()
    another_document.pages.add(page)
    document.pages.delete(2)
    document.save(input_file_name.replace(".pdf", "_new.pdf"))
    another_document.save(output_file_name)
```

## Déplacer plusieurs pages d’un document PDF à un autre

Contrairement à la copie, cette opération transfère les pages sélectionnées — les supprimant du fichier source et les enregistrant dans un nouveau PDF.

1. Créer un nouveau document de destination vide (`Document`).
1. Sélectionner plusieurs pages (dans ce cas, les pages 1 et 3) du document source [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Parcourez les pages sélectionnées et ajoutez chacune au document de destination [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Enregistrez le document de destination contenant les pages déplacées.
1. Supprimez les pages déplacées du document source en utilisant son [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Enregistrez le document source modifié avec un nouveau nom de fichier pour conserver les deux versions.

L'extrait de code suivant montre comment déplacer plusieurs pages.

```python
import aspose.pdf as ap

def move_multiple_pages_from_one_document_to_another(
    input_file_name: str, output_file_name: str
) -> None:
    src_document = ap.Document(input_file_name)
    dst_document = ap.Document()
    pages = [1, 2]
    for page_index in pages:
        page = src_document.pages[page_index]
        dst_document.pages.add(page)
    # Save output files
    dst_document.save(output_file_name)
    src_document.pages.delete(pages)
    src_document.save(input_file_name.replace(".pdf", "_new.pdf"))
```

## Déplacer une page vers un nouvel emplacement dans le même document PDF

Il montre comment déplacer une page spécifique vers une position différente au sein du même document — un besoin courant lors de la réorganisation ou de la modification de mises en page PDF.

1. Chargez le document PDF d'entrée en utilisant le [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe.
1. Sélectionnez la page que vous souhaitez déplacer (page 2) — ceci est un [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Ajoutez-le à la fin du document en utilisant le document [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Supprimez la page originale de son emplacement précédent via le [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Enregistrez le document modifié sous un nouveau fichier.

```python
import aspose.pdf as ap

def move_page_in_new_location_in_same_document(
    input_file_name: str, output_file_name: str
) -> None:
    src_document = ap.Document(input_file_name)

    page = src_document.pages[2]
    src_document.pages.add(page)
    src_document.pages.delete(2)

    # Save output file
    src_document.save(output_file_name)
```

## Sujets de page associés

- [Travailler avec des pages PDF en Python](/pdf/fr/python-net/working-with-pages/)
- [Ajouter des pages PDF en Python](/pdf/fr/python-net/add-pages/)
- [Supprimer les pages PDF en Python](/pdf/fr/python-net/delete-pages/)
- [Extraire des pages PDF en Python](/pdf/fr/python-net/extract-pages/)
