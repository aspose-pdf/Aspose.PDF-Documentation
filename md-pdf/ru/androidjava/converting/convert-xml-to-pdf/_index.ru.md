---
title: Convert XML to PDF 
linktitle: Convert XML to PDF
type: docs
weight: 320
url: /androidjava/convert-xml-to-pdf/
lastmod: "2021-06-05"
description: Библиотека Aspose.PDF предлагает несколько способов преобразования XML в PDF. Вы можете использовать XslFoLoadOptions или сделать это с некорректной структурой файла.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Попробуйте онлайн. Вы можете проверить качество преобразования Aspose.PDF и просмотреть результаты онлайн по этой ссылке [products.aspose.app/pdf/conversion/xml-to-pdf](https://products.aspose.app/pdf/conversion/xml-to-pdf)

{{% /alert %}}

Формат XML используется для хранения структурированных данных. Существует несколько способов преобразования <abbr title="Extensible Markup Language">XML</abbr> в PDF в Aspose.PDF.

Рассмотрим вариант использования XML-документа на основе стандарта XSL-FO.

## Преобразование XSL-FO в PDF

Преобразование файлов XSL-FO в PDF можно осуществить с помощью объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) с [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions), но иногда можно столкнуться с некорректной структурой файла.
 
// Преобразование XML в PDF
    public void convertXMLtoPDF() {
        // Инициализация объекта документа
        String pdfDocumentFileName = new File(fileStorage,"XML-to-PDF.pdf").toString();
        String xmlDocumentFileName = new File(fileStorage,"Conversion/employees.xml").toString();
        String xsltDocumentFileName = new File(fileStorage, "Conversion/employees.xslt").toString();

        try {
            XslFoLoadOptions options = new XslFoLoadOptions(xsltDocumentFileName);
            document = new Document(xmlDocumentFileName,options);
            // Сохранить результирующий PDF файл
            document.save(pdfDocumentFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }    
    ```