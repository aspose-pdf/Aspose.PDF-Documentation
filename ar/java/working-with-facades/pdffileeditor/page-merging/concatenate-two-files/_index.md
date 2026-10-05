---
title: دمج ملفين PDF
linktitle: دمج ملفين PDF
type: docs
weight: 60
url: /ar/java/concatenate-two-files/
description: دمج ملفين PDF في مستند واحد باستخدام Java مع واجهة PdfFileEditor.
lastmod: "2026-10-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: دمج ملفين PDF في مستند إخراج واحد باستخدام Java
Abstract: تعلم كيفية دمج ملفين PDF باستخدام Aspose.PDF for Java. يستخدم مثال Java فئة PdfFileEditor وتجاوز الدالة `concatenate` القائم على المصفوفة لدمج مستندين مصدرين في ملف PDF واحد كإخراج.
---
## دمج ملفين PDF

هذه المقالة ترتبط مباشرة بـ `mergePdfDocuments` مثال في `PdfFileEditorExamples.java`.

### خطوات

1. أنشئ مثيلًا من `PdfFileEditor`.
2. مرّر مسارات ملفي الإدخال كصفيف من السلاسل.
3. استدعِ `concatenate` مع المصفوفة ومسار ملف الإخراج.
4. احفظ ملف PDF المدمج.

```java
public static void mergePdfDocuments(Path firstInputFile, Path secondInputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.concatenate(new String[] {firstInputFile.toString(), secondInputFile.toString()}, outputFile.toString());
}
```
