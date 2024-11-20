---
title: PageSize
type: docs
weight: 60
url: /fr/reportingservices/pagesize/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Le concepteur de rapports Reporting Services ne prend pas en charge les tailles de page courantes telles que A4, B5, Lettre, etc. Avec Aspose.Pdf pour Reporting Services, vous pouvez l'obtenir comme dans l'exemple suivant.

{{% /alert %}}

{{% alert color="primary" %}}

**Nom du Paramètre**: PageSize  
**Type de Date**: String  
**Valeurs prises en charge**: A0, A1, A2, A3, A4, A5, A6, B5, Lettre, Legal, Ledger, P11x17  

**Exemple**

{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <PageSize>A4</PageSize>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
```