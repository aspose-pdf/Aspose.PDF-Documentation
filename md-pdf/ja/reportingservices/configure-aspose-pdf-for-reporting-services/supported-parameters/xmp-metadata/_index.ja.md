---
title: XMP メタデータ
type: docs
weight: 80
url: /reportingservices/xmp-metadata/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Reporting Services レポートデザイナーは、ドキュメントに XMP メタデータを埋め込むことをサポートしていません。Aspose.Pdf for Reporting Services は、対応する XMP メタデータを設定するための4つのパラメーターを提供します。それらは次のとおりです:

{{% /alert %}}

{{% alert color="primary" %}}
**パラメーター名**: CreationDate  
**データタイプ**: String  
**サポートされる値**: 日付形式のいずれかの日付

**パラメーター名**: ModifyDate  
**データタイプ**: String  
**サポートされる値**: 日付形式のいずれかの日付

**パラメーター名**: MetaDataDate  
**データタイプ**: String  
**サポートされる値**: 日付形式のいずれかの日付

**パラメーター名**: CreatorTool  
**データタイプ**: String  
**サポートされる値**: 任意のプレーンテキスト  

**例**
{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer, Aspose.Pdf.ReportingServices">
    <Configuration>

    <CreationDate>2017-12-10</CreationDate>
```

<ModifyDate>2018-1-12</ModifyDate>
<MetaDataDate>2018-3-7</MetaDataDate>
<CreatorTool>Aspose.Pdf for Reporting Services</CreatorTool>
</Configuration>
</Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
```