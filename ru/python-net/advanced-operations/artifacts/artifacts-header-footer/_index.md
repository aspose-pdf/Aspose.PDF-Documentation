---
title: Управляйте заголовками и нижними колонтитулами PDF с помощью Python
linktitle: Управляйте заголовками и нижними колонтитулами PDF
type: docs
weight: 70
url: /ru/python-net/artifacts-header-footer/
description: Узнайте, как управлять заголовками и нижними колонтитулами в PDF‑документах с помощью Python и Aspose.PDF.
lastmod: "2026-04-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Как добавлять, настраивать и удалять заголовки и нижние колонтитулы PDF с использованием Python
Abstract: Управление колонтитулами — это распространённое требование при работе с PDF‑документами в бизнесе, издательском деле и автоматизированных рабочих процессах. В этой статье демонстрируется, как с помощью Aspose.PDF for Python добавить профессиональные колонтитулы с пользовательским оформлением, таким как шрифт, размер, цвет и выравнивание. Также показывается, как обнаруживать и удалять существующие артефакты нумерации страниц, такие как колонтитулы, на странице PDF. Благодаря переиспользуемым функциям и понятным примерам разработчики могут быстро интегрировать эти возможности в системы обработки документов для брендирования, отчётности или очистки файлов.
---

## Создать стилизованные текстовые артефакты

Эта утилитная функция объясняет, как создать переиспользуемый текстовый артефакт для страниц PDF с использованием Aspose.PDF for Python. Она предназначена для генерации стилизованных заголовков или нижних колонтитулов с единообразным форматированием, включая настройки шрифтов, цвет, размер и выравнивание. Функция абстрагирует создание артефакта, чтобы его можно было переиспользовать для различных текстовых украшений уровня страницы.

1. Создайте объект артефакта.
1. Установите текстовое содержимое артефакта.
1. Примените стилизацию текста.
1. Установить выравнивание.
1. Вернуть сконфигурированный артефакт.

```python
from os import path
import aspose.pdf as ap
import sys

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

## Добавить заголовок в PDF

1. Откройте входной PDF.
1. Создайте HeaderArtifact с текстом "Sample Header".
1. Добавьте его к первой странице.
1. Сохраните обновлённый PDF.

```python
from os import path
import aspose.pdf as ap
import sys

def add_header_artifact(infile, outfile):
    """Add a header artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        header = _create_text_artifact(ap.HeaderArtifact, "Sample Header")
        document.pages[1].artifacts.append(header)
        document.save(outfile)
```

## Добавить нижний колонтитул в PDF

1. Откройте входной PDF.
1. Создайте FooterArtifact с текстом "Sample Footer".
1. Добавьте его к первой странице.
1. Сохраните выходной файл.

```python
from os import path
import aspose.pdf as ap
import sys

def add_footer_artifact(infile, outfile):
    """Add a footer artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        footer = _create_text_artifact(ap.FooterArtifact, "Sample Footer")
        document.pages[1].artifacts.append(footer)
        document.save(outfile)
```

## Удалить артефакты заголовка или нижнего колонтитула

1. Откройте PDF.
1. Найдите артефакты, помеченные как заголовки или нижние колонтитулы страниц.
1. Удалите их с первой страницы.
1. Сохраните очищенный документ.

```python
from os import path
import aspose.pdf as ap
import sys

def delete_header_footer_artifact(infile, outfile):
    with ap.Document(infile) as document:
        header_footers = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and (
                artifact.subtype == ap.Artifact.ArtifactSubtype.HEADER
                or artifact.subtype == ap.Artifact.ArtifactSubtype.FOOTER
            )
        ]

        for art in header_footers:
            document.pages[1].artifacts.delete(art)

        document.save(outfile)
```

## Связанные темы артефактов

- [Работа с PDF-артефактами в Python](/pdf/ru/python-net/artifacts/)
- [Добавить фон PDF в Python](/pdf/ru/python-net/add-backgrounds/)
- [Добавить нумерацию Бейтса в PDF на Python](/pdf/ru/python-net/add-bates-numbering/)
- [Подсчитать типы артефактов в PDF‑файлах](/pdf/ru/python-net/counting-artifacts/)