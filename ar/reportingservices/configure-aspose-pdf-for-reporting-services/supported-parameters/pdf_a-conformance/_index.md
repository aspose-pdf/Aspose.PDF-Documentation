---
title: مطابقة PDF_A
linktitle: مطابقة PDF_A
type: docs
weight: 100
url: /ar/reportingservices/pdf_a-conformance/
description: تمكين مطابقة PDF/A في Aspose.PDF for Reporting Services. إنشاء مستندات متوافقة مع الأرشفة بسهولة.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

يمكنك الحصول على مقدمة حول مطابقة PDF/A (PDF القابل للأرشفة) في وثائق Aspose.PDF.

إذا كنت تريد إنشاء مستند PDF/A، أضف معلمة التقرير التالية.

{{% /alert %}}


{{% alert color="primary" %}}

**اسم المعامل**: PdfConformance  
**نوع البيانات**: String  
**القيم المدعومة**: PdfA1A, PdfA1B, PdfA2A, PdfA2B, PdfA2U, PdfA3A, PdfA3B, PdfA3U, PdfA4, PdfA4E, PdfA4F  

**مثال**
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

