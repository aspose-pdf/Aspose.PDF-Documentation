---
title: Diviser les fichiers PDF en Python
linktitle: Diviser les fichiers PDF
type: docs
weight: 60
url: /fr/python-net/split-pdf-document/
description: Apprenez à diviser les fichiers PDF en Python en pages individuelles, parties égales, groupes de taille fixe, plages de pages personnalisées, ainsi que pages impaires ou paires.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Divisez un PDF en pages et plages de pages à l'aide de Python
Abstract: Cet article montre comment diviser des fichiers PDF avec Aspose.PDF for Python via .NET. Il couvre la division d'un PDF en pages individuelles, deux parties égales, groupes de pages de taille fixe, plages de pages personnalisées, groupes de pages nommés, noms de fichiers stables, ainsi que les fichiers de pages impaires ou paires.
---

Cette page montre comment **diviser des fichiers PDF en Python** en utilisant Aspose.PDF for Python via .NET.

Utilisez ces exemples lorsque vous devez découper un grand PDF en fichiers d’une page, en parties égales, en groupes de taille fixe, en plages de pages personnalisées, ou en ensembles de pages impaires et paires pour la distribution, la révision ou le traitement en aval.

## Exemple de fractionnement de PDF en ligne

[Aspose.PDF Diviseur](https://products.aspose.app/pdf/splitter) est une application web en ligne qui vous permet de tester la fonctionnalité de fractionnement de PDF.

[![Diviser le PDF avec Aspose](splitter.png)](https://products.aspose.app/pdf/splitter)

Pour diviser les pages PDF en fichiers PDF d'une seule page en Python, suivez ces étapes :

1. Boucler sur les pages du document PDF à travers le [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) de l'objet [CollectionDePages](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) collection
1. Pour chaque itération, créez un nouvel objet Document et ajoutez l'individuel [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) objet dans le document vide
1. Enregistrez le nouveau PDF en utilisant [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) méthode

## Diviser le PDF en plusieurs fichiers en Python

Le fragment de code Python suivant vous montre comment diviser les pages PDF en fichiers PDF individuels.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents(infile, outdir):
    document = ap.Document(infile)
    for page_num in range(1, len(document.pages) + 1):
        with ap.Document() as new_document:
            new_document.pages.add(document.pages[page_num])
            new_document.save(path.join(outdir, f"Page_{page_num}.pdf"))
```

## Diviser un PDF en deux parties égales

1. Chargez le document PDF.
1. Déterminer le nombre total de pages.
1. Calculer le point médian.
1. Créer le premier document de sortie.
1. Supprimer les pages de la seconde moitié du premier document.
1. Enregistrez la première partie.
1. Créer le deuxième document de sortie.
1. Supprimer les pages de la première moitié du deuxième document.
1. Enregistrez la deuxième partie.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_into_two_parts(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)
    mid_point = total_pages // 2

    # First part
    with ap.Document(infile) as first_document:
        first_part_range = range(mid_point + 1, total_pages + 1)
        first_document.pages.delete(first_part_range)
        first_document.save(path.join(outdir, "Part_1.pdf"))

    # Second part
    with ap.Document(infile) as second_document:
        second_part_range = range(1, mid_point + 1)
        second_document.pages.delete(second_part_range)
        second_document.save(path.join(outdir, "Part_2.pdf"))
```

## Diviser un PDF en plusieurs fichiers toutes les N pages

Divisez un document PDF en plusieurs fichiers plus petits en fonction d'un nombre fixe de pages à l'aide d'Aspose.PDF for Python.

1. Chargez le document PDF.
1. Déterminer le nombre total de pages.
1. Définir les pages par partie.
1. Parcourir le document par morceaux.
1. Calculez la plage de pages pour chaque partie.
1. Créer un nouveau document pour chaque partie.
1. Copier les pages dans le nouveau document.
1. Enregistrez le document scindé.
1. Répétez jusqu'à ce que toutes les pages soient traitées.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_every_n_pages(infile, outdir, pages_per_part=3):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    part_index = 1
    for start_page in range(1, total_pages + 1, pages_per_part):
        end_page = min(start_page + pages_per_part - 1, total_pages)

        with ap.Document() as part_document:
            for page_num in range(start_page, end_page + 1):
                part_document.pages.add(document.pages[page_num])
            part_document.save(
                path.join(outdir, f"Every_{pages_per_part}_Part_{part_index}.pdf")
            )

        part_index += 1
```

## Diviser un PDF par plages de pages personnalisées

Divisez un document PDF en plusieurs fichiers en fonction de plages de pages définies sur mesure à l'aide d'Aspose.PDF for Python.

1. Chargez le document PDF.
1. Déterminer le nombre total de pages.
1. Créez une liste de tuples représentant les intervalles (start_page, end_page).
1. Parcourir les plages définies.
1. Validez la page de démarrage.
1. Ajuster la page de fin.
1. Validez la plage effective.
1. Créez un nouveau document pour chaque plage.
1. Copier les pages dans le nouveau document.
1. Enregistrez chaque document fractionné.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_by_page_ranges(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)
    # Define ranges as (start_page, end_page). Use None to indicate last page.
    ranges = [(1, 3), (4, 6), (7, None)]

    for index, (start_page, end_page) in enumerate(ranges, start=1):
        if start_page > total_pages:
            continue

        effective_end = total_pages if end_page is None else min(end_page, total_pages)
        if start_page > effective_end:
            continue

        with ap.Document() as range_document:
            for page_num in range(start_page, effective_end + 1):
                range_document.pages.add(document.pages[page_num])
            range_document.save(
                path.join(outdir, f"Range_{index}_{start_page}_to_{effective_end}.pdf")
            )
```

## Diviser un PDF en première page et pages restantes

Séparez la première page d'un document PDF du reste des pages en utilisant Aspose.PDF for Python.

1. Chargez le document PDF.
1. Déterminer le nombre total de pages.
1. Vérifiez si le document est vide.
1. Créer un document pour la première page.
1. Ajouter la première page.
1. Enregistrez le document de la première page.
1. Vérifiez s'il y a des pages supplémentaires.
1. Créer un document pour les pages restantes.
1. Copier les pages restantes.
1. Enregistrez le document des pages restantes.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_first_page_and_rest(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    if total_pages == 0:
        return

    with ap.Document() as first_page_document:
        first_page_document.pages.add(document.pages[1])
        first_page_document.save(path.join(outdir, "First_Page.pdf"))

    if total_pages == 1:
        return

    with ap.Document() as remaining_pages_document:
        for page_num in range(2, total_pages + 1):
            remaining_pages_document.pages.add(document.pages[page_num])
        remaining_pages_document.save(path.join(outdir, "Remaining_Pages.pdf"))
```

## Diviser un PDF en dernière page et pages précédentes

Extrayez la dernière page d'un document PDF et séparez‑la des pages restantes en utilisant Aspose.PDF for Python.

1. Chargez le document PDF.
1. Déterminer le nombre total de pages.
1. Vérifiez si le document est vide.
1. Créer un document pour la dernière page.
1. Ajoutez la dernière page.
1. Enregistrez le document de la dernière page.
1. Vérifier les documents d'une seule page.
1. Supprimez la dernière page du document original.
1. Enregistrez les pages restantes.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_last_page_and_rest(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    if total_pages == 0:
        return

    with ap.Document() as last_page_document:
        last_page_document.pages.add(document.pages[total_pages])
        last_page_document.save(path.join(outdir, "Last_Page.pdf"))

    if total_pages == 1:
        return

    document.pages.delete(total_pages)  # Remove last page from original document
    document.save(path.join(outdir, "Previous_Pages.pdf"))
```

## Diviser un PDF en trois parties

Divisez un document PDF en trois parties distinctes en utilisant Aspose.PDF for Python.

1. Chargez le document PDF.
1. Déterminer le nombre total de pages.
1. Vérifiez si le document est vide.
1. Calculer la taille de la partie.
1. Itérer à travers trois parties.
1. Déterminer la plage de pages pour chaque partie.
1. Valider la plage de pages.
1. Créer un nouveau document pour chaque partie.
1. Copier les pages dans le document part.
1. Enregistrez chaque partie.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_into_three_parts(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    if total_pages == 0:
        return

    part_size = max(1, (total_pages + 2) // 3)

    for part_index in range(3):
        start_page = part_index * part_size + 1
        end_page = min((part_index + 1) * part_size, total_pages)

        if start_page > total_pages:
            break

        with ap.Document() as part_document:
            for page_num in range(start_page, end_page + 1):
                part_document.pages.add(document.pages[page_num])
            part_document.save(path.join(outdir, f"Three_Parts_{part_index + 1}.pdf"))
```

## Diviseur de pages PDF personnalisé

Divisez un document PDF en plusieurs fichiers en fonction de groupes de pages définis sur mesure en utilisant Aspose.PDF for Python.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_custom_page_groups(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)
    groups = [
        [1, 2, 5],
        [3, 4, 6, 7],
    ]

    for group_index, group in enumerate(groups, start=1):
        valid_pages = [page_num for page_num in group if 1 <= page_num <= total_pages]
        if not valid_pages:
            continue

        with ap.Document() as group_document:
            for page_num in valid_pages:
                group_document.pages.add(document.pages[page_num])
            group_document.save(path.join(outdir, f"Custom_Group_{group_index}.pdf"))
```

## Diviser le PDF en pages individuelles avec des noms de fichiers stables

Divisez un document PDF en pages individuelles et enregistrez-les avec des noms de fichiers stables en utilisant Aspose.PDF for Python.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_with_stable_filenames(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    for page_num in range(1, total_pages + 1):
        with ap.Document() as new_document:
            new_document.pages.add(document.pages[page_num])
            new_document.save(path.join(outdir, f"Page_{page_num:03d}.pdf"))
```

## Diviser le PDF en pages impaires et paires

Divisez un document PDF en deux fichiers distincts contenant respectivement les pages impaires et paires en utilisant Aspose.PDF for Python.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_odd_even_pages(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    # Odd pages document
    with ap.Document(infile) as document:
        with ap.Document() as odd_document:
            for page_num in range(1, total_pages + 1, 2):
                odd_document.pages.add(document.pages[page_num])
            odd_document.save(path.join(outdir, "Odd_Pages.pdf"))

        with ap.Document() as even_document:
            for page_num in range(2, total_pages + 1, 2):
                even_document.pages.add(document.pages[page_num])
            even_document.save(path.join(outdir, "Even_Pages.pdf"))
```

## Sujets de documents associés

- [Travailler avec des documents PDF en Python](/pdf/fr/python-net/working-with-documents/)
- [Fusionner des fichiers PDF en Python](/pdf/fr/python-net/merge-pdf-documents/)
- [Optimiser les fichiers PDF en Python](/pdf/fr/python-net/optimize-pdf/)
- [Manipuler des documents PDF en Python](/pdf/fr/python-net/manipulate-pdf-document/)

