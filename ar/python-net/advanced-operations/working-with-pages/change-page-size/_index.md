---
title: تغيير حجم صفحة PDF في بايثون
linktitle: تغيير حجم الصفحة
type: docs
weight: 40
url: /ar/python-net/change-page-size/
description: تعرف على كيفية قراءة أبعاد صفحة PDF وتغييرها في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تغيير حجم الصفحة باستخدام Python
Abstract: توضح هذه المقالة كيفية قراءة وتعديل أبعاد صفحة PDF باستخدام Aspose.PDF. يقوم مثال Get Page Size باسترداد عرض وارتفاع صفحة PDF محددة، مما يتيح للمستخدمين فحص تخطيط الصفحة أو التحقق من التنسيق أو تحليل بنية المستند. يوضح مثال تعيين حجم الصفحة كيفية تغيير أبعاد الصفحة - مثل تحويل الصفحة الأولى إلى حجم A4 - مع عرض خصائص المربع أيضًا (CropBox، TrimBox، ArtBox، BleedBox، MediaBox) قبل التعديل وبعده.
---

يتيح لك Aspose.PDF لـ Python عبر .NET تغيير حجم صفحة PDF بخطوط بسيطة من التعليمات البرمجية. يوضح هذا الموضوع كيفية تحديث أبعاد الصفحة باستخدام [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) و [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) واجهات برمجة التطبيقات.

استخدم هذا الدليل عندما تحتاج إلى تغيير حجم صفحات PDF الموجودة أو تطبيع أبعاد المستند أو فحص إعدادات مربع الصفحة في Python.

{{% alert color="primary" %}}

يرجى ملاحظة أن خصائص الارتفاع والعرض تستخدم النقاط كوحدة أساسية، حيث 1 بوصة = 72 نقطة و 1 سم = 1/2.54 بوصة = 0.3937 بوصة = 28.3 نقطة.

{{% /alert %}}

## قم بتعيين حجم صفحة PDF إلى A4

يقوم المثال بتحديث حجم الصفحة الأولى في وثيقة PDF إلى أبعاد A4 القياسية. يقوم أيضًا بطباعة أبعاد مربع الصفحة (CropBox و TrimBox و ArtBox و BleedBox و MediaBox) قبل تغيير الحجم وبعده حتى تتمكن من التحقق من التغييرات.

يوضح مقتطف الشفرة التالي كيفية تغيير أبعاد صفحة PDF إلى حجم A4:

1. الوصول إلى الأول [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) من ال [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. اعرض أحجام مربعات الصفحة قبل التعديل (كروب بوكس، تريمبوكس، أرتبوكس، بليدبوكس، ميديابوكس).
1. قم بتطبيق أبعاد A4 (597.6 × 842.4 نقطة) باستخدام واجهة برمجة التطبيقات للصفحة.
1. اعرض أحجام مربعات الصفحات المحدثة.
1. احفظ التعديل [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) إلى مسار الإخراج المحدد.

```python
import aspose.pdf as ap

def set_page_size(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    # Get particular page
    page = document.pages[1]

    # Set the page size as A4 (8.3 x 11.7 in) and in Aspose.Pdf, 1 inch = 72 points
    # So A4 dimensions in points will be (597.6, 842.4) for portrait orientation
    print("Before set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

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

## احصل على حجم صفحة PDF

يقرأ هذا المقتطف ملف PDF ويسترجع أبعاد (العرض والارتفاع) للصفحة الأولى. وهي تستخدم [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) API لاستخراج حدود الصفحة [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) ويطبع حجمه على وحدة التحكم. هذا مفيد لفحص تخطيط الصفحة أو التحقق من التنسيقات أو إعداد المستندات لمزيد من المعالجة.

1. قم بتحميل ملف PDF كملف [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. الوصول إلى الأول [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. استرجع المستطيل المحيط بالصفحة باستخدام `get_page_rect()`.
1. استخرج قيم العرض والارتفاع.
1. اطبع أبعاد الصفحة.

```python
import aspose.pdf as ap

def get_page_size(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    # Get particular page
    page = document.pages[1]
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```

### احصل على حجم صفحة PDF قبل التدوير وبعده

استرجع أبعاد صفحة PDF قبل وبعد تطبيق دوران 90 درجة. يوضح هذا كيف يؤثر الدوران على العرض والارتفاع وكيفية الاستخدام. `get_page_rect()` مع أو بدون النظر في التناوب.

1. افتح ملف PDF كملف [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. الوصول إلى الأول [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. قم بتطبيق دوران 90 درجة باستخدام `page.rotate = ap.Rotation.ON90` (راجع [`Rotation`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rotation/) التعداد).
1. استرجع مستطيل الصفحة بدون تدوير باستخدام `get_page_rect(False)` وقم بطباعة عرضها وارتفاعها.
1. استرجع مستطيل الصفحة مع مراعاة التدوير باستخدام `get_page_rect(True)` وقم بطباعة عرضها وارتفاعها.
1. قارن كيف تتغير الأبعاد بسبب الدوران.

```python
import aspose.pdf as ap

def get_page_size_rotation(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    # Get particular page
    page = document.pages[1]
    page.rotate = ap.Rotation.ON90
    rectangle = page.get_page_rect(False)
    print(f"{rectangle.width} : {rectangle.height}")
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```

## موضوعات الصفحة ذات الصلة

- [العمل مع صفحات PDF في بايثون](/pdf/ar/python-net/working-with-pages/)
- [قص صفحات PDF في بايثون](/pdf/ar/python-net/crop-pages/)
- [الحصول على خصائص صفحة PDF وتعيينها في Python](/pdf/ar/python-net/get-and-set-page-properties/)
- [تدوير صفحات PDF في بايثون](/pdf/ar/python-net/rotate-pages/)