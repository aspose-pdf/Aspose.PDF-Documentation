---
title: فك تشفير ملف PDF
linktitle: فك تشفير ملف PDF
type: docs
weight: 20
url: /java/decrypt-pdf-file/
description: تعرف على كيفية فك تشفير ملف PDF في Java باستخدام واجهة PdfFileSecurity.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بإزالة قيود أمان PDF باستخدام Java
Abstract: تعرف على كيفية فك تشفير ملف PDF باستخدام Aspose.PDF لـ Java. تتضمن مجموعة أمثلة Java فك التشفير المباشر لكلمة مرور المالك وسير عمل فك تشفير نمط المحاولة الذي يتيح لك التعامل مع الفشل دون إثارة استثناء.
---
## فك تشفير ملف PDF

استخدم سير العمل هذا عندما يكون لديك كلمة مرور المالك وتحتاج إلى إزالة الأمان من ملف PDF.

### خطوات

1. قم بإنشاء مثيل `PdfFileSecurity`.
2. قم بربط ملف PDF المشفر باستخدام `bindPdf`.
3. اتصل بـ `decryptFile` أو `tryDecryptFile` باستخدام كلمة مرور المالك.
4. احفظ الإخراج في حالة نجاح فك التشفير.
5. قم بإغلاق كائن الأمان.

### أمثلة جافا

```java
public static void decryptPdfWithOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.decryptFile("owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void tryDecryptPdfWithoutException(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    if (fileSecurity.tryDecryptFile("owner_password")) {
        fileSecurity.save(outputFile.toString());
    } else {
        System.out.println("Decryption failed. Check password or document security.");
    }
    fileSecurity.close();
}
```
