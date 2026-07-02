---
title: 将 XML 转换为 PDF
linktitle: 将 XML 转换为 PDF
type: docs
weight: 320
url: /zh/androidjava/convert-xml-to-pdf/
lastmod: "2026-07-01"
description: Aspose.PDF 库提供了多种将 XML 转换为 PDF 的方法。您可以使用 XslFoLoadOptions，或者在文件结构不正确的情况下执行此操作。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

在线尝试。您可以在此链接检查 Aspose.PDF 转换的质量并在线查看结果。 [products.aspose.app/pdf/conversion/xml-to-pdf](https://products.aspose.app/pdf/conversion/xml-to-pdf)

{{% /alert %}}

XML 格式用于存储结构化数据。有几种方法可以转换 <abbr title="Extensible Markup Language">XML</abbr> 在 Aspose.PDF 中转换为 PDF。

考虑使用基于 XSL-FO 标准的 XML 文档选项。

## 将 XSL-FO 转换为 PDF

可以使用以下方式实现 XSL-FO 文件到 PDF 的转换 [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) 对象为 [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions),  但有时你可能会遇到文件结构不正确的情况。 

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
    
