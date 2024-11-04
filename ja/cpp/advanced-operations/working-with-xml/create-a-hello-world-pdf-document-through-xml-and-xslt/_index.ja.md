---
title: XMLからXSLTを使用してPDFを作成
linktitle: XMLからXSLTを使用してPDFを作成
type: docs
weight: 10
url: /cpp/create-a-hello-world-pdf-document-through-xml-and-xslt/
description: C++ライブラリは、入力XMLファイルがAspose.PDFスキーマに従う必要があるPDFドキュメントにXMLファイルを変換する機能を提供します。
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

既存のXMLファイルにアプリケーションデータが含まれていて、これらのファイルを使用してPDFレポートを生成したい場合があります。XSLTを使用して、既存のXMLドキュメントをAspose.Pdf互換のXMLドキュメントに変換し、PDFファイルを生成できます。XMLとXSLTを使用してPDFを生成するには、次の3つのステップがあります。

XSLTを使用してXMLファイルをPDFドキュメントに変換するには、次の手順に従ってください:

* PDFドキュメントを表すPDFクラスのインスタンスを作成する
* ライセンスを購入している場合は、Aspose.Pdf名前空間のLicenseクラスを使用してそのライセンスを使用するコードを埋め込む必要があります

* BindXMLメソッドを呼び出して、入力XMLとXSLTファイルをPDFクラスのインスタンスにバインドする
 * PDFインスタンスとしてバインドされたXMLをPDFドキュメントとして保存する

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
          <DefaultTextState
                            Font = "Helvetica" FontSize="8" LineSpacing="4"/>
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

```cpp
using namespace System;
using namespace Aspose::Pdf;

static System::SharedPtr<System::IO::MemoryStream> TransformXmltoHtml(String inputXml, String xsltString);

void WorkingWithXML::CreatingPDFfromXMLusingXSLT()
{
 String _dataDir("C:\\Samples\\");
 //PDFドキュメントを作成
 auto pdf = MakeObject<Aspose::Pdf::Document>();
 //XMLとXSLTファイルをドキュメントにバインド
 try
 {
  pdf->BindXml(_dataDir + u"\\HelloWorld.xml", _dataDir + u"\\HelloWorld.xslt");
 }
 catch (System::Exception ex)
 {
  std::cerr << ex.what();
  throw;
 }

 //ドキュメントを保存
 pdf->Save(_dataDir + u"HelloWorldUsingXmlAndXslt.pdf");
}

```