---
title: XML Schema of Aspose.PDF
linktitle: Supported XML Schema
type: docs
weight: 10
url: konet/supported-xml-schema/
description: 이 문서에서는 Aspose.PDF for .NET에서 XML 문서를 다루기 위한 XML 스키마를 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "XML Schema of Aspose.PDF",
    "alternativeHeadline": "How to work with XML Schema in PDF ",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, XML schema",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "net/supported-xml-schema/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "net/supported-xml-schema/"
    },
    "dateModified": "2022-02-04",
    "description": "이 문서에서는 Aspose.PDF for .NET에서 XML 문서를 다루기 위한 XML 스키마를 설명합니다."
}
</script>

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

Aspose.PDF for .NET은 XML 문서 작업을 위해 다음 XML 스키마를 사용합니다:

```xml
<?xml version="1.0"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" attributeFormDefault="unqualified" elementFormDefault="qualified" targetNamespace="Aspose.Pdf">
  <xs:element xmlns:asp="Aspose.Pdf" name="Document" type="asp:DocumentType"/>
  <xs:complexType name="TextFragmentType">
    <xs:sequence>
      <xs:element name="TextSegment" maxOccurs="unbounded" minOccurs="0">
        <xs:complexType mixed="true">
          <xs:sequence>
            <xs:element xmlns:asp="Aspose.Pdf" type="asp:TextStateType" name="TextState" minOccurs="0"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:TextStateType" name="TextState" minOccurs="0"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:NoteType" name="FootNote" minOccurs="0"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:NoteType" name="EndNote" minOccurs="0"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="CellType" mixed="true">
    <xs:choice maxOccurs="unbounded" minOccurs="0">
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:BorderType" name="Border"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:TextStateType" name="DefaultCellTextState"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:GraphType" name="Graph"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:TextFragmentType" name="TextFragment"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:TableType" name="Table"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:MarginType" name="Margin"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:ImageType" name="Image" minOccurs="0"/>
      <xs:element type="xs:string" name="HtmlFragment" minOccurs="0"/>
    </xs:choice>
    <xs:attribute type="xs:string" name="BackgroundColor" use="optional"/>
    <xs:attribute type="xs:byte" name="ColSpan" use="optional"/>
    <xs:attribute type="xs:byte" name="RowSpan" use="optional"/>
    <xs:attribute type="xs:byte" name="Alignment" use="optional"/>
  </xs:complexType>
  <xs:complexType name="RowType">
    <xs:sequence>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:BorderType" name="DefaultCellBorder" minOccurs="0"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:TextStateType" name="DefaultCellTextState" minOccurs="0"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:CellType" name="Cell" maxOccurs="unbounded" minOccurs="0"/>
    </xs:sequence>
    <xs:attribute type="xs:string" name="BackgroundColor" use="optional"/>
    <xs:attribute type="xs:short" name="FixedRowHeight" use="optional"/>
    <xs:attribute type="xs:byte" name="MinRowHeight" use="optional"/>
    <xs:attribute type="xs:string" name="IsRowBroken" use="optional"/>
  </xs:complexType>
  <xs:complexType name="TableType"> 
    <xs:choice maxOccurs="unbounded" minOccurs="0">
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:BorderType" name="Border" minOccurs="0"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:BorderType" name="DefaultCellBorder" minOccurs="0"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:MarginType" name="DefaultCellPadding" minOccurs="0"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:TextStateType" name="DefaultCellTextState" minOccurs="0"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:MarginType" name="Margin"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:RowType" name="Row" minOccurs="0"/>
    </xs:choice>
    <xs:attribute type="xs:string" name="ColumnWidths" use="optional"/>
    <xs:attribute type="xs:byte" name="Broken" use="optional"/>
    <xs:attribute type="xs:byte" name="RepeatingRowsCount" use="optional"/>
    <xs:attribute type="xs:float" name="Left" use="optional"/>
    <xs:attribute type="xs:float" name="Right" use="optional"/>
    <xs:attribute type="xs:float" name="Top" use="optional"/>
    <xs:attribute type="xs:float" name="Bottom" use="optional"/>
    <xs:attribute type="xs:string" name="ColumnAdjustment" use="optional"/>
    <xs:attribute type="xs:string" name="IsInLineParagraph" use="optional"/>
    <xs:attribute type="xs:string" name="HorizontalAlignment" use="optional"/>
  </xs:complexType>
  <xs:complexType name="PageType">
    <xs:choice maxOccurs="unbounded" minOccurs="0">
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:HeaderType" name="Header"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:FooterType" name="Footer"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:PageInfoType" name="PageInfo"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:TableType" name="Table"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:ImageType" name="Image"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:GraphType" name="Graph"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:FloatingBoxType" name="FloatingBox"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:TextFragmentType" name="TextFragment"/>
      <xs:element type="xs:string" name="HtmlFragment"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:HeadingType" name="Heading"/>
    </xs:choice>
  </xs:complexType>
  <xs:complexType name="ImageType" mixed="true">
    <xs:sequence>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:TextFragmentType" name="Title" minOccurs="0"/>
    </xs:sequence>
    <xs:attribute type="xs:string" name="File" use="optional"/>
    <xs:attribute type="xs:short" name="FixWidth" use="optional"/>
    <xs:attribute type="xs:short" name="FixHeight" use="optional"/>
    <xs:attribute type="xs:string" name="HorizontalAlignment" use="optional"/>
    <xs:attribute type="xs:float" name="ImageScale" use="optional"/>
  </xs:complexType>
  <xs:complexType name="GraphInfoType">
    <xs:simpleContent>
      <xs:extension base="xs:string">
        <xs:attribute type="xs:string" name="FillColor" use="optional"/>
        <xs:attribute type="xs:string" name="Color" use="optional"/>
        <xs:attribute type="xs:byte" name="RotationAngle" use="optional"/>
        <xs:attribute type="xs:float" name="ScalingRateX" use="optional"/>
      </xs:extension>
    </xs:simpleContent>
  </xs:complexType>
  <xs:complexType name="LineType">
    <xs:simpleContent>
      <xs:extension base="xs:string">
        <xs:attribute type="xs:string" name="PositionArray" use="optional"/>
        <xs:attribute type="xs:short" name="PosX" use="optional"/>
        <xs:attribute type="xs:byte" name="PosY" use="optional"/>
        <xs:attribute type="xs:byte" name="Radius" use="optional"/>
        <xs:attribute type="xs:short" name="Alpha" use="optional"/>
        <xs:attribute type="xs:short" name="Beta" use="optional"/>
      </xs:extension>
    </xs:simpleContent>
  </xs:complexType>
  <xs:complexType name="ArcType">
    <xs:simpleContent>
      <xs:extension base="xs:string">
        <xs:attribute type="xs:short" name="PosX" use="optional"/>
        <xs:attribute type="xs:byte" name="PosY" use="optional"/>
        <xs:attribute type="xs:byte" name="Radius" use="optional"/>
        <xs:attribute type="xs:short" name="Alpha" use="optional"/>
        <xs:attribute type="xs:short" name="Beta" use="optional"/>
        <xs:attribute type="xs:string" name="PositionArray" use="optional"/>
      </xs:extension>
    </xs:simpleContent>
  </xs:complexType>
  <xs:complexType name="PathType">
    <xs:choice maxOccurs="unbounded" minOccurs="0">
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:GraphInfoType" name="GraphInfo"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:LineType" name="Line"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:ArcType" name="Arc"/>
    </xs:choice>
  </xs:complexType>
  <xs:complexType name="GraphType">
    <xs:sequence>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:PathType" name="Path" minOccurs="0"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:CircleType" name="Circle" minOccurs="0"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:EllipseType" name="Ellipse" minOccurs="0"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:GraphInfoType" name="GraphInfo" minOccurs="0"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:RectangleType" name="Rectangle" minOccurs="0"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:CurveType" name="Curve" minOccurs="0"/>
    </xs:sequence>
    <xs:attribute type="xs:short" name="Width" use="optional"/>
    <xs:attribute type="xs:short" name="Height" use="optional"/>
  </xs:complexType>
  <xs:complexType name="MarginType">
    <xs:simpleContent>
      <xs:extension base="xs:string">
        <xs:attribute type="xs:byte" name="Bottom" use="optional"/>
        <xs:attribute type="xs:byte" name="Left" use="optional"/>
        <xs:attribute type="xs:byte" name="Right" use="optional"/>
        <xs:attribute type="xs:byte" name="Top" use="optional"/>
      </xs:extension>
    </xs:simpleContent>
  </xs:complexType>
  <xs:complexType name="HeaderType">
    <xs:sequence>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:MarginType" name="Margin" minOccurs="0"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:TableType" name="Table"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:ImageType" name="Image"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:GraphType" name="Graph"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:FloatingBoxType" name="FloatingBox"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:TextFragmentType" name="TextFragment"/>
      <xs:element type="xs:string" name="HtmlFragment"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:HeadingType" name="Heading"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="FooterType">
    <xs:sequence>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:MarginType" name="Margin" minOccurs="0"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:TableType" name="Table"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:ImageType" name="Image"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:GraphType" name="Graph"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:FloatingBoxType" name="FloatingBox"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:TextFragmentType" name="TextFragment"/>
      <xs:element type="xs:string" name="HtmlFragment"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:HeadingType" name="Heading"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="PageInfoType">
    <xs:sequence>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:MarginType" name="Margin"/>
    </xs:sequence>
    <xs:attribute type="xs:short" name="Height" use="optional"/>
    <xs:attribute type="xs:short" name="Width" use="optional"/>
    <xs:attribute type="xs:string" name="IsLandscape" use="optional"/>
  </xs:complexType>
  <xs:complexType name="BorderType" mixed="true">
    <xs:sequence>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:GraphInfoType" name="Bottom" minOccurs="0"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:GraphInfoType" name="Top" minOccurs="0"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:GraphInfoType" name="Right" minOccurs="0"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:GraphInfoType" name="Left" minOccurs="0"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="FloatingBoxType">
    <xs:choice maxOccurs="unbounded" minOccurs="0">
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:BorderType" name="Border"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:TableType" name="Table"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:MarginType" name="Margin"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:ImageType" name="Image"/>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:TextFragmentType" name="TextFragment"/>
    </xs:choice>
    <xs:attribute type="xs:short" name="Width" use="optional"/>
    <xs:attribute type="xs:byte" name="Height" use="optional"/>
    <xs:attribute type="xs:string" name="IsNeedRepeating" use="optional"/>
    <xs:attribute type="xs:string" name="VerticalAlignment" use="optional"/>
  </xs:complexType>
  <xs:complexType name="TextStateType">
    <xs:simpleContent>
      <xs:extension base="xs:string">
        <xs:attribute type="xs:string" name="Font" use="optional"/>
        <xs:attribute type="xs:byte" name="FontSize" use="optional"/>
        <xs:attribute type="xs:byte" name="LineSpacing" use="optional"/>
        <xs:attribute type="xs:byte" name="FontStyle" use="optional"/>
        <xs:attribute type="xs:string" name="Underline" use="optional"/>
        <xs:attribute type="xs:string" name="ForegroundColor" use="optional"/>
      </xs:extension>
    </xs:simpleContent>
  </xs:complexType>
  <xs:complexType name="TextSegmentType" mixed="true">
    <xs:sequence>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:TextStateType" name="TextState" minOccurs="0"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="CircleType">
    <xs:sequence>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:GraphInfoType" name="GraphInfo"/>
    </xs:sequence>
    <xs:attribute type="xs:short" name="PosX" use="optional"/>
    <xs:attribute type="xs:byte" name="PosY" use="optional"/>
    <xs:attribute type="xs:byte" name="Radius" use="optional"/>
  </xs:complexType>
  <xs:complexType name="EllipseType" mixed="true">
    <xs:sequence>
      <xs:element xmlns:asp="Aspose.Pdf" type="asp:GraphInfoType" name="GraphInfo" minOccurs="0"/>
    </xs:sequence>
    <xs:attribute type="xs:byte" name="Left" use="

```json
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF 조작 라이브러리 for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
```