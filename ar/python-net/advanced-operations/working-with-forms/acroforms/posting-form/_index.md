---
title: نشر النماذج في PDF عبر Python
linktitle: نماذج النشر
type: docs
weight: 75
url: /ar/python-net/posting-form/
description: أضف أزرار الإرسال وإجراءات الإرسال إلى PDF AcroForms باستخدام Aspose.PDF لبيثون عبر .NET.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إضافة أزرار الإرسال وإجراءات تقديم النموذج إلى PDF باستخدام Python
Abstract: تعرض هذه المقالة طريقتين لإضافة وظيفة الإرسال إلى نماذج PDF باستخدام Aspose.PDF لـ Python عبر .NET. يمكنك إضافة زر إرسال جاهز من خلال ForMeditor أو إنشاء حقل زر مخصص باستخدام SubmitFormAction للتحكم المتقدم. تساعد هذه الأنماط على دمج نماذج PDF مع نقاط نهاية معالجة النماذج من جانب الخادم.
---

## إضافة زر إرسال مع ForMeditor

يوضح مقتطف الشفرة التالي كيفية إضافة زر إرسال إلى نموذج PDF باستخدام فئة ForMeditor في Aspose.PDF لـ Python عبر .NET. تم تكوين الزر لإرسال بيانات النموذج إلى عنوان URL محدد عند النقر عليه.

1. قم بإنشاء `FormEditor` كائن.
1. أضف زر إرسال إلى الصفحة المستهدفة.
1. قم بتعيين عنوان URL للإرسال وإحداثيات الزر.
1. احفظ ملف PDF المحدث.

```python
import aspose.pdf as ap

def add_submit_button(input_file_name, output_file_name):
    editor = ap.facades.FormEditor(input_file_name, output_file_name)
    editor.add_submit_btn(
        "submitbutton", 1, "Submit", "http://localhost/testing/show", 100, 450, 150, 475
    )
    editor.save()
```

## إضافة إجراء إرسال مخصص

يشرح مقتطف الشفرة التالي كيفية إنشاء زر إرسال مخصص في نموذج PDF باستخدام Aspose.PDF لـ Python عبر .NET. تم تكوين الزر لإرسال بيانات النموذج إلى عنوان URL محدد عند النقر عليه.

1. افتح ملف PDF باستخدام AP.document ().
1. قم بإنشاء إجراء إرسال.
1. قم بتعيين عنوان URL المستهدف وعلامات الإرسال.
1. قم بإنشاء حقل زر وربط إجراء النقر الخاص به.
1. أضف الزر إلى النموذج.
1. احفظ ملف PDF المحدث.

```python
import aspose.pdf as ap

def add_submit_action(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    submit_action = ap.annotations.SubmitFormAction()
    submit_action.url = ap.FileSpecification("http://localhost:3000/submit")
    submit_action.flags = (
        ap.annotations.SubmitFormAction.EXPORT_FORMAT
        | ap.annotations.SubmitFormAction.SUBMIT_COORDINATES
    )

    rect = ap.Rectangle(10, 10, 100, 40)
    submit_button = ap.forms.ButtonField(document.pages[1], rect)
    submit_button.partial_name = "SubmitButton"
    submit_button.value = "Submit"
    submit_button.actions.on_release_mouse_btn = submit_action

    document.form.add(submit_button, 1)
    document.save(output_file_name)
```

## موضوعات ذات صلة

- [إنشاء نموذج أكروفورم](/pdf/ar/python-net/create-form/)
- [املأ نموذج أكروفورم](/pdf/ar/python-net/fill-form/)
- [تعديل أكروفورم](/pdf/ar/python-net/modifying-form/)
- [استيراد وتصدير بيانات النموذج](/pdf/ar/python-net/import-export-form-data/)