---
title: XMP 元数据
type: docs
weight: 80
url: /zh/reportingservices/xmp-metadata/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Reporting Services 报表设计器不支持在文档中嵌入 XMP 元数据。Aspose.Pdf for Reporting Services 提供了四个参数来设置相应的 XMP 元数据，它们是：

{{% /alert %}}

{{% alert color="primary" %}}
**参数名称**: CreationDate  
**数据类型**: String  
**支持的值**: 日期格式之一的日期

**参数名称**: ModifyDate  
**数据类型**: String  
**支持的值**: 日期格式之一的日期

**参数名称**: MetaDataDate  
**数据类型**: String  
**支持的值**: 日期格式之一的日期

**参数名称**: CreatorTool  
**数据类型**: String  
**支持的值**: 任何纯文本  

**示例**
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