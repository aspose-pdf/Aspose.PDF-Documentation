---
title: ページ余白サイズ
type: docs
weight: 70
url: /ja/reportingservices/page-margin-size/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Reporting Services レポートデザイナーはページ余白サイズの設定をサポートしていません。Aspose.Pdf for Reporting Services は対応するページ余白サイズを設定するための4つのパラメータを提供します。それらは次の通りです：

{{% /alert %}}

{{% alert color="primary" %}}
1)  
**パラメータ名**: PageMarginLeft  
**データタイプ**: Float  
**サポートされる値**: 任意の正の数またはゼロ

2)  
**パラメータ名**: PageMarginRight  
**データタイプ**: Float  
**サポートされる値**: 任意の正の数またはゼロ

3)  
**パラメータ名**: PageMarginTop  
**データタイプ**: Float  
**サポートされる値**: 任意の正の数またはゼロ

4)  
**パラメータ名**: PageMarginBottom  
**データタイプ**: Float  
**サポートされる値**: 任意の正の数またはゼロ

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
```