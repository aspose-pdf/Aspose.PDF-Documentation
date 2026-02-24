---
title: إضافة طوابع الصفحات إلى PDF باستخدام بايثون
linktitle: إضافة طوابع الصفحات
type: docs
weight: 30
url: /ar/python-net/page-stamps-in-the-pdf-file/
description: Aspose.PDF for Python عبر .NET يتيح لك إضافة طابع صفحة إلى ملف PDF الخاص بك.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إضافة طوابع الصفحات إلى PDF باستخدام بايثون
Abstract: تشرح هذه المقالة كيفية إضافة طابع صفحة إلى مستند PDF باستخدام Aspose.PDF للبايثون. يتيح لك طابع الصفحة وضع محتوى فوق أو تحت—مثل الشعارات أو العلامات المائية أو التعليقات التوضيحية—على صفحة محددة في PDF. يوضح المثال كيفية فتح ملف PDF موجود، إنشاء كائن PdfPageStamp من صفحة PDF أخرى، تكوينه كطابع خلفية، وتطبيقه على صفحة معينة. يتم حفظ PDF المطبوع بعد ذلك كوثيقة جديدة. هذه التقنية مفيدة للعلامة التجارية أو إضافة علامات مائية أو لإبراز محتوى على مستوى الصفحة في تدفقات عمل PDF الآلية.
---

يوضح Aspose.PDF للبايثون عبر .NET كيفية تطبيق طابع صفحة (علامة مائية أو تغطية) على صفحة محددة في PDF [المستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). يمكن أن يكون طابع الصفحة صفحة PDF موجودة تُستخدم كطبقة خلفية أو أمامية (انظر [PdfPageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/)). هذا مفيد لإضافة الشعارات أو العلامات المائية أو أي محتوى صفحة متكرر آخر.

1. افتح مستند PDF باستخدام `ap.Document()` (انظر [`المستند`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. أنشئ كائن `PdfPageStamp` باستخدام صفحة PDF أو الملف لاستخدامه كطابع (انظر [`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/)).
1. عيّن خصائص الطابع، مثل `background = True` لوضعه خلف المحتوى.
1. أضف الطابع إلى صفحة محددة باستخدام `document.pages[page_number].add_stamp(page_stamp)` (انظر [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) و [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)).
1. احفظ ملف PDF المعدل إلى ملف الإخراج المحدد باستخدام [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_page_stamp(input_file_name, page_stamp_name, output_file_name):
    # Open PDF document
    document = ap.Document(input_file_name)

    page_stamp = ap.PdfPageStamp(page_stamp_name, 1)
    page_stamp.background = True

    # Add stamp to particular page
    document.pages[1].add_stamp(page_stamp)

    document.save(output_file_name)
```

