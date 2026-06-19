---
title: Orientação da Página
linktitle: Orientação da Página
type: docs
weight: 10
url: /pt/reportingservices/page-orientation/
description: Configure a orientação da página para relatórios PDF no Aspose.PDF for Reporting Services. Personalize layouts para melhor apresentação.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Report Definition Language não permite especificar a orientação das páginas no relatório explicitamente. Com Aspose.Pdf for Reporting Services você pode instruir facilmente o exportador a gerar documentos PDF com orientação de página paisagem. A orientação padrão é retrato.

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
    <IsLandscape>True</IsLandscape>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}

