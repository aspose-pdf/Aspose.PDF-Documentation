---
title: ページサイズ
linktitle: ページサイズ
type: docs
weight: 60
url: /reportingservices/pagesize/
description: 特定のドキュメント要件を満たすために、Aspose.PDF for Reporting Services の PDF レポートのページ サイズをカスタマイズします。
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Reporting Services レポート デザイナーは、A4、B5、レターなどの一般的なページ サイズをサポートしていません。 Aspose.PDF for Reporting Services を使用すると、次の例のように取得できます。

{{% /alert %}}

```text
Parameter Name: PageSize  
Date Type: String  
Values supported: A0, A1, A2, A3, A4, A5, A6, B5, Letter, Legal, Ledger, P11x17  
```

## 例

```xml
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <PageSize>A4</PageSize>
    </Configuration>
    </Extension>
</Render>
```