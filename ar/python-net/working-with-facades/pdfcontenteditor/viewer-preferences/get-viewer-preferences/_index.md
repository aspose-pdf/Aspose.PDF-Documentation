---
title: احصل على تفضيلات عارض PDF
linktitle: احصل على تفضيلات عارض PDF
type: docs
weight: 20
url: /ar/python-net/get-viewer-preferences/
description: كيفية قراءة وتعديل تفضيلات عارض PDF برمجيًا باستخدام Aspose.PDF لـ Python
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إدارة تفضيلات عارض PDF باستخدام Aspose.PDF في بايثون
Abstract: يوضح هذا الدليل كيفية قراءة وتعديل تفضيلات عارض PDF برمجيًا باستخدام Aspose.PDF لـ Python. تتحكم تفضيلات العارض في كيفية عرض PDF عند فتحه في عارض PDF، مثل الفتح باستخدام الخطوط العريضة أو إخفاء أشرطة الأدوات أو استخدام تخطيط صفحة واحدة.
---

يوفر Aspose.PDF أدوات للوصول إلى تفضيلات عارض PDF وتحديثها. تحدد هذه التفضيلات التخطيط الأولي وسلوك العرض التقديمي لمستند PDF في قارئات PDF. يتضمن ذلك خيارات مثل تمكين عرض المخطط التفصيلي أو إخفاء أشرطة القوائم أو تحديد أوضاع تخطيط الصفحة. باستخدام PDFContentEditor، يمكنك استرداد التفضيلات الحالية والتحقق من العلامات المحددة وتحديثها حسب الحاجة.

1. حدد علامات تفضيلات العارض.
1. تهيئة [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) وقم بربط ملف PDF.
1. احصل على تفضيلات العارض الحالية.
1. تحقق من العلامات المحددة.
1. عرض التفضيلات الحالية.

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
