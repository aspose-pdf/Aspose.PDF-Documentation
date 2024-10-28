---
title: HTML Formatting
type: docs
weight: 20
url: /reportingservices/html-formatting/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

有时候您可能希望在文本框中导出带格式的文本。不幸的是，Reporting Services 不支持此功能。然而，您仍然可以使用 Aspose.PDF for Reporting Services 来实现这一点。只需启用一种特殊模式，其中文本框中的所有文本都被视为 HTML，并在输出文档中放置必要的 HTML 标签以格式化文本。例如，要在同一个文本框中拥有普通、加粗和斜体文本，请输入以下文本框值：

Some of this text is ```<b>bold</b>``` and other text is ```<i>italic</i>```.

导出后，文本将显示为部分文本是 **加粗** 和其他文本是 *斜体*。

请注意，这种方法有一些限制。

{{% /alert %}}

{{% alert color="primary" %}}

- 设计时（在报告生成器、Reporting Services Web 门户等）看不到格式。  相反，您将看到带有标签的纯文本形式的HTML文本。
- Aspose.PDF for Reporting Services 渲染扩展识别并正确格式化文本框中的HTML代码。Reporting Services的默认PDF渲染器会将此标记导出为纯文本。

**参数名称**: IsHtmlTagSupported  
**数据类型**: Boolean  
**支持的值**: True, False (默认)   

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

如果您想在报表设计器中添加此参数，请使用'Boolean'数据类型。

目前，Aspose.Pdf for Reporting Services 支持所有HTML标签的子集。您可以在Aspose.PDF [文档](https://docs.aspose.com/pdf/net/add-text-to-pdf-file/#add-html-string-using-dom)中找到更多信息。

{{% /alert %}}