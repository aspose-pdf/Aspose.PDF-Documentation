---
title: قم بتعيين علامة الإرسال
linktitle: قم بتعيين علامة الإرسال
type: docs
weight: 40
url: /java/set-submit-flag/
description: قم بمراجعة تغطية Java الحالية لتعيين علامة إرسال على زر نموذج PDF باستخدام واجهة FormEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: إرسال تكوين العلامة في أمثلة Java FormEditor
Abstract: لا تعرض مجموعة نماذج Java الحالية تكوين علامة الإرسال كأسلوب مثال مستقل منفصل. بدلاً من ذلك، تم عرضه مع إرسال تكوين URL في `setSubmitUrl(...)`.
---
تتضمن طريقة Java `FormEditorExamples.setSubmitUrl(...)` ما يلي:

## تكوين علامة إرسال

1. قم بربط ملف PDF المصدر بالواجهة `FormEditor`.
2. قم بتعيين عنوان URL للإرسال لحقل الزر.
3. قم بتعيين علامة الإرسال للتنسيق المطلوب.
4. احفظ المستند المحدث.

```java
editor.setSubmitUrl("Script_Demo_Button", "http://www.example.com/submit");
editor.setSubmitFlag("Script_Demo_Button", SubmitFormFlag.Xfdf);
```

استخدم هذا المثال المدمج باعتباره سير عمل Java المدعوم من المصدر لتكوين علامة إرسال في هذا المستودع.
