---
title: Ориентация страницы
linktitle: Ориентация страницы
type: docs
weight: 10
url: /reportingservices/page-orientation/
description: Настройте ориентацию страницы для отчетов в формате PDF в Aspose.PDF для служб Reporting Services. Настройте макеты для лучшего представления.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Язык определения отчета не позволяет явно указывать ориентацию страниц отчета. С помощью Aspose.PDF for Reporting Services вы можете легко поручить экспортеру создавать PDF-документы с альбомной ориентацией страниц. Ориентация по умолчанию — книжная.

{{% /alert %}}

```text
The default orientation is portrait.
Parameter Name: IsLandscape
Date Type: Boolean
Values supported: True, False (default)
```

## Пример

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

