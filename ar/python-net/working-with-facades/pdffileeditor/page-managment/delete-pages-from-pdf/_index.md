---
title: حذف الصفحات من PDF
linktitle: حذف الصفحات من PDF
type: docs
weight: 20
url: /ar/python-net/delete-pages-from-pdf/
description: قم بإزالة الصفحات المحددة من مستند PDF باستخدام Aspose.PDF لـ Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: حذف صفحات محددة من وثيقة PDF في Python
Abstract: تعرف على كيفية إزالة الصفحات المحددة من مستند PDF باستخدام Aspose.PDF لـ Python. يوضح هذا المثال كيفية حذف صفحات معينة من ملف PDF موجود برمجيًا، وإنشاء مستند جديد بدون الصفحات التي تمت إزالتها.
---

تحتوي مستندات PDF أحيانًا على صفحات غير ضرورية أو حساسة تحتاج إلى إزالتها. باستخدام Aspose.PDF لـ Python، يمكن للمطورين حذف صفحات معينة برمجيًا من PDF دون تحرير الملف يدويًا.

يوضح مثالنا كيفية استخدام طريقة الحذف الخاصة بـ [محرر ملفات PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) فئة لإزالة الصفحات من مستند PDF. من خلال تحديد أرقام الصفحات لحذفها، يمكنك إنشاء PDF جديد يستبعد الصفحات غير المرغوب فيها. هذه الوظيفة مفيدة لتنظيف التقارير أو إزالة المعلومات السرية أو إعداد مقتطفات المستندات المخصصة.

1. قم بإنشاء كائن محرر ملفات PDF.
1. حدد الصفحات التي تريد حذفها.
1. احذف الصفحات.

```python

    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    import sys
    from os import path

    sys.path.append(path.join(path.dirname(__file__), ".."))
    from config import set_license, initialize_data_dir


    # Delete Pages from PDF
    def delete_pages_from_pdf(infile, outfile):
        # Create a PdfFileEditor object
        pdf_editor = pdf_facades.PdfFileEditor()

        # Define the page numbers to be deleted (1-based index)
        pages_to_delete = [2, 4]

        # Delete the specified pages from the PDF document
        pdf_editor.delete(infile, pages_to_delete, outfile)
```