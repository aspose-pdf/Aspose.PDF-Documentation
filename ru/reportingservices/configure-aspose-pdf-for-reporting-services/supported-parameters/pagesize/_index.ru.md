---
title: PageSize
type: docs
weight: 60
url: /reportingservices/pagesize/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Конструктор отчетов Reporting Services не поддерживает общие размеры страниц, такие как A4, B5, Letter и так далее. С Aspose.Pdf для Reporting Services вы можете получить это, как в следующем примере.

{{% /alert %}}

{{% alert color="primary" %}}

**Имя параметра**: PageSize  
**Тип данных**: String  
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