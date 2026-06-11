---
title: إنشاء كتيب PDF
linktitle: إنشاء كتيب PDF
type: docs
weight: 20
url: /ar/python-net/create-pdf-booklet/
description: قم بإنشاء ملف PDF بنمط كتيب من مستند موجود باستخدام Aspose.PDF لـ Python
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بإنشاء كتيب PDF من ملف PDF موجود باستخدام Python
Abstract: تعرف على كيفية إنشاء ملف PDF بنمط كتيب من مستند موجود باستخدام Aspose.PDF لـ Python. يوضح هذا المثال كيفية استخدام فئة PDFfileEditor لإعادة ترتيب الصفحات بحيث يمكن طباعتها وطيها ككتيب. تقوم الطريقة تلقائيًا بترتيب الصفحات لإنتاج تخطيط كتيب مناسب.
---

يعد إنشاء مستندات بنمط الكتيب مطلبًا شائعًا عند إعداد ملفات PDF للطباعة. في تخطيط الكتيب، يتم إعادة ترتيب الصفحات بحيث تظهر بالترتيب الصحيح عند طباعتها وطيها.

باستخدام Aspose.PDF لـ Python، يمكن للمطورين بسهولة تحويل ملف PDF قياسي إلى كتيب باستخدام [محرر ملفات PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) فئة. تقوم طريقة «make_booklet» تلقائيًا بإعادة تنظيم صفحات مستند الإدخال وإنشاء ملف PDF جديد محسّن لطباعة الكتيب.

1. افتح مستند PDF موجود.
1. قم بإنشاء مثيل محرر ملفات PDF.
1. استخدم طريقة make_booklet لإعادة تنظيم الصفحات.
1. احفظ الإخراج كملف PDF جاهز للكتيب.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Create PDF Booklet
def create_pdf_booklet(infile, outfile):
    # Create BookletMaker object
    booklet_maker = pdf_facades.PdfFileEditor()
    # Make booklet from input PDF file and save to output PDF file
    booklet_maker.make_booklet(FileIO(infile), FileIO(outfile, "w"))
```

يوضح مقتطف الشفرة هذا كيفية استخدام طريقة «try_make_booklet» الخاصة بـ [محرر ملفات PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) فئة لإعادة ترتيب الصفحات لطباعة الكتيب دون طرح استثناءات في حالة فشل العملية.

يقوم تخطيط الكتيب بإعادة ترتيب الصفحات بحيث يتم قراءة المستند بالترتيب الصحيح عند طباعته وطيه. تضمن أتمتة هذه العملية نتائج متسقة وتزيل الحاجة إلى إعادة ترتيب الصفحات يدويًا.

تعمل طريقة «try_make_booklet» بشكل مشابه لـ «make_booklet»، ولكن مع اختلاف مهم:

- يطرح 'make_booklet' استثناءً في حالة فشل العملية.
- يُرجع «try_make_booklet» الخطأ أو الخطأ، مما يسمح للمطورين بإدارة الأخطاء بأمان أكبر.

1. افتح مستند PDF موجود.
1. قم بإنشاء مثيل محرر ملفات PDF.
1. حاول إنشاء الكتيب.
1. تعامل مع النتيجة.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def try_create_pdf_booklet(infile, outfile):
    # Create BookletMaker object
    booklet_maker = pdf_facades.PdfFileEditor()
    # Make booklet from input PDF file and save to output PDF file
    # The try_make_booklet method is like the make_booklet method,
    # except the try_make_booklet method does not throw an exception if the operation fails.
    if not booklet_maker.try_make_booklet(FileIO(infile), FileIO(outfile, "w")):
        print("Failed to create booklet.")
```
