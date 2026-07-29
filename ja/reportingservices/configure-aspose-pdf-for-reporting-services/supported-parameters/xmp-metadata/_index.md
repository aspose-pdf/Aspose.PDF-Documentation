---
title: XMP メタデータ
linktitle: XMP メタデータ
type: docs
weight: 80
url: /ja/reportingservices/xmp-metadata/
description: Aspose.PDF for Reporting Services を使用して PDF レポートの XMP メタデータを管理する方法を学びます。ドキュメントのメタデータ処理を強化します。
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Reporting Services のレポート デザイナーは、ドキュメントへの XMP メタデータの埋め込みをサポートしていません。Aspose.PDF for Reporting Services は、対応する XMP メタデータを設定するための 4 つのパラメーターを提供します。それらは次のとおりです:

{{% /alert %}}

{{% alert color="primary" %}}
**パラメーター名**: CreationDate  
**日付タイプ**: 文字列  
**サポートされる値**: 日付形式のいずれかの日付

**パラメータ名**: ModifyDate  
**日付タイプ**: 文字列  
**サポートされる値**: 日付形式のいずれかの日付 

**パラメータ名**: MetaDataDate  
**日付タイプ**: 文字列  
**サポートされる値**: 日付形式のいずれかの日付 

**パラメータ名**: CreatorTool  
**日付タイプ**: 文字列  
**サポートされる値**: 任意のプレーンテキスト  

**例**
{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer, Aspose.Pdf.ReportingServices">
    <Configuration>
    <CreationDate>2017-12-10</CreationDate>
    <ModifyDate>2018-1-12</ModifyDate>
    <MetaDataDate>2018年3月7日</MetaDataDate>
    <CreatorTool>Aspose.PDF for Reporting Services</CreatorTool>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}

