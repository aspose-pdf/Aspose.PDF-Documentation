---
title: تحويل PDF إلى تنسيقات صور مختلفة في بايثون
linktitle: تحويل PDF إلى صور
type: docs
weight: 70
url: /python-cpp/convert-pdf-to-images-format/
lastmod: "2023-06-23"
description: يوضح هذا الموضوع كيفية استخدام Aspose.PDF لبايثون لتحويل PDF إلى تنسيقات صور مختلفة مثل TIFF، BMP، EMF، JPEG، PNG، GIF، SVG ببضع سطور من الكود.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## نظرة عامة

تشرح هذه المقالة كيفية تحويل PDF إلى تنسيقات صور مختلفة باستخدام بايثون. تغطي المقالة المواضيع التالية.

## تحويل PDF إلى صورة باستخدام بايثون

### تحويل PDF إلى PNG باستخدام بايثون

1. استيراد الوحدة AsposePdfPython، التي توفر غلاف بايثون لمكتبة Aspose.PDF.
2. فتح مستند PDF باستخدام وظيفة `document_open`، التي تأخذ اسم الملف كمعامل وتعيد كائن Document.
3. الحصول على صفحات المستند باستخدام وظيفة `document_get_pages`، التي تأخذ كائن Document كمعامل وتعيد كائن PageCollection.

1. الحصول على الصفحة المطلوبة من المستند باستخدام دالة `page_collection_get_page`، التي تأخذ كائن PageCollection وفهرس كمدخلات وتعيد كائن Page.
1. إنشاء كائن PngDevice باستخدام دالة `png_device_create`، التي لا تأخذ أي مدخلات. يمكن لهذا الكائن تحويل صفحات PDF إلى صور PNG بالمعايير الافتراضية.
1. حفظ الصفحة المطلوبة من المستند كصورة PNG باستخدام دالة `png_device_save_page_to_file`، التي تأخذ كائن PngDevice وكائن Page واسم ملف كمدخلات.
1. إغلاق مقابض كائنات PngDevice وDocument باستخدام دالة close_handle، التي تأخذ كائنًا كمدخل وتحرر موارده.

```python

from AsposePdfPython import *

doc = document_open("blank_pdf_document.pdf")
pages = document_get_pages(doc)
page = page_collection_get_page(pages,1)

pngDevice = png_device_create()
png_device_save_page_to_file(pngDevice,page,"test.png")

```

### تحويل PDF إلى JPEG باستخدام بايثون

1. افتح مستند PDF باستخدام دالة `document_open`، التي تأخذ اسم الملف كمعامل وتعيد كائن Document.
1. احصل على صفحات المستند باستخدام دالة `document_get_pages`، التي تأخذ كائن Document كمعامل وتعيد كائن PageCollection.
1. احصل على الصفحة المطلوبة من المستند باستخدام دالة `page_collection_get_page`، التي تأخذ كائن PageCollection وفهرس كمعاملات وتعيد كائن Page.
1. أنشئ كائن Resolution باستخدام دالة `resolution_create`، التي تأخذ قيمة الدقة بالنقاط في البوصة (DPI) كمعامل.
1. أنشئ كائن JpegDevice باستخدام دالة `jpeg_device_create_from_width_height_resolution`، التي تأخذ قيم العرض، الارتفاع والدقة كمعاملات. يمكن لهذا الكائن تحويل صفحات PDF إلى صور JPEG بالمعايير المحددة.

1. احفظ الصفحة المطلوبة من المستند كصورة JPEG باستخدام وظيفة `jpeg_device_save_page_to_file`، التي تأخذ كائن JpegDevice وكائن Page واسم ملف كوسائط.
1. أغلق المقابض لكائنات JpegDevice وDocument باستخدام وظيفة `close_handle`، التي تأخذ كائن كوسيط وتحرر موارده.

```python

    from AsposePdfPython import *

    doc = document_open("blank_pdf_document.pdf")
    pages = document_get_pages(doc)
    page = page_collection_get_page(pages,1)

    res = resolution_create(300)
    jpegDevice = jpeg_device_create_from_width_height_resolution(1239,1754,res)
    jpeg_device_save_page_to_file(jpegDevice,page,"test.jpeg")
```