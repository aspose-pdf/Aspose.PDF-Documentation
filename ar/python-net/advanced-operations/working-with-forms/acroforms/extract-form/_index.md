---
title: استخراج AcroForm - استخراج بيانات النموذج من PDF في Python
linktitle: استخراج أكروفورم
type: docs
weight: 30
url: /ar/python-net/extract-form/
description: استخرج القيم من حقول AcroForm في مستندات PDF باستخدام Aspose.PDF لبيثون عبر .NET.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية الحصول على بيانات النموذج من PDF باستخدام Python
Abstract: توضح هذه المقالة كيفية استخراج البيانات من حقول AcroForm في مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. يتكرر المثال من خلال أسماء حقول النموذج، ويقرأ القيم باستخدام واجهة النموذج، ويعيد قاموسًا للمعالجة النهائية. يُعد سير العمل هذا مفيدًا لإعداد التقارير والتحقق والتكامل مع الأنظمة الخارجية.
---

## استخراج البيانات من النموذج

### احصل على القيم من جميع الحقول في مستند PDF

لقراءة القيم من جميع الحقول في مستند PDF، قم بالتكرار من خلال أسماء حقول النموذج واسترجع كل قيمة من [نموذج](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) واجهة.

استخدم الخطوات التالية:

1. قم بربط ملف PDF المُدخل بـ `Form` كائن.
1. قم بالتكرار من خلال `field_names`.
1. اقرأ كل قيمة باستخدام `get_field()`.
1. قم بتخزين القيم في القاموس.
1. قم بإرجاع القيم المستخرجة أو معالجتها.

يعرض مقتطف شفرة Python التالي هذا الأسلوب.

```python
import aspose.pdf as ap


def get_values_from_all_fields(input_file_name):
    form = ap.facades.Form(input_file_name)

    form_values = {}
    for field_name in form.field_names:
        form_values[field_name] = form.get_field(field_name)

    print(form_values)
    return form_values
```

## موضوعات ذات صلة

- [إنشاء نموذج أكروفورم](/pdf/ar/python-net/create-form/)
- [املأ نموذج أكروفورم](/pdf/ar/python-net/fill-form/)
- [استيراد وتصدير بيانات النموذج](/pdf/ar/python-net/import-export-form-data/)
- [تعديل أكروفورم](/pdf/ar/python-net/modifying-form/)