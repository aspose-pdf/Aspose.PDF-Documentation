---
title: إضافة مرفق إلى مستند PDF باستخدام بايثون
linktitle: إضافة مرفق إلى مستند PDF
type: docs
weight: 10
url: /ar/python-net/add-attachment-to-pdf-document/
description: هذه الصفحة تصف كيفية إضافة مرفق إلى ملف PDF باستخدام مكتبة Aspose.PDF للبايثون عبر .NET.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إضافة مرفقات إلى PDF باستخدام بايثون
Abstract: هذه المقالة تقدم دليلًا خطوة بخطوة حول كيفية إضافة مرفقات إلى ملف PDF باستخدام بايثون ومكتبة Aspose.PDF. تفصل العملية التي تشمل إعداد مشروع بايثون جديد، استيراد حزمة Aspose.PDF اللازمة، وإنشاء كائن `Document`. توضح المقالة كيفية إنشاء كائن `FileSpecification` مع الملف المطلوب والوصف، وكيفية إضافة هذا الكائن إلى `EmbeddedFileCollection` في مستند PDF باستخدام طريقة `add`. الـ `EmbeddedFileCollection` يحتفظ بجميع المرفقات داخل ملف PDF. يتم تضمين مقتطف شفرة لتوضيح عملية فتح مستند، إعداد ملف للمرفق، إلحاقه بمجموعة مرفقات المستند، وحفظ ملف PDF المحدث.
---

يمكن للمرفقات أن تحتوي على مجموعة واسعة من المعلومات ويمكن أن تكون بأنواع متعددة من الملفات. تشرح هذه المقالة كيفية إضافة مرفق إلى ملف PDF.

1. إنشاء مشروع بايثون جديد.
1. استيراد حزمة Aspose.PDF
1. إنشاء كائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) .
1. إنشاء كائن [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) مع الملف الذي تضيفه، ووصف الملف.
1. إضافة كائن [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) إلى مجموعة [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) لكائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)، باستخدام طريقة [add](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods).

تحتوي مجموعة [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) على جميع المرفقات في ملف PDF. يوضح مقتطف الشفرة التالي كيفية إضافة مرفق في مستند PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Setup new file to be added as attachment
    fileSpecification = ap.FileSpecification(attachment_file, "Sample text file")

    # Add attachment to document's attachment collection
    document.embedded_files.append(fileSpecification)

    # Save new output
    document.save(output_pdf)
```


