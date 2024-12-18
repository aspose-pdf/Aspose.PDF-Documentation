---
title: تحويل XML إلى PDF
linktitle: تحويل XML إلى PDF
type: docs
weight: 320
url: /ar/androidjava/convert-xml-to-pdf/
lastmod: "2021-06-05"
description: مكتبة Aspose.PDF تقدم عدة طرق لتحويل XML إلى PDF. يمكنك استخدام XslFoLoadOptions أو القيام بذلك مع هيكل ملف غير صحيح.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

جرب عبر الإنترنت. يمكنك التحقق من جودة تحويل Aspose.PDF وعرض النتائج عبر الإنترنت على هذا الرابط [products.aspose.app/pdf/conversion/xml-to-pdf](https://products.aspose.app/pdf/conversion/xml-to-pdf)

{{% /alert %}}

يُستخدم تنسيق XML لتخزين البيانات المهيكلة. هناك عدة طرق لتحويل <abbr title="Extensible Markup Language">XML</abbr> إلى PDF في Aspose.PDF.

اعتبر الخيار باستخدام مستند XML بناءً على معيار XSL-FO.

## تحويل XSL-FO إلى PDF

يمكن تنفيذ تحويل ملفات XSL-FO إلى PDF باستخدام كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) مع [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions)، ولكن في بعض الأحيان قد تواجه هيكل ملف غير صحيح.
 
// تحويل XML إلى PDF
    public void convertXMLtoPDF() {
        // تهيئة كائن الوثيقة
        String pdfDocumentFileName = new File(fileStorage,"XML-to-PDF.pdf").toString();
        String xmlDocumentFileName = new File(fileStorage,"Conversion/employees.xml").toString();
        String xsltDocumentFileName = new File(fileStorage, "Conversion/employees.xslt").toString();

        try {
            XslFoLoadOptions options = new XslFoLoadOptions(xsltDocumentFileName);
            document = new Document(xmlDocumentFileName,options);
            // حفظ ملف PDF الناتج
            document.save(pdfDocumentFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }    
    ```