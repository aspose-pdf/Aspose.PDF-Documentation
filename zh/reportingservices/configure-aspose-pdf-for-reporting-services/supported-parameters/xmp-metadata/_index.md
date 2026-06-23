---
title: XMP 元数据
linktitle: XMP 元数据
type: docs
weight: 80
url: /zh/reportingservices/xmp-metadata/
description: 学习使用 Aspose.PDF for Reporting Services 在 PDF 报告中管理 XMP 元数据。提升文档元数据处理。
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Reporting Services 报表设计器不支持在文档中嵌入 XMP 元数据。Aspose.Pdf for Reporting Services 提供四个参数来设置相应的 XMP 元数据，它们是：

{{% /alert %}}

{{% alert color="primary" %}}
**参数名称**: CreationDate  
**日期类型**: 字符串  
**支持的值**: 日期，使用其中一种日期格式

**参数名称**: ModifyDate  
**日期类型**: 字符串  
**支持的值**: 日期，使用其中一种日期格式 

**参数名称**: MetaDataDate  
**日期类型**: 字符串  
**支持的值**: 日期，使用其中一种日期格式 

**参数名称**: CreatorTool  
**日期类型**: 字符串  
**支持的值**: 任意纯文本  

**示例**
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


