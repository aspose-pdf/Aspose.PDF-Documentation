---
title: من سطر واحد إلى متعدد
linktitle: من سطر واحد إلى متعدد
type: docs
weight: 60
url: /ar/java/single-to-multiple/
description: تعرّف على كيفية تحويل حقل نص من سطر واحد إلى حقل متعدد الأسطر في مستند PDF باستخدام Java عبر واجهة FormEditor في Aspose.PDF.
lastmod: "2026-10-01"
TechArticle: true
AlternativeHeadline: تحويل حقل PDF من سطر واحد إلى متعدد الأسطر في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود، وتحويل حقل من سطر واحد إلى حقل متعدد الأسطر، وحفظ المستند المحدث باستخدام واجهة FormEditor في Aspose.PDF for Java.
---
## تحويل حقل من سطر واحد إلى عدة أسطر

1. ربط ملف PDF المصدر إلى `FormEditor` واجهة.
2. اتصال `single2Multiple(...)` لاسم الحقل الهدف.
3. احفظ المستند المحدث.

```java
public static void singleToMultiple(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.single2Multiple("City");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
