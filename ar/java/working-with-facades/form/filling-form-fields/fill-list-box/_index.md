---
title: ملء صندوق القائمة
linktitle: ملء صندوق القائمة
type: docs
weight: 40
url: /ar/java/fill-list-box/
description: تعلم كيفية ملء حقل صندوق القائمة في نموذج PDF باستخدام Java وواجهة Form في Aspose.PDF.
lastmod: "2026-10-01"
TechArticle: true
AlternativeHeadline: تعيين قيمة حقل صندوق القائمة في نموذج PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية ربط نموذج PDF، وتعيين قيمة حقل صندوق القائمة، وحفظ المستند المحدث باستخدام واجهة Form في Aspose.PDF for Java.
---
استخدام `FormExamples.fillListBoxFields(...)` لملء حقل صندوق القائمة.

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
