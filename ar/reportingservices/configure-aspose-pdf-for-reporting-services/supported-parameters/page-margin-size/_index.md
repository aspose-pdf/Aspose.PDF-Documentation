---
title: حجم هامش الصفحة
type: docs
weight: 70
url: /ar/reportingservices/page-margin-size/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

لا يدعم مصمم تقارير خدمات التقارير إعداد حجم هوامش الصفحة. يوفر Aspose.Pdf لخدمات التقارير أربعة معلمات لتعيين حجم الهامش المقابل للصفحة، وهي:

{{% /alert %}}

{{% alert color="primary" %}}
1)  
**اسم المعلمة**: PageMarginLeft  
**نوع البيانات**: Float  
**القيم المدعومة**: أي رقم موجب أو صفر

2)  
**اسم المعلمة**: PageMarginRight  
**نوع البيانات**: Float  
**القيم المدعومة**: أي رقم موجب أو صفر

3)  
**اسم المعلمة**: PageMarginTop  
**نوع البيانات**: Float  
**القيم المدعومة**: أي رقم موجب أو صفر

4)  
**اسم المعلمة**: PageMarginBottom  
**نوع البيانات**: Float  
**القيم المدعومة**: أي رقم موجب أو صفر

**مثال**

{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type=" Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices ">

    <Configuration>
```

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