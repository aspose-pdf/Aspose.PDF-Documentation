---
title: Добавление нумерации Бейтса в PDF на Python
linktitle: Добавление нумерации Бейтса
type: docs
weight: 10
url: /ru/python-net/add-bates-numbering/
description: Добавить последовательные идентификаторы Bates к страницам PDF на Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавление нумерации Бейтса в PDF на Python
Abstract: Добавить последовательные идентификаторы Bates к страницам PDF на Python.
---

Нумерация Бейтса присваивает последовательные идентификаторы страницам в наборе документов. Настройте a `BatesNArtifact` для управления диапазоном страниц, начальным номером, количеством цифр, префиксом, суффиксом и расположением.

## Добавление нумерации Бейтса специальным методом

Передайте настроенный артефакт и страницы документа в `PageCollectionExtensions.add_bates_numbering`. Пример присваивает существующим страницам шестизначные идентификаторы начиная с `000001`.

```python
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


def add_bates_n_artifact(infile, outfile):
    """Add Bates numbering artifact to a PDF document."""
    with ap.Document(infile) as document:
        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_bates_numbering(document.pages, bates_artifact)
        document.save(outfile)
```

## Добавление нумерации Бейтса через артефакты пагинации

Чтобы добавить нумерацию Бейтса через API пагинации, воспользуйтесь функцией `_create_bates_artifact` из предыдущего примера. Передайте список с артефактом в `PageCollectionExtensions.add_pagination`.

```python
import aspose.pdf as ap

def add_bates_n_artifact_pagination(infile, outfile):
    """Add Bates numbering using pagination artifacts collection."""
    with ap.Document(infile) as document:
        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_pagination(document.pages, [bates_artifact])
        document.save(outfile)
```

## См. также

- [Удаление нумерации Бейтса](/pdf/ru/python-net/remove-bates-numbering/)
- [Работа с PDF-артефактами](/pdf/ru/python-net/artifacts/)
