---
title: Tamanho da página
linktitle: PageSize
type: docs
weight: 60
url: /reportingservices/pagesize/
description: Personalize tamanhos de página para relatórios PDF no Aspose.PDF for Reporting Services para atender a requisitos específicos de documentos.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

O designer de relatórios do Reporting Services não oferece suporte a tamanhos de página comuns, como A4, B5, Carta e assim por diante. Com Aspose.PDF for Reporting Services, você pode obtê-lo como no exemplo a seguir.

{{% /alert %}}

```text
Parameter Name: PageSize  
Date Type: String  
Values supported: A0, A1, A2, A3, A4, A5, A6, B5, Letter, Legal, Ledger, P11x17  
```

## Exemplo

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