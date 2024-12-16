---
title: Convert XML to PDF 
linktitle: Convert XML to PDF
type: docs
weight: 320
url: /zh/androidjava/convert-xml-to-pdf/
lastmod: "2021-06-05"
description: Aspose.PDF library presents several ways to convert XML to PDF. You can use the XslFoLoadOptions or do this with an incorrect file structure.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

在线试用。您可以在此链接上在线检查 Aspose.PDF 转换的质量并查看结果 [products.aspose.app/pdf/conversion/xml-to-pdf](https://products.aspose.app/pdf/conversion/xml-to-pdf)

{{% /alert %}}

XML 格式用于存储结构化数据。在 Aspose.PDF 中有几种将 <abbr title="Extensible Markup Language">XML</abbr> 转换为 PDF 的方法。

考虑使用基于 XSL-FO 标准的 XML 文档的选项。

## 将 XSL-FO 转换为 PDF

使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) 对象和 [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions) 可以实现 XSL-FO 文件到 PDF 的转换，但有时您可能会遇到文件结构不正确的问题。
 
// 将 XML 转换为 PDF
    public void convertXMLtoPDF() {
        // 初始化文档对象
        String pdfDocumentFileName = new File(fileStorage,"XML-to-PDF.pdf").toString();
        String xmlDocumentFileName = new File(fileStorage,"Conversion/employees.xml").toString();
        String xsltDocumentFileName = new File(fileStorage, "Conversion/employees.xslt").toString();

        try {
            XslFoLoadOptions options = new XslFoLoadOptions(xsltDocumentFileName);
            document = new Document(xmlDocumentFileName, options);
            // 保存生成的 PDF 文件
            document.save(pdfDocumentFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```