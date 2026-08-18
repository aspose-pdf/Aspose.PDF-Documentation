---
title: إنشاء ملف PDF متوافق مع PDF/3-A وإرفاق فاتورة ZUGFeRD في Java
linktitle: إرفاق ZUGFeRD إلى PDF
type: docs
weight: 10
url: /java/attach-zugferd/
description: تعرف على كيفية إرفاق XML لفاتورة ZUGFeRD بملف PDF وتحويله إلى PDF/A-3A في Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بإرفاق فاتورة ZUGFeRD بتنسيق XML إلى مستند PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية إنشاء مستند فاتورة متوافق مع PDF/A-3A باستخدام Aspose.PDF لـ Java. ويغطي إرفاق فاتورة XML كملف مضمن، وتعيين نوع MIME وعلاقة الملف المرتبط، وتحويل PDF إلى PDF/A-3A، وحفظ المستند النهائي الجاهز لـ ZUGFeRD.
---
استخدم واجهات برمجة التطبيقات `Document` و`FileSpecification` عندما تحتاج إلى حزم فاتورة XML داخل ملف PDF لسير العمل بنمط ZUGFeRD.

## قم بإرفاق فاتورة ZUGFeRD بتنسيق XML إلى ملف PDF

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) لملف فاتورة XML.
1. قم بتعيين بيانات تعريف الملف المضمنة، بما في ذلك نوع MIME و[AFRelationship](https://reference.aspose.com/pdf/java/com.aspose.pdf/afrelationship/).
1. أضف [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) إلى مجموعة الملفات المضمنة في المستند.
1. قم بتحويل المستند إلى [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_A_3A`.
1. احفظ ملف PDF المحدث [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void attachInvoiceZugferdFormat(Path inputFile, Path invoiceFile, Path outputFile) {
        try (Document document = new Document(inputFile.toString())) {
            String description = "Invoice metadata conforming to ZUGFeRD standard";
            FileSpecification fileSpecification = new FileSpecification(invoiceFile.toString(), description);

            fileSpecification.setMIMEType("text/xml");
            fileSpecification.setAFRelationship(AFRelationship.Alternative);

            document.getEmbeddedFiles().add("factur", fileSpecification);

            String outputFileName = outputFile.toString();
            String logPath = outputFileName.replace(".pdf", "_log.xml");
            document.convert(logPath, PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);
            document.save(outputFile.toString());
        }
        System.out.println("ZUGFeRD invoice attached to " + outputFile);
    }
```
