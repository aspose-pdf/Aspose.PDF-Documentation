---
title: احصل على معلومات الصفحة
linktitle: احصل على معلومات الصفحة
type: docs
weight: 10
url: /ar/python-net/get-page-info/
description: تعرف على كيفية الوصول برمجيًا إلى المعلومات على مستوى الصفحة في PDF باستخدام Aspose.PDF لـ Python. يوضح هذا الدليل كيفية استرداد عرض الصفحة والارتفاع والتدوير والإزاحات لصفحة معينة في مستند PDF.
lastmod: "2026-06-11"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: احصل على معلومات صفحة PDF باستخدام Aspose.PDF لبيثون
Abstract: تستخرج الدالة العرض والارتفاع والدوران والإزاحات الأفقية (X) والعمودية (Y) لصفحة PDF. يتم إرجاع هذه الخصائص بالنقاط وتعكس الحجم الفعلي للصفحة وموضع المحتوى داخل PDF. تقوم الوظيفة بطباعة القيم المستردة، مما يسمح للمطورين بفهم تخطيط الصفحة واتجاهها لمزيد من معالجة PDF.
---

تساعد وظيفة الأداة المساعدة «get_page_information» المطورين على فهم بنية وتخطيط صفحات PDF. قد تحتوي كل صفحة PDF على أبعاد ودوران وإزاحات داخلية مختلفة، مما قد يؤثر على وضع المحتوى أو مهام التشغيل الآلي.

يتميز باسترداد البيانات الوصفية الرئيسية ومعلومات التخطيط لصفحة معينة في ملف PDF. توفر واجهة برمجة تطبيقات Aspose.PDF للواجهات تفاصيل مثل عرض الصفحة والارتفاع والدوران وإزاحات X/Y. هذه المعلومات ضرورية لمهام مثل تحليل تخطيط الصفحة أو وضع التعليقات التوضيحية أو معالجة PDF الآلية.

1. قم بإنشاء كائن واجهة PDF.
1. استرجع أبعاد الصفحة وتخطيطها.
1. قم بطباعة القيم المستردة أو تخزينها.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_page_information(infile):

    # Get and display PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)
    page_width = pdf_info.get_page_width(1)
    page_height = pdf_info.get_page_height(1)
    page_rotation = pdf_info.get_page_rotation(1)
    page_x_offset = pdf_info.get_page_x_offset(1)
    page_y_offset = pdf_info.get_page_y_offset(1)

    print(f"Page Width: {page_width}")
    print(f"Page Height: {page_height}")
    print(f"Page Rotation: {page_rotation}")
```
