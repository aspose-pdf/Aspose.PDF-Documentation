---
title: قم بتوقيع مستندات PDF من البطاقة الذكية في Java
linktitle: توقيع PDF بالبطاقة الذكية
type: docs
weight: 30
url: /java/sign-pdf-document-from-smart-card/
description: قم بمراجعة تغطية مثال Java الحالية لتوقيع PDF المستند إلى الشهادة في Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تغطية توقيع PDF على أساس الشهادة في مجموعة أمثلة Java الحالية
Abstract: تصف هذه الصفحة النطاق الحالي لأمثلة التوقيع المتوفرة في شجرة مصدر وثائق Java. يتضمن المستودع أمثلة لتوقيع PDF مستندة إلى الشهادات باستخدام بيانات اعتماد PFX أو PKCS7، لكنه لا يتضمن حاليًا مثالًا مخصصًا لمخزن شهادات البطاقة الذكية لـ Java.
---
لا يتضمن مستودع Java الحالي مثالًا مخصصًا لتوقيع البطاقة الذكية المدعومة من المصدر ضمن `facades/pdffilesignature`، لكن سير العمل التالي يعرض نمط واجهة برمجة التطبيقات النموذجي لتوقيع ملف PDF بشهادة محددة من مخزن شهادات محلي.

## قم بتوقيع مستند PDF من البطاقة الذكية

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء واجهة [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) وربط مستند PDF المصدر.
1. استرد الشهادة المحلية وقم بإنشاء [ExternalSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/) المطلوب.
1. قم بتكوين مظهر التوقيع المرئي والهدف [المستطيل](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).
1. قم بتطبيق التوقيع على مستند PDF من خلال [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
1. احفظ مستند PDF المحدث.
1. قم بربط المستند الذي تم تحميله بالواجهة [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) باستخدام `bindPdf(...)`.
1. قم باسترداد الشهادة المحلية التي تمثل بيانات اعتماد البطاقة الذكية عن طريق الاتصال بـ `getLocalCertificate()`.
1. تحقق مما إذا تم العثور على الشهادة. إذا لم يكن الأمر كذلك، فاحفظ ملف الإخراج الذي لم يتغير وأوقف سير العمل.
1. قم بإنشاء [توقيع خارجي](https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/) من الشهادة المحددة.
1. قم بتعيين صورة مظهر التوقيع المرئي باستخدام `setSignatureAppearance(...)`.
1. اتصل بـ `sign(...)` مع الصفحة المستهدفة والسبب وجهة الاتصال والموقع وعلامة الرؤية والتوقيع [المستطيل](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) وكائن التوقيع الخارجي.
1. احفظ ملف PDF الموقع في مسار الإخراج.

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
