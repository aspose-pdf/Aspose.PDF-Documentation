---
title: حقول الأزرار والصور
linktitle: حقول الأزرار والصور
type: docs
weight: 40
url: /ar/java/button-fields-and-images/
description: تعلم كيفية إضافة مظهر صورة إلى حقل زر في نموذج PDF باستخدام واجهة Form في Aspose.PDF for Java.
lastmod: "2026-10-01"
TechArticle: true
AlternativeHeadline: إضافة مظهر صورة إلى حقل زر PDF في Java
Abstract: توضح هذه المقالة كيفية استخدام واجهة Form في Aspose.PDF for Java لربط نموذج PDF، تحميل صورة كتيار، تعبئة حقل زر صورة، وحفظ المستند المحدث.
---
مثال جافا في `FormExamples.addImageAppearanceToButtonField(...)` يُظهر كيفية تحديث مظهر حقل الزر باستخدام تدفق صورة.

سير العمل بسيط:

- ربط ملف PDF الإدخال بـ `form.bindPdf(...)`
- افتح ملف الصورة باستخدام `Files.newInputStream(...)`
- اتصال `form.fillImageField(...)` لحقل الزر
- حفظ ملف PDF المحدث

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
