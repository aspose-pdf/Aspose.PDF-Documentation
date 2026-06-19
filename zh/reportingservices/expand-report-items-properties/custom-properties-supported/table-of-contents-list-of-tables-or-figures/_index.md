---
title: 目录、表格列表或图形
linktitle: 目录、表格列表或图形
type: docs
weight: 10
url: /zh/reportingservices/table-of-contents-list-of-tables-or-figures/
description: 了解如何使用 Aspose.PDF for Reporting Services 在 PDF 报告中添加目录、表格列表或图形。
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Report Designer 不支持在报告文档中添加目录。使用 Aspose.PDF for Reporting Services，您可以轻松指示 PDF 渲染器生成带有目录、表格列表或图形的 PDF 文档。您可以按照以下步骤进行操作：

{{% /alert %}}

{{% alert color="primary" %}}
确保 Aspose.Pdf.ListSectionStyle.xml 文件存在于 ```<Instance>```/bin，在哪里 ```<Instance>``` 是 Report Server 的目录。如果文件不存在，请在其中创建。 ```<Instance>```/bin 目录，并将以下标记放入其中。

## 目录

**示例**

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

##  表格列表

**示例**

```cs
<ListSection ListType="ListOfTables">
              <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfTables</Segment>
              </Title>
</ListSection>
```

## 图表列表

**示例**

```cs
 <ListSection ListType="ListOfFigures">
    <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfFigures</Segment>
    </Title>
</ListSection>

```

请参阅 Aspose.Pdf 在线文档中的 'Working with TOC' 部分。

**2-** 添加报告参数 'IsListSectionSupported'，并将其值设置为 True，如 'List Section' 段落所示。
**3-** 为您想要列入目录、表格目录或图表目录的报告项添加自定义属性。

{{% /alert %}}

{{% alert color="primary" %}}

**自定义属性名称** :IsInList
**属性值** :Boolean
**自定义属性值** : True 或 False

{{% alert color="primary" %}}

将当前报告项标记为在目录、表格列表或图形列表中按索引列出。

{{% /alert %}}

**自定义属性名称** : 标题
**自定义属性类型** : 字符串

{{% alert color="primary" %}}

在目录、表格列表或图形列表中显示的项目标题。
{{% /alert %}}

**自定义属性名称** : 列表级别
**自定义属性类型** : 整数

{{% alert color="primary" %}}

目录中显示的列出项的层级。

{{% /alert %}}

{{% /alert %}}

