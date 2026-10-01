---
title: إزالة إجراء الفتح
linktitle: إزالة إجراء الفتح
type: docs
weight: 20
url: /ar/java/remove-open-action/
description: تعرّف على كيفية إزالة إجراء فتح المستند من ملف PDF في Java باستخدام واجهة PdfContentEditor في Aspose.PDF.
lastmod: "2026-10-01"
TechArticle: true
AlternativeHeadline: إزالة إجراء فتح المستند في PDF باستخدام Java
Abstract: يوضح هذا المقال كيفية ربط ملف PDF، وإزالة إجراء فتح المستند، وحفظ المستند المحدث باستخدام واجهة PdfContentEditor في Aspose.PDF for Java.
---
## إزالة إجراء فتح المستند

1. قم بربط ملف PDF المصدر بـ `PdfContentEditor` واجهة.
2. اتصال `removeDocumentOpenAction()`.
3. احفظ مستند PDF المحدث.

```java
public static void removeOpenAction(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeDocumentOpenAction();
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
