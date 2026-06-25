---
title: HTML 格式化
linktitle: HTML 格式化
type: docs
weight: 20
url: /zh/reportingservices/html-formatting/
description: 使用 Aspose.PDF for Reporting Services 在 PDF 报告中启用 HTML 格式化。轻松添加样式和结构。
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

有时您可能希望导出带有格式的文本框文本。遗憾的是，Reporting Services 不支持此功能。不过，您仍然可以使用 Aspose.PDF for Reporting Services 实现它。只需启用一种特殊模式，使所有文本框中的文本都被视为 HTML，并放置必要的 HTML 标记以在输出文档中格式化文本。例如，要在同一个文本框中拥有普通、粗体和斜体文本，请输入以下文本框值：

这段文字的一部分是 ```<b>bold</b>``` 以及其他文本是 ```<i>italic</i>```.

导出后，文本看起来会像这段文字的一部分是 **bold**，另一部分是 *italic*。

请注意，此方法有一些限制

{{% /alert %}}

{{% alert color="primary" %}}

- 在设计时（在 Report Builder、Reporting Services web portal 等）中，格式不可见。相反，您会看到以标签形式的纯文本 HTML 文本。
- Aspose.PDF for Reporting Services 渲染扩展能够识别并正确格式化文本框中的 HTML 代码。Reporting Services 的默认 PDF 渲染器会将此标记导出为纯文本。

**参数名称**: IsHtmlTagSupported  
**数据类型**: Boolean  
**支持的值**: True, False (default)   

**示例**

{{< highlight csharp >}}

 <Render>
...
    <Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices ">
    <Configuration>
    <IsHtmlTagSupported >True</IsHtmlTagSupported>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

如果您想在 Report Designer 中添加此参数，请使用 ‘Boolean’ 数据类型。

 
当前 Aspose.Pdf for Reporting Services 支持所有 HTML 标签的一个子集。您可以在 Aspose.PDF 中找到更多信息。 [文档](https://docs.aspose.com/pdf/net/add-text-to-pdf-file/#add-html-string-using-dom).

{{% /alert %}}

