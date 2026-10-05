---
title: تعيين علم الإرسال
linktitle: تعيين علم الإرسال
type: docs
weight: 40
url: /ar/java/set-submit-flag/
description: مراجعة التغطية الحالية لجافا لضبط علم الإرسال على زر نموذج PDF باستخدام واجهة FormEditor في Aspose.PDF.
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: تهيئة علم الإرسال في أمثلة FormEditor لجافا
Abstract: لا تعرض مجموعة عينات Java الحالية تكوين علم الإرسال كطريقة مثال مستقلة منفصلة. بدلاً من ذلك، يتم توضيحه مع تكوين عنوان URL للإرسال في `setSubmitUrl(...)`.
---
الجافا `FormEditorExamples.setSubmitUrl(...)` تشمل الطريقة:

## تكوين علم الإرسال

1. اربط ملف PDF المصدر بـ واجهة `FormEditor`.
2. عيّن عنوان URL للإرسال لحقل الزر.
3. عيّن علم الإرسال للتنسيق المطلوب.
4. احفظ المستند المحدث.

```java
editor.setSubmitUrl("Script_Demo_Button", "http://www.example.com/submit");
editor.setSubmitFlag("Script_Demo_Button", SubmitFormFlag.Xfdf);
```

استخدم ذلك المثال المدمج كمسار عمل Java المدعوم بالمصدر لتكوين علامة إرسال في هذا المستودع.
