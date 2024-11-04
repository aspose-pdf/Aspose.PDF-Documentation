---
title: XML을 사용하여 XSLT로 PDF 생성
linktitle: XML을 사용하여 XSLT로 PDF 생성
type: docs
weight: 10
url: /cpp/create-a-hello-world-pdf-document-through-xml-and-xslt/
description: C++ 라이브러리는 입력 XML 파일이 Aspose.PDF 스키마를 따라야 하는 XML 파일을 PDF 문서로 변환할 수 있는 기능을 제공합니다.
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

때때로 응용 프로그램 데이터가 포함된 기존 XML 파일을 가지고 있으며 이러한 파일을 사용하여 PDF 보고서를 생성하려고 할 수 있습니다. 기존 XML 문서를 Aspose.Pdf와 호환되는 XML 문서로 변환한 다음 PDF 파일을 생성하기 위해 XSLT를 사용할 수 있습니다. XML과 XSLT를 사용하여 PDF를 생성하는 데에는 3단계가 있습니다.

XML 파일을 XSLT를 사용하여 PDF 문서로 변환하려면 다음 단계를 따르세요:

* PDF 문서를 나타내는 PDF 클래스의 인스턴스를 생성합니다.
* 라이센스를 구입한 경우 Aspose.Pdf 네임스페이스의 License 클래스를 사용하여 해당 라이센스를 사용하는 코드를 포함해야 합니다.

* BindXML 메서드를 호출하여 입력 XML 및 XSLT 파일을 PDF 클래스의 인스턴스에 바인딩합니다.
 * PDF 인스턴스와 바인딩된 XML을 PDF 문서로 저장

## Input XML File

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Contents>
  <Content>안녕하세요 세계!</Content>
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
 //PDF 문서 생성
 auto pdf = MakeObject<Aspose::Pdf::Document>();
 // XML 및 XSLT 파일을 문서에 바인딩
 try
 {
  pdf->BindXml(_dataDir + u"\\HelloWorld.xml", _dataDir + u"\\HelloWorld.xslt");
 }
 catch (System::Exception ex)
 {
  std::cerr << ex.what();
  throw;
 }

 //문서 저장
 pdf->Save(_dataDir + u"HelloWorldUsingXmlAndXslt.pdf");
}

```