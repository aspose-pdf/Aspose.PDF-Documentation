---
title: حماية ملفات PDF في جافا
linktitle: تشفير وفك تشفير ملف PDF
type: docs
weight: 70
url: /java/protect-pdf-file/
description: تعرف على كيفية تشفير ملفات PDF وفك تشفير المستندات المحمية وتغيير كلمات المرور وفحص حماية كلمة المرور في Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بتعيين أذونات PDF وإدارة التشفير في Java
Abstract: يشرح هذا المقال كيفية حماية ملفات PDF في Java باستخدام Aspose.PDF. ويغطي تطبيق كلمات مرور المستخدم والمالك، وتعيين امتيازات المستندات، وتشفير وفك تشفير ملفات PDF، وتغيير كلمات المرور، والتحقق من كلمات مرور المرشحين للمستندات المشفرة.
---
يوفر Aspose.PDF for Java العديد من واجهات برمجة التطبيقات لتأمين ملفات PDF بكلمات المرور والأذونات.

## حماية مستندات PDF في جافا

توضح الأمثلة الموجودة في `ProtectDocumentExamples.java` كيفية:

1. قم بتطبيق التشفير على [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) باستخدام كلمات مرور المستخدم والمالك.
1. تقييد الأذونات باستخدام [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/).
1. اختر [خوارزمية التشفير](https://reference.aspose.com/pdf/java/com.aspose.pdf/cryptoalgorithm/) لـ [المستند] المحمي (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. فك تشفير [مستند] محمي (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بتغيير كلمات المرور الموجودة في [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اختبر كلمات المرور المرشحة باستخدام [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffileinfo/) و[المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

## تشفير ملف PDF بامتيازات مقيدة

```java
public static void encryptPassword(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    try {
        DocumentPrivilege documentPrivilege = DocumentPrivilege.getForbidAll();
        documentPrivilege.setAllowScreenReaders(true);

        document.encrypt(
                USER_PASSWORD,
                OWNER_PASSWORD,
                documentPrivilege,
                CryptoAlgorithm.AESx128,
                false);
        document.save(outputFile.toString());
    } finally {
        document.close();
    }
}
```

## تشفير ملف PDF

```java
public static void encryptPdfFile(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    try {
        document.encrypt(
                USER_PASSWORD,
                OWNER_PASSWORD,
                DocumentPrivilege.getAllowAll(),
                CryptoAlgorithm.RC4x128,
                false);
        document.save(outputFile.toString());
    } finally {
        document.close();
    }
}
```

## فك تشفير ملف PDF محمي

```java
public static void decryptPdfFile(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString(), USER_PASSWORD);
    try {
        document.decrypt();
        document.save(outputFile.toString());
    } finally {
        document.close();
    }
}
```

## تغيير كلمات المرور

```java
public static void changePassword(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString(), OWNER_PASSWORD);
    try {
        document.changePasswords(OWNER_PASSWORD, "newuser", "newowner");
        document.save(outputFile.toString());
    } finally {
        document.close();
    }
}
```

## تحديد كلمة المرور الصحيحة من القائمة

```java
public static void determineCorrectPasswordFromList(Path inputFile) {
    try (PdfFileInfo info = new PdfFileInfo(inputFile.toString())) {
        System.out.println("File is password protected: " + info.isEncrypted());
    }
    String[] passwords = {"test", "test1", "test2", "test3", USER_PASSWORD};
    for (String password : passwords) {
        try {
            Document document = new Document(inputFile.toString(), password);
            try {
                int pageCount = document.getPages().size();
                if (pageCount > 0) {
                    System.out.println("Password '" + password + "' is correct. Pages: " + pageCount);
                }
            } finally {
                document.close();
            }
        } catch (InvalidPasswordException ex) {
            System.out.println("Wrong password: " + password);
        }
    }
}
```
