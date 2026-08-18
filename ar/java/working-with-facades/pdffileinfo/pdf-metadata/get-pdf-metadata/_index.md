---
title: احصل على بيانات تعريف PDF
linktitle: احصل على بيانات تعريف PDF
type: docs
weight: 20
url: /java/get-pdf-metadata/
description: تعرف على كيفية قراءة بيانات تعريف PDF في Java باستخدام واجهة PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استرداد بيانات تعريف PDF باستخدام Aspose.PDF لـ Java.
Abstract: تعرف على كيفية استرداد بيانات تعريف PDF باستخدام Aspose.PDF لـ Java. يقرأ مثال Java الحقول القياسية مثل الموضوع والعنوان والكلمات الرئيسية والمنشئ وتاريخ الإنشاء وتاريخ التعديل، بالإضافة إلى إشارات حالة الملف وإدخال بيانات التعريف `Reviewer` المخصص.
---
## احصل على بيانات تعريف PDF

يقرأ هذا المثال معلومات المستند القياسية وعلامات حالة الملف ومفتاح بيانات التعريف المخصص.

### خطوات

1. قم بإنشاء كائن `PdfFileInfo` لملف PDF المصدر.
2. اقرأ حقول البيانات التعريفية القياسية مثل الموضوع والعنوان والكلمات الرئيسية والمنشئ.
3. افحص علامات حالة الملف، مثل ما إذا كان الملف صالحًا أو مشفرًا أو محميًا بكلمة مرور أو محفظة.
4. اقرأ قيمة بيانات التعريف المخصصة باستخدام `getMetaInfo`.
5. أغلق المثيل `PdfFileInfo`.

### مثال جافا

```java
public static void getPdfMetadata(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Subject: " + pdfInfo.getSubject());
    System.out.println("Title: " + pdfInfo.getTitle());
    System.out.println("Keywords: " + pdfInfo.getKeywords());
    System.out.println("Creator: " + pdfInfo.getCreator());
    System.out.println("Creation Date: " + pdfInfo.getCreationDate());
    System.out.println("Modification Date: " + pdfInfo.getModDate());
    System.out.println("Is Valid PDF: " + pdfInfo.isPdfFile());
    System.out.println("Is Encrypted: " + pdfInfo.isEncrypted());
    System.out.println("Has Open Password: " + pdfInfo.hasOpenPassword());
    System.out.println("Has Edit Password: " + pdfInfo.hasEditPassword());
    System.out.println("Is Portfolio: " + pdfInfo.hasCollection());
    String reviewer = pdfInfo.getMetaInfo("Reviewer");
    System.out.println("Reviewer: " + (reviewer == null || reviewer.isBlank() ? "No Reviewer metadata found." : reviewer));
    pdfInfo.close();
}
```
