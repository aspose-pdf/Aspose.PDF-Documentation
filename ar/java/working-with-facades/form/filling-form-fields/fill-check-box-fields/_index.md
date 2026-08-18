---
title: ملء حقول خانة الاختيار
linktitle: ملء حقول خانة الاختيار
type: docs
weight: 20
url: /java/fill-check-box-fields/
description: تعرف على كيفية ملء حقول مربع الاختيار في نموذج PDF باستخدام Java باستخدام واجهة النموذج في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: قم بتعيين قيم حقل خانة الاختيار في نموذج PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية ربط نموذج PDF، وتعيين حقول خانات الاختيار حسب الاسم، وحفظ المستند المحدث بواجهة النموذج في Aspose.PDF لـ Java.
---
استخدم `FormExamples.fillCheckBoxFields(...)` لتعيين قيم خانات الاختيار في نموذج.

```java
public static void fillCheckBoxFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("subscribe_newsletter", "Yes");
        form.fillField("accept_terms", "Yes");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
