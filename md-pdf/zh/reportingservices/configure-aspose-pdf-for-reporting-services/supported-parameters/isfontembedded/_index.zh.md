---
title: IsFontEmbedded
type: docs
weight: 50
url: /reportingservices/isfontembedded/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

RS 设计器不支持文本的嵌入字体；使用 Aspose.PDF for Reporting Services，您可以轻松地将字体信息嵌入到 PDF 文档中。

{{% /alert %}}

{{% alert color="primary" %}}
**参数名称**: IsFontEmbedded  
**数据类型**: Boolean  
**支持的值**: True, False (默认)  

**示例**
{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <IsFontEmbedded>True</IsFontEmbedded>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}