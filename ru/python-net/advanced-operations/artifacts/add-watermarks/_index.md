---
title: Добавить водяные знаки в PDF в Python
linktitle: Добавление водяного знака
type: docs
weight: 30
url: /ru/python-net/add-watermarks/
description: Узнайте, как добавить артефакты водяного знака в PDF‑файлы на Python, используя Aspose.PDF for Python via .NET.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как добавить водяной знак в PDF с помощью Python
Abstract: В статье рассматривается использование Aspose.PDF for Python via .NET для добавления водяных знаков в PDF‑документы посредством управления артефактами. Представляются ключевые классы для работы с артефактами — `Artifact` и `ArtifactCollection`, а также описывается, как получить к ним доступ через свойство `Artifacts` класса `Page`. В статье подробно описываются свойства класса `Artifact`, включая такие атрибуты, как `contents`, `form`, `image`, `text`, `rectangle`, `rotation` и `opacity`, которые позволяют осуществлять исчерпывающее управление артефактами в файлах PDF. Кроме того, приведён практический пример, демонстрирующий, как программно добавить водяной знак на первую страницу PDF с помощью Python. В фрагменте кода показано создание и настройка `WatermarkArtifact`, установка его текста, выравнивания, вращения и непрозрачности, после чего артефакт добавляется в PDF‑документ и сохраняются изменения.
---

Добавить артефакт водяного знака в PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) используя Aspose.PDF for Python via .NET. Водяной знак — это визуальное наложение, применяемое к страницам для брендинга, безопасности или информационных целей. Пример показывает, как настроить [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) внешний вид, позиционирование с [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) и [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/), вращение и прозрачность перед применением водяного знака к [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

## Извлечь водяные знаки из PDF

1. Загрузите документ PDF.
1. Получите доступ к артефактам страницы.
1. Отфильтруйте артефакты водяных знаков.
1. Соберите элементы водяных знаков.
1. Извлеките свойства водяного знака.
1. Выведите информацию о водяном знаке.

```python
from os import path
import sys
import aspose.pdf as ap

def extract_watermark_from_pdf(infile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            print(f"{watermark.text} {watermark.rectangle}")
```

## Добавить водяной знак в PDF

Добавьте текстовый водяной знак в PDF‑документ с помощью Aspose.PDF for Python:

1. Загрузите документ PDF.
1. Создайте состояние текста.
1. Создайте артефакт водяного знака.
1. Установите текст водяного знака и стиль.
1. Настройте позиционирование и вращение.
1. Установите непрозрачность и поведение фона.
1. Прикрепите водяной знак к странице.
1. Сохраните обновлённый документ.

```python
from os import path
import sys
import aspose.pdf as ap

def add_watermark_artifact(infile, outfile):
    with ap.Document(infile) as document:
        text_state = ap.text.TextState()
        text_state.font_size = 72
        text_state.foreground_color = ap.Color.blue_violet
        text_state.font_style = ap.text.FontStyles.BOLD
        text_state.font = ap.text.FontRepository.find_font("Arial")

        watermark = ap.WatermarkArtifact()
        watermark.set_text_and_state("WATERMARK", text_state)
        watermark.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
        watermark.artifact_vertical_alignment = ap.VerticalAlignment.CENTER
        watermark.rotation = 60
        watermark.opacity = 0.2
        watermark.is_background = True

        document.pages[1].artifacts.append(watermark)
        document.save(outfile)

```

## Удалить артефакты водяных знаков со страницы PDF

Удалить артефакты водяного знака с конкретной страницы PDF‑документа, используя API Aspose.PDF for Python. Этот подход ориентируется на элементы водяного знака, хранящиеся как артефакты страницы (в частности, классифицированные как подтипы пагинации водяного знака), проходит их в цикле и удаляет перед сохранением обновленного документа.

1. Загрузите документ PDF.
1. Получите доступ к артефактам страницы.
1. Отфильтруйте артефакты водяных знаков.
1. Удалите артефакты водяного знака.
1. Сохраните обновлённый документ.

```python
from os import path
import sys
import aspose.pdf as ap

def delete_watermark_artifact(infile, outfile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            document.pages[1].artifacts.delete(watermark)

        document.save(outfile)
```

## Связанные темы артефактов

- [Работа с PDF-артефактами в Python](/pdf/ru/python-net/artifacts/)
- [Добавить фон PDF в Python](/pdf/ru/python-net/add-backgrounds/)
- [Добавить нумерацию Бейтса в PDF на Python](/pdf/ru/python-net/add-bates-numbering/)
- [Подсчитать типы артефактов в PDF‑файлах](/pdf/ru/python-net/counting-artifacts/)