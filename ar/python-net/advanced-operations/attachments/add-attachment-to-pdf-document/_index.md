---
title: إضافة مرفقات إلى PDF في Python
linktitle: إضافة مرفق إلى وثيقة PDF
type: docs
weight: 10
url: /ar/python-net/add-attachment-to-pdf-document/
description: تعرف على كيفية إضافة مرفقات الملفات إلى مستندات PDF في Python باستخدام Aspose.PDF لـ Python عبر .NET.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إضافة المرفقات إلى PDF باستخدام Python
Abstract: توفر هذه المقالة دليلًا تفصيليًا حول كيفية إضافة مرفقات إلى ملف PDF باستخدام Python ومكتبة Aspose.PDF. وهي توضح بالتفصيل عملية إعداد مشروع Python جديد، واستيراد حزمة Aspose.PDF الضرورية، وإنشاء كائن «Document». تشرح المقالة كيفية إنشاء كائن «FileEspecification» بالملف والوصف المطلوبين، وكيفية إضافة هذا الكائن إلى «EmbeddedFileCollection» في مستند PDF باستخدام طريقة «الإضافة». تحتوي «مجموعة الملفات المضمنة» على جميع المرفقات داخل PDF. يتم تضمين مقتطف الشفرة لتوضيح عملية فتح مستند وإعداد ملف للمرفق وإلحاقه بمجموعة مرفقات المستند وحفظ ملف PDF المحدث.
---

يمكن أن تحتوي المرفقات على مجموعة متنوعة من المعلومات ويمكن أن تكون من مجموعة متنوعة من أنواع الملفات. توضح هذه المقالة كيفية إضافة مرفق إلى ملف PDF.

استخدم مرفقات PDF المضمنة عندما تحتاج إلى تجميع ملفات المصدر الداعمة أو جداول البيانات أو الصور أو المستندات ذات الصلة مع ملف PDF الرئيسي.

1. قم بإنشاء مشروع Python جديد.
1. قم باستيراد حزمة Aspose.PDF
1. قم بإنشاء [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) كائن.
1. قم بإنشاء [مواصفات الملف](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) الكائن مع الملف الذي تقوم بإضافته، ووصف الملف.
1. أضف [مواصفات الملف](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) الاعتراض على [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) الكائنات [مجموعة الملفات المضمنة](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) المجموعة، مع المجموعة [اضاف](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) طريقة.

ال [مجموعة الملفات المضمنة](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) تحتوي المجموعة على جميع المرفقات في ملف PDF. يوضح مقتطف الشفرة التالي كيفية إضافة مرفق في مستند PDF.

```python
from os import path
import aspose.pdf as ap

def add_attachments(infile, attachment_path, outfile):
    with ap.Document(infile) as document:
        file_spec = ap.FileSpecification(attachment_path, "Sample text file")
        document.embedded_files.add(path.basename(attachment_path), file_spec)
        document.save(outfile)
```

## موضوعات المرفقات ذات الصلة

- [العمل مع مرفقات PDF في بايثون](/pdf/ar/python-net/attachments/)
- [إزالة المرفقات من PDF في Python](/pdf/ar/python-net/removing-attachment-from-an-existing-pdf/)
- [إنشاء وإدارة حافظات PDF في Python](/pdf/ar/python-net/portfolio/)

