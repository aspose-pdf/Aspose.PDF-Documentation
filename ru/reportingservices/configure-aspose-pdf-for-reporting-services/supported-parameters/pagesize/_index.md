---
title: РазмерСтраницы
linktitle: РазмерСтраницы
type: docs
weight: 60
url: /ru/reportingservices/pagesize/
description: Настройте размеры страниц для PDF‑отчетов в Aspose.PDF for Reporting Services, чтобы соответствовать конкретным требованиям к документу.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Конструктор отчетов Reporting Services не поддерживает обычные размеры страниц, такие как A4, B5, Letter и т.д. С помощью Aspose.Pdf for Reporting Services вы можете получить их, как показано в следующем примере.

{{% /alert %}}

{{% alert color="primary" %}}

**Имя параметра**: PageSize  
**Тип даты**: String  
**Поддерживаемые значения**: A0, A1, A2, A3, A4, A5, A6, B5, Letter, Legal, Ledger, P11x17  

**Пример**

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

