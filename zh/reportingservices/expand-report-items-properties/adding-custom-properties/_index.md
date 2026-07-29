---
title: 添加自定义属性
linktitle: 添加自定义属性
type: docs
weight: 10
url: /zh/reportingservices/adding-custom-properties/
description: 了解如何使用 Aspose.PDF for Reporting Services 向 PDF 报告添加自定义属性。高效地自定义您的文档。
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

您可以为某些报表项添加自定义属性，以扩展其用途，例如目录、线条箭头等。本节描述了此过程。

{{% /alert %}}

{{% alert color="primary" %}}

您可以为某些报表项添加自定义属性，以扩展其用途，例如目录、线条箭头等。本节描述了此过程。

要添加自定义属性，您需要按照以下步骤编辑 RDL 文档的代码文件：

1. 如下面的图所示，打开您的项目，导航到解决方案资源管理器，右键单击选中的报表文件，然后选择‘View Code’菜单项。

![todo:image_alt_text](adding-custom-properties_1.png)

2. 编辑 XML 代码文件。例如，如果您想为图表报表项添加自定义属性，您需要添加类似以下示例中红色文本的代码。

**示例**

{{< highlight csharp >}}

<chart Name="chart1">
    <Left>5.5厘米</Left>
    <Top>0.5厘米</Top>
      ......
    <Style>
      ......
    </style>     
    <CustomProperties>
      <CustomProperty>
        <Name>是否在列表中</Name>
        <Value>真</Value>
      </CustomProperty>
    </CustomProperties>
</chart> 

{{< /highlight >}}

在此代码片段示例中，自定义属性名称为 IsInList，值为 'True'。

{{% /alert %}}
