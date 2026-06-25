---
title: 页面边距大小
linktitle: 页面边距大小
type: docs
weight: 70
url: /zh/reportingservices/page-margin-size/
description: 使用 Aspose.PDF for Reporting Services 调整 PDF 报告中的页面边距大小，以提高可读性和布局。
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Reporting Services 报表设计器不支持设置页面边距大小。Aspose.Pdf for Reporting Services 提供四个参数来设置相应的页面边距大小，它们是：

{{% /alert %}}

{{% alert color="primary" %}}
1)  
**参数名称**: PageMarginLeft  
**日期类型**: Float  
**支持的值**: 任何正数或零

2)  
**参数名称**: PageMarginRight  
**日期类型**: Float  
**支持的值**: 任何正数或零

3)  
**参数名称**: PageMarginTop  
**日期类型**: Float  
**支持的值**: 任何正数或零

4)  
**参数名称**: PageMarginBottom  
**日期类型**: Float  
**支持的值**: 任何正数或零

**示例**

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

