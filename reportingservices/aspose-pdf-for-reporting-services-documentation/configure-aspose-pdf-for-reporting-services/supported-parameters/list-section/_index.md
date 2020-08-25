---
title: List Section
type: docs
weight: 110
url: /reportingservices/list-section/
---


If you want to support creation of List Section, such as Table of Contents, List of Tables and so on, please add report parameter as the following:

{{% alert color="primary" %}} 

**Parameter Name**: IsListSectionSupported   
**Date Type**: Boolean   
**Values supported**: True, False(default)   

**Example**
{{< highlight csharp >}}

<Render>
...
<Extension Name="APPDF" Type="Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices">
<Configuration>
<IsListSectionSupported>True</IsListSectionSupported>
</Configuration>
</Extension>
</Render>

{{< /highlight >}}

{{% /alert %}} 