---
title: تحويل XML إلى PDF
linktitle: تحويل XML إلى PDF
type: docs
weight: 320
url: /ar/androidjava/convert-xml-to-pdf/
lastmod: "2026-06-30"
description: مكتبة Aspose.PDF تقدم عدة طرق لتحويل XML إلى PDF. يمكنك استخدام XslFoLoadOptions أو القيام بذلك بهيكل ملف غير صحيح.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

جرّب عبر الإنترنت. يمكنك التحقق من جودة تحويل Aspose.PDF وعرض النتائج عبر الإنترنت على هذا الرابط [products.aspose.app/pdf/conversion/xml-to-pdf](https://products.aspose.app/pdf/conversion/xml-to-pdf)

{{% /alert %}}

تنسيق XML يُستخدم لتخزين البيانات المُنظمة. هناك عدة طرق للتحويل <abbr title="Extensible Markup Language">XML</abbr> إلى PDF في Aspose.PDF.

فكِّر في خيار استخدام مستند XML مبنٍ على معيار XSL-FO.

## تحويل XSL-FO إلى PDF

يمكن تنفيذ تحويل ملفات XSL-FO إلى PDF باستخدام [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) كائن مع [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions),  لكن في بعض الأحيان قد تواجه بنية ملف غير صحيحة. 

```java
// Convert XML to PDF
    public void convertXMLtoPDF() {
        // Initialize document object
        String pdfDocumentFileName = new File(fileStorage,"XML-to-PDF.pdf").toString();
        String xmlDocumentFileName = new File(fileStorage,"Conversion/employees.xml").toString();
        String xsltDocumentFileName = new File(fileStorage, "Conversion/employees.xslt").toString();

        try {
            XslFoLoadOptions options = new XslFoLoadOptions(xsltDocumentFileName);
            document = new Document(xmlDocumentFileName,options);
            // Save resultant PDF file
            document.save(pdfDocumentFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }    
    ```
    
