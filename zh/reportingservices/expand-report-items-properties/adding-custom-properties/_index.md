---
title: 添加自定义属性
linktitle: 添加自定义属性
type: docs
weight: 10
url: /reportingservices/adding-custom-properties/
description: 了解如何使用 Aspose.PDF for Reporting Services 将自定义属性添加到 PDF 报告。高效定制您的文档。
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

您可以为某些报表项添加自定义属性以扩展其用途，例如目录、线条箭头等。本节描述了这个过程。

{{% /alert %}}

您可以为某些报表项添加自定义属性以扩展其用途，例如目录、线条箭头等。本节描述了这个过程。

要添加自定义属性，您需要按照以下步骤编辑RDL文档的代码文件：

1. 如下图所示，打开项目，导航到解决方案资源管理器，右键单击所选的报告文件，然后选择“查看代码”菜单项。

![Add Custom Properties](adding-custom-properties_1.png)

2. 编辑 XML 代码文件。例如，如果要为图表报表项添加自定义属性，则需要添加类似于以下示例中红色文本的代码。

## 例子

```xml
<chart Name="chart1">
    <Left>5.5cm</Left>
    <Top>0.5cm</Top>
      ......
    <Style>
      ......
    </style>     
    <CustomProperties>
      <CustomProperty>
        <Name>IsInList</Name>
        <Value>True</Value>
      </CustomProperty>
    </CustomProperties>
</chart> 
```

在此代码片段示例中，自定义属性名称为 IsInList，值为 `True`。

