---
title: Extraire des pages PDF en Python
linktitle: Extraction de pages PDF
type: docs
weight: 80
url: /fr/python-net/extract-pages/
description: Apprenez comment extraire une ou plusieurs pages PDF dans de nouveaux fichiers en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment extraire des pages PDF en utilisant Python
Abstract: Cet article explique comment extraire des pages de fichiers PDF en utilisant Aspose.PDF for Python via .NET. Apprenez comment copier une page unique ou plusieurs pages dans un nouveau document en utilisant l'indexation des pages à partir de 1 et l'API PageCollection.
---

## Extraire une seule page d'un PDF

Extrayez une page spécifique d'un document PDF et enregistrez‑la dans un nouveau fichier. En utilisant la bibliothèque Aspose.PDF, le script copie la page souhaitée dans un nouveau PDF, laissant le document original inchangé. Cela est utile pour diviser les PDF ou isoler des pages importantes à distribuer.

1. Chargez le PDF source en utilisant le [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) API (`ap.Document()`).
1. Créez un nouveau [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) pour contenir la page extraite.
1. Ajoutez le souhaité [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) du document source vers le nouveau PDF en utilisant le document de destination [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (`dst_document.pages.add(...)`).
    - Dans cet exemple, la page 2 est extraite (indexation à partir de 1).
1. Enregistrez le nouveau [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) avec la page extraite vers le fichier de sortie spécifié.

```python
import aspose.pdf as ap

def extract_page(input_file_name: str, output_file_name: str) -> None:
    src_document = ap.Document(input_file_name)
    dst_document = ap.Document()
    dst_document.pages.add(src_document.pages[2])
    dst_document.save(output_file_name)
```

## Extraire plusieurs pages d'un PDF

Extrayez plusieurs pages spécifiques d'un document PDF et enregistrez-les dans un nouveau fichier. En utilisant la bibliothèque Aspose.PDF, les pages sélectionnées sont copiées dans un nouveau PDF tout en laissant le document original intact. Cela est utile pour créer des PDF plus petits contenant uniquement les sections pertinentes d'un document plus volumineux.

1. Chargez le PDF source en utilisant le [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) API (`ap.Document()`).
1. Créez un nouveau [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) pour contenir les pages extraites.
1. Sélectionnez les pages à extraire (dans cet exemple, les pages 2 et 3 en utilisant une indexation à partir de 1).
1. Ajoutez chaque sélectionné [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) du document source au nouveau PDF en utilisant son [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Enregistrez le nouveau [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) avec les pages extraites vers le fichier de sortie spécifié.

```python
import aspose.pdf as ap

def extract_multiple_pages(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    pages = [2, 3]
    another_document = ap.Document()
    for page_index in pages:
        another_document.pages.add(document.pages[page_index])
    another_document.save(output_file_name)
```

## Sujets de page associés

- [Travailler avec des pages PDF en Python](/pdf/fr/python-net/working-with-pages/)
- [Supprimer les pages PDF en Python](/pdf/fr/python-net/delete-pages/)
- [Déplacer les pages PDF en Python](/pdf/fr/python-net/move-pages/)
- [Diviser les fichiers PDF en Python](/pdf/fr/python-net/split-document/)
