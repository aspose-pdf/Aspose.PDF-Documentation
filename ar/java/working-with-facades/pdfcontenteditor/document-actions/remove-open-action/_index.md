---
title: إزالة الإجراء المفتوح
linktitle: إزالة الإجراء المفتوح
type: docs
weight: 20
url: /java/remove-open-action/
description: تعرف على كيفية إزالة إجراء فتح المستند من ملف PDF في Java باستخدام واجهة PdfContentEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: قم بإزالة إجراء فتح مستند PDF في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF، وإزالة إجراء فتح المستند، وحفظ المستند المحدث باستخدام واجهة PdfContentEditor في Aspose.PDF لـ Java.
---
## قم بإزالة إجراء فتح المستند

1. قم بربط ملف PDF المصدر بالواجهة `PdfContentEditor`.
2. اتصل `removeDocumentOpenAction()`.
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
