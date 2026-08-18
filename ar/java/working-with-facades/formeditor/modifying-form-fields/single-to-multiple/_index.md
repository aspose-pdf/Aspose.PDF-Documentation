---
title: واحد إلى متعدد
linktitle: واحد إلى متعدد
type: docs
weight: 60
url: /java/single-to-multiple/
description: تعرف على كيفية تحويل حقل نص من سطر واحد إلى حقل متعدد الأسطر في مستند PDF في Java باستخدام واجهة FormEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: تحويل حقل PDF من سطر واحد إلى متعدد الأسطر في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود، وتحويل حقل من سطر واحد إلى حقل متعدد الأسطر، وحفظ المستند المحدث باستخدام واجهة FormEditor في Aspose.PDF لـ Java.
---
## تحويل حقل سطر واحد إلى أسطر متعددة

1. قم بربط ملف PDF المصدر بالواجهة `FormEditor`.
2. اتصل `single2Multiple(...)` للحصول على اسم الحقل الهدف.
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
