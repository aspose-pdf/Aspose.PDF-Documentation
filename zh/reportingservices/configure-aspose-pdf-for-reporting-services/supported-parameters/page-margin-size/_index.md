---
title: 页面边距大小
type: docs
weight: 70
url: zh/reportingservices/page-margin-size/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Reporting Services 报表设计器不支持设置页面边距大小。Aspose.Pdf for Reporting Services 提供了四个参数来设置相应的页面边距大小，它们是：

{{% /alert %}}

{{% alert color="primary" %}}
1)  
**参数名称**: PageMarginLeft  
**数据类型**: Float  
**支持的值**: 任何正数或零

2)  
**参数名称**: PageMarginRight  
**数据类型**: Float  
**支持的值**: 任何正数或零

3)  
**参数名称**: PageMarginTop  
**数据类型**: Float  
**支持的值**: 任何正数或零

4)  
**参数名称**: PageMarginBottom  
**数据类型**: Float  
**支持的值**: 任何正数或零

**例子**

{{< highlight csharp >}}

<Render>
â¦
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