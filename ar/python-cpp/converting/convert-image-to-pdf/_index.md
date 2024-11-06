---
title: تحويل الصورة إلى PDF في بايثون
linktitle: تحويل الصورة إلى ملف PDF
type: docs
weight: 10
url: ar/python-cpp/convert-image-to-pdf/
lastmod: "2024-04-22"
description: يوضح هذا الموضوع كيفية تحويل الصورة إلى PDF باستخدام Aspose.PDF لبايثون عبر مكتبة C++.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

توضح مكتبتنا مقتطفات من الأكواد لتحويل أشهر تنسيقات الصور - JPEG. يمكنك بسهولة تحويل صور JPG إلى PDF باستخدام Aspose.PDF لبايثون عبر C++ باتباع الخطوات التالية:

## تحويل الصورة إلى PDF

يمكنك بسهولة تحويل صور JPG إلى PDF باستخدام Aspose.PDF لـ C++ باتباع الخطوات التالية:

1. افتح ملف الصورة المدخل باستخدام مكتبة PIL
2. احصل على عرض وارتفاع الصورة
3. أنشئ مثيلًا جديدًا للوثيقة باستخدام مكتبة AsposePDFPythonWrappers
4. حدد الارتفاع والعرض الثابت للصورة
5. أضف صفحة جديدة إلى الوثيقة
6. أضف الصورة إلى الصفحة
7. احفظ ملف PDF الناتج باستخدام طريقة 'document.save'.

يوضح مقتطف الكود أدناه كيفية تحويل صورة JPG إلى PDF باستخدام بايثون عبر C++:

```python
import AsposePDFPythonWrappers as apw
import os
import os.path
from PIL import Image

# تعيين مسار الدليل لملفات البيانات
dataDir = os.path.join(os.getcwd(), "samples")

# تعيين مسار ملف الإدخال
input_file = os.path.join(dataDir, "sample.jpg")

# تعيين مسار ملف الإخراج
output_file = os.path.join(dataDir, "results", "jpg-to-pdf.pdf")

# فتح ملف الصورة المدخلة باستخدام مكتبة PIL
pil_img = Image.open(input_file)

# الحصول على عرض وارتفاع الصورة
width, height = pil_img.size

# إنشاء مثيل جديد لوثيقة باستخدام مكتبة AsposePDFPythonWrappers
document = apw.Document()

# إنشاء مثيل جديد للصورة باستخدام مكتبة AsposePDFPythonWrappers
image = apw.Image()

# تعيين مسار ملف الصورة
image.file = input_file

# تعيين الارتفاع الثابت والعرض للصورة
image.fix_height = height
image.fix_width = width

# إضافة صفحة جديدة إلى الوثيقة
page = document.pages.add()

# إضافة الصورة إلى الصفحة
page.paragraphs.add(image)

# حفظ الوثيقة في مسار ملف الإخراج
document.save(output_file)
```