---
title: PageSize
type: docs
weight: 60
url: /reportingservices/pagesize/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

مصمم تقرير خدمات التقارير لا يدعم أحجام الصفحات الشائعة مثل A4 و B5 و Letter وما إلى ذلك. مع Aspose.Pdf لخدمات التقارير، يمكنك الحصول عليها كما في المثال التالي.

{{% /alert %}}

{{% alert color="primary" %}}

**اسم المعامل**: PageSize  
**نوع البيانات**: String  
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