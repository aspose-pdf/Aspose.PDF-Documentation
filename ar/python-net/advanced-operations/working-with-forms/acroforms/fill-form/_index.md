---
title: ملء AcroForm - ملء نموذج PDF باستخدام بايثون
linktitle: ملء AcroForm
type: docs
weight: 20
url: /ar/python-net/fill-form/
description: يمكنك ملء النماذج في مستند PDF الخاص بك باستخدام مكتبة Aspose.PDF للبايثون.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية ملء حقل النموذج في PDF باستخدام بايثون
Abstract: توفر المقالة دليلًا حول كيفية ملء حقل نموذج في مستند PDF باستخدام مكتبة Aspose.PDF للبايثون. تشرح العملية كيفية الوصول إلى حقل نموذج من مجموعة نماذج المستند وتعيين قيمته عبر خاصية قيمة الحقل. يوضح كود المثال كيفية فتح مستند PDF، والتنقُّل عبر حقول النموذج للعثور على حقل معين باستخدام اسمه الجزئي (في هذه الحالة، "Field 1")، وتعديل قيمة حقل TextBoxField إلى "777". أخيرًا، يتم حفظ المستند المحدث إلى ملف إخراج. يتم توفير روابط إلى وثائق Aspose ذات الصلة لمزيد من المرجعية.
---

## ملء حقل النموذج في مستند PDF

المثال التالي يملأ حقول نموذج PDF بقيم جديدة باستخدام Aspose.PDF للبايثون عبر .NET ويحفظ المستند المحدث. يدعم تحديث حقول متعددة عن طريق تحديد قاموس بأسماء الحقول والقيم.

```python

    import aspose.pdf as ap

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    # Define the new field values
    new_field_values = {
        "First Name": "Alexander_New",
        "Last Name": "Greenfield_New",
        "City": "Yellowtown_New",
        "Country": "Redland_New"
    }

    # Create a Form object from the input PDF file
    form = ap.facades.Form(path_infile)

    # Fill out the form fields with the new values
    for formField in form.field_names:
        if formField in new_field_values:
            form.fill_field(formField, new_field_values[formField])

    # Save the modified form to the output PDF file
    form.save(path_outfile)
```



