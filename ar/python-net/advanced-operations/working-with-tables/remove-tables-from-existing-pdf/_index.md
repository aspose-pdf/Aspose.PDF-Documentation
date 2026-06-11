---
title: إزالة الجداول من مستندات PDF الموجودة
linktitle: إزالة الجداول
description: تعرف على كيفية إزالة جدول واحد أو أكثر من مستندات PDF الموجودة في Python.
lastmod: "2026-06-11"
type: docs
weight: 50
url: /ar/python-net/removing-tables/
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: احذف جدولًا واحدًا أو عدة جداول من ملفات PDF باستخدام Python
Abstract: توضح هذه المقالة كيفية إزالة الجداول من مستندات PDF الحالية باستخدام Aspose.PDF لـ Python عبر .NET. يقدم «TableAbsorber» لتحديد موقع الجداول ويوضح كيفية حذف جدول واحد أو إزالة جميع الجداول المكتشفة من الصفحة.
---

## إزالة الجدول من وثيقة PDF

Aspose.PDF لبيثون يتيح لك إزالة جدول من PDF. يفتح ملف PDF موجودًا، ويكتشف الجدول الأول في الصفحة الأولى باستخدام `TableAbsorber`، يحذف هذا الجدول باستخدام `remove()`، ويحفظ ملف PDF المحدث إلى ملف جديد.

استخدم هذه الصفحة عندما تحتاج إلى تنظيف ملفات PDF ذات الجداول الثقيلة أو إزالة المحتوى الجدولي القديم أو تبسيط المستندات قبل إعادة التوزيع.

```python
import aspose.pdf as ap
from os import path
import sys

def remove_one_table(infile: str, outfile: str) -> None:
    # Load existing PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(document.pages[1])
    # Get first table on the page
    table = absorber.table_list[0]
    # Remove the table
    absorber.remove(table)
    # Save PDF
    document.save(outfile)
```

## قم بإزالة جميع الجداول من وثيقة PDF

مع مكتبتنا، يمكنك إزالة جميع الجداول من صفحة معينة في PDF. يفتح الكود ملف PDF موجودًا، ويكتشف جميع الجداول في الصفحة الثانية باستخدام TableAbsorber، ويكرر الجداول المكتشفة، ويزيل كل منها، ثم يحفظ ملف PDF المعدل في ملف جديد. يكون مفيدًا عندما تحتاج إلى إزالة الجداول بشكل مجمّع من الصفحة مع ترك بقية محتوى PDF كما هو.

```python
import aspose.pdf as ap
from os import path
import sys

def remove_all_tables(infile: str, outfile: str) -> None:
    # Load existing PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(document.pages[1])
    #  Loop through the copy of collection and removing tables
    tables = list(absorber.table_list)
    for table in tables:
        absorber.remove(table)

    # Save document
    document.save(outfile)
```

## موضوعات الجدول ذات الصلة

- [العمل مع الجداول في PDF باستخدام Python](/pdf/ar/python-net/working-with-tables/)
- [إضافة جداول إلى PDF باستخدام Python](/pdf/ar/python-net/adding-tables/)
- [استخراج الجداول من مستندات PDF](/pdf/ar/python-net/extracting-table/)
- [معالجة الجداول في ملفات PDF الموجودة](/pdf/ar/python-net/manipulating-tables/)