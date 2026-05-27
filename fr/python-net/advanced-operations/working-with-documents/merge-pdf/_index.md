---
title: Fusionner des fichiers PDF en Python
linktitle: Fusionner des fichiers PDF
type: docs
weight: 50
url: /fr/python-net/merge-pdf-documents/
description: Apprenez à fusionner plusieurs fichiers PDF en un seul document avec Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Combinez les pages PDF en utilisant Python.
Abstract: Cet article répond au besoin commun de fusionner plusieurs fichiers PDF en un seul document, un processus précieux pour organiser et optimiser le stockage et le partage du contenu PDF. Il explore l'utilisation d'Aspose.PDF for Python via .NET pour combiner efficacement les fichiers PDF, en reconnaissant que la fusion de PDF en Python peut être difficile sans bibliothèques tierces. L'article fournit un guide étape par étape pour concaténer les fichiers PDF – création d'un nouveau document, fusion des fichiers et sauvegarde du document fusionné. Un extrait de code montre l'implémentation en utilisant Aspose.PDF, mettant en avant la capacité de la bibliothèque à rationaliser le processus de fusion. De plus, il présente Aspose.PDF Merger, un outil en ligne pour fusionner les PDF, permettant aux utilisateurs d'explorer la fonctionnalité dans un environnement web.
---

## Fusionner ou combiner plusieurs PDF en un seul PDF en Python

Combiner des fichiers PDF est une requête très populaire parmi les utilisateurs. Cela peut être utile lorsque vous avez plusieurs fichiers PDF que vous souhaitez partager ou stocker ensemble en un seul document.

La fusion de fichiers PDF peut vous aider à organiser vos documents, libérer de l'espace de stockage sur votre PC et partager plusieurs fichiers PDF avec d’autres en les combinant en un seul document.

La fusion de PDF en Python via .NET n'est pas une tâche simple sans utiliser de bibliothèque tierce.
Cet article montre comment fusionner plusieurs fichiers PDF en un seul document PDF à l'aide d'Aspose.PDF for Python via .NET. 

## Fusionner des fichiers PDF en utilisant Python et le DOM

Concaténer deux fichiers PDF :

1. Créer un nouveau document.
1. Fusionner les fichiers PDF
1. Enregistrer le document fusionné

Combiner plusieurs documents PDF en un seul fichier:

```python
import sys
import aspose.pdf as ap
from os import path


def merge_two_documents(infile1, infile2, outfile):
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    document1.pages.add(document2.pages)
    document1.save(outfile)
```

## Ajouter une plage de pages d’un PDF à un autre

Copier et ajouter une plage de pages spécifique d'un document PDF source à un document PDF de destination en utilisant Aspose.PDF for Python.

1. Ouvrez les fichiers PDF en utilisant la classe Document.
1. Vérifiez si le document source possède des pages.
1. Valider la plage de pages.
1. Ignorer l'opération si la page de début est supérieure à la page de fin.
1. Itérer à travers la plage de pages.
1. Ajouter des pages au document de destination.

```python
import sys
import aspose.pdf as ap
from os import path


def _append_page_range(source_document, destination_document, start_page, end_page):
    total_pages = len(source_document.pages)
    if total_pages == 0:
        return

    start = max(1, start_page)
    end = min(end_page, total_pages)
    if start > end:
        return

    for page_number in range(start, end + 1):
        destination_document.pages.add(source_document.pages[page_number])
```

## Fusionner plusieurs documents PDF en un seul

Cet extrait de code explique comment fusionner plusieurs fichiers PDF en un seul document :

1. Créer un document de sortie vide.
1. Parcourir les fichiers d'entrée.
1. Chargez chaque document source.
1. Déterminer la plage de pages.
1. Ajouter des pages au document de sortie.
1. Répétez pour tous les documents.
1. Enregistrez le PDF fusionné.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_multiple_documents(input_files, outfile):
    output_document = ap.Document()

    for input_file in input_files:
        source_document = ap.Document(input_file)
        _append_page_range(
            source_document, output_document, 1, len(source_document.pages)
        )

    output_document.save(outfile)
```

## Fusionner les plages de pages sélectionnées de plusieurs PDF

1. Chargez les documents PDF source.
1. Créer un document de sortie.
1. Définissez les plages de pages pour chaque document.
1. Ajouter les pages du premier document.
1. Ajouter les pages du deuxième document.
1. Combinez les pages dans l'ordre souhaité.
1. Enregistrez le PDF fusionné.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_selected_page_ranges(infile1, infile2, outfile):
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    output_document = ap.Document()

    _append_page_range(document1, output_document, 1, 2)
    _append_page_range(document2, output_document, 2, 3)

    output_document.save(outfile)
```

