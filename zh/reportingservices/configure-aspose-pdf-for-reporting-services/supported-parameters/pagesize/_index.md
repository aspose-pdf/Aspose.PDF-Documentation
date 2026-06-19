---
title: PageSize
linktitle: PageSize
type: docs
weight: 60
url: /zh/reportingservices/pagesize/
description: 定制 Aspose.PDF for Reporting Services 中 PDF 报告的页面尺寸，以满足特定文档需求。
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Reporting Services 报表设计器不支持常见的页面尺寸，如 A4、B5、Letter 等。使用 Aspose.Pdf for Reporting Services，您可以通过以下示例实现。

{{% /alert %}}

{{% alert color="primary" %}}

**参数名称**: PageSize  
**日期类型**: String  
**支持的值**: A0, A1, A2, A3, A4, A5, A6, B5, Letter, Legal, Ledger, P11x17  

**示例**

{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <PageSize>A4</PageSize>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}

