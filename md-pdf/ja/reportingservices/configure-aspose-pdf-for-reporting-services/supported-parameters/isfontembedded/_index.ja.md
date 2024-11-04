---
title: IsFontEmbedded
type: docs
weight: 50
url: /reportingservices/isfontembedded/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

RS デザイナーはテキストの埋め込みフォントをサポートしていませんが、Aspose.PDF for Reporting Services を使用すると、PDF ドキュメントにフォント情報を簡単に埋め込むことができます。

{{% /alert %}}

{{% alert color="primary" %}}
**パラメーター名**: IsFontEmbedded  
**データ型**: Boolean  
**サポートされている値**: True, False (デフォルト)  

**例**
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