---
title: XMP Metadata
type: docs
weight: 80
url: /ar/reportingservices/xmp-metadata/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

مصمم تقارير خدمات التقارير لا يدعم تضمين بيانات XMP الوصفية في الوثيقة. يوفر Aspose.Pdf لخدمات التقارير أربعة معلمات لإعداد بيانات XMP الوصفية المقابلة، وهي:

{{% /alert %}}

{{% alert color="primary" %}}
**اسم المعلمة**: CreationDate  
**نوع التاريخ**: String  
**القيم المدعومة**: تاريخ في أحد تنسيقات التاريخ

**اسم المعلمة**: ModifyDate  
**نوع التاريخ**: String  
**القيم المدعومة**: تاريخ في أحد تنسيقات التاريخ 

**اسم المعلمة**: MetaDataDate  
**نوع التاريخ**: String  
**القيم المدعومة**: تاريخ في أحد تنسيقات التاريخ 

**اسم المعلمة**: CreatorTool  
**نوع التاريخ**: String  
**القيم المدعومة**: أي نص عادي  

**مثال**
{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer, Aspose.Pdf.ReportingServices">
    <Configuration>

    <CreationDate>2017-12-10</CreationDate>
```

<ModifyDate>2018-1-12</ModifyDate>
<MetaDataDate>2018-3-7</MetaDataDate>
<CreatorTool>Aspose.Pdf لخدمات التقارير</CreatorTool>
</Configuration>
</Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
```