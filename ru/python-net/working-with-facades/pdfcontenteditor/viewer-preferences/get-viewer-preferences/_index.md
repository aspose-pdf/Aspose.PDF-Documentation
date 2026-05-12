---
title: Получить настройки просмотра PDF
type: docs
weight: 20
url: /python-net/get-viewer-preferences/
description: Как программно считывать и изменять настройки просмотра PDF с использованием Aspose.PDF for Python
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Управление настройками просмотра PDF с помощью Aspose.PDF в Python
Abstract: В этом руководстве демонстрируется, как программно считывать и изменять настройки просмотра PDF с использованием Aspose.PDF for Python. Настройки просмотра определяют, как PDF отображается при открытии в PDF‑просмотрщике, например, с открытыми оглавлениями, скрытыми панелями инструментов или в режиме одиночной страницы.
---

Aspose.PDF предоставляет инструменты для доступа к настройкам просмотра PDF и их обновления. Эти настройки определяют начальное расположение и поведение представления PDF‑документа в PDF‑читателях. Это включает такие варианты, как включение представления оглавления, скрытие строк меню или указание режимов расположения страниц. С помощью PdfContentEditor вы можете получить существующие настройки, проверить отдельные флаги и при необходимости обновить их.

1. Определить ViewerPreference Flags.
1. Инициализировать [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) и привязать PDF.
1. Получить текущие Viewer Preferences.
1. Проверьте конкретные флаги.
1. Отобразить текущие настройки.

```python
import aspose.pdf.facades as pdf_facades
import sys
from enum import IntFlag
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_viewer_preferences(infile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Read current viewer preference flags
    viewer_preference = ViewerPreference(content_editor.get_viewer_preference())
    if viewer_preference & ViewerPreference.PAGE_MODE_USE_OUTLINES:
        print("PageModeUseOutlines is enabled")
    print(f"Current viewer preference: {viewer_preference}")
```
