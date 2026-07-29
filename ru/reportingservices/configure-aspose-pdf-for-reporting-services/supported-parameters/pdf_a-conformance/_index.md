---
title: Соответствие PDF_A
linktitle: Соответствие PDF_A
type: docs
weight: 100
url: /ru/reportingservices/pdf_a-conformance/
description: Включите соответствие PDF/A в Aspose.PDF for Reporting Services. Создавайте документы, соответствующие архивным требованиям, без усилий.
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Вы можете ознакомиться с введением в соответствие PDF/A (архивируемый PDF) в документации Aspose.PDF.

Если вы хотите создать документ PDF/A, добавьте следующий параметр отчета.

{{% /alert %}}


{{% alert color="primary" %}}

**Имя параметра**: PdfConformance  
**Тип данных**: String  
**Поддерживаемые значения**: PdfA1A, PdfA1B, PdfA2A, PdfA2B, PdfA2U, PdfA3A, PdfA3B, PdfA3U, PdfA4, PdfA4E, PdfA4F  

**Пример**
{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <PdfConformance>PdfA1A</PdfConformance>
    </Configuration>
    </Extension>
</Render>
{{< /highlight >}}

{{% /alert %}}
