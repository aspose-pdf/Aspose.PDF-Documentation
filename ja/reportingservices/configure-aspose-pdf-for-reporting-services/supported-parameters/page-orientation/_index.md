---
title: ページの向き
linktitle: ページの向き
type: docs
weight: 10
url: /reportingservices/page-orientation/
description: Aspose.PDF for Reporting Services で PDF レポートのページの向きを構成します。レイアウトをカスタマイズしてプレゼンテーションを改善します。
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

レポート定義言語では、レポート内のページの方向を明示的に指定することはできません。 Aspose.PDF for Reporting Services を使用すると、横向きのページ方向で PDF ドキュメントを作成するようにエクスポーターに簡単に指示できます。デフォルトの向きは縦向きです。

{{% /alert %}}

```text
The default orientation is portrait.
Parameter Name: IsLandscape
Date Type: Boolean
Values supported: True, False (default)
```

## 例

```xml
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
    </Extension>
</Render>
```

