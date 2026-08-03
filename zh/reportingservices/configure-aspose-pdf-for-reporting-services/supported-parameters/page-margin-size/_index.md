---
title: 页边距大小
linktitle: 页边距大小
type: docs
weight: 70
url: /reportingservices/page-margin-size/
description: 使用 Aspose.PDF for Reporting Services 调整 PDF 报告中的页边距大小，以提高可读性和布局。
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Reporting Services 报表设计器不支持设置页边距大小。 Aspose.PDF for Reporting Services提供了四个参数来设置相应的页边距大小，它们是：

{{% /alert %}}

```text
Parameter Name: PageMarginLeft  
Date Type: Float  
Values supported:  Any positive number or zero
```

```text
Parameter Name: PageMarginRight  
Date Type: Float  
Values supported:  Any positive number or zero
```

```text
Parameter Name: PageMarginTop  
Date Type: Float  
Values supported:  Any positive number or zero
```

```text
Parameter Name: PageMarginBottom  
Date Type: Float  
Values supported:  Any positive number or zero
```

## 例子

```xml
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
```
