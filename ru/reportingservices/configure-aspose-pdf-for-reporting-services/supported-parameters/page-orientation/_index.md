---
title: Page Orientation
type: docs
weight: 10
url: ru/reportingservices/page-orientation/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Язык определения отчетов не позволяет явно указывать ориентацию страниц в отчете. С помощью Aspose.Pdf для Reporting Services вы можете легко указать экспортеру создавать PDF-документы с альбомной ориентацией страницы. Ориентация по умолчанию — портретная.

{{% /alert %}}

{{% alert color="primary" %}}

Ориентация по умолчанию — портретная.
**Имя параметра**: IsLandscape
**Тип данных**: Boolean
**Поддерживаемые значения**: True, False (по умолчанию)

**Пример**
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