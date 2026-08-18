---
title: قم بتسلسل ملفين PDF
linktitle: قم بتسلسل ملفين PDF
type: docs
weight: 60
url: /java/concatenate-two-files/
description: دمج ملفين PDF في مستند واحد في Java باستخدام واجهة PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بربط ملفين PDF في مستند إخراج واحد باستخدام Java
Abstract: تعرف على كيفية ربط ملفين PDF باستخدام Aspose.PDF لـ Java. يستخدم مثال Java PdfFileEditor والتحميل الزائد `concatenate` القائم على المصفوفة لدمج مستندين مصدر في ملف PDF واحد.
---
## قم بربط ملفين PDF

ترتبط هذه المقالة مباشرة بالمثال `mergePdfDocuments` في `PdfFileEditorExamples.java`.

### خطوات

1. قم بإنشاء مثيل `PdfFileEditor`.
2. قم بتمرير مساري ملف الإدخال كمصفوفة سلسلة.
3. اتصل `concatenate` بالمصفوفة ومسار ملف الإخراج.
4. احفظ ملف PDF المدمج.

```java
public static void mergePdfDocuments(Path firstInputFile, Path secondInputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.concatenate(new String[] {firstInputFile.toString(), secondInputFile.toString()}, outputFile.toString());
}
```
