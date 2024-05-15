---
title: Table of Contents List of Tables or Figures
type: docs
weight: 10
url: /reportingservices/table-of-contents-list-of-tables-or-figures/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Report Designer does not support adding table of contents for report documents. With Aspose.Pdf for Reporting Services you can easily instruct the PDF render to produce PDF documents with Table of Contents, or List of Tables or Figures. You can do it in the following steps:

{{% /alert %}}

{{% alert color="primary" %}}
Make sure that Aspose.Pdf.ListSectionStyle.xml file exists in ```<Instance>```/bin, where ```<Instance>``` is the directory of the Report Server. If the file does not exist, create it in the ```<Instance>```/bin directory and place the following markup inside.

## Table of Contents

**Example**

```cs
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

##  List of TableS

**Example**

```cs
<ListSection ListType="ListOfTables">
              <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfTables</Segment>
              </Title>
</ListSection>
```

## List of Figures

**Example**

```cs
 <ListSection ListType="ListOfFigures">
    <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfFigures</Segment>
    </Title>
</ListSection>

```

Please refer to 'Working with TOC' section of the Aspose.Pdf online documentation.

**2-** Add report parameter 'IsListSectionSupported' and set the value to be True as shown in the 'List Section' paragraph.
**3-** Add custom property for your report item you want to be listed in Table of Contents, List of Tables or Figures.

{{% /alert %}}

{{% alert color="primary" %}}

**Custom Property Name** :IsInList
**Property Value** :Boolean
**Custom Property Value** : True or False

{{% alert color="primary" %}}

Marks the current report item as listed by index in the table of contents, or the list of tables or figures.

{{% /alert %}}

**Custom Property Name** : Title
**Custom Property Type** : String

{{% alert color="primary" %}}

The item title displayed in the table of contents, list of tables or figures.
{{% /alert %}}

**Custom Property Name** : ListLevel
**Custom Property Type** : Integer

{{% alert color="primary" %}}

The level of listed items displayed in the table of contents.

{{% /alert %}}

{{% /alert %}}
