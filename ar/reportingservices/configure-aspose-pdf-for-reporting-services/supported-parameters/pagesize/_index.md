---
title: PageSize
linktitle: PageSize
type: docs
weight: 60
url: /ar/reportingservices/pagesize/
description: قم بتخصيص أحجام الصفحات لتقارير PDF في Aspose.PDF لخدمات التقارير لتلبية متطلبات المستند المحددة.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

مصمم تقارير Reporting Services لا يدعم أحجام الصفحات الشائعة مثل A4 و B5 و Letter وما إلى ذلك. باستخدام Aspose.PDF لخدمات التقارير، يمكنك الحصول عليها كما هو موضح في المثال التالي.

{{% /alert %}}

{{% alert color="primary" %}}

**اسم المعامل**: PageSize  
**نوع التاريخ**: String  
**القيم المدعومة**: A0, A1, A2, A3, A4, A5, A6, B5, Letter, Legal, Ledger, P11x17  

**مثال**

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

