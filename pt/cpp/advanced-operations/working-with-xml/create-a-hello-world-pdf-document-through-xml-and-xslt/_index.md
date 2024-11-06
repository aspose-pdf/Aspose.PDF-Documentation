---
title: Criando PDF a partir de XML usando XSLT 
linktitle: Criar PDF a partir de XML usando XSLT
type: docs
weight: 10
url: pt/cpp/create-a-hello-world-pdf-document-through-xml-and-xslt/
description: A biblioteca C++ fornece a capacidade de converter um arquivo XML em um documento PDF, exigindo que o arquivo XML de entrada siga o esquema Aspose.PDF.
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Às vezes, você pode ter arquivos XML existentes que contêm dados de aplicativos e deseja gerar um relatório PDF usando esses arquivos. Você pode usar XSLT para transformar seu documento XML existente em um documento XML compatível com Aspose.Pdf e, em seguida, gerar um arquivo PDF. Existem 3 etapas para gerar PDF usando XML e XSLT.

Por favor, siga estas etapas para converter um arquivo XML em um documento PDF usando XSLT:

* Crie uma instância da classe PDF que representa um documento PDF
* Se você adquiriu uma licença, então também deve incorporar o código para usar essa licença com a ajuda da classe License no namespace Aspose.Pdf

* Vincule os arquivos XML e XSLT de entrada à instância da classe PDF chamando seu método BindXML
* Salve o XML vinculado com a instância PDF como um documento PDF

## Arquivo XML de Entrada

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Contents>
  <Content>Olá Mundo!</Content>
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
 //Crie documento pdf
 auto pdf = MakeObject<Aspose::Pdf::Document>();
 //Vincule os arquivos XML e XSLT ao documento
 try
 {
  pdf->BindXml(_dataDir + u"\\HelloWorld.xml", _dataDir + u"\\HelloWorld.xslt");
 }
 catch (System::Exception ex)
 {
  std::cerr << ex.what();
  throw;
 }

 //Salve o documento
 pdf->Save(_dataDir + u"HelloWorldUsingXmlAndXslt.pdf");
}

```