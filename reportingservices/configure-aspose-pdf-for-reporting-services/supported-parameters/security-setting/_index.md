---
title: Security Setting
type: docs
weight: 30
url: /reportingservices/security-setting/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Security has always been the most important issue in every field, be it the protection of a network or a PDF document. Documents are made secure for many possible reasons: the writer of the document may like to keep the content of the document safe and doesn't want to allow others to change it, etc.

Aspose.Pdf for Reporting Services has taken much care of such security aspects by providing these features to developers that can be useful for them to protect their PDF documents. Therefore, it contains a number of parameters that allow developers to apply different security measures to PDF documents.

One of these measures is to password protect the PDF document during encryption. You can also restrict or allow contents modification, copying the content, document printing or allow/disable form filling. These features are at this time not supported by the default SQL Reporting Services PDF Exporter but you can implement these features using Aspose.Pdf for Reporting Services. Just add corresponding security parameters to a report or a report server configuration file, and you will be able to create secure PDF documents with limited privileges.

Currently, Aspose.Pdf for Reporting Services renderer supports following security attributes:

{{% /alert %}}

{{% alert color="primary" %}}

**Parameter Name**: User Password  
**Date Type**: String  
**Values supported**: Any plain text

**Parameter Name**: Master Password  
**Date Type**: String  
**Values supported**: Any plain text 

**Parameter Name**: IsCopyingAllowed  
**Date Type**: Boolean  
**Values supported**: True, False (default)  

**Parameter Name**: IsPrintingAllowed  
**Date Type**: Boolean  
**Values supported**: True, False (default)  

**Parameter Name**: IsContentsModifyingAllowed  
**Date Type**: Boolean  
**Values supported**: True, False (default)  

**Parameter Name**: IsFormFillingAllowed  
**Date Type**: Boolean  
**Values supported**: True, False (default)  

**Example**

{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <UserPassword>aspose</UserPassword>
    <IsCopyingAllowed>False</IsCopyingAllowed>
    <IsPrintingAllowed>False</IsPrintingAllowed>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
