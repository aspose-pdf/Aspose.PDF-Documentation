---
title: قم بتعيين الامتيازات على ملف PDF موجود
linktitle: قم بتعيين الامتيازات على ملف PDF موجود
type: docs
weight: 40
url: /java/set-privileges/
description: تعرف على كيفية تعيين امتيازات PDF في Java باستخدام واجهة PdfFileSecurity.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إدارة أذونات PDF وعناصر التحكم في الوصول في Java
Abstract: تعرف على كيفية التحكم في أذونات PDF باستخدام Aspose.PDF لـ Java. تغطي مجموعة أمثلة Java تطبيق الامتيازات بدون كلمات مرور، وتطبيق الامتيازات باستخدام كلمات مرور المستخدم والمالك، وسير عمل تحديث امتيازات نمط المحاولة الذي يُرجع علامة نجاح.
---
## قم بتعيين الامتيازات على ملف PDF موجود

استخدم سير العمل هذا عندما تحتاج إلى تغيير ما يمكن للمستخدمين فعله باستخدام ملف PDF موجود.

### خطوات

1. قم بإنشاء مثيل `PdfFileSecurity`.
2. قم بربط ملف PDF المصدر بـ `bindPdf`.
3. قم بإنشاء كائن `DocumentPrivilege` وقم بتكوين الإجراءات المسموح بها.
4. اتصل بالحمل الزائد `setPrivilege` أو `trySetPrivilege` المناسب.
5. احفظ النتيجة إذا نجح التحديث، ثم أغلق الكائن.

### أمثلة جافا

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
