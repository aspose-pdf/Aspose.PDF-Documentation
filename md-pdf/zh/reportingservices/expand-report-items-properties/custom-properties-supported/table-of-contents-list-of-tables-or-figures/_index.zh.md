---
title: 目录 表格或图形列表
type: docs
weight: 10
url: /reportingservices/table-of-contents-list-of-tables-or-figures/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

报表设计器不支持为报表文档添加目录。使用 Aspose.Pdf for Reporting Services，您可以轻松指示 PDF 渲染器生成带有目录或表格或图形列表的 PDF 文档。您可以通过以下步骤来实现：

{{% /alert %}}

{{% alert color="primary" %}}
确保 Aspose.Pdf.ListSectionStyle.xml 文件存在于 ```<Instance>```/bin 中，其中 ```<Instance>``` 是报表服务器的目录。如果文件不存在，请在 ```<Instance>```/bin 目录中创建该文件并在其中放置以下标记。

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

## 表格列表

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

请参阅 Aspose.Pdf 在线文档的“目录工作”部分。

**2-** 添加报告参数 'IsListSectionSupported' 并将值设置为 True，如“列表部分”段落中所示。
**3-** 为您希望在目录、表格或图表列表中列出的报告项添加自定义属性。

{{% /alert %}}

{{% alert color="primary" %}}

**自定义属性名称**: IsInList
**属性值**: Boolean
**自定义属性值**: True 或 False

{{% alert color="primary" %}}

将当前报告项标记为在目录、表格或图表列表中按索引列出。

{{% /alert %}}

**Custom Property Name** : Title
**Custom Property Type** : String

{{% alert color="primary" %}}

项目标题显示在目录、表格或图表列表中。
{{% /alert %}}

**Custom Property Name** : ListLevel
**Custom Property Type** : Integer

{{% alert color="primary" %}}

列出项目在目录中显示的级别。

{{% /alert %}}

{{% /alert %}}