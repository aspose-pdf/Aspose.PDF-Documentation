---
title: Ajouter des pages PDF en Python
linktitle: Ajout de pages
type: docs
weight: 10
url: /fr/python-net/add-pages/
description: Apprenez comment ajouter ou insérer des pages dans des documents PDF en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter ou insérer des pages PDF avec Python
Abstract: Cet article explique comment ajouter des pages aux fichiers PDF en utilisant Aspose.PDF for Python via .NET. Apprenez comment insérer des pages vierges à des positions spécifiques, ajouter des pages à la fin d’un document, et importer une page d’un autre PDF en utilisant les API Document et PageCollection.
---

Aspose.PDF for Python via .NET offre des opérations flexibles au niveau des pages pour les documents PDF. Vous pouvez gérer les pages via [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) et ajouter des pages à un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) à des positions spécifiques ou à la fin du fichier.

Utilisez cette page lorsque vous devez insérer de nouvelles pages blanches dans un PDF existant ou ajouter des pages à la fin d'un document lors des flux de génération.

## Ajouter ou insérer des pages dans un fichier PDF

Aspose.PDF for Python via .NET prend en charge à la fois l'insertion de pages à un indice spécifique et l'ajout de pages à la fin d'un PDF.

### Insérer une page vide dans un fichier PDF

Pour insérer une page vide dans un fichier PDF :

1. Ouvrez un existant [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) en utilisant les méthodes appropriées.
1. Insérez une nouvelle page vide à un indice spécifique en utilisant le [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) `insert()` méthode.
1. Enregistrez le modifié [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) vers le chemin de sortie souhaité.

Insérez une page vierge dans un fichier PDF existant à une position spécifiée:

```python
import aspose.pdf as ap

def insert_empty_page(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    document.pages.insert(2)
    document.save(output_file_name)
```

### Ajouter une page vide à la fin d'un fichier PDF

Parfois, vous souhaitez vous assurer qu'un document se termine par une page vide. Ce sujet explique comment insérer une page vide à la fin du document PDF.

Pour insérer une page vide à la fin d'un fichier PDF :

1. Ouvrez un existant [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) en utilisant les méthodes appropriées.
1. Ajoutez une nouvelle page vide à la fin du document en utilisant le [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) `add()` méthode.
1. Enregistrez le mis à jour [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

Le fragment de code suivant vous montre comment insérer une page vide à la fin d'un fichier PDF.

```python
import aspose.pdf as ap

def add_empty_page_to_end(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    document.pages.add()
    document.save(output_file_name)
```

### Ajouter une page à partir d'un autre document PDF

Avec Aspose.PDF for Python via .NET, vous pouvez créer un nouveau [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), ajoutez une page initiale, puis importez une page d'un autre PDF dans celle‑ci.

1. Créer un nouveau [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Ajoutez une nouvelle page vierge [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) et écrivez du texte dessus en utilisant [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/).
1. Ouvrez un autre existant [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Copiez un [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) à partir de ce document.
1. Collez la page copiée dans votre document principal en utilisant [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Enregistrez le fichier combiné.

```python
import aspose.pdf as ap

def add_page_from_another_document(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document()
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("This is first page!")
    page.paragraphs.add(text_fragment)

    another_document = ap.Document(input_file_name)
    document.pages.add(another_document.pages[1])

    document.save(output_file_name)
```

## Sujets de page associés

- [Travailler avec les pages PDF en Python](/pdf/fr/python-net/working-with-pages/)
- [Déplacer des pages PDF en Python](/pdf/fr/python-net/move-pages/)
- [Supprimer des pages PDF en Python](/pdf/fr/python-net/delete-pages/)
- [Extraire des pages PDF en Python](/pdf/fr/python-net/extract-pages/)
