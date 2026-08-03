---
title: ページ余白サイズ
linktitle: ページ余白サイズ
type: docs
weight: 70
url: /reportingservices/page-margin-size/
description: Aspose.PDF for Reporting Services を使用して PDF レポートのページ余白サイズを調整し、読みやすさとレイアウトを向上させます。
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Reporting Services レポート デザイナーは、ページ余白サイズの設定をサポートしていません。 Aspose.PDF for Reporting Services には、対応するページ余白サイズを設定するための 4 つのパラメータが用意されています。

{{% /alert %}}

```text
Parameter Name: PageMarginLeft  
Date Type: Float  
Values supported:  Any positive number or zero
```

```text
Parameter Name: PageMarginRight  
Date Type: Float  
Values supported:  Any positive number or zero
```

```text
Parameter Name: PageMarginTop  
Date Type: Float  
Values supported:  Any positive number or zero
```

```text
Parameter Name: PageMarginBottom  
Date Type: Float  
Values supported:  Any positive number or zero
```

## 例

```xml
<Render>
…
    <Extension Name="APPDF" Type=" Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices ">
    <Configuration>
    <PageMarginLeft>50</PageMarginLeft>
    <PageMarginRight>50</PageMarginRight>
    <PageMarginTop>50</PageMarginTop>
    <PageMarginBottom>50</PageMarginBottom>
    </Configuration>
    </Extension>
</Render>
```
