---
title: Tamanho da margem da página
linktitle: Tamanho da margem da página
type: docs
weight: 70
url: /pt/reportingservices/page-margin-size/
description: Ajuste os tamanhos das margens da página em relatórios PDF com Aspose.PDF for Reporting Services para melhorar a legibilidade e o layout.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

O designer de relatórios do Reporting Services não suporta a definição do tamanho das margens da página. Aspose.Pdf for Reporting Services fornece quatro parâmetros para definir o tamanho correspondente da margem da página, que são:

{{% /alert %}}

{{% alert color="primary" %}}
1)  
**Nome do parâmetro**: PageMarginLeft  
**Tipo de Dados**: Float  
**Valores suportados**:  Qualquer número positivo ou zero

2)  
**Nome do Parâmetro**: PageMarginRight  
**Tipo de Dados**: Float  
**Valores suportados**:  Qualquer número positivo ou zero

3)  
**Nome do Parâmetro**: PageMarginTop  
**Tipo de Dados**: Float  
**Valores suportados**:  Qualquer número positivo ou zero

4)  
**Nome do Parâmetro**: PageMarginBottom  
**Tipo de Dados**: Float  
**Valores suportados**:  Qualquer número positivo ou zero

**Exemplo**

{{< highlight csharp >}}

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

{{< /highlight >}}

{{% /alert %}}

