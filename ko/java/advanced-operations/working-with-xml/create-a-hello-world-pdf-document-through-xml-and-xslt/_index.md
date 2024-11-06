---
title: XML 및 XSLT를 통해 Hello World PDF 문서 생성
linktitle: XML 및 XSLT를 통해 Hello World PDF 문서 생성
type: docs
weight: 10
url: ko/java/create-a-hello-world-pdf-document-through-xml-and-xslt/
description: Aspose.PDF for Java는 입력 XML 파일이 Aspose.PDF XSD Java 스키마를 따라야 한다는 조건 하에 XML 파일을 PDF 문서로 변환할 수 있는 기회를 제공합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

기존의 XML 파일에 애플리케이션 데이터가 포함되어 있고, 이 파일을 사용하여 PDF 보고서를 생성하려는 경우가 있습니다. XSLT를 사용하여 기존 XML 문서를 Aspose.Pdf의 호환 가능한 XML 문서로 변환한 다음 PDF 파일을 생성할 수 있습니다. XML 및 XSLT를 사용하여 PDF를 생성하는 3가지 단계가 있습니다.

XSLT를 사용하여 XML 파일을 PDF 문서로 변환하려면 다음 단계를 따르십시오:

* PDF 문서를 나타내는 PDF 클래스의 인스턴스를 생성합니다.

* 라이센스를 구매한 경우, Aspose.Pdf 네임스페이스의 License 클래스를 사용하여 해당 라이센스를 사용할 수 있도록 코드를 삽입해야 합니다.
* XML 및 XSLT 입력 파일을 PDF 클래스의 인스턴스에 BindXML 메서드를 호출하여 바인딩합니다.
* PDF 인스턴스와 함께 바인딩된 XML을 PDF 문서로 저장합니다.

## 입력 XML 파일

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Contents>
  <Content>안녕하세요 세계!</Content>
</Contents>
```

## 입력 XSLT 파일

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


## XML과 Java를 사용하여 Hello World 만들기

```java
public static void Example_XML_to_PDF_02() {
      com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document();
      pdfDocument.bindXml(_dataDir + "XMLFile1.xml",_dataDir +  "XSLTFile1.xslt");
      pdfDocument.save(_dataDir + "data_xml.pdf");
}    
```