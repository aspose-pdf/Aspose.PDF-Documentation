---
title: تعيين علم الإرسال
linktitle: تعيين علم الإرسال
type: docs
weight: 40
url: /ar/java/set-submit-flag/
description: مراجعة التغطية الحالية لجافا لضبط علم الإرسال على زر نموذج PDF باستخدام واجهة FormEditor في Aspose.PDF.
lastmod: "2026-10-01"
TechArticle: true
AlternativeHeadline: تهيئة علم الإرسال في أمثلة FormEditor لجافا
Abstract: لا تعرض مجموعة عينات جافا الحالية تكوين علم الإرسال كطريقة مثال مستقلة منفصلة. بدلاً من ذلك، يتم توضيحه مع تكوين عنوان URL للإرسال في `setSubmitUrl(...)`.
---
الجافا `FormEditorExamples.setSubmitUrl(...)` تشمل الطريقة:

## تكوين علم الإرسال

1. ربط ملف PDF المصدر بـ `FormEditor` واجهة.
2. تعيين عنوان URL للإرسال لحقل الزر.
3. تعيين علم الإرسال للتنسيق المطلوب.
4. حفظ المستند المحدث.

```java
editor.setSubmitUrl("Script_Demo_Button", "http://www.example.com/submit");
editor.setSubmitFlag("Script_Demo_Button", SubmitFormFlag.Xfdf);
```

استخدم ذلك المثال المدمج كمسار عمل Java المدعوم بالمصدر لتكوين علامة إرسال في هذا المستودع.
