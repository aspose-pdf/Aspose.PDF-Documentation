---
title: حجم هامش الصفحة
linktitle: حجم هامش الصفحة
type: docs
weight: 70
url: /reportingservices/page-margin-size/
description: اضبط أحجام هوامش الصفحة في تقارير PDF باستخدام Aspose.PDF لخدمات التقارير لتحسين إمكانية القراءة والتخطيط.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

لا يدعم مصمم تقارير خدمات التقارير إعداد حجم هوامش الصفحة. يوفر Aspose.PDF لخدمات التقارير أربع معلمات لتعيين حجم هامش الصفحة المقابل، وهي:

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

## مثال

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
