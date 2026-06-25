---
title: PageSize
linktitle: PageSize
type: docs
weight: 60
url: /ja/reportingservices/pagesize/
description: Aspose.PDF for Reporting Services の PDF レポートのページサイズをカスタマイズして、特定のドキュメント要件に合わせます。
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Reporting Services のレポート デザイナーは、A4、B5、Letter などの一般的なページサイズをサポートしていません。Aspose.Pdf for Reporting Services を使用すると、以下の例のように取得できます。

{{% /alert %}}

{{% alert color="primary" %}}

**パラメータ名**: PageSize  
**Date Type**: 文字列  
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

