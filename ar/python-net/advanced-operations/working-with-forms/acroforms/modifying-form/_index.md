---
title: تعديل أكروفورم
linktitle: تعديل أكروفورم
type: docs
weight: 45
url: /ar/python-net/modifying-form/
description: قم بتعديل حقول AcroForm في مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET، بما في ذلك مسح النص وتعيين الحدود وحقول التصميم وإزالة الحقول.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إدارة حقول نموذج PDF وتخصيصها
Abstract: تقدم هذه المقالة أمثلة عملية لتعديل حقول AcroForm باستخدام Aspose.PDF لـ Python عبر .NET. ويغطي مسح النص من محتوى نموذج الآلة الكاتبة، وإعداد حدود أحرف حقل النص وقراءتها، وتطبيق مظهر الخط المخصص، وإزالة الحقول بالاسم. تدعم عمليات سير العمل هذه مهام صيانة النماذج الشائعة في خطوط أنابيب معالجة PDF الآلية.
---

## مسح النص في النموذج

يوضح هذا المثال كيفية مسح النص من حقول نموذج الآلة الكاتبة في PDF باستخدام Aspose.PDF لـ Python عبر .NET. يقوم بمسح الصفحة الأولى من PDF، ويحدد نماذج الآلة الكاتبة، ويزيل محتواها، ويحفظ المستند المحدث. هذا الأسلوب مفيد لإعادة تعيين حقول النموذج أو تعقيمها قبل إعادة توزيع PDF.

1. قم بتحميل وثيقة PDF المدخلة.
1. الوصول إلى النماذج في الصفحة الأولى.
1. كرر كل نموذج وتحقق مما إذا كان `Typewriter` نموذج.
1. استخدم TextFragmentAbsorber للعثور على أجزاء النص في النموذج.
1. امسح نص كل جزء.
1. احفظ ملف PDF المعدل في ملف الإخراج.

```python
import aspose.pdf as ap


def clear_text_in_form(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    forms = document.pages[1].resources.forms

    for form in forms:
        if form.it == "Typewriter" and form.subtype == "Form":
            absorber = ap.text.TextFragmentAbsorber()
            absorber.visit(form)

            for fragment in absorber.text_fragments:
                fragment.text = ""

    document.save(output_file_name)
```

## تعيين حد الحقل

استخدم `set_field_limit(field, limit)` من عند `FormEditor` لتحديد الحد الأقصى لعدد الأحرف المسموح بها في حقل النص.

1. قم بإنشاء `FormEditor` كائن.
1. قم بربط ملف PDF المدخل.
1. قم بتعيين حد الحقل للحقل الهدف.
1. احفظ ملف PDF المحدث.

```python
import aspose.pdf as ap


def set_field_limit(input_file_name, output_file_name):
    form = ap.facades.FormEditor()
    form.bind_pdf(input_file_name)
    form.set_field_limit("First Name", 15)
    form.save(output_file_name)
```

## احصل على حد الحقل

يمكنك أيضًا قراءة حد الأحرف من حقل نصي.

1. قم بتحميل وثيقة PDF.
1. قم بالوصول إلى حقل النموذج الهدف.
1. تأكد من أن الحقل عبارة عن `TextBoxField`.
1. القراءة والطباعة `max_len`.

```python
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable


def get_field_limit(input_file_name):
    document = ap.Document(input_file_name)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        text_box_field = cast(ap.forms.TextBoxField, document.form[1])
        print(f"Limit: {text_box_field.max_len}")
```

## تعيين خط مخصص لحقل النموذج

يقوم هذا المثال بتعيين مظهر افتراضي مخصص لحقل مربع النص، بما في ذلك الخط والحجم واللون.

1. قم بتحميل وثيقة PDF.
1. قم بالوصول إلى الحقل الهدف وتحقق من نوعه.
1. ابحث عن الخط في `FontRepository`.
1. قم بتقديم طلب جديد `DefaultAppearance`.
1. احفظ ملف PDF المحدث.

```python
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable


def set_form_field_font(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        text_box_field = cast(ap.forms.TextBoxField, document.form[1])
        font = ap.text.FontRepository.find_font("Calibri")
        text_box_field.default_appearance = ap.annotations.DefaultAppearance(
            font, 10, ap.Color.black.to_rgb()
        )

    document.save(output_file_name)
```

## إزالة الحقول في نموذج موجود

يزيل هذا الرمز حقل نموذج معين (باسمه) من مستند PDF ويحفظ الملف المحدث باستخدام Aspose.PDF لـ Python عبر .NET.

1. قم بتحميل وثيقة PDF.
1. احذف حقل النموذج بالاسم.
1. احفظ ملف PDF المحدث.

```python
import aspose.pdf as ap


def delete_form_field(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    document.form.delete("First Name")
    document.save(output_file_name)
```

## موضوعات ذات صلة

- [إنشاء نموذج أكروفورم](/pdf/ar/python-net/create-form/)
- [املأ نموذج أكروفورم](/pdf/ar/python-net/fill-form/)
- [استخراج أكروفورم](/pdf/ar/python-net/extract-form/)
- [استيراد وتصدير بيانات النموذج](/pdf/ar/python-net/import-export-form-data/)
