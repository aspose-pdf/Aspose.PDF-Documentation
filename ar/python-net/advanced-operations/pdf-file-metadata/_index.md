---
title: العمل مع البيانات الوصفية لملف PDF في Python
linktitle: بيانات تعريف ملف PDF
type: docs
weight: 200
url: /ar/python-net/pdf-file-metadata/
description: تعرف على كيفية استخراج البيانات الوصفية لملف PDF وخصائص XMP وتحديثها وإدارتها في Python باستخدام Aspose.PDF.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: احصل على معلومات مستند PDF وبيانات XMP الوصفية وقم بتعيينها في Python
Abstract: تشرح هذه المقالة كيفية العمل مع بيانات PDF الوصفية في Aspose.PDF لـ Python عبر .NET. تعرف على كيفية قراءة معلومات المستند مثل المؤلف والعنوان والكلمات الرئيسية وتحديث خصائص الملف وتعيين حقول بيانات XMP الوصفية وتسجيل بادئات البيانات الوصفية المخصصة لملفات PDF في Python.
---

استخدم هذا الدليل عندما تحتاج إلى فحص خصائص المستند أو تحديث معلومات ملف PDF للبحث أو الفهرسة أو إدارة بيانات XMP الوصفية برمجيًا في Python.

## احصل على معلومات ملف PDF

يوضح مقتطف الشفرة هذا كيفية استخراج البيانات الوصفية من مستند PDF باستخدام Aspose.PDF لـ Python عبر .NET. من خلال الوصول إلى خاصية المعلومات الخاصة بكائن المستند، فإنه يسترد المعلومات الأساسية مثل المؤلف وتاريخ الإنشاء والكلمات الأساسية وتاريخ التعديل والموضوع والعنوان. هذه الوظيفة ضرورية للتطبيقات التي تتطلب فهرسة المستندات أو تحسين البحث أو التحقق من خصائص المستند.

1. افتح ملف PDF باستخدام فئة المستند
1. استرجع البيانات الوصفية للمستند من خلال خاصية المعلومات
1. عرض معلومات البيانات الوصفية. اطبع حقول البيانات الوصفية المطلوبة

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def get_pdf_file_information(infile):
    # Open PDF document
    document = ap.Document(infile)

    # Get document information
    doc_info = document.info

    # Display document information
    print(f"Author: {doc_info.author}")
    print(f"Creation Date: {doc_info.creation_date}")
    print(f"Keywords: {doc_info.keywords}")
    print(f"Modify Date: {doc_info.mod_date}")
    print(f"Subject: {doc_info.subject}")
    print(f"Title: {doc_info.title}")
```

## قم بتعيين معلومات ملف PDF

يسمح لك Aspose.PDF لـ Python عبر .NET بتعيين معلومات خاصة بالملف لملف PDF ومعلومات مثل المؤلف وتاريخ الإنشاء والموضوع والعنوان. لتعيين هذه المعلومات:

1. افتح ملف PDF باستخدام فئة المستند.
1. قم بإنشاء [معلومات المستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/documentinfo/) الكائن وتعيين خصائص البيانات الوصفية المطلوبة.
1. احفظ التغييرات على ملف PDF جديد باستخدام طريقة الحفظ.

يوضح لك مقتطف الشفرة التالي كيفية تعيين معلومات ملف PDF.

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def set_file_information(infile, outfile):

    # Open PDF document
    document = ap.Document(infile)

    # Specify document information
    doc_info = ap.DocumentInfo(document)
    doc_info.author = "Aspose"
    doc_info.creation_date = datetime.datetime.now()
    doc_info.keywords = "Aspose.Pdf, DOM, API"
    doc_info.mod_date = datetime.datetime.now()
    doc_info.subject = "PDF Information"
    doc_info.title = "Setting PDF Document Information"
    doc_info.producer = "Custom producer"
    doc_info.creator = "Custom creator"

    # Save PDF document
    document.save(outfile)
```

## قم بتعيين بيانات XMP الأولية في ملف PDF

يوضح مقتطف الشفرة هذا كيفية تعيين بيانات XMP الوصفية أو تحديثها برمجيًا في مستند PDF باستخدام Aspose.PDF لـ Python عبر .NET. من خلال تعديل خصائص مثل XMP:createDate و XMP: الاسم المستعار والحقول المحددة حسب الطلب، يمكنك تضمين بيانات وصفية موحدة في ملفات PDF الخاصة بك. هذا الأسلوب مفيد بشكل خاص لتعزيز تنظيم المستندات وتسهيل إمكانية البحث ودمج المعلومات الأساسية مباشرة في الملف.

يسمح لك Aspose.PDF بتعيين البيانات الوصفية في ملف PDF. لتعيين البيانات الوصفية:

1. افتح ملف PDF باستخدام [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) فئة.
1. قم بتعديل بيانات XMP الأولية عن طريق تعيين قيم لمفاتيح محددة.
1. احفظ مستند PDF المحدث.

يوضح لك مقتطف الشفرة التالي كيفية تعيين البيانات الوصفية في ملف PDF.

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def set_xmp_metadata(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Set XMP metadata properties
    document.metadata.add("xmp:CreateDate", datetime.datetime.now().isoformat())
    document.metadata.add("xmp:Nickname", "Nickname")
    document.metadata.add("xmp:CustomProperty", "Custom Value")

    # Save the updated PDF document
    document.save(outfile)
```

## إدراج بيانات التعريف باستخدام البادئة

يحتاج بعض المطورين إلى إنشاء مساحة اسم بيانات تعريف جديدة باستخدام بادئة. يوضح مقتطف الشفرة التالي كيفية إدراج البيانات الوصفية بالبادئة.

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def set_prefix_metadata(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Register a namespace URI for the 'xmp' prefix
    document.metadata.register_namespace_uri("xmp", "http://ns.adobe.com/xap/1.0/")

    # Set the metadata property using the registered prefix
    document.metadata.add(
        "xmp:ModifyDate", datetime.datetime.now().isoformat()
    )  # ISO 8601 format

    # Save the updated PDF document
    document.save(outfile)
```

## موضوعات ذات صلة

- [عمليات PDF المتقدمة في بايثون](/pdf/ar/python-net/advanced-operations/)
- [العمل مع مستندات PDF في بايثون](/pdf/ar/python-net/working-with-documents/)
- [العمل مع مرفقات PDF في بايثون](/pdf/ar/python-net/attachments/)
- [قارن مستندات PDF في Python](/pdf/ar/python-net/compare-pdf-documents/)
