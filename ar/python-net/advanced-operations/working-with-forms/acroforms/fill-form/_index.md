---
title: املأ أكروفورم - املأ نموذج PDF باستخدام بايثون
linktitle: املأ نموذج أكروفورم
type: docs
weight: 20
url: /ar/python-net/fill-form/
description: املأ حقول أكروفورم في وثيقة PDF باستخدام Aspose.PDF لبيثون عبر.NET.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية ملء حقل النموذج في PDF باستخدام Python
Abstract: تشرح هذه المقالة كيفية ملء حقول AcroForm في مستند PDF باستخدام Aspose.PDF لـ Python عبر .NET. يستخدم المثال واجهة النموذج، ويقوم بتعيين أسماء الحقول للقيم الجديدة في القاموس، ويقوم بتحديث الحقول المطابقة، ويحفظ ملف PDF الناتج. هذا الأسلوب مفيد لعمليات سير عمل إكمال المستندات المؤتمتة ومعالجة النماذج المجمعة.
---

## املأ حقل النموذج في مستند PDF

المثال التالي يملأ حقول متعددة في نموذج PDF موجود باستخدام [نموذج](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) واجهة.

استخدم الخطوات التالية:

1. قم بإنشاء قاموس بأسماء الحقول والقيم.
1. قم بربط ملف PDF المدخل بكائن النموذج.
1. قم بالتكرار من خلال حقول النموذج المتاحة.
1. املأ الحقول الموجودة في القاموس.
1. احفظ ملف PDF المحدث.

```python
import aspose.pdf as ap

def fill_form(input_file_name, output_file_name):
    new_field_values = {
        "First Name": "Alexander_New",
        "Last Name": "Greenfield_New",
        "City": "Yellowtown_New",
        "Country": "Redland_New",
    }

    form = ap.facades.Form(input_file_name)

    for field_name in form.field_names:
        if field_name in new_field_values:
            form.fill_field(field_name, new_field_values[field_name])

    form.save(output_file_name)
```

## موضوعات ذات صلة

- [إنشاء نموذج أكروفورم](/pdf/ar/python-net/create-form/)
- [استخراج أكروفورم](/pdf/ar/python-net/extract-form/)
- [استيراد وتصدير بيانات النموذج](/pdf/ar/python-net/import-export-form-data/)