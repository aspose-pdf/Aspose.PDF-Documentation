---
title: افتح مستند PDF برمجيًا
linktitle: افتح PDF
type: docs
weight: 20
url: /ar/java/open-pdf-document/
description: تعلم كيفية فتح ملف PDF في Java باستخدام Aspose.PDF من مسار ملف أو تدفق أو باستخدام كلمة مرور.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: فتح مستندات PDF باستخدام مكتبة Aspose.PDF في Java
Abstract: توضح هذه المقالة كيفية فتح مستندات PDF موجودة في Java باستخدام Aspose.PDF. وتغطي فتح PDF عن طريق مسار الملف، وفتح PDF من InputStream، وفتح مستند محمي بكلمة مرور، حيث يقرأ كل مثال عدد الصفحات من المستند المحمل.
---
يدعم Aspose.PDF for Java عدة طرق لتحميل مستند PDF موجود اعتمادًا على مصدر البيانات.

## فتح مستند PDF في Java

يمكنك فتح مستند PDF:

1. افتح [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مباشرةً من مسار ملف.
1. افتح [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) من `InputStream`.
1. افتح مشفرًا [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) عن طريق توفير كلمة المرور.

## افتح المستند من الملف

```java
public static void openDocumentFromFile(Path inputFile) {
    Document document = new Document(inputFile.toString());
    System.out.println("Pages: " + document.getPages().size());
    document.close();
}
```

## فتح المستند من الدفق

```java
public static void openDocumentFromStream(Path inputFile) throws Exception {
    try (InputStream stream = Files.newInputStream(inputFile)) {
        Document document = new Document(stream);
        System.out.println("Pages: " + document.getPages().size());
        document.close();
    }
}
```

## افتح مستندًا مشفرًا

```java
public static void openDocumentEncrypted(Path inputFile) {
    Document document = new Document(inputFile.toString(), "P@ssw0rd");
    System.out.println("Pages: " + document.getPages().size());
    document.close();
}
```