## Insérer un PDF dans un autre à une position spécifique

1. Chargez la base et insérez les documents.
1. Créer un document de sortie.
1. Déterminer le nombre total de pages dans le document de base.
1. Valider l'indice d'insertion.
1. Ajouter des pages avant le point d'insertion.
1. Ajouter toutes les pages du document d'insertion.
1. Ajouter les pages restantes du document de base.
1. Enregistrez le PDF résultant.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_insert_document_at_position(infile1, infile2, insert_after_page, outfile):
    base_document = ap.Document(infile1)
    insert_document = ap.Document(infile2)
    output_document = ap.Document()

    base_total_pages = len(base_document.pages)
    insert_index = max(0, min(insert_after_page, base_total_pages))

    _append_page_range(base_document, output_document, 1, insert_index)
    _append_page_range(insert_document, output_document, 1, len(insert_document.pages))
    _append_page_range(
        base_document, output_document, insert_index + 1, base_total_pages
    )

    output_document.save(outfile)
```

## Fusionner les PDF en alternant les pages

Cet exemple montre comment fusionner deux documents PDF en alternant leurs pages à l'aide d'Aspose.PDF for Python.

1. Chargez les documents PDF d'entrée.
1. Créer un document de sortie.
1. Obtenez le nombre de pages dans chaque document.
1. Calculez le nombre maximal de pages.
1. Itérer à travers les numéros de page.
1. Ajouter les pages alternativement.
1. Gérer des nombres de pages inégaux.
1. Enregistrez le PDF fusionné.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_alternating_pages(infile1, infile2, outfile):
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    output_document = ap.Document()

    document1_pages = len(document1.pages)
    document2_pages = len(document2.pages)
    max_pages = max(document1_pages, document2_pages)

    for page_number in range(1, max_pages + 1):
        if page_number <= document1_pages:
            output_document.pages.add(document1.pages[page_number])
        if page_number <= document2_pages:
            output_document.pages.add(document2.pages[page_number])

    output_document.save(outfile)
```

## Fusionner des PDF avec des séparateurs de section et des signets

Fusionnez plusieurs documents PDF en un seul fichier avec des sections structurées et des signets de navigation en utilisant Aspose.PDF pour Python.

1. Créer un document de sortie.
1. Parcourir les fichiers d'entrée.
1. Chargez le document source.
1. Ajouter une page de séparation.
1. Créer un signet de section.
1. Ajouter les pages du document source.
1. Suivez la première page de contenu.
1. Ajoutez un signet de contenu imbriqué (facultatif).
1. Répétez pour tous les documents.
1. Enregistrez le PDF fusionné.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_with_section_separators_and_bookmarks(input_files, outfile):
    output_document = ap.Document()

    for section_index, input_file in enumerate(input_files, start=1):
        source_document = ap.Document(input_file)
        source_page_count = len(source_document.pages)

        separator_page = output_document.pages.add()
        separator_page.paragraphs.add(
            ap.text.TextFragment(
                f"Section {section_index}: {path.basename(input_file)}"
            )
        )

        section_bookmark = ap.OutlineItemCollection(output_document.outlines)
        section_bookmark.title = f"Section {section_index}"
        section_bookmark.action = ap.annotations.GoToAction(separator_page)
        output_document.outlines.append(section_bookmark)

        first_content_page_number = len(output_document.pages) + 1
        _append_page_range(source_document, output_document, 1, source_page_count)

        if source_page_count > 0 and first_content_page_number <= len(
            output_document.pages
        ):
            content_bookmark = ap.OutlineItemCollection(output_document.outlines)
            content_bookmark.title = f"Section {section_index} Content"
            content_bookmark.action = ap.annotations.GoToAction(
                output_document.pages[first_content_page_number]
            )
            section_bookmark.append(content_bookmark)

    output_document.save(outfile)
```

## Exemple en direct

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) est une application web gratuite en ligne qui vous permet d'examiner le fonctionnement de la fonctionnalité de fusion de présentations.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)

## Sujets de documents associés

- [Travailler avec des documents PDF en Python](/pdf/fr/python-net/working-with-documents/)
- [Diviser les fichiers PDF en Python](/pdf/fr/python-net/split-document/)
- [Optimiser les fichiers PDF en Python](/pdf/fr/python-net/optimize-pdf/)
- [Manipuler des documents PDF en Python](/pdf/fr/python-net/manipulate-pdf-document/)

