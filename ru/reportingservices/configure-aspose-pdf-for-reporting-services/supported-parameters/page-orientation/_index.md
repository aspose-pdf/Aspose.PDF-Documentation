---
title: Ориентация страницы
linktitle: Ориентация страницы
type: docs
weight: 10
url: /ru/reportingservices/page-orientation/
description: Настройте ориентацию страниц для PDF‑отчетов в Aspose.PDF for Reporting Services. Настраивайте макеты для лучшего отображения.
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Язык определения отчетов (Report Definition Language) не позволяет явно задавать ориентацию страниц в отчете. С помощью Aspose.PDF for Reporting Services вы можете легко указать экспортеру создавать PDF‑документы с альбомной ориентацией страниц. Ориентация по умолчанию — портретная.

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
    <IsLandscape>Истина</IsLandscape>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
