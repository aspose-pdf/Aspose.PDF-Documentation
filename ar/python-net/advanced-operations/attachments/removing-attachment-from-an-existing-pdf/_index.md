---
title: إزالة المرفقات من PDF في Python
linktitle: إزالة المرفق من ملف PDF موجود
type: docs
weight: 30
url: /ar/python-net/removing-attachment-from-an-existing-pdf/
description: يمكن لـ Aspose.PDF إزالة المرفقات من مستندات PDF الخاصة بك. استخدم واجهة برمجة تطبيقات Python PDF لإزالة المرفقات في ملفات PDF باستخدام Aspose.PDF لبيثون عبر مكتبة.NET.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية حذف المرفقات من PDF باستخدام Python
Abstract: تتناول هذه المقالة كيفية إزالة المرفقات من ملفات PDF باستخدام Aspose.PDF لـ Python. يتم تخزين المرفقات في مستند PDF ضمن مجموعة «الملفات المضمنة» لكائن «المستند». لحذف جميع المرفقات من PDF، يمكنك استدعاء طريقة `delete () `في مجموعة `EmbeddedFiles` ثم حفظ المستند المحدث باستخدام طريقة `save ()` الخاصة بكائن `Document`. يتم توفير مقتطف شفرة لتوضيح هذه العملية، وعرض خطوات فتح مستند وحذف مرفقاته وحفظ الملف المعدل.
---

يمكن لـ Aspose.PDF لبيثون إزالة المرفقات من ملفات PDF. يتم الاحتفاظ بمرفقات وثيقة PDF في كائنات المستند [ملفات مضمّنة](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) مجموعة.

يعد سير العمل هذا مفيدًا عندما تحتاج إلى تنظيف الملفات المضمنة القديمة أو تقليل حجم الحزمة أو إعداد PDF لإعادة التوزيع بدون مواد المصدر المرفقة.

لحذف جميع المرفقات المرتبطة بملف PDF:

1. اتصل بـ [ملفات مضمّنة](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) مجموعات [حذف ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) طريقة.
1. احفظ الملف المحدث باستخدام [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) الكائنات [حفظ ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) طريقة.

يوضح مقتطف الشفرة التالي كيفية إزالة المرفقات من مستند PDF.

```python

import aspose.pdf as ap

def remove_attachment(infile, outfile):
    # Open PDF document
    with ap.Document(infile) as document:
        document.embedded_files.delete()
        document.save(outfile)
```

## قم بإزالة مرفق محدد بالاسم

إذا كنت بحاجة إلى إزالة مرفق واحد فقط والاحتفاظ بالمرفقات الأخرى، فاستخدم [حذف بواسطة المفتاح ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/delete_by_key/) الطريقة وتمرير اسم المرفق.

لحذف مرفق محدد:

1. افتح ملف PDF المصدر.
1. اتصل `document.embedded_files.delete_by_key(attachment_name)`.
1. احفظ ملف PDF المحدث.

يزيل مقتطف الشفرة التالي مرفقًا واحدًا باسمه.

```python

import aspose.pdf as ap

def remove_attachment(infile, attachment_name, outfile):
    # Open PDF document
    with ap.Document(infile) as document:
        document.embedded_files.delete_by_key(attachment_name)
        document.save(outfile)
```

## موضوعات المرفقات ذات الصلة

- [العمل مع مرفقات PDF في بايثون](/pdf/ar/python-net/attachments/)
- [إضافة مرفقات إلى PDF في Python](/pdf/ar/python-net/add-attachment-to-pdf-document/)
- [إنشاء وإدارة حافظات PDF في Python](/pdf/ar/python-net/portfolio/)

