---
title: PDF_A المطابقة
linktitle: PDF_A المطابقة
type: docs
weight: 100
url: /reportingservices/pdf_a-conformance/
description: تمكين توافق PDF/A في Aspose.PDF لخدمات التقارير. قم بإنشاء مستندات متوافقة مع الأرشيف دون عناء.
lastmod: "2025-05-22"
---

{{% alert color="primary" %}}

يمكنك الحصول على مقدمة حول توافق PDF/A (ملف PDF قابل للأرشفة) في وثائق Aspose.PDF.

إذا كنت تريد إنشاء مستند PDF/A، أضف معلمة التقرير التالية.

{{% /alert %}}

```text
Parameter Name: PdfConformance  
Date Type: String  
Values supported: PdfA1A, PdfA1B, PdfA2A, PdfA2B, PdfA2U, PdfA3A, PdfA3B, PdfA3U, PdfA4, PdfA4E, PdfA4F  
```

## مثال

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
