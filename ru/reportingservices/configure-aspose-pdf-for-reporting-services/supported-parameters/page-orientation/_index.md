---
title: Ориентация страницы
linktitle: Ориентация страницы
type: docs
weight: 10
url: /ru/reportingservices/page-orientation/
description: Настройте ориентацию страниц для PDF‑отчетов в Aspose.PDF for Reporting Services. Настройте макеты для лучшего представления.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Report Definition Language не позволяет явно указывать ориентацию страниц в отчете. С помощью Aspose.Pdf for Reporting Services вы можете легко указать экспортеру создавать PDF‑документы с альбомной ориентацией страниц. Ориентация по умолчанию — портретная.

{{% /alert %}}

{{% alert color="primary" %}}

Ориентация по умолчанию — портретная.
**Имя параметра**: IsLandscape
**Тип данных**: Boolean
**Поддерживаемые значения**: True, False (default)

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

