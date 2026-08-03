---
title: Taille de la page
linktitle: Taille de la page
type: docs
weight: 60
url: /reportingservices/pagesize/
description: Personnalisez la taille des pages des rapports PDF dans Aspose.PDF for Reporting Services afin de répondre aux exigences spécifiques des documents.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Le concepteur de rapports Reporting Services ne prend pas en charge les formats de page courants tels que A4, B5, Letter, etc. Avec Aspose.PDF pour Reporting Services, vous pouvez l'obtenir comme dans l'exemple suivant.

{{% /alert %}}

```text
Parameter Name: PageSize  
Date Type: String  
Values supported: A0, A1, A2, A3, A4, A5, A6, B5, Letter, Legal, Ledger, P11x17  
```

## Exemple

```xml
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <PageSize>A4</PageSize>
    </Configuration>
    </Extension>
</Render>
```
