---
title: استخراج الجداول من PDF في Python
linktitle: جدول الاستخراج
type: docs
weight: 20
url: /ar/python-net/extracting-table/
description: تعرف على كيفية استخراج بيانات الجدول من مستندات PDF الموجودة في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استخراج بيانات الجدول من ملفات PDF باستخدام Python
Abstract: توضح هذه المقالة كيفية استخراج الجداول من مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. يوضح كيفية استخدام `TableAbsorber` لاكتشاف الجداول حسب الصفحة، وتكرار الصفوف والخلايا، واسترداد نص الخلية للتحليل ومعالجة البيانات النهائية.
---

## استخراج الجدول من PDF

يعد استخراج الجداول من ملفات PDF مفيدًا لإعداد التقارير وترحيل البيانات وعمليات سير عمل التحليلات. باستخدام Aspose.PDF لـ Python عبر .NET، يمكنك اكتشاف وقراءة محتوى الجدول من مستندات PDF الموجودة بكفاءة.

يفتح مقتطف الشفرة هذا ملف PDF موجودًا، ويفحص كل صفحة بحثًا عن الجداول، ويستخرج محتوى نص الخلية. يستخدم `TableAbsorber` لاكتشاف الجداول ثم التكرار من خلال الصفوف والخلايا لطباعة النص المستخرج.

1. يقوم بتحميل ملف PDF إلى كائن AP.Document.
1. تصفح الصفحات.
1. يقوم بإنشاء كائن TableAbsorber.
1. قم بالتكرار من خلال الجداول.
1. قم بالتكرار من خلال الصفوف والخلايا.
1. استخراج النص وطباعته من الخلايا.

يقوم هذا المثال بقراءة ملف PDF والعثور على جميع الجداول وطباعة محتويات الخلايا الخاصة بها صفًا تلو الآخر.

```python
import aspose.pdf as ap
from os import path
import sys

def extract(infile: str) -> None:
    """Extract and print all tables from a PDF file."""
    document = ap.Document(infile)
    for page in document.pages:
        absorber = ap.text.TableAbsorber()
        absorber.visit(page)
        for table in absorber.table_list:
            print("Table ----")
            for row in table.row_list:
                print("Row:")
                row_txt = ""
                for cell in row.cell_list:
                    cell_txt = ""
                    text_fragment_collection = cell.text_fragments
                    for fragment in text_fragment_collection:
                        for seg in fragment.segments:
                            cell_txt += seg.text
                    row_txt += " | "
                    row_txt += cell_txt
                print(row_txt)
```

## موضوعات الجدول ذات الصلة

- [العمل مع الجداول في PDF باستخدام Python](/pdf/ar/python-net/working-with-tables/)
- [إضافة جداول إلى PDF باستخدام Python](/pdf/ar/python-net/adding-tables/)
- [دمج جداول PDF مع مصادر البيانات](/pdf/ar/python-net/integrate-table/)
- [إزالة الجداول من ملفات PDF الموجودة](/pdf/ar/python-net/removing-tables/)