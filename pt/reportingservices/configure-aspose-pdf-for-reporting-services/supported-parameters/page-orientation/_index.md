---
title: Orientação da página
linktitle: Orientação da página
type: docs
weight: 10
url: /pt/reportingservices/page-orientation/
description: Configure a orientação da página para relatórios PDF no Aspose.PDF for Reporting Services. Personalize layouts para melhor apresentação.
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Report Definition Language não permite especificar a orientação das páginas no relatório explicitamente. Com o Aspose.PDF for Reporting Services você pode instruir facilmente o exportador a produzir documentos PDF com orientação de página paisagem. A orientação padrão é retrato.

{{% /alert %}}

{{% alert color="primary" %}}

A orientação padrão é retrato.
**Nome do parâmetro**: IsLandscape
**Tipo de dado**: Boolean
**Valores suportados**: True, False (default)

**Exemplo**
{{< highlight csharp >}}
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <IsLandscape>Verdadeiro</IsLandscape>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
