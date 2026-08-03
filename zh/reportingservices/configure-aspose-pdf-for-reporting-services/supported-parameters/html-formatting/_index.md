---
title: HTML 格式
linktitle: HTML 格式
type: docs
weight: 20
url: /reportingservices/html-formatting/
description: 使用 Aspose.PDF for Reporting Services 在 PDF 报告中启用 HTML 格式。轻松添加样式和结构。
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

有时您可能希望导出带有格式的文本框中的文本。不幸的是，Reporting Services 不支持此功能。但是，您仍然可以使用 Aspose.PDF for Reporting Services 来实现它。只需启用一种特殊模式，在该模式中，文本框中的所有文本都被视为 HTML，并放置必要的 HTML 标签来格式化输出文档中的文本。例如，要在同一文本框中包含正常、粗体和斜体文本，请输入以下文本框值：

其中一些文本是`<b>bold</b>`，其他文本是`<i>italic</i>`。

导出时，文本将如下所示：其中一些文本为**粗体**，其他文本为*斜体*。

请注意，这种方法有一些限制

{{% /alert %}}

{{% alert color="primary" %}}

- 格式在设计时不可见（在报表生成器、Reporting Services Web 门户等中）。相反，您将看到带有标签的纯文本形式的 HTML 文本。
- Aspose.PDF for Reporting Services 渲染扩展可识别文本框中的 HTML 代码并正确设置其格式。 Reporting Services 的默认 PDF 渲染器会将此标记导出为纯文本。

```text
Parameter Name: IsHtmlTagSupported  
Date Type: Boolean  
Values supported: True, False (default)   
```

## 例子

```xml
<Render>
...
    <Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices ">
    <Configuration>
    <IsHtmlTagSupported >True</IsHtmlTagSupported>
    </Configuration>
    </Extension>
</Render>
```

如果要在报表设计器中添加此参数，请使用`Boolean` 数据类型。

目前 Aspose.Pdf for Reporting Services 支持所有 HTML 标签的子集。您可以在 Aspose.PDF [文档](https://docs.aspose.com/pdf/net/add-text-to-pdf-file/#add-html-string-using-dom) 中找到更多信息。

{{% /alert %}}
