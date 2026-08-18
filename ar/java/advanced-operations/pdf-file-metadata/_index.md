---
title: العمل مع بيانات تعريف ملف PDF في Java
linktitle: البيانات الوصفية لملف PDF
type: docs
weight: 200
url: /java/pdf-file-metadata/
description: تعرف على كيفية استخراج البيانات التعريفية لملف PDF وتحديثها وإدارتها ومعلومات المستند وخصائص XMP في Java باستخدام Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: احصل على معلومات مستند PDF وبيانات تعريف XMP وقم بتعيينها في Java
Abstract: تشرح هذه المقالة كيفية التعامل مع بيانات تعريف PDF باستخدام Aspose.PDF لـ Java. تعرف على كيفية قراءة معلومات المستند مثل المؤلف والعنوان والكلمات الأساسية، وتحديث خصائص الملف، وفحص إصدار PDF وامتيازاته، وتعيين حقول بيانات تعريف XMP، وحفظ البيانات التعريفية من خلال واجهات برمجة تطبيقات DOM والواجهة.
---
يوفر Aspose.PDF for Java طريقتين رئيسيتين للعمل مع البيانات التعريفية:

- واجهة برمجة تطبيقات DOM من خلال `Document` و`DocumentInfo` و`document.getMetadata()`.
- واجهة برمجة التطبيقات (API) للواجهة من خلال `PdfFileInfo`.

## الحصول على معلومات ملف PDF

استخدم هذا المثال عندما تحتاج إلى قراءة حقول معلومات المستند القياسية مثل المؤلف أو العنوان أو الموضوع أو الكلمات الأساسية.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بالوصول إلى كائن [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/documentinfo/).
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

## قم بتعيين البيانات التعريفية ببادئة مساحة الاسم

استخدم هذا المثال عندما تحتاج إلى إضافة خاصية XMP أو تحديثها باستخدام بادئة مساحة الاسم المسجلة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بتسجيل مساحة اسم XMP المطلوبة وأضف عنصر بيانات التعريف.
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

استخدم هذا المثال عندما تريد كتابة خصائص ملف PDF القياسية مثل المؤلف أو العنوان أو المنتج أو تاريخ الإنشاء.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بالوصول إلى [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/documentinfo/) وقم بتعيين قيم بيانات التعريف الجديدة.
1. احفظ المستند بمعلومات الملف المحدثة.

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

## قم بتعيين خصائص بيانات تعريف XMP

استخدم هذا المثال عندما تحتاج إلى تخزين إدخالات XMP إضافية، بما في ذلك قيم بيانات التعريف المخصصة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإضافة عناصر بيانات تعريف XMP المطلوبة من خلال `document.getMetadata()`.
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
