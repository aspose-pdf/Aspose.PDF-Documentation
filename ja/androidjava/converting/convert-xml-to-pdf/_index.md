---
title: XMLをPDFに変換 
linktitle: XMLをPDFに変換
type: docs
weight: 320
url: ja/androidjava/convert-xml-to-pdf/
lastmod: "2021-06-05"
description: Aspose.PDFライブラリは、XMLをPDFに変換するためのいくつかの方法を提供します。XslFoLoadOptionsを使用するか、不正なファイル構造でこれを行うことができます。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

オンラインで試してみてください。Aspose.PDFの変換品質をチェックし、このリンクで結果をオンラインで確認できます [products.aspose.app/pdf/conversion/xml-to-pdf](https://products.aspose.app/pdf/conversion/xml-to-pdf)

{{% /alert %}}

XML形式は構造化データを保存するために使用されます。Aspose.PDFでは、<abbr title="Extensible Markup Language">XML</abbr>をPDFに変換するいくつかの方法があります。

XSL-FO標準に基づいたXMLドキュメントを使用するオプションを考慮してください。

## XSL-FOをPDFに変換

XSL-FOファイルのPDFへの変換は、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document)オブジェクトと[XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions)を使用して実装できますが、時には不正なファイル構造に遭遇することもあります。
 
// XMLをPDFに変換
    public void convertXMLtoPDF() {
        // ドキュメントオブジェクトを初期化
        String pdfDocumentFileName = new File(fileStorage,"XML-to-PDF.pdf").toString();
        String xmlDocumentFileName = new File(fileStorage,"Conversion/employees.xml").toString();
        String xsltDocumentFileName = new File(fileStorage, "Conversion/employees.xslt").toString();

        try {
            XslFoLoadOptions options = new XslFoLoadOptions(xsltDocumentFileName);
            document = new Document(xmlDocumentFileName,options);
            // 結果のPDFファイルを保存
            document.save(pdfDocumentFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }    
    ```