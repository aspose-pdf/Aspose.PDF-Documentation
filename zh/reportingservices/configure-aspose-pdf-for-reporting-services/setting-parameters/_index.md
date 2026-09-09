---
title: 设置参数
linktitle: 设置参数
type: docs
weight: 10
url: /zh/reportingservices/setting-parameters/
description: 了解如何在 Aspose.PDF for Reporting Services 中设置 PDF 渲染参数，以便精确控制输出结果。
lastmod: "2026-08-31"
---

{{% alert color="primary" %}}

您可以指定某些配置参数，这些参数会影响 Aspose.PDF for Reporting Services 生成文档的方式。本节介绍该过程。

{{% /alert %}}

要配置 Aspose.PDF for Reporting Services，您需要编辑 `C:\Program Files\Microsoft SQL Server\<Instance>\Reporting Services\ReportServer\rsreportserver.config` 文件。该文件是 XML 文件，渲染器配置位于与 Aspose.PDF 渲染器对应的 ```<Extension>``` 元素内。

**示例**

{{< highlight csharp >}}

<Render>
...
<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
<!--Insert configuration elements for exporting to PDF here. The following is an example
For PageOrientation -->
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
</Extension>
</Render>

{{< /highlight >}}

{{% alert color="primary" %}}

如果您只想为某个特定报表文件设置参数，而不是为服务器上的每个报表都设置参数，则可以在 Report Builder 中为该报表添加报表参数。下面以添加前面展示的 `IsLandscape` 参数为例说明操作步骤。

1. 在 Report Designer 中打开报表，右键单击 `Report Data` 窗格中的 `Parameters` 文件夹，然后选择 `Add Parameter...`。或者，您也可以展开 `New` 列表并选择 `Parameter...`。
 
![todo:image_alt_text](setting-parameters_1.png)

1. 在 `Report Parameter Properties` 对话框中，创建名为 `IsLandscape` 的参数，将数据类型设置为 Boolean，并在 `Default Values` 选项卡中添加值 True。

![todo:image_alt_text](setting-parameters_2.png)

{{% /alert %}}

