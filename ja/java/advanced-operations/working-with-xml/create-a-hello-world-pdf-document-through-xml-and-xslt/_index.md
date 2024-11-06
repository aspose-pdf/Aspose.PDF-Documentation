---
title: XMLとXSLTを使用してHello World PDFドキュメントを作成する
linktitle: XMLとXSLTを使用してHello World PDFドキュメントを作成する
type: docs
weight: 10
url: ja/java/create-a-hello-world-pdf-document-through-xml-and-xslt/
description: Aspose.PDF for Javaは、入力XMLファイルがAspose.PDF XSD Java Schemaに従う必要があることを要求し、XMLファイルをPDFドキュメントに変換する機会を提供します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

既存のXMLファイルにアプリケーションデータが含まれていて、これらのファイルを使用してPDFレポートを生成したい場合があります。XSLTを使用して既存のXMLドキュメントをAspose.Pdfの互換XMLドキュメントに変換し、PDFファイルを生成できます。XMLとXSLTを使用してPDFを生成するための3つのステップがあります。

XSLTを使用してXMLファイルをPDFドキュメントに変換するには、以下の手順に従ってください：

* PDFドキュメントを表すPDFクラスのインスタンスを作成します

* ライセンスを購入している場合は、Aspose.Pdf名前空間のLicenseクラスを使用してそのライセンスを使用するコードを埋め込む必要があります
* 入力XMLとXSLTファイルをPDFクラスのインスタンスにバインドし、そのBindXMLメソッドを呼び出します
* PDFインスタンスでバインドされたXMLをPDFドキュメントとして保存します

## 入力XMLファイル

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Contents>
  <Content>こんにちは世界！</Content>
</Contents>
```

## 入力XSLTファイル

```xml
<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="text()"/>
    <xsl:template match="/Contents">
    <html>
      <Document xmlns="Aspose.Pdf" IsAutoHyphenated="false">
        <PageInfo>
          <DefaultTextState Font = "Helvetica" FontSize="8" LineSpacing="4"/>
          <Margin Left="5cm" Right="5cm" Top="3cm" Bottom="15cm" />
        </PageInfo>
        <Page id="mainSection">
          <TextFragment>
            <TextSegment>
              <xsl:value-of select="Content"/>
            </TextSegment>
          </TextFragment>
        </Page>
      </Document>
    </html>
</xsl:template>
</xsl:stylesheet>
```


## XMLとJavaを使用してHello Worldを作成する

```java
public static void Example_XML_to_PDF_02() {
      com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document();
      pdfDocument.bindXml(_dataDir + "XMLFile1.xml",_dataDir +  "XSLTFile1.xslt");
      pdfDocument.save(_dataDir + "data_xml.pdf");
}    
```