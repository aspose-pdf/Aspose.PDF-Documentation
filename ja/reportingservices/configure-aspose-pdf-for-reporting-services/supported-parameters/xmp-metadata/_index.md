---
title: XMPメタデータ
linktitle: XMPメタデータ
type: docs
weight: 80
url: /reportingservices/xmp-metadata/
description: Aspose.PDF for Reporting Services を使用して PDF レポート内の XMP メタデータを管理する方法を学びます。ドキュメントのメタデータ処理を強化します。
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Reporting Services レポート デザイナーは、ドキュメントへの XMP メタデータの埋め込みをサポートしていません。 Aspose.PDF for Reporting Services には、対応する XMP メタデータを設定するための 4 つのパラメータが用意されています。

{{% /alert %}}

```text
**Parameter Name: CreationDate  
**Date Type: String  
**Values supported: Date in one of the date formats
```

```text
**Parameter Name: ModifyDate  
**Date Type: String  
**Values supported: Date in one of the date formats 
```

```text
**Parameter Name: MetaDataDate  
**Date Type: String  
**Values supported: Date in one of the date formats 
```

```text
**Parameter Name: CreatorTool  
**Date Type: String  
**Values supported: Any plain text  
```

## 例

```xml
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer, Aspose.Pdf.ReportingServices">
    <Configuration>
    <CreationDate>2017-12-10</CreationDate>
    <ModifyDate>2018-1-12</ModifyDate>
    <MetaDataDate>2018-3-7</MetaDataDate>
    <CreatorTool>Aspose.PDF for Reporting Services</CreatorTool>
    </Configuration>
    </Extension>
</Render>
```


