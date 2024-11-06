---
title: Page Orientation
type: docs
weight: 10
url: pt/reportingservices/page-orientation/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

A Linguagem de Definição de Relatórios não permite especificar a orientação das páginas no relatório explicitamente. Com o Aspose.Pdf para Serviços de Relatórios, você pode facilmente instruir o exportador a produzir documentos PDF com orientação de página em paisagem. A orientação padrão é retrato.

{{% /alert %}}

{{% alert color="primary" %}}

A orientação padrão é retrato.
**Nome do Parâmetro**: IsLandscape
**Tipo de Dados**: Booleano
**Valores suportados**: True, False (padrão)

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