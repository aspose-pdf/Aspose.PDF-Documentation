---
title: العمل مع بيانات تعريف ملفات PDF في بايثون
linktitle: بيانات تعريف ملف PDF
type: docs
weight: 200
url: /ar/python-net/pdf-file-metadata/
description: استكشف كيفية استخراج وإدارة بيانات تعريف PDF، مثل المؤلف والعنوان، في بايثون باستخدام Aspose.PDF.
lastmod: "2025-05-12"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: الحصول على البيانات وتعيينها في PDF باستخدام بايثون
Abstract: توفر المقالة دليلًا شاملًا حول تعديل بيانات تعريف PDF باستخدام Aspose.PDF لبايثون عبر .NET. توضح طرق استخراج وتعيين خصائص البيانات، بما في ذلك المؤلف، تاريخ الإنشاء، الكلمات المفتاحية، والمزيد، والتي تعتبر أساسية لفهرسة المستندات، تحسين البحث، أو التحقق. توضح مقتطفات الشيفرة كيفية استرجاع البيانات من ملف PDF باستخدام فئة `Document` وخاصية `info`، وتعيين بيانات جديدة باستخدام كائن `DocumentInfo`، وحفظ التغييرات. بالإضافة إلى ذلك، تُظهر كيفية تحديث بيانات XMP برمجيًا، مما يعزز تنظيم المستندات وإمكانية البحث فيها. كما تشرح المقالة كيفية إدراج بيانات تعريف ببادئة مخصصة عن طريق تسجيل مساحة اسم URI. هذه الوظائف ضرورية للمطورين الذين يسعون لإدارة معلومات مستندات PDF بفعالية داخل التطبيقات.
---

## الحصول على معلومات ملف PDF

يوضح هذا المقتطف من الشيفرة كيفية استخراج بيانات التعريف من مستند PDF باستخدام Aspose.PDF لبايثون عبر .NET. من خلال الوصول إلى خاصية info لكائن Document، يتم استخراج المعلومات الرئيسية مثل المؤلف، تاريخ الإنشاء، الكلمات المفتاحية، تاريخ التعديل، الموضوع، والعنوان. هذه الوظيفة أساسية للتطبيقات التي تتطلب فهرسة المستندات، تحسين البحث، أو التحقق من خصائص المستند.

1. افتح ملف PDF باستخدام فئة Document
1. استرجع بيانات تعريف المستند عبر خاصية info
1. عرض معلومات البيانات. طباعة الحقول المطلوبة للبيانات

```python

    import aspose.pdf as ap

    def get_pdf_file_information():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf()

        # Open PDF document
        document = ap.Document(data_dir + "GetFileInfo.pdf")

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

## تعيين معلومات ملف PDF

يتيح لك Aspose.PDF لبايثون عبر .NET تعيين معلومات خاصة بملف PDF، مثل المؤلف، تاريخ الإنشاء، الموضوع، والعنوان. لتعيين هذه المعلومات:

1. افتح ملف PDF باستخدام فئة Document.
1. أنشئ كائن [DocumentInfo]() وحدد خصائص البيانات المطلوبة.
1. احفظ التغييرات في ملف PDF جديد باستخدام طريقة الحفظ.

المقتطف البرمجي التالي يوضح لك كيفية تعيين معلومات ملف PDF.

```python

    import aspose.pdf as ap
    import datetime

    def set_file_information():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_workingdocuments()

        # Open PDF document
        document = ap.Document(data_dir + "SetFileInfo.pdf")

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
        document.save(data_dir + "SetFileInfo_out.pdf")
```

## تعيين بيانات XMP في ملف PDF

يوضح هذا المقتطف البرمجي كيفية تعيين أو تحديث بيانات XMP برمجيًا في مستند PDF باستخدام Aspose.PDF لبايثون عبر .NET. من خلال تعديل خصائص مثل xmp:CreateDate و xmp:Nickname والحقول المعرفة مخصّصًا، يمكنك تضمين بيانات تعريف موحدة في ملفات PDF الخاصة بك. هذه الطريقة مفيدة بشكل خاص لتعزيز تنظيم المستندات، تسهيل إمكانية البحث، وتضمين المعلومات الأساسية مباشرةً في الملف.

يسمح لك Aspose.PDF بتعيين البيانات في ملف PDF. لتعيين البيانات:

1. افتح ملف PDF باستخدام الفئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. عدّل بيانات XMP عن طريق تعيين قيم للمفاتيح المحددة.
1. احفظ مستند PDF المحدث.

المقتطف البرمجي التالي يوضح لك كيفية تعيين البيانات في ملف PDF.

```python

    import aspose.pdf as ap
    import datetime

    def set_xmp_metadata():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf()

        # Open PDF document
        document = ap.Document(data_dir + "SetXMPMetadata.pdf")

        # Set XMP metadata properties
        document.metadata["xmp:CreateDate"] = datetime.datetime.now().isoformat()
        document.metadata["xmp:Nickname"] = "Nickname"
        document.metadata["xmp:CustomProperty"] = "Custom Value"

        # Save the updated PDF document
        document.save(data_dir + "SetXMPMetadata_out.pdf")
```

## إدراج بيانات مع بادئة

بعض المطورين يحتاجون إلى إنشاء مساحة اسم بيانات جديدة مع بادئة. يوضح المقتطف البرمجي التالي كيفية إدراج بيانات مع بادئة.

```python

    import aspose.pdf as ap
    import datetime

    def set_prefix_metadata():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf()

        # Open PDF document
        document = ap.Document(data_dir + "SetXMPMetadata.pdf")

        # Register a namespace URI for the 'xmp' prefix
        document.metadata.register_namespace_uri("xmp", "http://ns.adobe.com/xap/1.0/")

        # Set the metadata property using the registered prefix
        document.metadata["xmp:ModifyDate"] = datetime.datetime.now().isoformat()  # ISO 8601 format

        # Save the updated PDF document
        document.save(data_dir + "SetPrefixMetadata_out.pdf")
```
