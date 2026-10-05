---
title: العمل مع بيانات تعريف ملفات PDF في Java
linktitle: بيانات تعريف ملف PDF
type: docs
weight: 200
url: /ar/java/pdf-file-metadata/
description: تعلم كيفية استخراج وتحديث وإدارة بيانات تعريف ملفات PDF ومعلومات المستند وخصائص XMP في Java باستخدام Aspose.PDF.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: احصل على معلومات مستند PDF وقم بتعيين بيانات تعريف XMP في Java
Abstract: تشرح هذه المقالة كيفية العمل مع بيانات تعريف PDF باستخدام Aspose.PDF for Java. تعرف على كيفية قراءة معلومات المستند مثل المؤلف والعنوان والكلمات المفتاحية، وتحديث خصائص الملف، وفحص نسخة PDF والامتيازات، وضبط حقول بيانات تعريف XMP، وحفظ بيانات التعريف عبر كل من واجهات DOM و facade.
---
يقدم Aspose.PDF for Java طريقين رئيسيين للعمل مع بيانات التعريف:

- واجهة برمجة تطبيقات DOM عبر `Document`, `DocumentInfo`، و `document.getMetadata()`.
- واجهة API من خلال `PdfFileInfo`.

## احصل على معلومات ملف PDF

استخدم هذا المثال عندما تحتاج إلى قراءة حقول معلومات المستند القياسية مثل المؤلف، العنوان، الموضوع، أو الكلمات المفتاحية.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. انتقل إلى كائن [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/documentinfo/).
1. اقرأ حقول البيانات الوصفية المطلوبة وأخرج قيمها.

```java
public static void getPdfFileInformation(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocumentInfo docInfo = document.getInfo();

        System.out.println("Author: " + docInfo.getAuthor());
        System.out.println("Creation Date: " + docInfo.getCreationDate());
        System.out.println("Keywords: " + docInfo.getKeywords());
        System.out.println("Modify Date: " + docInfo.getModDate());
        System.out.println("Subject: " + docInfo.getSubject());
        System.out.println("Title: " + docInfo.getTitle());
    }
}
```

## تعيين البيانات الوصفية مع بادئة مساحة الاسم

استخدم هذا المثال عندما تحتاج إلى إضافة أو تحديث خاصية XMP باستخدام بادئة مساحة اسم مسجلة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. سجّل مساحة الاسم XMP المطلوبة وأضف عنصر البيانات الوصفية.
1. احفظ المستند المحدث.

```java
public static void setPrefixMetadata(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getMetadata().registerNamespaceUri("xmp", "http://ns.adobe.com/xap/1.0/");
        document.getMetadata().addItem("xmp:ModifyDate", OffsetDateTime.now().toString());
        document.save(outputFile.toString());
    }
    System.out.println("Prefix metadata saved to " + outputFile);
}
```

## تحديث حقول معلومات المستند

استخدم هذا المثال عندما تريد كتابة خصائص ملف PDF القياسية مثل المؤلف، العنوان، المنتج، أو تاريخ الإنشاء.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. انتقل إلى [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/documentinfo/) وعيّن قيم بيانات تعريفية جديدة.
1. احفظ المستند مع معلومات الملف المحدثة.

```java
public static void setFileInformation(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocumentInfo docInfo = document.getInfo();
        Date now = new Date();

        docInfo.setAuthor("Aspose");
        docInfo.setCreationDate(now);
        docInfo.setKeywords("Aspose.Pdf, DOM, API");
        docInfo.setModDate(now);
        docInfo.setSubject("PDF Information");
        docInfo.setTitle("Setting PDF Document Information");
        docInfo.setProducer("Custom producer");
        docInfo.setCreator("Custom creator");

        document.save(outputFile.toString());
    }
    System.out.println("File information saved to " + outputFile);
}
```

## تعيين خصائص بيانات XMP الوصفية

استخدم هذا المثال عندما تحتاج إلى تخزين إدخالات XMP إضافية، بما في ذلك قيم البيانات التعريفية المخصصة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف عناصر البيانات الوصفية XMP المطلوبة عبر `document.getMetadata()`.
1. احفظ ملف الإخراج.

```java
public static void setXmpMetadata(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getMetadata().addItem("xmp:CreateDate", OffsetDateTime.now().toString());
        document.getMetadata().addItem("xmp:Nickname", "Nickname");
        document.getMetadata().addItem("xmp:CustomProperty", "Custom Value");
        document.save(outputFile.toString());
    }
    System.out.println("XMP metadata saved to " + outputFile);
}
```
