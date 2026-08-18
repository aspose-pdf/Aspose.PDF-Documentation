---
title: تغيير كلمة المرور لملف PDF
linktitle: تغيير كلمة المرور لملف PDF
type: docs
weight: 10
url: /java/change-password/
description: تعرف على كيفية تغيير كلمات مرور PDF في Java باستخدام واجهة PdfFileSecurity.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بتحديث كلمات مرور مستخدم ومالك PDF في Java
Abstract: تعرف على كيفية تغيير كلمات مرور PDF باستخدام Aspose.PDF لـ Java. تغطي مجموعة أمثلة Java تغيير كلمات مرور المستخدم والمالك مباشرةً، وتغيير كلمات المرور أثناء إعادة تعيين إعدادات الأمان، وسير عمل تغيير كلمة المرور على نمط المحاولة الذي يُرجع علامة نجاح.
---
## تغيير كلمة المرور لملف PDF

استخدم `PdfFileSecurity` عندما تحتاج إلى تدوير بيانات الاعتماد على ملف PDF مؤمن بالفعل.

### خطوات

1. قم بإنشاء مثيل `PdfFileSecurity`.
2. قم بربط ملف PDF الآمن باستخدام `bindPdf`.
3. اتصل بالحمل الزائد `changePassword` المناسب، اعتمادًا على ما إذا كنت تريد أيضًا إعادة تعيين الامتيازات وحجم المفتاح.
4. احفظ الملف المحدث وأغلق كائن الأمان.

### أمثلة جافا

```java
public static void changeUserAndOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.changePassword("owner_password", "new_user_password", "new_owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void changePasswordAndResetSecurity(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.changePassword("owner_password", "new_user_password", "new_owner_password", privilege, KeySize.x128);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void tryChangePasswordWithoutException(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    if (fileSecurity.tryChangePassword("owner_password", "new_user_password", "new_owner_password")) {
        fileSecurity.save(outputFile.toString());
    } else {
        System.out.println("Password change failed. Check owner password or document security.");
    }
    fileSecurity.close();
}
```
