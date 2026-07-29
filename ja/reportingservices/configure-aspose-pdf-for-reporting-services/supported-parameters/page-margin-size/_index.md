---
title: ページ余白サイズ
linktitle: ページ余白サイズ
type: docs
weight: 70
url: /ja/reportingservices/page-margin-size/
description: Aspose.PDF for Reporting Services を使用して PDF レポートのページ余白サイズを調整し、可読性とレイアウトを向上させます。
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Reporting Services のレポート デザイナーはページ余白サイズの設定をサポートしていません。Aspose.PDF for Reporting Services は、対応するページ余白サイズを設定するための 4 つのパラメータを提供します。それらは次のとおりです：

{{% /alert %}}

{{% alert color="primary" %}}
1)  
**パラメータ名**: PageMarginLeft  
**日付型**: Float  
**サポートされる値**:  任意の正の数またはゼロ

2)  
**パラメータ名**: PageMarginRight  
**日付型**: Float  
**サポートされる値**:  任意の正の数またはゼロ

3)  
**パラメータ名**: PageMarginTop  
**日付型**: Float  
**サポートされる値**:  任意の正の数またはゼロ

4)  
**パラメータ名**: PageMarginBottom  
**日付型**: Float  
**サポートされる値**:  任意の正の数またはゼロ

**例**

{{< highlight csharp >}}

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

{{< /highlight >}}

{{% /alert %}}
