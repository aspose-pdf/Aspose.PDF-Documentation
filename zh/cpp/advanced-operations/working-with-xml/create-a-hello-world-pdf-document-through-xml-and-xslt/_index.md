---
title: 使用XSLT从XML创建PDF
linktitle: 使用XSLT从XML创建PDF
type: docs
weight: 10
url: /zh/cpp/create-a-hello-world-pdf-document-through-xml-and-xslt/
description: C++库提供了将XML文件转换为PDF文档的能力，要求输入的XML文件必须遵循Aspose.PDF Schema。
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

有时候您可能有现有的XML文件包含应用程序数据，并且您想使用这些文件生成PDF报告。您可以使用XSLT将现有的XML文档转换为Aspose.Pdf兼容的XML文档，然后生成PDF文件。使用XML和XSLT生成PDF有3个步骤。

请按照以下步骤使用XSLT将XML文件转换为PDF文档：

* 创建一个PDF类的实例，代表一个PDF文档
* 如果您购买了许可证，那么您还应该通过Aspose.Pdf命名空间中的License类嵌入代码以使用该许可证

* 通过调用其BindXML方法将输入的XML和XSLT文件绑定到PDF类的实例上
* 将绑定的 XML 与 PDF 实例保存为 PDF 文档

## 输入 XML 文件

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Contents>
  <Content>你好，世界！</Content>
</Contents>
```

## 输入 XSLT 文件

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
 //创建 pdf 文档
 auto pdf = MakeObject<Aspose::Pdf::Document>();
 //将 XML 和 XSLT 文件绑定到文档
 try
 {
  pdf->BindXml(_dataDir + u"\\HelloWorld.xml", _dataDir + u"\\HelloWorld.xslt");
 }
 catch (System::Exception ex)
 {
  std::cerr << ex.what();
  throw;
 }

 //保存文档
 pdf->Save(_dataDir + u"HelloWorldUsingXmlAndXslt.pdf");
}

```