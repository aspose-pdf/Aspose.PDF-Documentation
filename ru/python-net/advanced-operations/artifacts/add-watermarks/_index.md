---
title: Добавление водяного знака в PDF с использованием Python
linktitle: Добавление водяного знака
type: docs
weight: 30
url: /ru/python-net/add-watermarks/
description: Эта статья объясняет возможности работы с артефактами и создания водяных знаков в PDF с помощью Python программно.
lastmod: "2025-11-21"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как добавить водяной знак в PDF с помощью Python
Abstract: В статье рассматривается использование Aspose.PDF для Python через .NET для добавления водяных знаков в PDF‑документы посредством управления артефактами. Она представляет ключевые классы для работы с артефактами — `Artifact` и `ArtifactCollection`, и описывает, как получить к ним доступ через свойство `Artifacts` класса `Page`. В статье подробно описываются свойства класса `Artifact`, включая атрибуты такие как `contents`, `form`, `image`, `text`, `rectangle`, `rotation` и `opacity`, которые позволяют комплексно манипулировать артефактами в файлах PDF. Кроме того, приведён практический пример, демонстрирующий, как программно добавить водяной знак на первую страницу PDF с помощью Python. Фрагмент кода иллюстрирует создание и настройку `WatermarkArtifact`, установку его текста, выравнивания, вращения и непрозрачности, перед добавлением его в PDF‑документ и сохранением изменений.
---

## Программные примеры: Как добавить водяной знак в PDF‑файлы

Добавьте артефакт водяного знака в PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) с использованием Aspose.PDF для Python через .NET. Водяной знак — это визуальное наложение, применяемое к страницам для брендинга, безопасности или информационных целей. Пример показывает, как настроить внешний вид [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) и позиционирование с помощью [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) и [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/), вращение и прозрачность перед применением водяного знака к [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

1. Создайте артефакт водяного знака (см. [`WatermarkArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/)).
1. Настройте состояние текста (см. [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/)).
1. Привяжите текст к водяному знаку.
1. Определите позиционирование и стиль, используя [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) и [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/).
1. Прикрепите водяной знак к [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) через коллекцию [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) страницы (см. [`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)).
1. Сохраните обновлённый [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) с помощью [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

import aspose.pdf as ap

def add_watermark(input_pdf, output_pdf):
    # Load the existing PDF document
    document = ap.Document(input_pdf)

    # Create a watermark artifact
    watermark = ap.WatermarkArtifact()

    # Configure text state for the watermark
    text_state = ap.text.TextState()
    text_state.font_size = 72
    text_state.foreground_color = ap.Color.blue
    text_state.font = ap.text.FontRepository.find_font("Courier")

    # Apply text and style to the watermark
    watermark.set_text_and_state("WATERMARK", text_state)

    # Position and style settings
    watermark.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
    watermark.artifact_vertical_alignment = ap.VerticalAlignment.CENTER
    watermark.rotation = 45
    watermark.opacity = 0.5
    watermark.is_background = True

    # Add watermark to the first page
    document.pages[1].artifacts.append(watermark)

    # Save the updated PDF
    document.save(output_pdf)
```


