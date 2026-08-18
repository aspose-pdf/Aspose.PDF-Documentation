---
title: حقول الأزرار والصور
linktitle: حقول الأزرار والصور
type: docs
weight: 40
url: /java/button-fields-and-images/
description: تعرف على كيفية إضافة مظهر صورة إلى حقل زر في نموذج PDF باستخدام واجهة النموذج في Aspose.PDF لـ Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: أضف مظهر صورة إلى حقل زر PDF في Java
Abstract: توضح هذه المقالة كيفية استخدام واجهة النموذج في Aspose.PDF لـ Java لربط نموذج PDF، وتحميل صورة كتدفق، وملء حقل زر الصورة، وحفظ المستند المحدث.
---
يوضح مثال Java في `FormExamples.addImageAppearanceToButtonField(...)` كيفية تحديث مظهر حقل الزر باستخدام دفق الصور.

سير العمل واضح ومباشر:

- قم بربط ملف PDF المُدخل بـ `form.bindPdf(...)`
- افتح ملف الصورة باستخدام `Files.newInputStream(...)`
- اتصل بـ `form.fillImageField(...)` للحصول على حقل الزر
- احفظ ملف PDF المحدث

```java
public static void addImageAppearanceToButtonField(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream imageStream = Files.newInputStream(imageFile)) {
        form.bindPdf(inputFile.toString());
        form.fillImageField("Image1_af_image", imageStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
