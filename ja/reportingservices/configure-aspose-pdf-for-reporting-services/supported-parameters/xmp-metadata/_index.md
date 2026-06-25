---
title: XMP メタデータ
linktitle: XMP メタデータ
type: docs
weight: 80
url: /ja/reportingservices/xmp-metadata/
description: Aspose.PDF for Reporting Services を使用して PDF レポートの XMP メタデータを管理する方法を学びます。ドキュメントのメタデータ処理を強化します。
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Reporting Services のレポート デザイナーはドキュメントに XMP メタデータを埋め込むことをサポートしていません。Aspose.Pdf for Reporting Services は、対応する XMP メタデータを設定するための 4 つのパラメータを提供します。

{{% /alert %}}

{{% alert color="primary" %}}
**パラメータ名**: CreationDate  
**Date Type**: 文字列  
**Values supported**: 日付形式のいずれかの日付

**パラメータ名**: ModifyDate  
**Date Type**: 文字列  
**Values supported**: 日付形式のいずれかの日付 

**パラメータ名**: MetaDataDate  
**Date Type**: 文字列  
**Values supported**: 日付形式のいずれかの日付 

**パラメータ名**: CreatorTool  
**Date Type**: 文字列  
**Values supported**: 任意のプレーンテキスト  

**例**
{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer, Aspose.Pdf.ReportingServices">
    <Configuration>
    <CreationDate>2017-12-10</CreationDate>
    <ModifyDate>2018-1-12</ModifyDate>
    <MetaDataDate>2018-3-7</MetaDataDate>
    <CreatorTool>Aspose.Pdf for Reporting Services</CreatorTool>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}


