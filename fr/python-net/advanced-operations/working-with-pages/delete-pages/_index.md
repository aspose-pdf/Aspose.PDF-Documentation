---
title: Supprimer des pages PDF en Python
linktitle: Suppression de pages PDF
type: docs
weight: 80
url: /fr/python-net/delete-pages/
description: Apprenez comment supprimer des pages de fichiers PDF en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer une ou plusieurs pages PDF en Python
Abstract: Cet article explique comment supprimer des pages de fichiers PDF en utilisant Aspose.PDF for Python via .NET. Apprenez comment supprimer une page unique ou plusieurs pages d'un document en utilisant l'API PageCollection, puis enregistrez le PDF mis à jour.
---

Vous pouvez supprimer des pages d'un fichier PDF en utilisant Aspose.PDF for Python via .NET. Pour supprimer une page particulière, utilisez le [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) d'un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

Utilisez ce flux de travail lorsque vous devez supprimer des pages indésirables d'un PDF avant de le partager, de l'archiver ou de combiner des documents.

## Supprimer la page du fichier PDF

Aspose.PDF for Python via .NET supprime la page 2 du PDF d'entrée et enregistre le document mis à jour dans un nouveau fichier. Cette fonction est utile pour supprimer des pages indésirables ou sensibles sans altérer le reste du document.

1. Chargez le PDF d'entrée en tant que [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Supprimez la page en utilisant le [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Appelez le [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) méthode pour enregistrer le fichier PDF mis à jour.

L'extrait de code suivant montre comment supprimer une page particulière du fichier PDF à l'aide de Python.

```python
import aspose.pdf as ap

def delete_page(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    document.pages.delete(2)
    document.save(output_file_name)
```

## Supprimer plusieurs pages d'un document PDF

Supprimer plusieurs pages vous permet de retirer un ensemble de pages spécifiées en une seule opération, ce qui est plus efficace que de supprimer les pages une par une. Le PDF résultant est enregistré dans un nouveau fichier, préservant le document original.

1. Chargez le PDF d'entrée en tant que [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Supprimez les pages répertoriées dans le tableau pages en utilisant le [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Enregistrez le mis à jour [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) dans un nouveau fichier.

```python
import aspose.pdf as ap

def delete_multiple_pages(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    # Example: delete pages 2, 3, and 4.
    pages = [2, 3, 4]
    document.pages.delete(pages)
    document.save(output_file_name)
```

## Sujets de page associés

- [Travailler avec les pages PDF en Python](/pdf/fr/python-net/working-with-pages/)
- [Ajouter des pages PDF en Python](/pdf/fr/python-net/add-pages/)
- [Déplacer des pages PDF en Python](/pdf/fr/python-net/move-pages/)
- [Extraire des pages PDF en Python](/pdf/fr/python-net/extract-pages/)
