---
title: تشفير ملف PDF
linktitle: تشفير ملف PDF
type: docs
weight: 30
url: /ar/java/encrypt-pdf-file/
description: تعلم كيفية تشفير ملف PDF وتكوين الأذونات في Java باستخدام واجهة PdfFileSecurity.
lastmod: "2026-10-01"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تشفير ملفات PDF وتحديد أذونات المستخدم في Java
Abstract: تعلم كيفية تشفير ملف PDF باستخدام Aspose.PDF for Java. تغطي مجموعة أمثلة Java التشفير القائم على كلمة المرور مع امتيازات مقيدة، التشفير الموجه بالأذونات، والتشفير القائم على AES بمفتاح بحجم 256 بت.
---
## تشفير ملف PDF

استخدام `PdfFileSecurity` عندما تحتاج إلى حماية ملف PDF بكلمات مرور وقواعد الامتياز.

### الخطوات

1. إنشاء `PdfFileSecurity` مثال.
2. ربط ملف PDF المصدر بـ `bindPdf`.
3. بناء `DocumentPrivilege` كائن يطابق الإجراءات المسموح بها.
4. استدعِ المناسب `encryptFile` تحميل زائد لحجم المفتاح والخوارزمية التي تحتاجها.
5. احفظ الملف المؤمَّن وأغلق الكائن.

### أمثلة Java

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

public static void encryptPdfWithPermissions(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getAllowAll();
    privilege.setAllowPrint(false);
    privilege.setAllowCopy(false);
    fileSecurity.encryptFile("user_password", "owner_password", privilege, KeySize.x128);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void encryptPdfWithEncryptionAlgorithm(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.encryptFile("user_password", "owner_password", privilege, KeySize.x256, Algorithm.AES);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}
```
