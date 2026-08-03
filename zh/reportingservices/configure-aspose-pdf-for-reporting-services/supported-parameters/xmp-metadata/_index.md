---
title: XMP元数据
linktitle: XMP元数据
type: docs
weight: 80
url: /reportingservices/xmp-metadata/
description: 了解使用 Aspose.PDF for Reporting Services 管理 PDF 报告中的 XMP 元数据。增强文档元数据处理。
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Reporting Services 报表设计器不支持在文档中嵌入 XMP 元数据。 Aspose.PDF for Reporting Services提供了四个参数来设置相应的XMP元数据，它们是：

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

## 例子

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


