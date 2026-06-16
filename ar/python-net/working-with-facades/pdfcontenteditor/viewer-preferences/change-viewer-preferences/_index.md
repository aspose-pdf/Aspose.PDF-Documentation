---
title: تغيير تفضيلات عارض PDF
linktitle: تغيير تفضيلات عارض PDF
type: docs
weight: 10
url: /ar/python-net/change-viewer-preferences/
description: توضح هذه الوحدة كيفية ضبط إعدادات عارض مستند PDF باستخدام Aspose.PDF لـ Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تخصيص تجربة عارض PDF باستخدام Python
Abstract: تحكم في كيفية ظهور مستند PDF عند فتحه عن طريق تعديل تفضيلات المشاهد برمجيًا. تسمح لك هذه الوظيفة بتخصيص واجهة المستخدم والتخطيط، مما يضمن تجربة مشاهدة متسقة.
---

تحتوي ملفات PDF على تفضيلات عارض مضمنة تتحكم في جوانب مثل تخطيط الصفحة ورؤية شريط الأدوات وسلوك النافذة. باستخدام هذا البرنامج النصي، يمكنك:

- افحص تفضيلات المشاهد الحالية لملف PDF.
- قم بتعديل خيارات التخطيط (على سبيل المثال، صفحة واحدة، عمود واحد، عمودين).
- قم بتبديل عناصر واجهة المستخدم مثل شريط الأدوات أو شريط القوائم أو عرض العنوان.
- احفظ ملف PDF مع التفضيلات المحدثة لتجربة مشاهدة محكومة.

1. حدد علامات تفضيلات العارض.
1. احصل على تفضيلات العارض الحالية.
1. تعديل التفضيلات.
1. قم بتطبيق التفضيلات المحدثة.
1. احفظ ملف PDF.

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
