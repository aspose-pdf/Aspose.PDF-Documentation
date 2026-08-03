---
title: PDF_A 一致性
linktitle: PDF_A 一致性
type: docs
weight: 100
url: /reportingservices/pdf_a-conformance/
description: 在 Aspose.PDF for Reporting Services 中启用 PDF/A 一致性。轻松创建符合存档要求的文档。
lastmod: "2025-05-22"
---

{{% alert color="primary" %}}

您可以在 Aspose.PDF 文档中了解 PDF/A（可存档 PDF）一致性的介绍。

如果要创建 PDF/A 文档，请添加以下报告参数。

{{% /alert %}}

```text
Parameter Name: PdfConformance  
Date Type: String  
Values supported: PdfA1A, PdfA1B, PdfA2A, PdfA2B, PdfA2U, PdfA3A, PdfA3B, PdfA3U, PdfA4, PdfA4E, PdfA4F  
```

## 例子

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
