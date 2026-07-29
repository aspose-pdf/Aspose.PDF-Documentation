---
title: ページサイズ
linktitle: ページサイズ
type: docs
weight: 60
url: /ja/reportingservices/pagesize/
description: Aspose.PDF for Reporting Services の PDF レポートでページサイズをカスタマイズし、特定のドキュメント要件を満たす。
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Reporting Services のレポート デザイナーは A4、B5、Letter などの一般的なページサイズをサポートしていません。Aspose.PDF for Reporting Services を使用すれば、以下の例のように実現できます。

{{% /alert %}}

{{% alert color="primary" %}}

**パラメータ名**: PageSize  
**日付タイプ**: String  
**サポートされる値**: A0, A1, A2, A3, A4, A5, A6, B5, Letter, Legal, Ledger, P11x17  

**例**

{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <PageSize>A4</PageSize>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
