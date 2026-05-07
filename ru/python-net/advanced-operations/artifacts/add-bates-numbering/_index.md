---
title: Добавить нумерацию Бейтса в PDF с помощью Python
linktitle: Добавление нумерации Бейтса
type: docs
weight: 10
url: /ru/python-net/add-bates-numbering/
description: Узнайте, как добавлять и удалять нумерацию Бейтса в PDF‑документах, используя Python с Aspose.PDF for Python via .NET.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Добавить нумерацию Бейтса с помощью Python
Abstract: Нумерация Бейтса является критической функцией в юридических, медицинских и бизнес‑процессах работы с документами, обеспечивая уникальный последовательный идентификатор для каждой страницы набора, что повышает надёжность ссылок. В этой статье показано, как Aspose.PDF for Python via .NET упрощает автоматизацию нумерации Бейтса с помощью гибкого API. С помощью класса BatesNArtifact разработчики могут настроить поведение нумерации — включая количество цифр, префиксы, суффиксы, выравнивание и отступы — и применить её программно ко всему документу. Представлено несколько подходов, от прямого применения артефакта до конфигурации на основе делегатов, предлагающих как статический, так и динамический контроль. Кроме того, API поддерживает полное удаление номеров Бейтса одним вызовом метода, обеспечивая полное управление жизненным циклом артефактов нумерации. Чёткие пошаговые примеры кода демонстрируют, как добавить, настроить и удалить нумерацию Бейтса, делая это руководство практическим ресурсом для разработчиков, желающих оптимизировать процессы обработки документов.
---

Нумерация Бейтса широко используется в юридических, медицинских и бизнес-процессах для назначения уникальных последовательных идентификаторов страницам в наборе документов. Aspose.PDF for Python via .NET предлагает простой и гибкий API для автоматизации этого процесса, позволяя программно применять стандартизированные номера Бейтса к любому PDF.

Используя [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) класс, разработчики могут полностью настраивать поведение нумерации — включая начальный номер, количество цифр, префиксы и суффиксы, выравнивание и отступы. После настройки артефакт может быть применён к [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) через `add_bates_numbering` метод на [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) или добавлено как часть списка [`PaginationArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paginationartifact/) objects. Aspose.PDF также поддерживает стиль конфигурации на основе делегатов, позволяя динамически управлять настройками артефактов во время выполнения.

Помимо создания номеров Бейтса, API предоставляет простой способ их удаления с помощью `delete_bates_numbering`, предлагая полную гибкость в рабочих процессах обработки документов.

В этой статье показаны различные методы добавления и удаления нумерации Бейтса в PDF с использованием Aspose.PDF for Python via .NET, с наглядными примерами настройки артефактов, их применения и удаления.

## Добавление артефакта нумерации Бейтса

В этом примере показано, как программно добавить нумерацию Бейтса в PDF‑документ, используя Aspose.PDF for Python via .NET. Настраивая a [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) с желаемыми настройками и применяя её к страницам документа, вы можете автоматизировать процесс добавления стандартных идентификаторов к каждой странице.

Чтобы добавить артефакт нумерации Бейтса в a [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), вызовите `AddBatesNumbering(BatesNArtifact)` расширяющий метод для [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/), передавая [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) экземпляр в качестве параметра:

```python
import sys
from os import path
import aspose.pdf as ap

def _create_bates_artifact():
    """Create a Bates numbering artifact with default settings."""
    artifact = ap.BatesNArtifact()
    artifact.start_page = 1
    artifact.end_page = 0
    artifact.subset = ap.Subset.ALL
    artifact.number_of_digits = 6
    artifact.start_number = 1
    artifact.prefix = ""
    artifact.suffix = ""
    artifact.artifact_vertical_alignment = ap.VerticalAlignment.BOTTOM
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.RIGHT
    artifact.right_margin = 72
    artifact.left_margin = 72
    artifact.top_margin = 36
    artifact.bottom_margin = 36
    return artifact
```

```python
import sys
from os import path
import aspose.pdf as ap

def add_bates_n_artifact(infile, outfile):
    """Add Bates numbering artifact to a PDF document."""
    with ap.Document(infile) as document:
        for _ in range(2):
            document.pages.add()

        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_bates_numbering(document.pages, bates_artifact)
        document.save(outfile)
```

## Добавить нумерацию Bates с использованием артефактов пагинации

Добавьте нумерацию Bates в PDF, используя коллекцию артефактов пагинации в Aspose.PDF for Python:

1. Загрузите документ PDF.
1. Вставьте дополнительные страницы при необходимости перед применением нумерации.
1. Создайте артефакт Bates.
1. Настройте свойства артефакта.
1. Добавьте артефакт в коллекцию нумерации.
1. Примените пагинацию к страницам.
1. Сохраните обновлённый документ.

```python
import sys
from os import path
import aspose.pdf as ap

def add_bates_n_artifact_pagination(infile, outfile):
    """Add Bates numbering using pagination artifacts collection."""
    with ap.Document(infile) as document:
        for _ in range(2):
            document.pages.add()

        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_pagination(document.pages, [bates_artifact])
        document.save(outfile)
```

## Удалить нумерацию Bates

Чтобы удалить нумерацию Bates из [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), используйте `delete_bates_numbering()` метод на [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/):

```python
import sys
from os import path
import aspose.pdf as ap

def delete_bates_numbering(infile, outfile):
    """Delete Bates numbering from a PDF document."""
    with ap.Document(infile) as document:
        ap.PageCollectionExtensions.delete_bates_numbering(document.pages)
        document.save(outfile)
```

## Связанные темы артефактов

- [Работа с PDF-артефактами в Python](/pdf/ru/python-net/artifacts/)
- [Добавить водяные знаки в PDF на Python](/pdf/ru/python-net/add-watermarks/)
- [Добавить фон PDF в Python](/pdf/ru/python-net/add-backgrounds/)
- [Подсчитать типы артефактов в PDF‑файлах](/pdf/ru/python-net/counting-artifacts/)