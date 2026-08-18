---
title: تسلسل ملفات PDF متعددة
linktitle: تسلسل ملفات PDF متعددة
type: docs
weight: 20
url: /java/concatenate-pdf-files/
description: دمج ملفات PDF في Java باستخدام سير العمل المتسلسل PdfFileEditor القائم على المصفوفة.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: دمج ملفات PDF متعددة في مستند واحد باستخدام Java
Abstract: تعرف على كيفية ربط ملفات PDF باستخدام Aspose.PDF لـ Java. يستخدم نموذج المستودع التحميل الزائد `concatenate` القائم على المصفوفة مع مدخلين، ويمكن توسيع سير العمل نفسه ليشمل قوائم ملفات أطول لأن الطريقة تقبل مصفوفة سلسلة من مسارات المصدر.
---
## ربط ملفات PDF

يقوم نموذج Java بدمج ملفين عن طريق تمريرهما إلى التحميل الزائد `concatenate` القائم على الصفيف.

### خطوات

1. قم بإنشاء مثيل `PdfFileEditor`.
2. أنشئ مصفوفة سلسلة باستخدام مسارات إدخال PDF.
3. اتصل `concatenate` بمصفوفة الإدخال ومسار ملف الإخراج.
4. احفظ المستند المدمج.

```java
public static void mergePdfDocuments(Path firstInputFile, Path secondInputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.concatenate(new String[] {firstInputFile.toString(), secondInputFile.toString()}, outputFile.toString());
}
```

لدمج أكثر من ملفين، قم بتوسيع صفيف السلسلة الذي تم تمريره إلى `concatenate`.
