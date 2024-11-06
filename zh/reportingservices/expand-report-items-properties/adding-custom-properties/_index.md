---
title: 添加自定义属性
type: docs
weight: 10
url: zh/reportingservices/adding-custom-properties/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

您可以为某些报告项添加自定义属性以扩展其使用范围，例如目录、线箭头等。本节将描述此过程。

{{% /alert %}}

{{% alert color="primary" %}}

您可以为某些报告项添加自定义属性以扩展其使用范围，例如目录、线箭头等。本节将描述此过程。

要添加自定义属性，您需要按以下步骤编辑 RDL 文档的代码文件：

1. 如下图所示，打开您的项目，导航到解决方案资源管理器，右键单击所选的报告文件，然后选择“查看代码”菜单项。

![todo:image_alt_text](adding-custom-properties_1.png)

2. 编辑 XML 代码文件。例如，如果您想为图表报告项添加自定义属性，您需要添加类似于以下示例中红色文本的代码。

**Example**

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

在这个代码片段示例中，自定义属性名称是 IsInList，值是 'True'。

{{% /alert %}}