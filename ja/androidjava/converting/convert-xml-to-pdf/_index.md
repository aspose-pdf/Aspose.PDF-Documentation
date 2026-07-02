---
title: XML を PDF に変換
linktitle: XML を PDF に変換
type: docs
weight: 320
url: /ja/androidjava/convert-xml-to-pdf/
lastmod: "2026-07-01"
description: Aspose.PDF ライブラリは、XML を PDF に変換するいくつかの方法を提供しています。XslFoLoadOptions を使用するか、誤ったファイル構造でこれを行うことができます。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

オンラインで試してください。Aspose.PDF の変換品質を確認し、結果をオンラインでこのリンクで表示できます。 [products.aspose.app/pdf/conversion/xml-to-pdf](https://products.aspose.app/pdf/conversion/xml-to-pdf)

{{% /alert %}}

構造化データを保存するために使用されるXML形式です。Aspose.PDFで<abbr title="Extensible Markup Language">XML</abbr>をPDFに変換する方法はいくつかあります。

XSL-FO標準に基づくXMLドキュメントを使用するオプションを検討してください。

## XSL-FOをPDFに変換する

XSL-FOファイルをPDFに変換することは、次を使用して実装できます。 [ドキュメント](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) オブジェクトとともに [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions), しかし時々、誤ったファイル構造に遭遇することがあります。 

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
    
