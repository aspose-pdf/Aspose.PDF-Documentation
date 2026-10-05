---
title: إنشاء ملف PDF متوافق مع PDF/3-A وإرفاق فاتورة ZUGFeRD باستخدام Java
linktitle: إرفاق ZUGFeRD إلى PDF
type: docs
weight: 10
url: /ar/java/attach-zugferd/
description: تعلم كيفية إرفاق ملف XML لفاتورة ZUGFeRD إلى ملف PDF وتحويله إلى PDF/A-3A باستخدام Java.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إرفاق ملف XML لفاتورة ZUGFeRD إلى مستند PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية إنشاء مستند فاتورة متوافق مع PDF/A-3A باستخدام Aspose.PDF for Java. تغطي إرفاق ملف XML للفاتورة كملف مضمن، ضبط نوع MIME وعلاقة الملف المرتبط، تحويل ملف PDF إلى PDF/A-3A، وحفظ المستند النهائي جاهزًا لـ ZUGFeRD.
---
استخدم `Document` و `FileSpecification` واجهات برمجة التطبيقات عندما تحتاج إلى تعبئة XML الفاتورة داخل ملف PDF لتدفقات عمل بنمط ZUGFeRD.

## إرفاق ملف XML الفاتورة ZUGFeRD إلى PDF

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) لملف الفاتورة XML..
1. عيّن بيانات تعريف الملف المدمج، بما في ذلك نوع MIME و [AFRelationship](https://reference.aspose.com/pdf/java/com.aspose.pdf/afrelationship/).
1. أضف [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) إلى مجموعة ملفات المستند المدمجة.
1. حوّل المستند إلى [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_A_3A`.
1. احفظ ملف PDF المحدث [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
