---
title: ページの向き
linktitle: ページの向き
type: docs
weight: 10
url: /ja/reportingservices/page-orientation/
description: Aspose.PDF for Reporting Services の PDF レポートのページ向きを設定します。レイアウトをカスタマイズして、プレゼンテーションを改善します。
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Report Definition Language は、レポート内のページの向きを明示的に指定することを許可していません。Aspose.PDF for Reporting Services を使用すると、エクスポーターに対して横向きページの PDF ドキュメントを生成するよう簡単に指示できます。デフォルトの向きは縦向きです。

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

