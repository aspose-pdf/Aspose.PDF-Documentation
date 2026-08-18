---
title: فتح مستند PDF برمجياً
linktitle: افتح ملف PDF
type: docs
weight: 20
url: /java/open-pdf-document/
description: تعرف على كيفية فتح ملف PDF في Java باستخدام Aspose.PDF من مسار ملف أو دفق أو باستخدام كلمة مرور.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: فتح مستندات PDF باستخدام مكتبة Aspose.PDF في Java
Abstract: توضح هذه المقالة كيفية فتح مستندات PDF الموجودة في Java باستخدام Aspose.PDF. وهو يغطي فتح ملف PDF عن طريق مسار الملف، وفتح ملف PDF من InputStream، وفتح مستند محمي بكلمة مرور، مع قراءة كل مثال لعدد الصفحات من المستند الذي تم تحميله.
---
يدعم Aspose.PDF for Java عدة طرق لتحميل مستند PDF موجود اعتمادًا على مصدر البيانات المصدر.

## افتح مستند PDF في جافا

يمكنك فتح مستند PDF:

1. افتح [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مباشرة من مسار الملف.
1. افتح [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) من `InputStream`.
1. افتح [مستندًا](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مشفرًا عن طريق توفير كلمة المرور.

## فتح المستند من الملف

```java
public static void openDocumentFromFile(Path inputFile) {
    Document document = new Document(inputFile.toString());
    System.out.println("Pages: " + document.getPages().size());
    document.close();
}
```

## افتح المستند من الدفق

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
