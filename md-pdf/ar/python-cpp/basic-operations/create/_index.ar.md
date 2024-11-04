---
title: إنشاء مستند PDF
linktitle: إنشاء PDF
type: docs
weight: 10
url: /python-cpp/create-document/
description: تصف هذه الصفحة كيفية إنشاء مستند PDF من الصفر باستخدام Aspose.PDF لـ Python عبر مكتبة C++.
---

بالنسبة للمطورين، هناك العديد من السيناريوهات حيث يصبح من الضروري إنشاء ملفات PDF برمجيًا. قد تحتاج إلى إنشاء تقارير PDF برمجيًا وملفات PDF أخرى في برنامجك. إن كتابة الكود والوظائف من الصفر يعد طويلًا وغير فعال. لإنشاء ملف PDF باستخدام Python، هناك حل أفضل - **Aspose.PDF لـ Python عبر C++**.

## إنشاء ملف PDF باستخدام Python

لإنشاء ملف PDF باستخدام Python، يمكن استخدام الخطوات التالية.

* استيراد جميع الفئات والأساليب من مكتبة Aspose.PDF لـ Python عبر C++.
* إنشاء كائن Document جديد يمثل مستند PDF فارغ باستخدام [document_create](https://reference.aspose.com/pdf/python-cpp/core/document_create/)

* الحصول على كائن [document_get_pages](https://reference.aspose.com/pdf/python-cpp/core/document_get_pages/) الذي يحتوي على جميع الصفحات في المستند.

* إضافة صفحة جديدة إلى نهاية مجموعة الصفحات [page_collection_add_page](https://reference.aspose.com/pdf/python-cpp/core/page_collection_add_page/) ويعيد كائن Page الذي يمثل الصفحة المضافة.
* حفظ المستند إلى ملف بالاسم المحدد في دليل العمل الحالي.
* يغلق المقبض للمستند ويحرر أي موارد مرتبطة به.

```python

    from AsposePDFPython import *

    doc = document_create()
    pages = document_get_pages(doc)
    page = page_collection_add_page(pages)
    document_save(doc, "blank_pdf_document.pdf")
    close_handle(doc)
```


## إنشاء ملف PDF بناءً على DOM

```python

    from AsposePDFPythonWrappers import *

    doc = Document()
    page = doc.pages.add()
    doc.save("blank_pdf_document1.pdf")
```