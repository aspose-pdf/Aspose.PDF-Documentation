---
title: استخراج البيانات من الجدول في PDF باستخدام Python
linktitle: استخراج البيانات من الجدول
type: docs
weight: 40
url: /ar/python-net/extract-data-from-table-in-pdf/
description: تعرف على كيفية استخراج بيانات الجدول من ملفات PDF باستخدام Aspose.PDF لـ Python وتصدير النتائج لمزيد من المعالجة.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية استخراج البيانات من الجدول في PDF عبر Python
Abstract: تشرح هذه المقالة كيفية استخراج ومعالجة بيانات الجدول من مستندات PDF باستخدام Aspose.PDF لـ Python. يوضح كيفية مسح كل صفحة باستخدام TableAbsorber، وقراءة الصفوف والخلايا من الجداول المكتشفة، والحد من الاستخراج إلى منطقة مشروحة محددة، وتصدير محتوى PDF إلى تنسيق CSV لاستخدامه في أدوات جداول البيانات والمعالجة النهائية.
---

## استخراج الجداول من PDF برمجيًا

استخدم [ممتص الطاولة](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) لاكتشاف الجداول في كل صفحة من صفحات [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). بعد زيارة الصفحة، قم بالتكرار `table_list`، ثم انتقل عبر كل صف وخلية لإعادة بناء محتوى الجدول بتنسيق نصي قابل للقراءة.

1. افتح ملف PDF كملف `Document`.
1. قم بالتكرار من خلال الصفحات في `document.pages`.
1. قم بإنشاء `TableAbsorber` لكل صفحة ومكالمة `visit(page)`.
1. قم بالتمرير عبر الجداول والصفوف والخلايا المكتشفة.
1. اقرأ أجزاء النص من كل خلية وقم بتجميع إخراج الصف المستخرج.

```python
import aspose.pdf as apdf
from os import path

path_infile = path.join(self.dataDir, infile)

# Open PDF document
document = apdf.Document(path_infile)

# Iterate through each page in the document
for page in document.pages:
    absorber = apdf.text.TableAbsorber()
    absorber.visit(page)

    for table in absorber.table_list:
        print("Table")
        for row in table.row_list:
            row_text = []
            for cell in row.cell_list:
                cell_text = []
                for fragment in cell.text_fragments:
                    cell_text.append("".join(seg.text for seg in fragment.segments))
                row_text.append("|".join(cell_text))
            print("|".join(row_text))
```

## استخراج الجدول في منطقة محددة من صفحة PDF

إذا كنت بحاجة إلى استخراج الجداول الموجودة داخل منطقة محددة فقط، فقم بدمجها [ممتص الطاولة](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) مع [تعليق توضيحي على شكل مربع](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation/). في هذا المثال، يتم استخدام مستطيل التعليق التوضيحي كحدود، وتتم معالجة الجداول الموجودة بالكامل داخل تلك المنطقة فقط.

1. افتح ملف PDF كملف `Document`.
1. حدد الصفحة المستهدفة.
1. ابحث عن التعليق التوضيحي المربع الذي يشير إلى منطقة الاهتمام.
1. قم بإنشاء `TableAbsorber` وقم بزيارة الصفحة.
1. قارن كل مستطيل جدول تم اكتشافه بمستطيل التعليق التوضيحي.
1. قم بمعالجة الجداول التي تقع بالكامل داخل المنطقة المحددة فقط.

```python
import aspose.pdf as apdf
from os import path

# The path to the documents directory
path_infile = path.join(self.dataDir, infile)

# Open PDF document
document = apdf.Document(path_infile)

# Get the first page (index starts from 1 in Aspose.PDF)
page = document.pages[1]

# Find the first square annotation
square_annotation = next(
    (
        ann
        for ann in page.annotations
        if ann.annotation_type == apdf.annotations.AnnotationType.SQUARE
    ),
    None,
)

if square_annotation is None:
    print("No square annotation found.")
    return

# Initialize the TableAbsorber
absorber = apdf.text.TableAbsorber()
absorber.visit(page)

# Iterate through tables on the page
for table in absorber.table_list:
    table_rect = table.rectangle
    annotation_rect = square_annotation.rect

    # Check if the table is inside the annotation region
    is_in_region = (
        annotation_rect.llx < table_rect.llx
        and annotation_rect.lly < table_rect.lly
        and annotation_rect.urx > table_rect.urx
        and annotation_rect.ury > table_rect.ury
    )

    if is_in_region:
        for row in table.row_list:
            row_text = []
            for cell in row.cell_list:
                cell_text = []
                for fragment in cell.text_fragments:
                    cell_text.append("".join(seg.text for seg in fragment.segments))
                row_text.append("|".join(cell_text))
            print("|".join(row_text))
```

## تصدير بيانات الجدول من PDF إلى CSV

عندما تحتاج إلى البيانات المستخرجة بتنسيق مناسب لجدول البيانات، احفظ ملف PDF باستخدام [خيارات الحفظ في Excel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) وقم بتعيين تنسيق الإخراج إلى CSV. يمكن فتح الملف الناتج في Excel أو Google Sheets أو استيراده إلى عمليات سير عمل التحليلات.

1. افتح ملف PDF المصدر كملف [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. قم بإنشاء `ExcelSaveOptions` مثال.
1. مجموعة `excel_save.format` إلى `ExcelSaveOptions.ExcelFormat.CSV`.
1. احفظ المستند إلى مسار CSV الهدف.

```python
import aspose.pdf as apdf
from os import path

path_infile = path.join(self.dataDir, infile)
path_outfile = path.join(self.dataDir, outfile)

document = apdf.Document(path_infile)
excel_save = apdf.ExcelSaveOptions()
excel_save.format = apdf.ExcelSaveOptions.ExcelFormat.CSV
document.save(path_outfile, excel_save)
```
