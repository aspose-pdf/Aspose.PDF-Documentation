---
title: PDF_A Conformance
type: docs
weight: 100
url: /reportingservices/pdf_a-conformance/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Вы можете получить введение в соответствие PDF/A (архивируемого PDF) в документации Aspose.PDF.

Если вы хотите создать документ PDF/A, добавьте следующий параметр отчета.

{{% /alert %}}


{{% alert color="primary" %}}

**Имя параметра**: PdfConformance  
**Тип данных**: String  
**Поддерживаемые значения**: PdfA1A, PdfA1B, PdfA2A, PdfA2B, PdfA2U, PdfA3A, PdfA3B, PdfA3U  

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