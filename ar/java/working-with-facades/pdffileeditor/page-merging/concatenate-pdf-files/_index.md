---
title: دمج ملفات PDF متعددة
linktitle: دمج ملفات PDF متعددة
type: docs
weight: 20
url: /ar/java/concatenate-pdf-files/
description: دمج ملفات PDF في Java باستخدام سير عمل دمج القائم على المصفوفة في PdfFileEditor.
lastmod: "2026-10-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: دمج ملفات PDF متعددة في مستند واحد باستخدام Java
Abstract: تعرف على كيفية دمج ملفات PDF باستخدام Aspose.PDF for Java. يستخدم مثال المستودع التحميل الزائد `concatenate` القائم على المصفوفة مع مدخلين، ويمكن توسيع نفس سير العمل إلى قوائم ملفات أطول لأن الطريقة تقبل مصفوفة نصية من مسارات المصدر.
---
## دمج ملفات PDF

عينة Java تدمج ملفين عن طريق تمريرهما إلى المصفوفة القائمة على المصفوفة `concatenate` زيادة التحميل.

### الخطوات

1. إنشاء `PdfFileEditor` مثال.
2. بناء مصفوفة سلاسل نصية تحتوي على مسارات ملفات PDF المدخلات.
3. اتصال `concatenate` مع مصفوفة الإدخال ومسار ملف الإخراج.
4. احفظ المستند المدمج.

```java
public static void mergePdfDocuments(Path firstInputFile, Path secondInputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.concatenate(new String[] {firstInputFile.toString(), secondInputFile.toString()}, outputFile.toString());
}
```

لدمج أكثر من ملفين، قم بتمديد مصفوفة السلاسل التي تم تمريرها إلى `concatenate`.
