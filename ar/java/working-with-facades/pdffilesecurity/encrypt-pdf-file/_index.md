---
title: تشفير ملف PDF
linktitle: تشفير ملف PDF
type: docs
weight: 30
url: /java/encrypt-pdf-file/
description: تعرف على كيفية تشفير ملف PDF وتكوين الأذونات في Java باستخدام واجهة PdfFileSecurity.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تشفير ملفات PDF وتحديد أذونات المستخدم في Java
Abstract: تعرف على كيفية تشفير ملف PDF باستخدام Aspose.PDF لـ Java. تغطي مجموعة أمثلة Java التشفير المستند إلى كلمة المرور مع امتيازات مقيدة، والتشفير الذي يركز على الأذونات، والتشفير المستند إلى AES بحجم مفتاح 256 بت.
---
## تشفير ملف PDF

استخدم `PdfFileSecurity` عندما تحتاج إلى حماية ملف PDF باستخدام كلمات المرور وقواعد الامتياز.

### خطوات

1. قم بإنشاء مثيل `PdfFileSecurity`.
2. قم بربط ملف PDF المصدر بـ `bindPdf`.
3. قم بإنشاء كائن `DocumentPrivilege` يطابق الإجراءات المسموح بها.
4. اتصل بالحمل الزائد `encryptFile` المناسب لحجم المفتاح والخوارزمية التي تحتاجها.
5. احفظ الملف الآمن وأغلق الكائن.

### أمثلة جافا

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
