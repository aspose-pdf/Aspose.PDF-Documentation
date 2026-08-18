---
title: تشفير وفك تشفير ملفات PDF في جافا
linktitle: تشفير وفك تشفير ملف PDF
type: docs
weight: 70
url: /java/set-privileges-encrypt-and-decrypt-pdf-file/
description: تعرف على كيفية تعيين امتيازات PDF، وتشفير الملفات، وفك تشفير ملفات PDF المحمية، وتغيير كلمات المرور في Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بتعيين أذونات PDF وإدارة التشفير في Java
Abstract: يشرح هذا المقال كيفية تأمين ملفات PDF باستخدام Aspose.PDF لـ Java. ويغطي تشفير المستندات بكلمات مرور المستخدم والمالك، وتطبيق قيود الأذونات، وفك تشفير الملفات، وتغيير كلمات المرور، وتعيين الامتيازات باستخدام أو بدون طرق آمنة للاستثناء.
---
يعرض Aspose.PDF لـ Java عمليات أمان PDF من خلال الواجهة `PdfFileSecurity`.

## تشفير ملف PDF بكلمات مرور المستخدم والمالك

1. قم بإنشاء واجهة [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) وربطها بمستند PDF المصدر.
1. قم بتكوين خصائص [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) و[KeySize](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/keysize/) التي يتطلبها المثال.
1. احفظ مستند PDF المحدث من خلال [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

```java
public static void encryptPdfWithUserOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.encryptFile("user_password", "owner_password", privilege, KeySize.x128);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}
```

## تشفير ملف PDF باستخدام خوارزمية محددة

يستخدم `encryptPdfWithEncryptionAlgorithm` `KeySize.x256` مع `Algorithm.AES` لتطبيق إعدادات تشفير أقوى.

## فك تشفير ملف PDF محمي

1. قم بإنشاء واجهة [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) وربطها بمستند PDF المصدر.
1. قم بفك تشفير المستند المحمي بكلمة مرور المالك.
1. احفظ مستند PDF المحدث من خلال [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

```java
public static void decryptPdfWithOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.decryptFile("owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}
```

تتضمن مجموعة الأمثلة أيضًا `tryDecryptPdfWithoutException`، والتي تُرجع `false` بدلاً من الرمي عند فشل فك التشفير.

## تغيير كلمات المرور وإعادة ضبط الأمان

يوضح الفصل `PdfFileSecurityExamples`:

- `changeUserAndOwnerPassword` لاستبدال كلمتي المرور.
- `changePasswordAndResetSecurity` لتغيير كلمات المرور وإعادة تطبيق الامتيازات في خطوة واحدة.
- `tryChangePasswordWithoutException` لتدفق تغيير كلمة المرور بدون طرح.

## تعيين امتيازات المستند

لتقييد إجراءات مثل الطباعة والنسخ:

1. قم بإنشاء واجهة [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) وربطها بمستند PDF المصدر.
1. قم بتعيين أذونات [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) المطلوبة أو خيارات التشفير.
1. قم بتعيين الخصائص التي يتطلبها المثال.
1. احفظ مستند PDF المحدث من خلال [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

```java
public static void setPdfPrivilegesWithPasswords(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    privilege.setAllowCopy(false);
    fileSecurity.setPrivilege("user_password", "owner_password", privilege);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}
```
