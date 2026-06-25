---
title: حجم هامش الصفحة
linktitle: حجم هامش الصفحة
type: docs
weight: 70
url: /ar/reportingservices/page-margin-size/
description: قم بضبط أحجام هوامش الصفحة في تقارير PDF باستخدام Aspose.PDF for Reporting Services لتحسين قابلية القراءة والتخطيط.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

مصمم تقارير Reporting Services لا يدعم ضبط حجم هوامش الصفحة. يوفر Aspose.Pdf for Reporting Services أربعة معلمات لتعيين حجم هامش الصفحة المقابل، وهي:

{{% /alert %}}

{{% alert color="primary" %}}
1)  
**اسم المعلمة**: PageMarginLeft  
**نوع التاريخ**: Float  
**القيم المدعومة**:  Any positive number or zero

2)  
**اسم المعامل**: PageMarginRight  
**نوع التاريخ**: Float  
**القيم المدعومة**:  Any positive number or zero

3)  
**اسم المعامل**: PageMarginTop  
**نوع التاريخ**: Float  
**القيم المدعومة**:  Any positive number or zero

4)  
**اسم المعامل**: PageMarginBottom  
**نوع التاريخ**: Float  
**القيم المدعومة**:  Any positive number or zero

**مثال**

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

