---
title: Set Size of PDF using pythob via C++
linktitle: Set Size of PDF
type: docs
weight: 30
url: ar/python-cpp/get-and-set-page-properties/
description: يوضح هذا القسم كيفية الحصول على خصائص صفحة PDF أو تعيينها مثل حجم المستند باستخدام Python عبر C++.
lastmod: "2024-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## ضبط حجم ملف PDF

تمكنك Aspose.PDF for Python عبر C++ من قراءة وتعيين خصائص الصفحات في ملف PDF في تطبيقات Python الخاصة بك.

يفتح مقتطف الشفرة التالي ملف PDF، ويعيد ضبط حجم الصفحة الأولى عن طريق تعديل **مربع القص** (مربع القص هو حجم "الصفحة" الذي يتم فيه عرض مستند PDF الخاص بك في Adobe Acrobat)، ويحفظ المستند المعدل في ملف جديد.

1. إنشاء كائن مستند من الملف المدخل
1. احصل على مجموعة الصفحات من المستند باستخدام [document_get_pages](https://reference.aspose.com/pdf/python-cpp/core/document_get_pages/)

1. احصل على الصفحة الأولى من مجموعة الصفحات باستخدام [page_collection_get_page](https://reference.aspose.com/pdf/python-cpp/core/page_collection_get_page/)
1. احصل على مستطيل مربع الاقتصاص من الصفحة باستخدام [page_get_rectangle](https://reference.aspose.com/pdf/python-cpp/core/page_get_rectangle/)
1. احسب الإحداثيات الجديدة لمربع الاقتصاص
1. حدّث إحداثيات مربع الاقتصاص بالقيم الجديدة
1. احفظ المستند المعدل في ملف الإخراج باستخدام طريقة 'document.save'

```python

    import AsposePDFPython as apCore
    import os
    import os.path

    # احصل على دليل العمل الحالي وأنشئ المسار إلى دليل "samples"
    dataDir = os.path.join(os.getcwd(), "samples")

    # أنشئ مسارات ملفات الإدخال والإخراج
    input_file = os.path.join(dataDir, "sample0.pdf")
    output_file = os.path.join(dataDir, "results", "resized_document.pdf")

    # أنشئ كائن مستند من ملف الإدخال
    doc = apCore.document_create_from_file(inputFile)

    # احصل على مجموعة الصفحات من المستند
    pages = apCore.document_get_pages(doc)

    # احصل على الصفحة الأولى من مجموعة الصفحات
    page = apCore.page_collection_get_page(pages, 1)

    # احصل على مستطيل مربع الاقتصاص من الصفحة
    crop_box = apCore.page_get_rectangle(page)

    # احسب الإحداثيات الجديدة لمربع الاقتصاص
    LLX = apCore.rectangle_get_LLX(crop_box) + 10
    LLY = apCore.rectangle_get_LLY(crop_box) + 10
    URX = apCore.rectangle_get_URX(crop_box) - 10
    URY = apCore.rectangle_get_URY(crop_box) - 10

    # حدّث إحداثيات مربع الاقتصاص بالقيم الجديدة
    apCore.rectangle_set_LLX(crop_box, LLX)
    apCore.rectangle_set_LLY(crop_box, LLY)
    apCore.rectangle_set_URX(crop_box, URX)
    apCore.rectangle_set_URY(crop_box, URY)

    # احفظ المستند المعدل في ملف الإخراج
    apCore.document_save(doc, output_file)

    # أغلق المقبض المستند
    apCore.close_handle(doc)
```