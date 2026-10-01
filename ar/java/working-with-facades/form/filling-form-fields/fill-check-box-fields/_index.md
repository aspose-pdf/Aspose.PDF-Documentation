---
title: ملء حقول مربعات الاختيار
linktitle: ملء حقول مربعات الاختيار
type: docs
weight: 20
url: /ar/java/fill-check-box-fields/
description: تعرف على كيفية ملء حقول مربعات الاختيار في نموذج PDF باستخدام Java عبر واجهة Form في Aspose.PDF.
lastmod: "2026-10-01"
TechArticle: true
AlternativeHeadline: تعيين قيم حقول مربعات الاختيار في نموذج PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية ربط نموذج PDF، وتعيين حقول مربعات الاختيار حسب الاسم، وحفظ المستند المحدث عبر واجهة Form في Aspose.PDF for Java.
---
استخدام `FormExamples.fillCheckBoxFields(...)` لتعيين قيم مربعات الاختيار في نموذج.

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
