---
title: 页面大小
linktitle: 页面大小
type: docs
weight: 60
url: /reportingservices/pagesize/
description: 在 Aspose.PDF for Reporting Services 中自定义 PDF 报告的页面大小，以满足特定的文档要求。
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Reporting Services 报表设计器不支持常见的页面尺寸，例如 A4、B5、Letter 等。使用 Aspose.PDF for Reporting Services，您可以按照以下示例获取它。

{{% /alert %}}

```text
Parameter Name: PageSize  
Date Type: String  
Values supported: A0, A1, A2, A3, A4, A5, A6, B5, Letter, Legal, Ledger, P11x17  
```

## 例子

```xml
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <PageSize>A4</PageSize>
    </Configuration>
    </Extension>
</Render>
```
