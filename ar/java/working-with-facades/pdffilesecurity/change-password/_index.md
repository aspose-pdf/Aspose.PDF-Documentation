---
title: تغيير كلمة مرور ملف PDF
linktitle: تغيير كلمة مرور ملف PDF
type: docs
weight: 10
url: /ar/java/change-password/
description: تعرف على كيفية تغيير كلمات مرور PDF في Java باستخدام واجهة PdfFileSecurity.
lastmod: "2026-10-01"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تحديث كلمات مرور المستخدم والمالك لملف PDF في Java
Abstract: تعرف على كيفية تغيير كلمات مرور PDF باستخدام Aspose.PDF for Java. مجموعة أمثلة Java تغطي تغيير كلمات مرور المستخدم والمالك مباشرةً، وتغيير كلمات المرور أثناء إعادة ضبط إعدادات الأمان، بالإضافة إلى سير عمل لتغيير كلمة المرور بنمط try يُعيد علامة نجاح.
---
## تغيير كلمة مرور ملف PDF

استخدم `PdfFileSecurity` عندما تحتاج إلى تدوير بيانات الاعتماد على PDF مؤمن بالفعل.

### خطوات

1. إنشاء `PdfFileSecurity` مثيل.
2. ربط ملف PDF المحمي بـ `bindPdf`.
3. استدعِ المناسب `changePassword` تحميل زائد، اعتمادًا على ما إذا كنت تريد أيضًا إعادة تعيين الامتيازات وحجم المفتاح.
4. احفظ الملف المحدث وأغلق كائن الأمان.

### أمثلة Java

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
