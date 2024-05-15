---
title: Why choose Aspose.Pdf for Reporting Services
type: docs
weight: 10
url: /reportingservices/why-choose-aspose-pdf-for-reporting-services/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF for Reporting Services is a robust .NET solution which allows you to produce PDF reports using Microsoft SQL Server 2000, 2005 and 2008 Reporting Services. Aspose.PDF for Reporting Services does not operate independently but, it’s a rendering extension for SQL Reporting Services. Not only it supports the basic report elements such as tables, charts, images, Header/Footers, lines etc but, it also provides the capability to add custom properties which gives its an extra leverage upon SQL Reporting Services. While using these properties, you can generate List Of Contents which is not supported by Report Designer. You may even like to have Footnotes/Endnotes in the resultant PDF document which is natively not supported by Report Builder. Another interesting feature is to have Line Arrow which is also not supported by SQL Reporting Services but Aspose.PDF for Reporting Services can provide the capability to add arrows at the beginning or end of the line element. More along, Aspose.PDF for Reporting Services provides the functionality to specify the text alignment (Justify or FullJustify) information which is not supported by Report Designer. These text modes make the resultant document better formatted and easy-readable.

{{% /alert %}}

With Aspose.PDF for Reporting Services you can easily instruct the PDF render to produce PDF documents with Table of Contents, List of Tables or Figures. For that reason, you only need to have Aspose.PDF.ListSectionStyle.xml file in Bin folder of reporting Services instance and copy the following contents inside it.

##### ***Table of Contents***
**Example**
```
<ListSection ListType="TableOfContents">
  <Title Alignment="Center">
    <Segment IsTrueTypeFontBold="true" FontSize="30">TableOfContents</Segment>
  </Title>
  <ListLevelFormat Level="1" LeftMargin="0">
    <TextInfo IsTrueTypeFontBold="true" IsTrueTypeFontItalic="true"></TextInfo>
  </ListLevelFormat>
  <ListLevelFormat Level="2" LeftMargin="10">
    <TextInfo IsUnderline="true" FontSize="10"></TextInfo>
  </ListLevelFormat>
  <ListLevelFormat Level="3" LeftMargin="20">
    <TextInfo IsTrueTypeFontBold="true"></TextInfo>
  </ListLevelFormat>
  <ListLevelFormat Level="4" LeftMargin="30">
    <TextInfo IsTrueTypeFontBold="true"></TextInfo>
  </ListLevelFormat>
</ListSection>
```

##### ***List of Tables***
**Example**
```
<ListSection ListType="ListOfTables">
  <Title>
    <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfTables</Segment>
  </Title>
</ListSection>
```
##### ***List of Figures***
**Example**
```
<ListSection ListType="ListOfFigures">
    <Title>
        <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfFigures</Segment>
    </Title>
</ListSection>
```

**Report builder cannot set the footnote or endnote for textboxes. With Aspose.PDF for Reporting Services, you can do that easily by adding custom properties. For example, the content of some Textbox in the current report is 'AsposePdf4RS', you want to describe the phrase ‘AsposePdf4RS’ in detail with the style of footnote, which content is "An optional PDF renderer for SSRS from Aspose".**

**In SSRS2005, the code should be like the following:**

**Example**
```
  <Textbox Name="textbox1">
      ......
      <Style>
        ......
   </style>
   <value> AsposePdf4RS </value>
      <CustomProperties>
        <CustomProperty>
          <Name>Footnote</Name>
            <Value> An optional PDF renderer for SSRS from Aspose</Value>
        </CustomProperty>
       </CustomProperties>
   </Textbox> 
```

   **Following is a brief of such features which are only offered in Aspose.PDF for Reporting Services Security Settings:**

  * Sometimes you might wish to export PDF document with opening password, limited text copying and printing privilege. Unfortunately, Reporting Services does not support this possibility. However, you still can implement it using Aspose.PDF for Reporting Services. Just add corresponding security parameters to report or report server, you would get secure PDF document with limited privilege. For more information, please visit Security Setting. 
  * Custom Font Embedding: RS designer does not support the embedded font for text; with Aspose.PDF for Reporting Services you can easily embed font information into your PDF document. For more information, please visit IsFontEmbedded.
  * XMP Metadata: Reporting Services designer does not support the embedding of XMP data. Aspose.PDF for Reporting Services provides four parameters (CreationDate, ModifyDate, MetaDataDate and CreatorTool) to set the corresponding XMP Metadata. For more related information, please visit XMP Metadata.
  * PDF/A: When using SQL Reporting Services, you can only generate the PDF document in simple format whereas the generation of PDF/A documents is not support. But, Aspose.PDF for Reporting Services provides the feature to create PDF/A compliant documents. With the addition of a single configuration parameter, you can generate PDF/A document. For more related information, please visit PDF Conformance.
  * Page Rotation Angle: When using Aspose.PDF for Reporting Services, you can set the number of degrees by which the page should be rotated clockwise when displayed or printed. For more related information, please visit Page Rotating Angle.
  * Page Margin Size: Reporting Services designer does not support the setting of page margin size. But, Aspose.PDF for Reporting Services provides four parameters to set the corresponding page margin size. i.e. PageMarginLeft, PageMarginRight, PageMarginTop and pageMarginBottom. For more related information, please visit Page Margin Size.
