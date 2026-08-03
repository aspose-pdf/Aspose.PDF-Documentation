---
title: Page Orientation
linktitle: اتجاه الصفحة
type: docs
weight: 10
url: /reportingservices/page-orientation/
description: قم بتكوين اتجاه الصفحة لتقارير PDF في Aspose.PDF لخدمات التقارير. تخصيص التخطيطات لعرض أفضل.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

لغة تعريف التقرير لا تسمح بتحديد اتجاه الصفحات في التقرير بشكل صريح. باستخدام Aspose.PDF لخدمات التقارير، يمكنك بسهولة توجيه المُصدر لإنتاج مستندات PDF ذات اتجاه الصفحة الأفقي. الاتجاه الافتراضي هو عمودي.

{{% /alert %}}

```text
The default orientation is portrait.
Parameter Name: IsLandscape
Date Type: Boolean
Values supported: True, False (default)
```

## مثال

```xml
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
    </Extension>
</Render>
```

