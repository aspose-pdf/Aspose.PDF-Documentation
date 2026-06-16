---
title: حذف النماذج من PDF في Python
linktitle: حذف النماذج
type: docs
weight: 70
url: /ar/python-net/remove-form/
description: قم بإزالة كائنات النموذج من صفحات PDF باستخدام Aspose.PDF لـ Python عبر .NET، بما في ذلك التنظيف الكامل والحذف المستهدف.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إزالة النماذج من PDF باستخدام Aspose.PDF لبيثون عبر.NET
Abstract: تقدم هذه المقالة طريقتين لإزالة عناصر النموذج من مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. تقوم الطريقة الأولى بمسح جميع كائنات النموذج من صفحة محددة، بينما تزيل الطريقة الثانية موارد نموذج الآلة الكاتبة المطابقة فقط. تساعد هذه الأمثلة في تنظيف النموذج وإعداد القالب وسير عمل تسوية المستندات.
---

## إزالة جميع النماذج من صفحة

يزيل هذا الرمز جميع كائنات النموذج من الصفحة المحددة بواسطة `page_num` ويحفظ المستند المحدث.

1. قم بتحميل وثيقة PDF.
1. موارد صفحة الوصول.
1. مسح كائنات النموذج.
1. احفظ المستند المحدث.

```python
import aspose.pdf as ap

def remove_all_forms(input_file_name, page_num, output_file_name):
    document = ap.Document(input_file_name)
    forms = document.pages[page_num].resources.forms
    forms.clear()
    document.save(output_file_name)
```

## إزالة نوع نموذج معين

يقوم المثال التالي بتكرار كائنات النموذج في صفحة PDF معينة، ويحدد التعليقات التوضيحية لنموذج الآلة الكاتبة، ويحذفها، ثم يحفظ ملف PDF المحدث باستخدام Aspose.PDF لـ Python عبر .NET.

1. قم بتحميل وثيقة PDF.
1. نماذج صفحة الوصول.
1. كرر النماذج.
1. تحقق من نماذج الآلة الكاتبة.
1. احذف النموذج المطابق.
1. احفظ المستند المحدث.

```python
import aspose.pdf as ap

def remove_specified_form(input_file_name, page_num, output_file_name):
    document = ap.Document(input_file_name)
    forms = document.pages[page_num].resources.forms
    for form in forms:
        if form.it == "Typewriter" and form.subtype == "Form":
            name = forms.get_form_name(form)
            forms.delete(name)
    document.save(output_file_name)
```

## موضوعات ذات صلة

- [إنشاء نموذج أكروفورم](/pdf/ar/python-net/create-form/)
- [املأ نموذج أكروفورم](/pdf/ar/python-net/fill-form/)
- [تعديل أكروفورم](/pdf/ar/python-net/modifying-form/)
- [نماذج النشر](/pdf/ar/python-net/posting-form/)
