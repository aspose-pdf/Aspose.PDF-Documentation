---
title: إنشاء محافظ PDF في بايثون
linktitle: محفظة
type: docs
weight: 20
url: /ar/python-net/portfolio/
description: تعرف على كيفية إنشاء وإدارة حافظات PDF في بايثون باستخدام Aspose.PDF لبيثون عبر .NET.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إنشاء وتحرير حافظات PDF مع الملفات المضمنة في Python
Abstract: تشرح هذه المقالة كيفية إنشاء وإدارة حافظات PDF باستخدام Aspose.PDF لـ Python عبر .NET. تعرف على كيفية تجميع أنواع ملفات متعددة في محفظة PDF واحدة، وإضافة ملفات إلى مجموعة مستندات، وإزالة عناصر المحفظة برمجيًا باستخدام Python.
---

يتيح إنشاء محفظة PDF دمج أنواع مختلفة من الملفات وأرشفتها في مستند واحد متسق. يمكن أن تتضمن هذه الوثيقة ملفات نصية وصور وجداول بيانات وعروض تقديمية ومواد أخرى، وتضمن تخزين جميع المواد ذات الصلة وتنظيمها في مكان واحد.

سوف تساعد محفظة PDF على عرض العرض التقديمي الخاص بك بطريقة عالية الجودة، أينما كنت تستخدمه. بشكل عام، يعد إنشاء محفظة PDF مهمة حديثة وحديثة للغاية.

استخدم محفظة PDF عندما تريد توزيع مجموعة من الملفات ذات الصلة معًا مع الاحتفاظ بكل ملف بتنسيقه الأصلي داخل حاوية PDF واحدة.

## كيفية إنشاء محفظة PDF

يسمح Aspose.PDF لبيثون عبر .NET بإنشاء مستندات حافظة PDF باستخدام [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) فئة. أضف ملفًا إلى كائن document.collection بعد الحصول عليه باستخدام [مواصفات الملف](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) فئة. عند إضافة الملفات، استخدم فئة «المستند» [حفظ ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) طريقة لحفظ مستند المحفظة.

يستخدم المثال التالي ملف Microsoft Excel ومستند Word وملف صورة لإنشاء محفظة PDF.

ينتج عن الكود أدناه المحفظة التالية.

### محفظة PDF تم إنشاؤها باستخدام Aspose.PDF لبيثون

![محفظة PDF تم إنشاؤها باستخدام Aspose.PDF لبيثون](working-with-pdf-portfolio_1.jpg)

```python
import aspose.pdf as ap

def create_pdf_portfolio(input_files, outfile):
    # Instantiate Document Object
    document = ap.Document()

    # Instantiate document Collection object
    document.collection = ap.Collection()

    # Get Files to add to Portfolio
    excel = ap.FileSpecification(input_files[0])
    word = ap.FileSpecification(input_files[1])
    image = ap.FileSpecification(input_files[2])

    # Provide description of the files
    excel.description = "Excel File"
    word.description = "Word File"
    image.description = "Image File"

    # Add files to document collection
    document.collection.append(excel)
    document.collection.append(word)
    document.collection.append(image)

    # Save Portfolio document
    document.save(outfile)
```

## إزالة الملفات من محفظة PDF

من أجل حذف/إزالة الملفات من محفظة PDF، حاول استخدام أسطر التعليمات البرمجية التالية.

```python
import aspose.pdf as ap

def remove_files_from_pdf_portfolio(infile, outfile):
    # Open document
    document = ap.Document(infile)
    document.collection.delete()

    # Save updated file
    document.save(outfile)
```

## موضوعات المرفقات ذات الصلة

- [العمل مع مرفقات PDF في بايثون](/pdf/ar/python-net/attachments/)
- [إضافة مرفقات إلى PDF في Python](/pdf/ar/python-net/add-attachment-to-pdf-document/)
- [إزالة المرفقات من PDF في Python](/pdf/ar/python-net/removing-attachment-from-an-existing-pdf/)

