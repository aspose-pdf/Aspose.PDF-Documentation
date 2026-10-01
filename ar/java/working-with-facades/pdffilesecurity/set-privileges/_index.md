---
title: تعيين الصلاحيات على ملف PDF موجود
linktitle: تعيين الصلاحيات على ملف PDF موجود
type: docs
weight: 40
url: /ar/java/set-privileges/
description: تعلم كيفية تعيين صلاحيات PDF في Java باستخدام واجهة PdfFileSecurity.
lastmod: "2026-10-01"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إدارة أذونات PDF وضوابط الوصول في Java
Abstract: تعلم كيفية التحكم في أذونات PDF باستخدام Aspose.PDF for Java. تتضمن مجموعة الأمثلة في Java تطبيق الامتيازات بدون كلمات مرور، وتطبيق الامتيازات باستخدام كلمات مرور المستخدم والمالك، وسير عمل لتحديث الامتيازات بأسلوب try يُعيد إشارة نجاح.
---
## تعيين الصلاحيات على ملف PDF موجود

استخدم هذا سير العمل عندما تحتاج إلى تغيير ما يمكن للمستخدمين القيام به مع ملف PDF موجود

### الخطوات

1. إنشاء `PdfFileSecurity` مثال.
2. ربط ملف PDF المصدر بـ `bindPdf`.
3. إنشاء `DocumentPrivilege` الكائن وتكوين الإجراءات المسموح بها.
4. اتصل بالملائم `setPrivilege` أو `trySetPrivilege` تحميل زائد.
5. احفظ النتيجة إذا نجح التحديث، ثم أغلق الكائن.

### أمثلة Java

```java
public static void setPdfPrivilegesWithoutPasswords(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.setPrivilege(privilege);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

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

public static void trySetPdfPrivilegesWithoutException(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    if (fileSecurity.trySetPrivilege("user_password", "owner_password", privilege)) {
        fileSecurity.save(outputFile.toString());
    } else {
        System.out.println("Setting privileges failed. Check passwords or document state.");
    }
    fileSecurity.close();
}
```
