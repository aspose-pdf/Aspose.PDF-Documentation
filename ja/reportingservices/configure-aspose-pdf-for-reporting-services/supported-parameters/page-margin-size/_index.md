---
title: ページ余白サイズ
linktitle: ページ余白サイズ
type: docs
weight: 70
url: /ja/reportingservices/page-margin-size/
description: Aspose.PDF for Reporting Services を使用して PDF レポートのページ余白サイズを調整し、読みやすさとレイアウトを向上させます。
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Reporting Services のレポート デザイナーはページ余白サイズの設定をサポートしていません。Aspose.Pdf for Reporting Services は対応するページ余白サイズを設定するための4つのパラメータを提供しています。そのパラメータは次のとおりです：

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

