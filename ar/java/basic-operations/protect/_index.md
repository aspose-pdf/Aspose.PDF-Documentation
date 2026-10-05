---
title: حماية ملفات PDF في Java
linktitle: تشفير وفك تشفير ملف PDF
type: docs
weight: 70
url: /ar/java/protect-pdf-file/
description: تعرّف على كيفية تشفير ملفات PDF، فك تشفير المستندات المحمية، تغيير كلمات المرور، وفحص حماية كلمة المرور في Java.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تعيين أذونات PDF وإدارة التشفير في Java
Abstract: تشرح هذه المقالة كيفية حماية ملفات PDF في Java باستخدام Aspose.PDF. تغطي تطبيق كلمات مرور المستخدم والمالك، وتعيين امتيازات المستند، وتشفير وفك تشفير ملفات PDF، وتغيير كلمات المرور، والتحقق من كلمات المرور المرشحة للوثائق المشفرة.
---
يوفر Aspose.PDF for Java عدة واجهات برمجة تطبيقات لتأمين ملفات PDF باستخدام كلمات المرور والإذن.

## حماية مستندات PDF في Java

الأمثلة في `ProtectDocumentExamples.java` إظهار كيفية:

1. طبّق التشفير على [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مع كلمات مرور المستخدم والمالك.
1. قيّد الأذونات باستخدام [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/).
1. اختر [CryptoAlgorithm](https://reference.aspose.com/pdf/java/com.aspose.pdf/cryptoalgorithm/) للمحمى [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. فك تشفير محمي [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. تغيير كلمات المرور الحالية على [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اختبر كلمات المرور المرشحة باستخدام [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffileinfo/) و [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

## تشفير ملف PDF مع امتيازات مقيدة

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
