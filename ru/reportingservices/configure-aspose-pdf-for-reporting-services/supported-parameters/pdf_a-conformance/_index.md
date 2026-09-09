---
title: PDF_A Соответствие
linktitle: PDF_A Соответствие
type: docs
weight: 100
url: /ru/reportingservices/pdf_a-conformance/
description: Включите соответствие PDF/A в Aspose.PDF для служб Reporting Services. Легко создавайте архивные документы.
lastmod: "2025-05-22"
---

{{% alert color="primary" %}}

Вы можете получить введение в соответствие PDF/A (архивируемый PDF) в документации Aspose.PDF.

Если вы хотите создать документ PDF/A, добавьте следующий параметр отчета.

{{% /alert %}}

```text
Parameter Name: PdfConformance  
Date Type: String  
Values supported: PdfA1A, PdfA1B, PdfA2A, PdfA2B, PdfA2U, PdfA3A, PdfA3B, PdfA3U, PdfA4, PdfA4E, PdfA4F  
```

## Пример

```xml
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <PdfConformance>PdfA1A</PdfConformance>
    </Configuration>
    </Extension>
</Render>
```


