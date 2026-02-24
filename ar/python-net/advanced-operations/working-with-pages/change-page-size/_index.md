---
title: تغيير حجم الصفحة باستخدام بايثون
linktitle: تغيير حجم الصفحة
type: docs
weight: 40
url: /ar/python-net/change-page-size/
description: تغيير حجم الصفحة من مستند PDF الخاص بك باستخدام Aspose.PDF للبايثون عبر مكتبة .NET.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تغيير حجم الصفحة باستخدام بايثون
Abstract: تُظهر هذه المقالة كيفية قراءة وتعديل أبعاد صفحات PDF باستخدام Aspose.PDF. يستخرج مثال الحصول على حجم الصفحة عرض وارتفاع صفحة PDF محددة، مما يتيح للمستخدمين فحص تخطيط الصفحة، والتحقق من التنسيق، أو تحليل هيكل المستند. يوضح مثال تعيين حجم الصفحة كيفية تغيير أبعاد الصفحة—مثل تحويل الصفحة الأولى إلى حجم A4—مع عرض خصائص الصناديق (CropBox، TrimBox، ArtBox، BleedBox، MediaBox) قبل وبعد التعديل.
---

تتيح Aspose.PDF للبايثون عبر .NET تغيير حجم صفحة PDF باستخدام أسطر بسيطة من الشيفرة. يوضح هذا الموضوع كيفية تحديث أبعاد الصفحة باستخدام واجهة برمجة التطبيقات [`المستند`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) و[`الصفحة`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

{{% alert color="primary" %}}

يرجى ملاحظة أن خصائص الارتفاع والعرض تستخدم النقاط كوحدة أساسية، حيث 1 بوصة = 72 نقطة و 1 سم = 1/2.54 بوصة = 0.3937 بوصة = 28.3 نقطة.

{{% /alert %}}

### تعيين حجم الصفحة لصفحة PDF إلى A4

يُحدّث المثال حجم الصفحة الأولى في مستند PDF إلى أبعاد A4 القياسية. كما يطبع أبعاد صناديق الصفحة (CropBox، TrimBox، ArtBox، BleedBox، MediaBox) قبل وبعد تغيير الحجم لتتمكن من التحقق من التغييرات.

المقتطف التالي من الشيفرة يُظهر كيفية تغيير أبعاد صفحة PDF إلى حجم A4:

1. الوصول إلى الـ[`الصفحة`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) الأولى من الـ[`المستند`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. عرض أحجام صناديق الصفحة قبل التعديل (CropBox، TrimBox، ArtBox، BleedBox، MediaBox).
1. تطبيق أبعاد A4 (597.6 × 842.4 نقطة) باستخدام واجهة برمجة تطبيقات الصفحة.
1. عرض أحجام صناديق الصفحة المحدثة.
1. حفظ الـ[`المستند`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) المعدل إلى المسار المحدد للإخراج.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def set_page_size(input_file_name, output_file_name):
    """
    Set the size of the first page in the PDF document to A4 and save the updated document.

    Parameters:
    - input_file_name (str): Path to the input PDF file.
    - output_file_name (str): Path to save the output PDF file.
    """
    # Open the PDF document using the Document class
    document = ap.Document(input_file_name)
    # Get particular page (Page API)
    page = document.pages[1]

    # Set the page size as A4 (8.3 x 11.7 in). In Aspose.PDF 1 inch = 72 points.
    # A4 dimensions in points are (597.6, 842.4) for portrait orientation
    print("Before set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

    # Use the Page API to set page size
    page.set_page_size(597.6, 842.4)
    print("After set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

    # Save the updated document
    document.save(output_file_name)
```

## الحصول على حجم صفحة PDF

يقرأ هذا المقتطف ملف PDF ويستخرج الأبعاد (العرض والارتفاع) للصفحة الأولى. يستخدم واجهة برمجة تطبيقات [`الصفحة`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) لاستخراج المستطيل المحيط بالصفحة [`المستطيل`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) ويطبع حجمه إلى وحدة التحكم. يكون ذلك مفيدًا لفحص تخطيط الصفحة، والتحقق من الصيغ، أو إعداد المستندات لمزيد من المعالجة.

1. تحميل ملف PDF كـ[`المستند`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. الوصول إلى الـ[`الصفحة`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) الأولى.
1. استرجاع المستطيل المحيط بالصفحة باستخدام `get_page_rect()`.
1. استخراج قيم العرض والارتفاع.
1. طباعة أبعاد الصفحة.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_size(input_file_name, output_file_name):
    # Open document (Document API)
    document = ap.Document(input_file_name)

    # Get particular page (Page API)
    page = document.pages[1]
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```

### الحصول على حجم صفحة PDF قبل وبعد التدوير

استرجاع أبعاد صفحة PDF قبل وبعد تطبيق تدوير 90°. يوضح ذلك كيف يؤثر التدوير على العرض والارتفاع وكيفية استخدام `get_page_rect()` مع أو بدون مراعاة التدوير.

1. فتح ملف PDF كـ[`المستند`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. الوصول إلى الـ[`الصفحة`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) الأولى.
1. تطبيق تدوير 90° باستخدام `page.rotate = ap.Rotation.ON90` (انظر تعداد [`التدوير`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rotation/)).
1. استرجاع مستطيل الصفحة بدون تدوير باستخدام `get_page_rect(False)` وطباعة عرضه وارتفاعه.
1. استرجاع مستطيل الصفحة مع مراعاة التدوير باستخدام `get_page_rect(True)` وطباعة عرضه وارتفاعه.
1. مقارنة كيف تتغير الأبعاد بسبب التدوير.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_size_rotation(input_file_name, output_file_name):
    # Open document (Document API)
    document = ap.Document(input_file_name)
    # Get particular page (Page API)
    page = document.pages[1]
    # Apply rotation using Rotation enum
    page.rotate = ap.Rotation.ON90
    rectangle = page.get_page_rect(False)
    print(f"{rectangle.width} : {rectangle.height}")
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```
