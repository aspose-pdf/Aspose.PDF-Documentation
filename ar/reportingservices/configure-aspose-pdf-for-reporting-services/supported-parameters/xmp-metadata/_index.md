---
title: بيانات تعريف XMP
linktitle: بيانات تعريف XMP
type: docs
weight: 80
url: /reportingservices/xmp-metadata/
description: تعرف على كيفية إدارة بيانات تعريف XMP في تقارير PDF باستخدام Aspose.PDF لخدمات التقارير. تحسين معالجة البيانات التعريفية للوثيقة.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

لا يدعم مصمم تقارير خدمات التقارير تضمين بيانات تعريف XMP في المستند. يوفر Aspose.PDF لخدمات التقارير أربع معلمات لتعيين بيانات تعريف XMP المقابلة، وهي:

{{% /alert %}}

```text
**Parameter Name: CreationDate  
**Date Type: String  
**Values supported: Date in one of the date formats
```

```text
**Parameter Name: ModifyDate  
**Date Type: String  
**Values supported: Date in one of the date formats 
```

```text
**Parameter Name: MetaDataDate  
**Date Type: String  
**Values supported: Date in one of the date formats 
```

```text
**Parameter Name: CreatorTool  
**Date Type: String  
**Values supported: Any plain text  
```

## مثال

```xml
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer, Aspose.Pdf.ReportingServices">
    <Configuration>
    <CreationDate>2017-12-10</CreationDate>
    <ModifyDate>2018-1-12</ModifyDate>
    <MetaDataDate>2018-3-7</MetaDataDate>
    <CreatorTool>Aspose.PDF for Reporting Services</CreatorTool>
    </Configuration>
    </Extension>
</Render>
```


