---
title: Create a Hello World PDF Document through XML and XSLT
linktitle: Create a Hello World PDF Document through XML and XSLT
type: docs
weight: 10
url: /androidjava/create-a-hello-world-pdf-document-through-xml-and-xslt/
description: Aspose.PDF for Java provides the opportunity to convert an XML file into PDF document requiring that the input XML file must follow the Aspose.PDF XSD Java Schema.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Sometimes you may have existing XML files that contain application data and you want to generate PDF report using these files. You can use XSLT to transform your existing XML document to Aspose.Pdf's compatible XML document and then generate PDF file. There are 3 steps to generate PDF using XML and XSLT.

Please follow these steps to convert an XML file into a PDF document using XSLT:

* Create an instance of PDF class that represents a PDF document
* If you have purchased a license then you should also embed the code to use that license with the help of License class in Aspose.Pdf namespace
* Bind the input XML and XSLT files to the instance of PDF class by calling its BindXML method
* Save the bound XML with PDF instance as a PDF document

## Input XML File

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Contents>
  <Content>Hello World!</Content>
</Contents>
```

## Input XSLT File

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

## Making Hello World using XML and Java

```java
public static void Example_XML_to_PDF_02() {
      com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document();
      pdfDocument.bindXml(_dataDir + "XMLFile1.xml",_dataDir +  "XSLTFile1.xslt");
      pdfDocument.save(_dataDir + "data_xml.pdf");
}    
```
