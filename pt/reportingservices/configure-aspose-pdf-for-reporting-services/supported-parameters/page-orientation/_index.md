---
title: Orientação da página
linktitle: Page Orientation
type: docs
weight: 10
url: /reportingservices/page-orientation/
description: Configure a orientação da página para relatórios PDF em Aspose.PDF para Reporting Services. Personalize layouts para uma melhor apresentação.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

A linguagem de definição de relatório não permite especificar explicitamente a orientação das páginas do relatório. Com Aspose.PDF for Reporting Services você pode facilmente instruir o exportador a produzir documentos PDF com orientação de página paisagem. A orientação padrão é retrato.

{{% /alert %}}

```text
The default orientation is portrait.
Parameter Name: IsLandscape
Date Type: Boolean
Values supported: True, False (default)
```

## Exemplo

```xml
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
    </Extension>
</Render>
```

