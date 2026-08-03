---
title: 目录 表格或图形列表
linktitle: 目录 表格或图形列表
type: docs
weight: 10
url: /reportingservices/table-of-contents-list-of-tables-or-figures/
description: 了解如何使用 Aspose.PDF for Reporting Services 在 PDF 报告中添加目录、表格列表或图表。
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

报表设计器不支持添加报表文档的目录。使用 Aspose.PDF for Reporting Services，您可以轻松指示 PDF 渲染器生成带有目录、表格或图形列表的 PDF 文档。您可以按照以下步骤进行操作：

{{% /alert %}}

确保 Aspose.Pdf.ListSectionStyle.xml 文件存在于 ```<Instance>```/bin, where ```<Instance>``` is the directory of the Report Server. If the file does not exist, create it in the ```<Instance>```/bin 目录中，并将以下标记放入其中。

## 目录

### 例子

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

##  表列表

### 例子

```cs
<ListSection ListType="ListOfTables">
              <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfTables</Segment>
              </Title>
</ListSection>
```

## 图列表

### 例子

```cs
 <ListSection ListType="ListOfFigures">
    <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfFigures</Segment>
    </Title>
</ListSection>

```

请参阅 Aspose.Pdf 在线文档的“使用 TOC”部分。

**2-** 添加报告参数`IsListSectionSupported` 并将值设置为True，如`List Section` 段落中所示。
**3-** 为您想要在目录、表格或图形列表中列出的报告项目添加自定义属性。

```text
Custom Property Name: IsInList
Property Value: Boolean
Custom Property Value: True or False
```

将当前报告项目标记为按目录或表格或图形列表中的索引列出。

```text
Custom Property Name: Title
Custom Property Type: String
```

目录、表格或图形列表中显示的项目标题。

```text
Custom Property Name: ListLevel
Custom Property Type: Integer
```

目录中显示的列出项目的级别。
