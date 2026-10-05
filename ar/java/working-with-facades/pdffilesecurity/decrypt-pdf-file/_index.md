---
title: فك تشفير ملف PDF
linktitle: فك تشفير ملف PDF
type: docs
weight: 20
url: /ar/java/decrypt-pdf-file/
description: تعلم كيفية فك تشفير ملف PDF في Java باستخدام واجهة PdfFileSecurity.
lastmod: "2026-10-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إزالة قيود أمان PDF باستخدام Java
Abstract: تعلم كيفية فك تشفير ملف PDF باستخدام Aspose.PDF for Java. تتضمن مجموعة أمثلة Java فك تشفير مباشر باستخدام كلمة مرور المالك وسير عمل فك تشفير بنمط try يتيح لك معالجة الفشل دون رفع استثناء.
---
## فك تشفير ملف PDF

استخدم هذا سير العمل عندما تكون لديك كلمة مرور المالك وتحتاج إلى إزالة الأمان من ملف PDF.

### الخطوات

1. أنشئ مثيلًا من `PdfFileSecurity`.
2. اربط ملف PDF المشفر بـ `bindPdf`.
3. استدعِ `decryptFile` أو `tryDecryptFile` مع كلمة مرور المالك.
4. احفظ الناتج إذا نجحت عملية فك التشفير.
5. أغلق كائن الأمان.

### أمثلة Java

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
