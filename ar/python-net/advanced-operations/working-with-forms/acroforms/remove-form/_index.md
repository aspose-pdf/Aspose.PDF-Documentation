---
title: حذف النماذج من PDF باستخدام بايثون
linktitle: حذف النماذج
type: docs
weight: 70
url: /ar/python-net/remove-form/
description: إزالة النص بناءً على النوع الفرعي/النموذج باستخدام Aspose.PDF للبايثون عبر مكتبة .NET. حذف جميع النماذج من PDF.
lastmod: "2025-09-17"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: حذف النماذج من PDF باستخدام Aspose.PDF للبايثون عبر .NET
Abstract: هذا المستند يقدم نهجين معتمدين على بايثون لإزالة عناصر النماذج من ملفات PDF باستخدام Aspose.PDF للبايثون عبر .NET. الطريقة الأولى توضح كيفية مسح جميع كائنات النماذج من صفحة محددة عن طريق الوصول إلى قاموس الموارد الخاص بها واستدعاء طريقة clear() على مجموعة النماذج. الطريقة الثانية توفر حلاً أكثر استهدافًا من خلال تكرار تعليقات النماذج، وتحديد النماذج من نوع الآلة كاتبة، وحذفها انتقائيًا بناءً على سماتها. كلتا التقنيتين تنتهيان بحفظ ملف PDF المحدث إلى مسار الإخراج المحدد، مما يوفر خيارات مرنة لتنظيف النماذج وتحسين الوثيقة في سير العمل الآلي.
---

## إزالة جميع النماذج من PDF

يقوم هذا الكود بإزالة جميع عناصر النموذج من الصفحة الأولى من مستند PDF ثم يحفظ المستند المعدل إلى مسار الإخراج المحدد.

1. تحميل مستند PDF.
1. الوصول إلى موارد الصفحة.
1. مسح كائنات النموذج.
1. حفظ المستند المحدث.

```python

    import aspose.pdf as ap
    import os

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(data_dir, infile)
    path_outfile = os.path.join(data_dir, outfile)

    document = ap.Document(path_infile)
    forms = document.pages[page_num].resources.forms
    forms.clear()
    document.save(path_outfile)
```

## إزالة النموذج المحدد

في المثال التالي يتم تكرار كائنات النموذج على صفحة PDF معينة، وتحديد تعليقات النماذج من نوع الآلة كاتبة، وحذفها، ثم حفظ ملف PDF المحدث باستخدام Aspose.PDF للبايثون عبر .NET.

1. تحميل مستند PDF.
1. الوصول إلى نماذج الصفحة.
1. التكرار عبر النماذج.
1. التحقق من نماذج الآلة كاتبة.
1. حذف النموذج المطابق.
1. حفظ المستند المحدث.

```python

    import aspose.pdf as ap
    import os

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    document = ap.Document(path_infile)
    forms = document.pages[page_num].resources.forms
    for form in forms:
        if (form.it == "Typewriter" and form.subtype == "Form"):
            name = forms.get_form_name(form)
            forms.delete(name)
    document.save(path_outfile)
```
