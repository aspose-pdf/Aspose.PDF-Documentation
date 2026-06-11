---
title: معالجة الجداول في مستندات PDF الحالية
linktitle: معالجة الجداول
type: docs
weight: 40
url: /ar/python-net/manipulating-tables/
description: تعرف على كيفية فحص وتعديل الجداول في مستندات PDF الحالية باستخدام Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: فحص وتعديل جداول PDF الموجودة باستخدام Python
Abstract: توضح هذه المقالة كيفية التعامل مع الجداول الموجودة بالفعل في مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. تعرف على كيفية تحديد موقع الجداول باستخدام TableAbsorber، والوصول إلى صفوف وخلايا محددة، وتحديث محتوى نص الجدول، وحفظ ملف PDF المعدل في Python.
---

## معالجة الجداول في PDF الحالي

Aspose.PDF لـ Python عبر .NET يتيح لك تحديث الجداول الموجودة بالفعل في مستند PDF. يمكنك استخدام [ممتص الطاولة](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) فئة للبحث عن الجداول على الصفحة، والوصول إلى الصفوف والخلايا، وتغيير محتوى النص، وحفظ الملف المحدث.

استخدم هذه الصفحة عندما تحتاج إلى تحديث محتوى الجدول الموجود في ملفات PDF دون إعادة إنشاء تخطيط المستند بالكامل.

## ابحث عن النص واستبدله في خلايا جدول PDF

يعثر هذا المثال على الجدول الأول في الصفحة 1، ويصل إلى الخلية الأولى، ويستبدل نصها، ويحفظ ملف PDF الناتج.

1. افتح ملف PDF المُدخل.
1. قم بإنشاء TableAbsorber وقم بزيارة الصفحة 1.
1. تأكد من اكتشاف جدول واحد على الأقل.
1. قم بالوصول إلى الخلية الأولى في الصف الأول من الجدول الأول.
1. تأكد من أن الخلية تحتوي على أجزاء نصية، ثم قم بتحديث الجزء الأول.
1. احفظ ملف PDF المعدل.

```python
import aspose.pdf as ap

def replace_cell_text(infile: str, outfile: str) -> None:
    """Replace text in the first cell of the first detected table."""
    # Open PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    if len(absorber.table_list) == 0:
        raise ValueError("No tables were found on page 1.")

    first_cell = absorber.table_list[0].row_list[0].cell_list[0]
    if len(first_cell.text_fragments) == 0:
        raise ValueError("The target cell has no text fragments.")

    # Change text of the first text fragment in the cell
    first_cell.text_fragments[0].text = "New Value"

    # Save PDF document
    document.save(outfile)
```

## استبدال جدول موجود بجدول جديد

يمكنك أيضًا استبدال الجدول المكتشف بجدول تم إنشاؤه حديثًا. هذا النهج مفيد عندما يجب تغيير كل من البنية والمحتوى.

يفتح الكود أدناه ملف PDF، ويجد الجدول الأول في الصفحة 1، ويقوم بإنشاء جدول بديل، ويستبدل الجدول القديم بالجدول الجديد، ويحفظ النتيجة.

```python
import aspose.pdf as ap

def replace_table(infile: str, outfile: str) -> None:
    """Replace an entire table with a new one."""
    # Open PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    if len(absorber.table_list) == 0:
        raise ValueError("No tables were found on page 1.")

    # Get first table on the page
    old_table = absorber.table_list[0]

    # Create new table
    new_table = ap.Table()
    new_table.column_widths = "100 100 100"
    new_table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 1.0)

    row = new_table.rows.add()
    row.cells.add("Col 1")
    row.cells.add("Col 2")
    row.cells.add("Col 3")
    row = new_table.rows.add()
    row.cells.add("Col 12")
    row.cells.add("Col 22")
    row.cells.add("Col 32")

    # Replace the old table with the new one
    absorber.replace(document.pages[1], old_table, new_table)

    # Save PDF document
    document.save(outfile)
```

## موضوعات الجدول ذات الصلة

- [العمل مع الجداول في PDF باستخدام Python](/pdf/ar/python-net/working-with-tables/)
- [إضافة جداول إلى PDF باستخدام Python](/pdf/ar/python-net/adding-tables/)
- [استخراج الجداول من مستندات PDF](/pdf/ar/python-net/extracting-table/)
- [إزالة الجداول من ملفات PDF الموجودة](/pdf/ar/python-net/removing-tables/)
