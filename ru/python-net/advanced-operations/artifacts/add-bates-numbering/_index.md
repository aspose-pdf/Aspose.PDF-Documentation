---
title: Добавление артефакта нумерации Бейтса в Python через .NET
linktitle: Добавление нумерации Бейтса
type: docs
weight: 10
url: /ru/python-net/add-bates-numbering/
description: Aspose.PDF for Python via .NET позволяет добавить нумерацию Бейтса в PDF.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить нумерацию Бейтса через Python
Abstract: Нумерация Бейтса является критически важной функцией в юридических, медицинских и бизнес‑документооборотах, обеспечивая уникальный последовательный идентификатор для каждой страницы в наборе, что гарантирует надёжную ссылку. Эта статья демонстрирует, как Aspose.PDF для Python через .NET упрощает автоматизацию нумерации Бейтса с помощью гибкого API. С помощью класса BatesNArtifact разработчики могут настроить поведение нумерации, включая количество знаков, префиксы, суффиксы, выравнивание и поля, и применять её программно ко всему документу. Представлены несколько подходов, от прямого применения артефакта до конфигурации на основе делегатов, предлагая как статический, так и динамический контроль. Кроме того, API поддерживает полное удаление нумерации Бейтса одним вызовом метода, обеспечивая полное управление жизненным циклом артефактов нумерации. Чёткие пошаговые примеры кода показывают, как добавлять, настраивать и удалять нумерацию Бейтса, делая это руководство практическим ресурсом для разработчиков, стремящихся оптимизировать процессы обработки документов.
---

Нумерация Бейтса широко используется в юридических, медицинских и бизнес‑процессах для назначения уникальных последовательных идентификаторов страницам в наборе документов. Aspose.PDF для Python через .NET предлагает простой и гибкий API для автоматизации этого процесса, позволяя программно применять стандартизированные номера Бейтса в любом PDF.

Используя класс [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/), разработчики могут полностью настроить поведение нумерации, включая начальное число, количество знаков, префиксы и суффиксы, выравнивание и поля. После настройки артефакт можно применить к [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) через метод `add_bates_numbering` на [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) или добавить в список объектов [`PaginationArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paginationartifact/). Aspose.PDF также поддерживает стиль конфигурации на основе делегатов, позволяя динамически управлять настройками артефакта во время выполнения.

Помимо создания номеров Бейтса, API предоставляет простой способ их удаления с помощью `delete_bates_numbering`, обеспечивая полную гибкость в процессах обработки документов.

В этой статье представлены различные методы добавления и удаления нумерации Бейтса в PDF с использованием Aspose.PDF для Python через .NET, с наглядными примерами настройки, применения и удаления артефакта.

## Добавление артефакта нумерации Бейтса

Этот пример показывает, как программно добавить нумерацию Бейтса в PDF‑документ с использованием Aspose.PDF для Python через .NET. Настраивая [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) с нужными параметрами и применяя его к страницам документа, вы можете автоматизировать процесс добавления стандартизированных идентификаторов к каждой странице.

Чтобы добавить артефакт нумерации Бейтса к [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), вызовите расширяющий метод `AddBatesNumbering(BatesNArtifact)` у [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/), передавая в качестве параметра экземпляр [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/).

```python

import aspose.pdf as ap

def add_bates_numbering(path_outfile):
    # Create a new or empty PDF document
    with ap.Document() as document:

        # Add 10 blank pages
        for _ in range(10):
            document.pages.add()

        # Create Bates numbering artifact
        bates = ap.BatesNArtifact(
            start_page=1,
            end_page=0,  # 0 = apply until last page
            subset=ap.Subset.ALL,
            number_of_digits=6,
            start_number=1,
            prefix="",
            suffix="",
            artifact_vertical_alignment=ap.VerticalAlignment.BOTTOM,
            artifact_horizontal_alignment=ap.HorizontalAlignment.RIGHT,
            right_margin=72,
            left_margin=72,
            top_margin=36,
            bottom_margin=36
        )

        # Add Bates numbering to all pages
        document.pages.add_bates_numbering(bates)

        # Save the resulting PDF
        document.save(path_outfile)
```

Или вы можете передать коллекцию объектов [`PaginationArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paginationartifact/).

```python

import aspose.pdf as ap

def add_bates_numbering_collection(path_outfile):
    with ap.Document() as document:

        # Add 10 pages
        for _ in range(10):
            document.pages.add()

        # Create Bates artifact
        bates = ap.BatesNArtifact(
            start_page=1,
            end_page=0,
            subset=ap.Subset.ALL,
            number_of_digits=6,
            start_number=1,
            prefix="",
            suffix="",
            artifact_vertical_alignment=ap.VerticalAlignment.BOTTOM,
            artifact_horizontal_alignment=ap.HorizontalAlignment.RIGHT,
            right_margin=72,
            left_margin=72,
            top_margin=36,
            bottom_margin=36
        )

        # Add as a pagination artifact list
        document.pages.add_pagination([bates])

        # Save document
        document.save(path_outfile)
```

Добавьте артефакт нумерации Бейтса, используя делегат действия:

```python

import aspose.pdf as ap

def add_bates_numbering_delegate(path_outfile):
    def configure_bates(b):
        """Configure Bates numbering artifact with desired settings."""
        b.start_page = 1
        b.end_page = 0
        b.subset = ap.Subset.ALL
        b.number_of_digits = 6
        b.start_number = 1
        b.prefix = ""
        b.suffix = ""
        b.artifact_vertical_alignment = ap.VerticalAlignment.BOTTOM
        b.artifact_horizontal_alignment = ap.HorizontalAlignment.RIGHT
        b.right_margin = 72
        b.left_margin = 72
        b.top_margin = 36
        b.bottom_margin = 36
        b.text_state.font_size = 10
    
    with ap.Document() as document:

        # Add 10 pages
        for _ in range(10):
            document.pages.add()

        # Use delegate function to configure Bates artifact
        document.pages.add_bates_numbering(configure_bates)

        # Save output PDF
        document.save(path_outfile)
```

## Удалить нумерацию Бейтса

Чтобы удалить нумерацию Бейтса из [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), используйте метод `delete_bates_numbering()` у [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/):

```python

import aspose.pdf as ap

def delete_bates_numbering(path_infile, path_outfile):
    with ap.Document(path_infile) as document:

        # Remove Bates numbering from all pages
        document.pages.delete_bates_numbering()

        # Save updated document
        document.save(path_outfile)
```
