---
title: ملء مربع القائمة
linktitle: ملء مربع القائمة
type: docs
weight: 40
url: /java/fill-list-box/
description: تعرف على كيفية ملء حقل مربع قائمة في نموذج PDF باستخدام Java باستخدام واجهة النموذج في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: قم بتعيين قيمة حقل مربع القائمة في نموذج PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية ربط نموذج PDF وتعيين قيمة حقل مربع القائمة وحفظ المستند المحدث باستخدام واجهة النموذج في Aspose.PDF لـ Java.
---
استخدم `FormExamples.fillListBoxFields(...)` لملء حقل مربع القائمة.

```java
public static void fillListBoxFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("favorite_colors", "Red");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
