---
title: إضافة طوابع الصفحة إلى PDF في Python
linktitle: إضافة طوابع الصفحة
type: docs
weight: 30
url: /ar/python-net/page-stamps-in-the-pdf-file/
description: تعرف على كيفية إضافة طوابع صفحات PDF كتراكبات أو خلفيات في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إضافة طوابع الصفحة إلى PDF باستخدام Python
Abstract: توضح هذه المقالة كيفية إضافة طابع صفحة إلى مستند PDF باستخدام Aspose.PDF لـ Python. يسمح لك ختم الصفحة بتراكب المحتوى أو وضعه تحت الأرض - مثل الشعارات أو العلامات المائية أو التعليقات التوضيحية - على صفحة محددة في PDF. يوضح المثال كيفية فتح PDF موجود، وإنشاء كائن PDFPageStamp من صفحة PDF أخرى، وتكوينه كختم خلفية، وتطبيقه على صفحة معينة. ثم يتم حفظ ملف PDF المختوم كمستند جديد. هذه التقنية مفيدة للعلامة التجارية أو وضع علامة مائية أو التأكيد على المحتوى على مستوى الصفحة في عمليات سير عمل PDF الآلية.
---

يوضح Aspose.PDF لـ Python عبر .NET كيفية تطبيق طابع صفحة (علامة مائية أو تراكب) على صفحة معينة في PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). يمكن أن يكون ختم الصفحة صفحة PDF موجودة تستخدم كخلفية أو طبقة أمامية (انظر [`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/)). هذا مفيد لإضافة الشعارات أو العلامات المائية أو محتوى الصفحة المتكرر الآخر.

1. افتح مستند PDF باستخدام `ap.Document()` (انظر [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. قم بإنشاء `PdfPageStamp` كائن يستخدم صفحة أو ملف PDF لاستخدامه كختم (انظر [`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/)).
1. قم بتعيين خصائص الطابع، على سبيل المثال، `background = True` لوضعه خلف المحتوى.
1. أضف الطابع إلى صفحة معينة باستخدام `document.pages[page_number].add_stamp(page_stamp)` (انظر [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) و [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)).
1. احفظ ملف PDF المعدل إلى ملف الإخراج المحدد باستخدام [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python
import sys
import aspose.pdf as ap
from os import path

def add_page_stamp(input_file_name, page_stamp_name, output_file_name):
    # Open PDF document
    document = ap.Document(input_file_name)

    page_stamp = ap.PdfPageStamp(page_stamp_name, 1)
    page_stamp.background = True

    # Add stamp to particular page
    document.pages[1].add_stamp(page_stamp)

    document.save(output_file_name)
```

## موضوعات الختم ذات الصلة

- [ختم صفحات PDF في بايثون](/pdf/ar/python-net/stamping/)
- [إضافة أرقام الصفحات إلى PDF في Python](/pdf/ar/python-net/add-page-number/)
- [أضف طوابع صور إلى PDF في Python](/pdf/ar/python-net/image-stamps-in-pdf-page/)
- [أضف طوابع نصية إلى PDF في Python](/pdf/ar/python-net/text-stamps-in-the-pdf-file/)