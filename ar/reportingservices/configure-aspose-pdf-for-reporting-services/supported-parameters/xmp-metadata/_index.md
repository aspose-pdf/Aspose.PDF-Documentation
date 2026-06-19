---
title: بيانات XMP الوصفية
linktitle: بيانات XMP الوصفية
type: docs
weight: 80
url: /ar/reportingservices/xmp-metadata/
description: تعلم كيفية إدارة بيانات XMP الوصفية في تقارير PDF باستخدام Aspose.PDF لـ Reporting Services. حسّن التعامل مع بيانات المستند الوصفية.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

مصمم تقارير Reporting Services لا يدعم تضمين بيانات XMP الوصفية في المستند. يوفر Aspose.Pdf لـ Reporting Services أربعة معلمات لتعيين بيانات XMP الوصفية المقابلة، وهي:

{{% /alert %}}

{{% alert color="primary" %}}
**اسم المعامل**: CreationDate  
**نوع التاريخ**: String  
**القيم المدعومة**: التاريخ بأحد تنسيقات التاريخ

**اسم المعامل**: ModifyDate  
**نوع التاريخ**: String  
**القيم المدعومة**: التاريخ بأحد تنسيقات التاريخ 

**اسم المعامل**: MetaDataDate  
**نوع التاريخ**: String  
**القيم المدعومة**: التاريخ بأحد تنسيقات التاريخ 

**اسم المعامل**: CreatorTool  
**نوع التاريخ**: String  
**القيم المدعومة**: أي نص عادي  

**مثال**
{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer, Aspose.Pdf.ReportingServices">
    <Configuration>
    <CreationDate>2017-12-10</CreationDate>
    <ModifyDate>2018-1-12</ModifyDate>
    <MetaDataDate>2018-3-7</MetaDataDate>
    <CreatorTool>Aspose.Pdf for Reporting Services</CreatorTool>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}


