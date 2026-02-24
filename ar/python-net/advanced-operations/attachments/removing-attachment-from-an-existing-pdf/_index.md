---
title: إزالة المرفق من ملف PDF باستخدام Python
linktitle: إزالة المرفق من ملف PDF موجود
type: docs
weight: 30
url: /ar/python-net/removing-attachment-from-an-existing-pdf/
description: يمكن لـ Aspose.PDF إزالة المرفقات من مستندات PDF الخاصة بك. استخدم واجهة برمجة تطبيقات PDF للبايثون لإزالة المرفقات في ملفات PDF باستخدام Aspose.PDF للبايثون عبر مكتبة .NET.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية حذف المرفقات من PDF باستخدام بايثون
Abstract: هذا المقال يناقش كيفية إزالة المرفقات من ملفات PDF باستخدام Aspose.PDF للبايثون. تُخزن المرفقات في مستند PDF داخل مجموعة `EmbeddedFiles` لكائن `Document`. لحذف جميع المرفقات من PDF، يمكنك استدعاء طريقة `delete()` على مجموعة `EmbeddedFiles` ثم حفظ المستند المحدث باستخدام طريقة `save()` لكائن `Document`. تم توفير مقطع شفرة لتوضيح هذه العملية، يُظهر خطوات فتح المستند، حذف مرفقاته، وحفظ الملف المعدل.
---

يمكن لـ Aspose.PDF للبايثون إزالة المرفقات من ملفات PDF. تُحفظ مرفقات مستند PDF في مجموعة [الملفات المضمنة](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) لكائن Document.

لحذف جميع المرفقات المرتبطة بملف PDF:

1. استدعِ طريقة [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) لمجموعة [الملفات المضمنة](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/).
1. احفظ الملف المحدث باستخدام طريقة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) لكائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

يعرض مقتطف الشيفرة التالي كيفية إزالة المرفقات من مستند PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Delete all attachments
    document.embedded_files.delete()

    # Save updated file
    document.save(output_pdf)
```


