---
title: اتجاه الصفحة
linktitle: اتجاه الصفحة
type: docs
weight: 10
url: /ar/reportingservices/page-orientation/
description: قم بتكوين اتجاه الصفحة لتقارير PDF في Aspose.PDF for Reporting Services. خصص التخطيطات للحصول على عرض أفضل.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

لغة تعريف التقرير لا تسمح بتحديد اتجاه صفحات التقرير صراحةً. باستخدام Aspose.PDF for Reporting Services يمكنك بسهولة إرشاد المُصدِّر لإنشاء مستندات PDF باتجاه صفحة عرضية. الاتجاه الافتراضي هو عمودي.

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

