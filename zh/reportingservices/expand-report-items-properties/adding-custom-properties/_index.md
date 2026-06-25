---
title: 添加自定义属性
linktitle: 添加自定义属性
type: docs
weight: 10
url: /zh/reportingservices/adding-custom-properties/
description: 了解如何使用 Aspose.PDF for Reporting Services 向 PDF 报告添加自定义属性。高效地自定义您的文档。
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

您可以为某些报表项添加自定义属性，以扩展它们的用途，例如 ToC、线条箭头等。本节介绍此过程。

{{% /alert %}}

{{% alert color="primary" %}}

您可以为某些报表项添加自定义属性，以扩展它们的用途，例如目录、线条箭头等。本节介绍此过程。

要添加自定义属性，您需要按照以下步骤编辑 RDL 文档的代码文件：

1. 如以下图所示，打开您的项目，导航至解决方案资源管理器，右键单击所选的报告文件，然后选择 'View Code' 菜单项。

![todo:image_alt_text](adding-custom-properties_1.png)

2. 编辑 XML 代码文件。例如，如果您想为图表报告项添加自定义属性，则需要在下面示例中添加类似红色文本的代码。

**示例**

{{< highlight csharp >}}

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

{{< /highlight >}}

在此代码片段示例中，自定义属性名称是 IsInList，值为 'True'。

{{% /alert %}}

