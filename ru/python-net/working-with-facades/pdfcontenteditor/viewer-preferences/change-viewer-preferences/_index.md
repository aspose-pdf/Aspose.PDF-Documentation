---
title: Изменить параметры просмотра PDF
linktitle: Изменить параметры просмотра PDF
type: docs
weight: 10
url: /python-net/change-viewer-preferences/
description: Этот модуль демонстрирует, как настроить параметры просмотра PDF‑документа с помощью Aspose.PDF for Python.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Настройте просмотр PDF с помощью Python
Abstract: Управляйте тем, как ваш PDF‑документ отображается при открытии, программно изменяя параметры просмотра. Эта возможность позволяет настроить пользовательский интерфейс и макет, обеспечивая единообразный опыт просмотра.
---

Файлы PDF имеют встроенные параметры просмотра, которые управляют такими аспектами, как расположение страниц, видимость панели инструментов и поведение окна. С помощью этого скрипта вы можете:

- Проверьте текущие параметры просмотра PDF.
- Изменить параметры макета (например, одностраничный, одноколоночный, двухколоночный).
- Переключать элементы интерфейса, такие как панель инструментов, строка меню или отображение заголовка.
- Сохранить PDF с обновлёнными настройками для контролируемого просмотра.

1. Определите ViewerPreference Flags.
1. Получите текущие Viewer Preferences.
1. Измените настройки.
1. Примените обновлённые настройки.
1. Сохраните PDF.

```python
import aspose.pdf.facades as pdf_facades
import sys
from enum import IntFlag
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Define ViewerPreference flags
class ViewerPreference(IntFlag):
    HIDE_TOOLBAR = 1
    HIDE_MENUBAR = 2
    HIDE_WINDOW_UI = 4
    FIT_WINDOW = 8
    CENTER_WINDOW = 16
    DISPLAY_DOC_TITLE = 32
    NON_FULL_SCREEN_PAGE_MODE_USE_NONE = 64
    NON_FULL_SCREEN_PAGE_MODE_USE_OUTLINES = 128
    NON_FULL_SCREEN_PAGE_MODE_USE_THUMBS = 256
    NON_FULL_SCREEN_PAGE_MODE_USE_OC = 512
    DIRECTION_L2R = 1024
    DISPLAY_DOC_TITLE_IN_TITLE_BAR = 2048
    PAGE_LAYOUT_SINGLE_PAGE = 4096
    PAGE_LAYOUT_ONE_COLUMN = 8192
    PAGE_LAYOUT_TWO_COLUMN_LEFT = 16384
    PAGE_LAYOUT_TWO_COLUMN_RIGHT = 32768
    PAGE_LAYOUT_TWO_PAGE_LEFT = 65536
    PAGE_LAYOUT_TWO_PAGE_RIGHT = 131072


def change_viewer_preferences(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    # Get current viewer preference and toggle single-page layout
    current_preference = ViewerPreference(content_editor.get_viewer_preference())
    updated_preference = current_preference | ViewerPreference.PAGE_LAYOUT_SINGLE_PAGE
    content_editor.change_viewer_preference(int(updated_preference))

    # Save updated document
    content_editor.save(outfile)
```
