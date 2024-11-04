---
title: 通过 XML 和 XSLT 创建一个 Hello World PDF 文档
linktitle: 通过 XML 和 XSLT 创建一个 Hello World PDF 文档
type: docs
weight: 10
url: /java/create-a-hello-world-pdf-document-through-xml-and-xslt/
description: Aspose.PDF for Java 提供了将 XML 文件转换为 PDF 文档的机会，要求输入的 XML 文件必须遵循 Aspose.PDF XSD Java Schema。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

有时您可能有现有的包含应用程序数据的 XML 文件，并且您希望使用这些文件生成 PDF 报告。您可以使用 XSLT 将现有的 XML 文档转换为 Aspose.Pdf 兼容的 XML 文档，然后生成 PDF 文件。使用 XML 和 XSLT 生成 PDF 有三个步骤。

请按照以下步骤使用 XSLT 将 XML 文件转换为 PDF 文档：

* 创建一个表示 PDF 文档的 PDF 类实例

* 如果您购买了许可证，那么您也应该嵌入代码以在 Aspose.Pdf 命名空间中使用 License 类来使用该许可证
* 通过调用PDF类的BindXML方法将输入的XML和XSLT文件绑定到实例
* 将绑定的XML与PDF实例保存为PDF文档

## 输入XML文件

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Contents>
  <Content>你好，世界！</Content>
</Contents>
```

## 输入XSLT文件

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


## 使用 XML 和 Java 制作 Hello World

```java
public static void Example_XML_to_PDF_02() {
      com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document();
      pdfDocument.bindXml(_dataDir + "XMLFile1.xml",_dataDir +  "XSLTFile1.xslt");
      pdfDocument.save(_dataDir + "data_xml.pdf");
}    
```