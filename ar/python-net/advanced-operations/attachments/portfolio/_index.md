---
title: العمل مع محفظة PDF باستخدام بايثون
linktitle: محفظة
type: docs
weight: 20
url: /ar/python-net/portfolio/
description: كيفية إنشاء محفظة PDF باستخدام بايثون. يجب عليك استخدام ملف مايكروسوفت إكسل، ومستند Word، وملف صورة لإنشاء محفظة PDF.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية العمل مع محفظة PDF باستخدام بايثون
Abstract: تناقش هذه المقالة إنشاء وإدارة محفظات PDF باستخدام Aspose.PDF للبايثون عبر .NET. تسهل محفظة PDF دمج أنواع مختلفة من الملفات — مثل ملفات النصوص، والصور، وجداول البيانات، والعروض التقديمية — في مستند واحد منظم، مما يضمن تخزين جميع المواد ذات الصلة معًا. توضح المقالة عملية إنشاء محفظة PDF، مبرزةً استخدام فئة `Document` وفئة `FileSpecification` لإضافة ملفات إلى مجموعة المستندات. يتم تقديم مثال يوضح تضمين ملف مايكروسوفت إكسل، ومستند Word، وملف صورة في محفظة PDF. بالإضافة إلى ذلك، تتضمن المقالة مقتطفات شيفرة لإنشاء محفظة وإزالة ملفات منها، مما يوضح بساطة وكفاءة إدارة محفظات PDF باستخدام Aspose.PDF للبايثون.
---

يسمح إنشاء محفظة PDF بتجميع وأرشفة أنواع مختلفة من الملفات في مستند واحد متسق. يمكن أن يتضمن هذا المستند ملفات نصية، وصورًا، وجداول بيانات، وعروض تقديمية، ومواد أخرى، ويضمن أن جميع المواد ذات الصلة مخزنة ومنظمة في مكان واحد.

ستساعد محفظة PDF في عرض تقديمك بجودة عالية، أينما استخدمتها. بشكل عام، إنشاء محفظة PDF هو مهمة حديثة ومعاصرة للغاية.

## كيفية إنشاء محفظة PDF

Aspose.PDF للبايثون عبر .NET يتيح إنشاء مستندات محفظة PDF باستخدام الفئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) . أضف ملفًا إلى كائن document.collection بعد الحصول عليه باستخدام الفئة [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) . عندما تُضاف الملفات، استخدم طريقة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) من الفئة Document لحفظ مستند المحفظة.

المثال التالي يستخدم ملف مايكروسوفت إكسل، ومستند Word، وملف صورة لإنشاء محفظة PDF.

الشيفرة أدناه تنتج المحفظة التالية.

### محفظة PDF تم إنشاؤها باستخدام Aspose.PDF للبايثون

![محفظة PDF تم إنشاؤها باستخدام Aspose.PDF للبايثون](working-with-pdf-portfolio_1.jpg)

```python

    import aspose.pdf as ap

    # Instantiate Document Object
    document = ap.Document()

    # Instantiate document Collection object
    document.collection = ap.Collection()

    # Get Files to add to Portfolio
    excel = ap.FileSpecification(input_excel)
    word = ap.FileSpecification(input_doc)
    image = ap.FileSpecification(input_jpg)

    # Provide description of the files
    excel.description = "Excel File"
    word.description = "Word File"
    image.description = "Image File"

    # Add files to document collection
    document.collection.append(excel)
    document.collection.append(word)
    document.collection.append(image)

    # Save Portfolio document
    document.save(output_pdf)
```

## إزالة الملفات من محفظة PDF

لحذف/إزالة الملفات من محفظة PDF، جرب استخدام الأسطر البرمجية التالية.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    document.collection.delete()

    # Save updated file
    document.save(output_pdf)
```


