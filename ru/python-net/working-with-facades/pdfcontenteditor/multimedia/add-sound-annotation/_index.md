---
title: Добавить звуковую аннотацию
type: docs
weight: 20
url: /python-net/add-sound-annotation/
description: В этом примере привязывается входной PDF, добавляется звуковая аннотация на странице 1 и сохраняется изменённый PDF.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить звуковую аннотацию в PDF с помощью PdfContentEditor в Python
Abstract: В этом примере показывается, как встроить аудио в документ PDF с использованием Aspose.PDF for Python через API Facades. Показано, как добавить кликабельную звуковую аннотацию, которая воспроизводит аудиофайл непосредственно в PDF.
---

Звуковые аннотации в PDF позволяют добавлять аудиоконтент, такой как голосовые заметки, музыка или звуковые эффекты, в ваши документы. Используя [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), вы можете определить небольшой кликабельный прямоугольник на странице, который воспроизводит указанный аудиофайл при активации.

1. Создайте экземпляр PdfContentEditor.
1. Привяжите входной PDF‑документ.
1. Определите прямоугольник для звуковой аннотации.
1. Укажите аудиофайл, имя аннотации, номер страницы и частоту дискретизации.
1. Сохраните обновлённый PDF‑документ.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_sound_annotation(infile, sound_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add sound annotation to page 1
    content_editor.create_sound(
        apd.Rectangle(80, 450, 30, 30), sound_file, "Speaker", 1, "8000"
    )
    # Save updated document
    content_editor.save(outfile)
```
