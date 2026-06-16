---
title: احصل على تعويض الصفحة
linktitle: احصل على تعويض الصفحة
type: docs
weight: 20
url: /ar/python-net/get-page-offset/
description: يوضح هذا المثال كيفية استخدام PDFfileInfo للحصول على إزاحة X و Y لصفحة معينة وتحويلها إلى بوصات للتخطيط الدقيق وتحليل تحديد المواقع.
lastmod: "2026-06-11"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: احصل على إزاحات صفحة PDF باستخدام Python
Abstract: تقوم وظيفة «get_page_offsets» باستخراج الإزاحات الأفقية (X) والعمودية (Y) لكل صفحة في ملف PDF. تمثل هذه الإزاحات موضع محتوى الصفحة بالنسبة إلى أصل PDF. من خلال تحويل النقاط إلى بوصات، توفر الوظيفة قياسات دقيقة يمكن للبشر قراءتها ويمكن استخدامها لوضع التعليقات التوضيحية أو الصور أو النصوص بدقة. وهو يدعم ملفات PDF متعددة الصفحات وهو مخصص للمطورين الذين يعملون على مهام تخطيط PDF أو التشغيل الآلي أو محاذاة المحتوى.
---

توفر وظيفة «get_page_offsets» للمطورين الإزاحات الأفقية (X) والعمودية (Y) الدقيقة للصفحات في ملف PDF. في مستندات PDF، قد تحتوي كل صفحة على نقطة أصل داخلية تختلف عن الزاوية العلوية اليسرى من الصفحة، والتي يمكن أن تؤثر على موضع النص أو الصور أو التعليقات التوضيحية أو أي محتوى آخر.

باستخدام واجهات Aspose.PDF، تقوم هذه الوظيفة باستخراج هذه الإزاحات بالنقاط وتحويلها إلى بوصات لسهولة التفسير. وهو يدعم ملفات PDF متعددة الصفحات، مما يجعلها مناسبة لسير العمل الآلي الذي يتطلب وضع المحتوى بدقة.

1. قم بإنشاء كائن واجهة PDF.
1. احصل على عدد الصفحات في PDF.
1. قم بالتمرير عبر كل صفحة للحصول على الإزاحات.
1. قم بطباعة الإزاحات أو تخزينها.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_page_offsets(infile):
    # Get and display PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)
    page_x_offset = pdf_info.get_page_x_offset(1) / 72.0
    page_y_offset = pdf_info.get_page_y_offset(1) / 72.0
    print(f"Page X Offset: {page_x_offset} inches")
    print(f"Page Y Offset: {page_y_offset} inches")
```
