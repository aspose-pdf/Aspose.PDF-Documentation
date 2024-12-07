---
title: XMP Metadata
type: docs
weight: 80
url: /reportingservices/xmp-metadata/
description: Learn to manage XMP metadata in PDF reports using Aspose.PDF for Reporting Services. Enhance document metadata handling.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Reporting Services report designer does not support embedding XMP metadata in the document. Aspose.Pdf for Reporting Services provides four parameters to set the corresponding XMP metadata, they are:

{{% /alert %}}

{{% alert color="primary" %}}
**Parameter Name**: CreationDate  
**Date Type**: String  
**Values supported**: Date in one of the date formats

**Parameter Name**: ModifyDate  
**Date Type**: String  
**Values supported**: Date in one of the date formats 

**Parameter Name**: MetaDataDate  
**Date Type**: String  
**Values supported**: Date in one of the date formats 

**Parameter Name**: CreatorTool  
**Date Type**: String  
**Values supported**: Any plain text  

**Example**
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

