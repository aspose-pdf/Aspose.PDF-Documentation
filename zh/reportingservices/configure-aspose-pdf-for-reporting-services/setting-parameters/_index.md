```
title: 设置参数
type: docs
weight: 10
url: zh/reportingservices/setting-parameters/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

您可以指定某些配置参数，这些参数会影响 Aspose.Pdf for Reporting Services 如何生成文档。本节描述了此过程。

{{% /alert %}}

要配置 Aspose.Pdf for Reporting Services，您需要编辑 C:\Program Files\Microsoft SQL Server\<Instance>\Reporting Services\ReportServer\rsreportserver.config 文件。这是一个 XML 文件，渲染器配置在与 Aspose.PDF 渲染器对应的 ```<Extension>``` 元素中。

**示例**

{{< highlight csharp >}}

<Render>
…
<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
<!--在此处插入导出为 PDF 的配置元素。以下是一个示例
用于 PageOrientation -->
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
</Extension>
</Render>

{{< /highlight >}}


{{% alert color="primary" %}}
```

如果您想为特定报告文件设置参数，而不是为服务器上的每个报告设置参数，您可以按照以下步骤在报表生成器中为特定报告添加报表参数（例如，我们将添加前面显示的 'IsLandscape' 参数）：

1. 在报表设计器中打开报告，右键单击 '报表数据' 窗格中的 '参数' 文件夹，然后选择 '添加参数…'（或者，下拉 '新建' 列表并选择 '参数…'）。

![todo:image_alt_text](setting-parameters_1.png)

1. 在 '报表参数属性' 对话框中，创建名为 'IsLandscape' 的参数，数据类型为布尔型，并在 '默认值' 选项卡中添加值 True。

![todo:image_alt_text](setting-parameters_2.png)

{{% /alert %}}