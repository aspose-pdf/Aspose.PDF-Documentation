---
title: إنشاء مستند PDF من N-Up
linktitle: إنشاء مستند PDF من N-Up
type: docs
weight: 10
url: /ar/python-net/create-n-up-pdf-document/
description: تعرف على كيفية إنشاء مستند N-Up PDF أثناء معالجة الأخطاء المحتملة بأمان باستخدام Aspose.PDF لـ Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بإنشاء تخطيط N-Up PDF في بايثون
Abstract: تعرف على كيفية إنشاء تخطيط N-Up PDF باستخدام Aspose.PDF لبيثون. يوضح هذا المثال كيفية دمج صفحات متعددة من مستند PDF في صفحة واحدة باستخدام طريقة «make_n_up» أو «try_make_n_up» لفئة PDFfileEditor.
---

يضع تخطيط N-Up صفحات متعددة من مستند PDF على صفحة واحدة بتنسيق شبكي. يُستخدم هذا التخطيط غالبًا لطباعة العروض التقديمية أو النشرات أو التقارير حيث يمكن عرض صفحات متعددة في وقت واحد.

باستخدام Aspose.PDF لـ Python، يمكن للمطورين إنشاء مستند N-Up بسرعة عن طريق تحديد عدد الصفوف والأعمدة التي تحدد عدد الصفحات الأصلية التي تظهر في كل صفحة إخراج.

في مقتطف الشفرة هذا، طريقة «make_n_up» الخاصة بـ [محرر ملفات PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) يقوم الفصل بترتيب صفحات ملف PDF المُدخل في شبكة 2 × 2، مما يعني ظهور أربع صفحات أصلية على صفحة واحدة في مستند الإخراج.

في المثال الموضح، يستخدم التخطيط صفين وعمودين، مما ينتج أربع صفحات لكل ورقة:

1. افتح ملف PDF المصدر.
1. قم بإنشاء مثيل محرر ملفات PDF.
1. حدد عدد الصفوف والأعمدة لتخطيط N-Up.
1. قم بإنشاء ملف PDF جديد بصفحات مدمجة.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Create N-Up PDF Document
def create_nup_pdf_document(infile, outfile):
    # Create NUpMaker object
    nup_maker = pdf_facades.PdfFileEditor()
    # Make N-Up layout from input PDF file and save to output PDF file
    nup_maker.make_n_up(
        FileIO(infile), FileIO(outfile, "w"), 2, 2
    )  # 2 rows and 2 columns for N-Up layout
```

Aspose.PDF لبيثون عبر .NET يسمح لك بإنشاء تخطيطات N-Up مع فئة PDFfileEditor. تعمل طريقة 'try_make_n_up' بشكل مشابه لـ make_n_up، ولكن بدلاً من رفع الاستثناء عند فشل العملية، فإنها تُرجع قيمة منطقية تشير إلى ما إذا كانت العملية قد نجحت أم لا.

يقوم تخطيط N-Up بترتيب صفحات PDF متعددة على صفحة واحدة باستخدام شبكة محددة بالصفوف والأعمدة.

توفر طريقة 'try_make_n_up' طريقة أكثر أمانًا لتنفيذ هذه العملية للأسباب التالية:

- تقوم بإرجاع True إذا تم إنشاء التخطيط بنجاح
- تقوم بإرجاع False إذا فشلت العملية
- لا يقطع تنفيذ البرنامج مع استثناءات

في المثال أدناه، يتم ترتيب المستند باستخدام شبكة 2 × 2، والتي تضع أربع صفحات أصلية في كل صفحة إخراج.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Create N-Up PDF Document
def try_create_nup_pdf_document(infile, outfile):
    # Create NUpMaker object
    nup_maker = pdf_facades.PdfFileEditor()
    # Make N-Up layout from input PDF file and save to output PDF file
    if not nup_maker.try_make_n_up(FileIO(infile), FileIO(outfile, "w"), 2, 2):
        print("Failed to create N-Up PDF document.")
```
