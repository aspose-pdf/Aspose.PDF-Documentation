---
title: احصل على بيانات تعريف PDF
linktitle: احصل على بيانات تعريف PDF
type: docs
weight: 20
url: /ar/java/get-pdf-metadata/
description: تعلم كيفية قراءة بيانات تعريف PDF في Java باستخدام واجهة PdfFileInfo.
lastmod: "2026-10-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استرجاع بيانات تعريف PDF باستخدام Aspose.PDF for Java.
Abstract: تعلم كيفية استرجاع بيانات تعريف PDF باستخدام Aspose.PDF for Java. يقرأ مثال Java الحقول القياسية مثل الموضوع، العنوان، الكلمات المفتاحية، المُنشئ، تاريخ الإنشاء، وتاريخ التعديل، بالإضافة إلى علامات حالة الملف ومفتاح بيانات تعريف مخصص `Reviewer`.
---
## احصل على بيانات تعريف PDF

يقوم هذا المثال بقراءة معلومات المستند القياسية، وعلامات حالة الملف، ومفتاح بيانات تعريف مخصص.

### الخطوات

1. أنشئ كائن `PdfFileInfo` لملف PDF المصدر.
2. اقرأ حقول البيانات الوصفية القياسية مثل الموضوع، العنوان، الكلمات المفتاحية، والمنشئ.
3. افحص علامات حالة الملف مثل ما إذا كان الملف صالحًا، مشفرًا، محميًا بكلمة مرور، أو مجموعة ملفات.
4. اقرأ قيمة بيانات تعريف مخصصة باستخدام `getMetaInfo`.
5. أغلق `PdfFileInfo` مثال.

### مثال Java

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
