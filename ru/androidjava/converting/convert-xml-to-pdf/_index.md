---
title: Преобразовать XML в PDF
linktitle: Преобразовать XML в PDF
type: docs
weight: 320
url: /ru/androidjava/convert-xml-to-pdf/
lastmod: "2026-07-01"
description: Библиотека Aspose.PDF предлагает несколько способов преобразования XML в PDF. Вы можете использовать XslFoLoadOptions или выполнить это с некорректной структурой файла.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Попробуйте онлайн. Вы можете проверить качество конвертации Aspose.PDF и просмотреть результаты онлайн по этой ссылке [products.aspose.app/pdf/conversion/xml-to-pdf](https://products.aspose.app/pdf/conversion/xml-to-pdf)

{{% /alert %}}

Формат XML используется для хранения структурированных данных. Существует несколько способов конвертации. <abbr title="Extensible Markup Language">XML</abbr> в PDF в Aspose.PDF.

Рассмотрите вариант использования XML-документа, основанного на стандарте XSL-FO.

## Преобразовать XSL-FO в PDF

Преобразование XSL-FO файлов в PDF может быть реализовано с использованием [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) объект с [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions),  но иногда вы можете столкнуться с некорректной структурой файла. 

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
    
