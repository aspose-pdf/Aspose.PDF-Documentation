---
title: توقيع مستندات PDF من بطاقة ذكية في Java
linktitle: توقيع PDF باستخدام بطاقة ذكية
type: docs
weight: 30
url: /ar/java/sign-pdf-document-from-smart-card/
description: مراجعة تغطية أمثلة Java الحالية لتوقيع PDF القائم على الشهادة في Aspose.PDF.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تغطية توقيع PDF القائم على الشهادة في مجموعة أمثلة Java الحالية
Abstract: تصفّح هذه الصفحة النطاق الحالي لأمثلة التوقيع المتاحة في شجرة مصدر وثائق Java. يحتوي المستودع على أمثلة توقيع PDF القائم على الشهادة باستخدام بيانات اعتماد PFX أو PKCS7، لكنه لا يتضمن حاليًا مثالًا مخصصًا لمخزن شهادات البطاقة الذكية لـ Java.
---
المستودع الحالي لجافا لا يتضمن مثالًا مخصصًا لتوقيع بطاقة ذكية مدعوم بالمصدر تحت `facades/pdffilesignature`، ولكن سير العمل التالي يُظهر نمط API النموذجي لتوقيع ملف PDF باستخدام شهادة مختارة من مخزن الشهادات المحلي.

## توقيع مستند PDF باستخدام بطاقة ذكية

1. افتح PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) facade وربط مستند PDF المصدر.
1. استرجع الشهادة المحلية وأنشئ المطلوب [ExternalSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/).
1. هيّئ مظهر التوقيع البصري والهدف [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).
1. طبّق التوقيع على مستند PDF عبر [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
1. احفظ مستند PDF المحدث.
1. اربط المستند المحمَّل بـ واجهة [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) مع `bindPdf(...)`.
1. استرجع الشهادة المحلية التي تمثل اعتماد البطاقة الذكية عن طريق الاستدعاء `getLocalCertificate()`.
1. تحقّق مما إذا تم العثور على شهادة. إذا لم يتم العثور عليها، احفظ ملف الإخراج غير المعدل وأوقف سير العمل.
1. أنشئ كائنًا من الفئة [ExternalSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/) من الشهادة المحددة.
1. عيّن صورة مظهر التوقيع البصري باستخدام `setSignatureAppearance(...)`.
1. استدعِ `sign(...)` مع الصفحة المستهدفة، السبب، جهة الاتصال، الموقع، علامة الرؤية، التوقيع [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/)، وكائن التوقيع الخارجي.
1. احفظ ملف PDF الموقع إلى مسار الإخراج.

```java
public static void signWithSmartCard(Path inputFile, Path outputFile, Path pngFile) {
    try (Document document = new Document(inputFile.toString());
            PdfFileSignature pdfSignature = new PdfFileSignature()) {
        pdfSignature.bindPdf(document);
        X509Certificate2 selectedCertificate = getLocalCertificate();
        if (selectedCertificate == null) {
            System.out.println("Local certificate was not found.");
            document.save(outputFile.toString());
            return;
        }

        ExternalSignature externalSignature = new ExternalSignature(selectedCertificate, null);
        pdfSignature.setSignatureAppearance(pngFile.toString());
        pdfSignature.sign(1, "Reason", "Contact", "Location", true,
                new java.awt.Rectangle(100, 100, 200, 200), externalSignature);
        pdfSignature.save(outputFile.toString());
    }
}
```
