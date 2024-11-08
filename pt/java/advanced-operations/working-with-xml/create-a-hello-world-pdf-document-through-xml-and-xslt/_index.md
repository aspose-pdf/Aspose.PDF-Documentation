---
title: Criar um Documento PDF Hello World através de XML e XSLT
linktitle: Criar um Documento PDF Hello World através de XML e XSLT
type: docs
weight: 10
url: /pt/java/create-a-hello-world-pdf-document-through-xml-and-xslt/
description: O Aspose.PDF para Java oferece a oportunidade de converter um arquivo XML em um documento PDF, exigindo que o arquivo XML de entrada siga o Esquema XSD Java do Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Às vezes, você pode ter arquivos XML existentes que contêm dados de aplicativos e deseja gerar um relatório PDF usando esses arquivos. Você pode usar XSLT para transformar seu documento XML existente em um documento XML compatível com Aspose.Pdf e, em seguida, gerar o arquivo PDF. Existem 3 etapas para gerar PDF usando XML e XSLT.

Por favor, siga estas etapas para converter um arquivo XML em um documento PDF usando XSLT:

* Crie uma instância da classe PDF que representa um documento PDF

* Se você comprou uma licença, deve também incorporar o código para usar essa licença com a ajuda da classe License no namespace Aspose.Pdf
* Vincule os arquivos XML e XSLT de entrada à instância da classe PDF chamando seu método BindXML
* Salve o XML vinculado com a instância PDF como um documento PDF

## Arquivo XML de Entrada

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Contents>
  <Content>Hello World!</Content>
</Contents>
```

## Arquivo XSLT de Entrada

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


## Fazendo Hello World usando XML e Java

```java
public static void Example_XML_to_PDF_02() {
      com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document();
      pdfDocument.bindXml(_dataDir + "XMLFile1.xml",_dataDir +  "XSLTFile1.xslt");
      pdfDocument.save(_dataDir + "data_xml.pdf");
}    
```