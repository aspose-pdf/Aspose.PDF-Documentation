---
title: استخراج البيانات من جدول في PDF باستخدام بايثون
linktitle: استخراج البيانات من جدول
type: docs
weight: 40
url: /ar/python-net/extract-data-from-table-in-pdf/
description: تعلم كيفية استخراج الجداول من PDF باستخدام Aspose.PDF للبايثون
lastmod: "2025-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية استخراج البيانات من جدول في PDF عبر بايثون
Abstract: يوفر هذا المقال دليلًا شاملاً حول استخراج الجداول ومعالجتها برمجيًا من مستندات PDF باستخدام Aspose.PDF، مكتبة بايثون. يقدم المقال برنامجًا بلغة بايثون يفتح مستند PDF، يتنقل عبر كل صفحة، ويستخرج الجداول باستخدام الفئة `TableAbsorber`. ثم تُنظم بيانات الجدول المستخرجة وتُطبع لمزيد من التحليل. يصف هذا القسم كيفية استخراج الجداول من مناطق محددة في PDF، مثل المناطق المحاطة بتعليقات مربعة. يحدد البرنامج هذه التعليقات، يهيئ الفئة `TableAbsorber`، ويتحقق مما إذا كانت الجداول تقع ضمن المناطق المشروحة قبل استخراج وطباعة البيانات. يوضح القسم النهائي طريقة تحويل البيانات الجدولية المستخرجة من PDF إلى تنسيق ملف CSV.
---

## استخراج الجداول من PDF برمجيًا

يقوم هذا الكود باستخراج جداول PDF وتحويل البيانات الجدولية من ملف PDF إلى صيغة قابلة للقراءة ومهيكلة لمزيد من المعالجة أو التحليل.

1. فتح مستند PDF
1. التنقل عبر صفحات PDF
1. استخراج بيانات الجدول

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

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
                        cell_text.append(
                            "".join(seg.text for seg in fragment.segments)
                        )
                    row_text.append("|".join(cell_text))
                print("|".join(row_text))
```

## استخراج جدول في منطقة محددة من صفحة PDF

يستخرج مقطع الشيفرة هذا البيانات الجدولية من مناطق محددة في PDF، مثل البيانات داخل مربع مميز أو تعليق محدد.

1. فتح مستند PDF
1. الحصول على الصفحة الأولى
1. العثور على أول تعليق مربع
1. تهيئة الـ TableAbsorber
1. التنقل عبر الجداول في الصفحة
1. التحقق مما إذا كان الجدول داخل منطقة التعليق

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

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
                        cell_text.append(
                            "".join(seg.text for seg in fragment.segments)
                        )
                    row_text.append("|".join(cell_text))
                print("|".join(row_text))
```

## استخراج بيانات الجدول من PDF وتخزينها في ملف إكسل

يستخرج مقطع الشيفرة التالي البيانات الجدولية من PDF ويصدّرها كملف CSV لمزيد من التحليل أو المعالجة في تطبيقات الجداول مثل Excel أو Google Sheets.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    excel_save = apdf.ExcelSaveOptions()
    excel_save.format = apdf.ExcelSaveOptions.ExcelFormat.CSV
    document.save(path_outfile, excel_save)
```

