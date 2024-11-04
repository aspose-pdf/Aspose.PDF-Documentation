---
title: ページの向き
type: docs
weight: 10
url: /reportingservices/page-orientation/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

レポート定義言語では、レポート内のページの向きを明示的に指定することはできません。Aspose.Pdf for Reporting Services を使用すると、エクスポーターに指示して横向きページのPDFドキュメントを簡単に作成することができます。デフォルトの向きは縦向きです。

{{% /alert %}}

{{% alert color="primary" %}}

デフォルトの向きは縦向きです。
**パラメータ名**: IsLandscape
**データ型**: Boolean
**サポートされる値**: True, False (デフォルト)

**例**
{{< highlight csharp >}}
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}