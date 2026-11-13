---
title: Добавление верхних и нижних колонтитулов в PDF на Python
linktitle: Добавление колонтитулов
type: docs
weight: 70
url: /ru/python-net/artifacts-header-footer/
description: Добавить стилизованные элементы заголовка и нижнего колонтитула на страницы PDF в Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавление верхних и нижних колонтитулов в PDF на Python
Abstract: Добавить стилизованные элементы заголовка и нижнего колонтитула на страницы PDF в Python.
---

Использовать `HeaderArtifact` и `FooterArtifact` чтобы добавить бегущий текст на страницы PDF. Эти примеры добавляют артефакты на первую страницу.

## Создание текстовых артефактов с общим оформлением

Определите вспомогательную функцию перед запуском любого примера добавления. Она задаёт одинаковые шрифт, размер, цвет и выравнивание для верхних и нижних колонтитулов.

```python
import aspose.pdf as ap

def _create_text_artifact(artifact_class, text):
    """Create a text artifact (header/footer) with common styling."""
    artifact = artifact_class()
    artifact.text = text
    artifact.text_state.font_size = 14
    artifact.text_state.font = ap.text.FontRepository.find_font("Arial")
    artifact.text_state.foreground_color = ap.Color.navy
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
    return artifact
```

## Добавление артефакта верхнего колонтитула

Передайте класс `HeaderArtifact` вспомогательной функции и добавьте полученный артефакт на страницу.

```python
import aspose.pdf as ap

def add_header_artifact(infile, outfile):
    """Add a header artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        header = _create_text_artifact(ap.HeaderArtifact, "Sample Header")
        document.pages[1].artifacts.append(header)
        document.save(outfile)
```

## Добавление артефакта нижнего колонтитула

Передайте класс `FooterArtifact` вспомогательной функции и добавьте полученный артефакт на страницу.

```python
import aspose.pdf as ap

def add_footer_artifact(infile, outfile):
    """Add a footer artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        footer = _create_text_artifact(ap.FooterArtifact, "Sample Footer")
        document.pages[1].artifacts.append(footer)
        document.save(outfile)
```

## См. также

- [Удаление колонтитулов](/pdf/ru/python-net/remove-headers-footers/)
- [Работа с PDF-артефактами](/pdf/ru/python-net/artifacts/)
