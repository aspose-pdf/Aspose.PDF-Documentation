---
title: PDF_A Conformance
type: docs
weight: 100
url: /reportingservices/pdf_a-conformance/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

يمكنك الحصول على مقدمة حول توافق PDF/A (PDF المؤرشف) في وثائق Aspose.PDF.

إذا كنت تريد إنشاء مستند PDF/A، أضف معلمة التقرير التالية.

{{% /alert %}}


{{% alert color="primary" %}}

**اسم المعلمة**: PdfConformance  
**نوع البيانات**: String  
**القيم المدعومة**: PdfA1A, PdfA1B, PdfA2A, PdfA2B, PdfA2U, PdfA3A, PdfA3B, PdfA3U  

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