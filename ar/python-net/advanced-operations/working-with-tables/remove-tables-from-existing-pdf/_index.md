---
title: إزالة الجداول من ملف PDF موجود
linktitle: إزالة الجداول
type: docs
weight: 50
url: /ar/python-net/removing-tables/
lastmod: "2025-09-27"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية حذف الجداول من PDF باستخدام بايثون
Abstract: تناقش هذه المقالة وظائف Aspose.PDF للبايثون عبر .NET، مع التركيز بشكل خاص على معالجة الجداول داخل مستندات PDF. تسمح المكتبة للمستخدمين بإدراج أو إنشاء جداول في ملفات PDF جديدة أو الموجودة، وكذلك تعديل أو إزالة الجداول من ملفات PDF الحالية. تقدم المقالة فئة `TableAbsorber`، التي تُعد أساسية لتحديد الجداول والتفاعل معها في PDF. تمت إضافة طريقة جديدة، `remove()`, لتمكين إزالة الجداول. يوفر المستند مقتطفين من الشيفرة - أحدهما يوضح كيفية إزالة جدول واحد من PDF، وآخر يوضح إزالة عدة جداول. تُبرز هذه الأمثلة التطبيق العملي لفئة `TableAbsorber` لتحقيق إزالة الجداول من مستندات PDF.
---

## إزالة جدول من مستند PDF

يسمح Aspose.PDF للبايثون بإزالة جدول من PDF. يفتح ملف PDF موجود، يكتشف أول جدول في الصفحة الأولى باستخدام TableAbsorber، يحذف ذلك الجدول باستخدام [remove_one_table](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods). بعد ذلك، يحفظ الـ PDF المحدث في ملف جديد.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    # Load existing PDF document
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(document.pages[1])
    # Get first table on the page
    table = absorber.table_list[0]
    # Remove the table
    absorber.remove(table)
    # Save PDF
    document.save(path_outfile)
```

## إزالة جميع الجداول من مستند PDF

مع مكتبتنا، يمكنك إزالة جميع الجداول من صفحة محددة في PDF. يفتح الكود ملف PDF موجود، يكتشف جميع الجداول في الصفحة الثانية باستخدام TableAbsorber، يتنقل عبر الجداول المكتشفة، يزيل كل جدول، ثم يحفظ ملف PDF المعدل في ملف جديد. يكون ذلك مفيدًا عندما تحتاج إلى إزالة الجداول جماعيًا من صفحة مع إبقاء باقي محتوى PDF دون تغيير.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    # Load existing PDF document
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit second page with absorber
    absorber.visit(document.pages[1])
    #  Loop through the copy of collection and removing tables
    tables = list(absorber.table_list)
    for table in tables:
        absorber.remove(table)

    # Save document
    document.save(path_outfile)
```


