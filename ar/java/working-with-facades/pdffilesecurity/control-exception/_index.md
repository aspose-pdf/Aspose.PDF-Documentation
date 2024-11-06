---
title: التحكم في استثناء ملف PDF
type: docs
weight: 30
url: ar/java/control-exception/
description: يشرح هذا الموضوع كيفية التحكم في الاستثناءات في ملف PDF باستخدام فئة PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

تسمح لك فئة [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) بالتحكم في الاستثناءات. للقيام بذلك، تحتاج إلى ضبط [setAllowExceptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#setAllowExceptions-boolean-) على false أو true. إذا قمت بضبط العملية على false، فإن نتيجة [decryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#decryptFile-java.lang.String-) ستعيد true أو false اعتمادًا على صحة كلمة المرور.

إذا قمت بضبط [setAllowExceptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#setAllowExceptions-boolean-) على true، يمكنك الحصول على نتيجة العملية باستخدام مشغل try-catch.

```java
    public static void ControlExceptionPDFFile() {
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample_encrypted.pdf");
        fileSecurity.setAllowExceptions(false);
        // فك تشفير مستند PDF

        if (!fileSecurity.decryptFile("IncorrectPassword")) {
            System.out.println("هناك خطأ ما...");
            System.out.println("آخر استثناء: " + fileSecurity.getLastException().getMessage());
        }
        fileSecurity.save(_dataDir + "sample_decrtypted.pdf");
    }
```