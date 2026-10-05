---
title: تشفير وفك تشفير ملفات PDF في Java
linktitle: تشفير وفك تشفير ملف PDF
type: docs
weight: 70
url: /ar/java/set-privileges-encrypt-and-decrypt-pdf-file/
description: تعلم كيفية ضبط امتيازات PDF، تشفير الملفات، فك تشفير ملفات PDF المحمية، وتغيير كلمات المرور في Java.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: ضبط أذونات PDF وإدارة التشفير في Java
Abstract: تشرح هذه المقالة كيفية تأمين ملفات PDF باستخدام Aspose.PDF for Java. تغطي تشفير المستندات باستخدام كلمات مرور المستخدم والمالك، وتطبيق قيود الأذونات، وفك تشفير الملفات، وتغيير كلمات المرور، وتعيين الامتيازات مع أو بدون طرق آمنة من الاستثناءات.
---
Aspose.PDF for Java يعرض عمليات أمان PDF من خلال واجهة `PdfFileSecurity`.

## تشفير PDF باستخدام كلمات مرور المستخدم والمالك

1. أنشئ وربط الـ واجهة [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) إلى مستند PDF المصدر.
1. اضبط [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) و [KeySize](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/keysize/) الخصائص المطلوبة في المثال.
1. احفظ مستند PDF المحدث عبر [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

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

## تشفير PDF باستخدام خوارزمية محددة

`encryptPdfWithEncryptionAlgorithm` يستخدم `KeySize.x256` مع `Algorithm.AES` لتطبيق إعدادات تشفير أقوى.

## فك تشفير PDF محمي

1. أنشئ وربط الـ واجهة [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) إلى مستند PDF المصدر.
1. فك تشفير المستند المحمي باستخدام كلمة مرور المالك.
1. احفظ مستند PDF المحدث عبر [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

```java
public static void decryptPdfWithOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.decryptFile("owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}
```

تتضمن مجموعة الأمثلة أيضًا `tryDecryptPdfWithoutException`، الذي يُرجِع `false` بدلاً من إلقاء الاستثناء عندما يفشل فك التشفير.

## تغيير كلمات المرور وإعادة تعيين الأمان

ال الفئة `PdfFileSecurityExamples` توضح:

- `changeUserAndOwnerPassword` لإستبدال كلتا كلمة المرور.
- `changePasswordAndResetSecurity` لتغيير كلمات المرور وإعادة تطبيق الصلاحيات في خطوة واحدة.
- `tryChangePasswordWithoutException` لتدفق تغيير كلمة المرور غير رامي الاستثناءات.

## تعيين امتيازات المستند

لتقييد الإجراءات مثل الطباعة والنسخ:

1. أنشئ وربط الـ واجهة [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) إلى مستند PDF المصدر.
1. حدّد المطلوب [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) أذونات أو خيارات التشفير.
1. عيّن الخصائص المطلوبة في المثال.
1. احفظ مستند PDF المحدث عبر [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

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
