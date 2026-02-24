---
title: تحويل PDF/x إلى صيغ PDF باستخدام Python
linktitle: تحويل PDF/x إلى صيغ PDF
type: docs
weight: 120
url: /ar/python-net/convert-pdf_x-to-pdf/
lastmod: "2025-09-27"
description: يوضح هذا الموضوع كيفية تحويل PDF/x إلى صيغ PDF باستخدام Aspose.PDF للـ Python عبر .NET.
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: كيفية تحويل PDF/x إلى صيغ PDF
Abstract: توفر المقالة دليلًا شاملاً حول تحويل PDF/UA و PDF/A إلى ملف PDF باستخدام Aspose.PDF للـ Python.
---

**تحويل PDF/x إلى صيغة PDF يعني القدرة على تحويل PDF/UA و PDF/A إلى ملف PDF.**

## تحويل PDF/A إلى PDF

1. تحميل مستند PDF باستخدام 'ap.Document'.
1. استدعاء 'remove_pdfa_compliance()' لإزالة جميع إعدادات الامتثال والبيانات الوصفية المتعلقة بـ PDF/A.
1. حفظ ملف PDF الناتج إلى مسار الإخراج.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.remove_pdfa_compliance()
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## إزالة امتثال PDF/UA

توضح هذه الدالة عملية تحويل من خطوتين: أولاً إزالة امتثال PDF/UA (الوصولية العامة)، ثم تحويل ملف PDF الناتج إلى صيغة PDF/A-1B مع وضع العلامات تلقائيًا لتسهيل الوصول والبنية الدلالية.

1. تحميل مستند PDF باستخدام 'ap.Document()'.
1. استدعاء 'document.remove_pdfa_compliance()' لإزالة أي قيود أو إعدادات امتثال لـ PDF/A.
1. حفظ ملف PDF المعدل إلى 'path_outfile'.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.remove_pdfa_compliance()
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```
