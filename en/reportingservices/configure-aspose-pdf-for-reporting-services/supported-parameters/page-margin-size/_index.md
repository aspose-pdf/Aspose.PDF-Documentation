---
title: Page margin size
linktitle: Page margin size
type: docs
weight: 70
url: /reportingservices/page-margin-size/
description: Adjust page margin sizes in PDF reports with Aspose.PDF for Reporting Services for improved readability and layout.
lastmod: "2026-08-31"
---

{{% alert color="primary" %}}

Reporting Services report designer does not support setting page margins size. Aspose.PDF for Reporting Services provides four parameters to set the corresponding page margin size, they are:

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

## Example

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
