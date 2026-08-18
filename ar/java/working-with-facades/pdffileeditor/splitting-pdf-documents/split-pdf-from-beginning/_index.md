---
title: تقسيم ملف PDF من البداية
linktitle: تقسيم ملف PDF من البداية
type: docs
weight: 10
url: /java/split-pdf-from-beginning/
description: قم بتقسيم ملف PDF من البداية في Java باستخدام واجهة PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم باستخراج الصفحات الأولى من ملف PDF إلى مستند جديد باستخدام Java
Abstract: تعرف على كيفية تقسيم ملف PDF من البداية باستخدام Aspose.PDF لـ Java. يستخدم مثال Java PdfFileEditor لأخذ الصفحات الثلاث الأولى من المستند وحفظها كملف PDF منفصل.
---
## تقسيم ملف PDF من البداية

يقوم نموذج Java باستخراج الصفحات الثلاث الأولى من المستند المصدر.

### خطوات

1. قم بإنشاء مثيل `PdfFileEditor`.
2. اتصل `splitFromFirst` بالملف المصدر وعدد الصفحات المطلوب الاحتفاظ بها وملف الإخراج.
3. احفظ مستند PDF الجديد.

```java
public static void splitPdfFromBeginning(Path inputFile, Path outputFile) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitFromFirst(inputFile.toString(), 3, outputFile.toString());
}
```
