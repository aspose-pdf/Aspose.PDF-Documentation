---
title: Импорт и экспорт аннотаций с использованием Python
linktitle: Импорт и экспорт аннотаций
type: docs
weight: 80
url: /python-net/import-export-annotations/
description: Узнайте, как импортировать аннотации из одного PDF и экспортировать их в новый PDF-документ, используя Aspose.PDF for Python via .NET.
lastmod: "2026-04-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Переносите аннотации PDF между документами в Python.
Abstract: В этой статье объясняется, как копировать аннотации из исходного PDF и экспортировать их в новый PDF‑документ с использованием Aspose.PDF for Python via .NET. Пошаговое руководство разбивает процесс на небольшие шаги, включая загрузку исходного файла, создание целевого документа, добавление страницы, копирование аннотаций с первой страницы и сохранение результата.
---

В этой статье показано, как импортировать аннотации из существующего PDF и экспортировать их в новый PDF‑документ, используя Aspose.PDF for Python via .NET.

Пример считывает аннотации с первой страницы исходного файла, создает новый PDF, добавляет пустую страницу и копирует каждую аннотацию на эту новую страницу. Такой подход полезен, когда необходимо перенести комментарии, разметку или заметки рецензии в отдельный выходной документ.

## Загрузите исходный PDF

Создать `Document` объект входного файла, который уже содержит аннотации. Этот объект предоставляет доступ к коллекции страниц и аннотациям, хранящимся на каждой странице.

```python
source_document = ap.Document(infile)
```

## Создать целевой PDF

Затем создайте пустой PDF‑документ, который будет принимать импортированные аннотации. На данном этапе целевой документ не содержит страниц.

```python
destination_document = ap.Document()
```

## Добавить страницу для экспортированных аннотаций

Поскольку аннотации должны принадлежать странице, добавьте новую страницу в целевой документ перед копированием чего‑либо.

```python
page = destination_document.pages.add()
```

## Скопировать аннотации с исходной страницы

Пройдитесь по коллекции аннотаций на первой странице исходного PDF и добавьте каждую аннотацию на новую страницу в целевом документе.

Второй аргумент в `page.annotations.add(annot, True)` сообщает Aspose.PDF копировать аннотацию в целевую страницу вместо простого переиспользования существующей ссылки на объект.

```python
for annot in source_document.pages[1].annotations:
    page.annotations.add(annot, True)
```

## Сохранить выходной документ

После того как все аннотации будут скопированы, сохраните целевой документ, чтобы создать окончательный PDF‑файл.

```python
destination_document.save(outfile)
```

## Полный пример

Следующий код объединяет все шаги в одну переиспользуемую функцию:

```python
import sys
import aspose.pdf as ap
from os import path


sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def import_export(infile, outfile):
    """
    Import annotations from one PDF document and export them to a new PDF document.
    """
    source_document = ap.Document(infile)
    destination_document = ap.Document()

    page = destination_document.pages.add()

    for annot in source_document.pages[1].annotations:
        page.annotations.add(annot, True)

    destination_document.save(outfile)
```

## Связанные темы

- [Интерактивные аннотации](/python-net/interactive-annotations/)
- [Разметка аннотаций](/python-net/markup-annotations/)
- [Медиа‑аннотации](/python-net/media-annotations/)
- [Аннотации безопасности](/python-net/security-annotations/)
- [Фигурные аннотации](/python-net/shape-annotations/)
- [Текстовые аннотации](/python-net/text-based-Annotations/)
- [Аннотации водяных знаков](/python-net/watermark-annotations/)
