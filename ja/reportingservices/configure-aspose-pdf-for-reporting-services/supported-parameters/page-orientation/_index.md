---
title: ページの向き
linktitle: ページの向き
type: docs
weight: 10
url: /ja/reportingservices/page-orientation/
description: Aspose.PDF for Reporting Services で PDF レポートのページ向きを構成します。レイアウトをカスタマイズして、より良いプレゼンテーションを実現します。
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Report Definition Language はレポート内のページの向きを明示的に指定することができません。Aspose.PDF for Reporting Services を使用すると、エクスポーターに対して横向きページの PDF ドキュメントを生成するよう簡単に指示できます。デフォルトの向きは縦向きです。

{{% /alert %}}

{{% alert color="primary" %}}

デフォルトの向きは縦向きです。
**パラメータ名**: IsLandscape
**データ型**: Boolean
**サポートされる値**: True, False (default)

**例**
{{< highlight csharp >}}
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <IsLandscape>真</IsLandscape>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
