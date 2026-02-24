---
title: العمل مع نماذج XFA
linktitle: نماذج XFA
type: docs
weight: 20
url: /ar/python-net/xfa-forms/
description: تتيح لك Aspose.PDF للـ Python عبر .NET API العمل مع حقول XFA و XFA Acroform في مستند PDF.
lastmod: "2025-02-17"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## تحويل XFA إلى Acroform

{{% alert color="primary" %}}

جرّب عبر الإنترنت
يمكنك التحقق من جودة تحويل Aspose.PDF وعرض النتائج عبر الإنترنت عبر هذا الرابط: [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

يظهر المقتطف البرمجي التالي كيفية تحويل نموذج XFA الديناميكي (XML Forms Architecture) إلى AcroForm قياسي.

**تشمل الخطوات الرئيسية:**

1. تحميل مستند PDF الإدخال.
1. تغيير نوع النموذج إلى STANDARD.
1. حفظ ملف PDF المحول إلى ملف جديد.

يسمح هذا التحويل بتوافقية أفضل ومعالجة نماذج موحدة عبر مختلف قارئات PDF والتطبيقات.

```python

    import aspose.pdf as ap


    path_infile = self.data_dir + "DynamicXFAToAcroForm.pdf.pdf"
    path_outfile = self.data_dir + "StandardAcroForm_out.pdf"

    # Load dynamic XFA form
    with ap.Document(path_infile) as document:
        # Set the form fields type as standard AcroForm
        document.form.type = ap.forms.FormType.STANDARD
        # Save PDF document
        document.save(path_outfile)
```

## استخدام IgnoreNeedsRendering

يوضح هذا المثال كيفية تحويل نموذج XFA الديناميكي إلى AcroForm قياسي باستخدام Aspose.PDF للـ Python. يتحقق الكود مما إذا كان ملف PDF الإدخال يحتوي على نموذج XFA ويعيد كتابة العرض إذا لزم الأمر. ثم يضبط نوع النموذج إلى STANDARD ويحفظ ملف PDF المحدث.

```python

    import aspose.pdf as ap


    path_infile = self.data_dir + "DynamicXFAToAcroForm.pdf.pdf"
    path_outfile = self.data_dir + "StandardAcroForm_out.pdf"

    # Load dynamic XFA form
    with ap.Document(path_infile) as document:
        # check if XFA is present & if rendering should be overwritten
        if not document.form.needs_rendering and document.form.has_xfa:
            document.form.ignore_needs_rendering = True
        # Set the form fields type as standard AcroForm
        document.form.type = ap.forms.FormType.STANDARD
        # Save the resultant PDF
        document.save(path_outfile)
```

