---
title: Tamanho da margem da página
linktitle: Page margin size
type: docs
weight: 70
url: /reportingservices/page-margin-size/
description: Ajuste os tamanhos das margens das páginas em relatórios PDF com Aspose.PDF para Reporting Services para melhorar a legibilidade e o layout.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

O designer de relatórios do Reporting Services não dá suporte à configuração do tamanho das margens da página. Aspose.PDF para Reporting Services fornece quatro parâmetros para definir o tamanho da margem da página correspondente, são eles:

{{% /alert %}}

```text
Parameter Name: PageMarginLeft  
Date Type: Float  
Values supported:  Any positive number or zero
```

```text
Parameter Name: PageMarginRight  
Date Type: Float  
Values supported:  Any positive number or zero
```

```text
Parameter Name: PageMarginTop  
Date Type: Float  
Values supported:  Any positive number or zero
```

```text
Parameter Name: PageMarginBottom  
Date Type: Float  
Values supported:  Any positive number or zero
```

## Exemplo

```xml
<Render>
…
    <Extension Name="APPDF" Type=" Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices ">
    <Configuration>
    <PageMarginLeft>50</PageMarginLeft>
    <PageMarginRight>50</PageMarginRight>
    <PageMarginTop>50</PageMarginTop>
    <PageMarginBottom>50</PageMarginBottom>
    </Configuration>
    </Extension>
</Render>
```
