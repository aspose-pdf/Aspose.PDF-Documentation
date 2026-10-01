---
title: تقسيم PDF من البداية
linktitle: تقسيم PDF من البداية
type: docs
weight: 10
url: /ar/java/split-pdf-from-beginning/
description: تقسيم PDF من البداية في Java باستخدام واجهة PdfFileEditor.
lastmod: "2026-10-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استخراج الصفحات الأولى من PDF إلى مستند جديد باستخدام Java
Abstract: تعلم كيفية تقسيم PDF من البداية باستخدام Aspose.PDF for Java. يستخدم مثال Java مكتبة PdfFileEditor لأخذ الصفحات الثلاث الأولى من المستند وحفظها كملف PDF منفصل.
---
## تقسيم PDF من البداية

يعرض عينة Java استخراج الصفحات الثلاث الأولى من المستند المصدر.

### خطوات

1. إنشاء `PdfFileEditor` مثال.
2. اتصال `splitFromFirst` مع ملف المصدر، عدد الصفحات التي يجب الاحتفاظ بها، وملف الإخراج.
3. احفظ مستند PDF الجديد.

```java
public static void splitPdfFromBeginning(Path inputFile, Path outputFile) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitFromFirst(inputFile.toString(), 3, outputFile.toString());
}
```
