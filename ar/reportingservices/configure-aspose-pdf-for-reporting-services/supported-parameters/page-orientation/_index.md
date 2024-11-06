---
title: Page Orientation
type: docs
weight: 10
url: ar/reportingservices/page-orientation/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

لا يسمح تعريف لغة التقرير بتحديد اتجاه الصفحات في التقرير بشكل صريح. مع Aspose.Pdf لخدمات التقارير يمكنك بسهولة توجيه المصدّر لإنشاء مستندات PDF باتجاه الصفحة الأفقي. الاتجاه الافتراضي هو عمودي.

{{% /alert %}}

{{% alert color="primary" %}}

الاتجاه الافتراضي هو عمودي.
**اسم المعامل**: IsLandscape
**نوع البيانات**: Boolean
**القيم المدعومة**: True, False (default)

**مثال**
{{< highlight csharp >}}
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}