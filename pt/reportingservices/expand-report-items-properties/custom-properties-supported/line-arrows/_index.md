---
title: Setas de Linha
linktitle: Setas de Linha
type: docs
weight: 20
url: /pt/reportingservices/line-arrows/
description: Aprenda a adicionar setas de linha em relatórios PDF usando Aspose.PDF for Reporting Services. Melhore os visuais dos relatórios sem esforço.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

A especificação RDL não especifica setas para o elemento de linha, portanto o report builder não oferece suporte à configuração de setas para linhas. Com Aspose.Pdf for Reporting Services você pode fazer isso facilmente.

{{% /alert %}}

{{% alert color="primary" %}}

Atualmente, o renderizador Aspose.PDF suporta a adição de setas no início ou no final de linhas adicionando propriedades personalizadas.

Adicionar seta inicial para a linha  
**Propriedade Personalizada** **Nome**: HasArrowAtStart  
**Valor da Propriedade Personalizada**: True  

Adicionar seta final para a linha  
**Propriedade Personalizada** **Nome**: HasArrowAtEnd  
**Valor da Propriedade Personalizada**: True  

Por exemplo, há duas linhas chamadas ‘line1’ e ‘line2’ no arquivo de relatório atual, e a line1 tem a seta inicial, a line2 tem as setas inicial e final; para atender a esses requisitos, você pode adicionar propriedades personalizadas como no fragmento de código a seguir.

**Exemplo**

{{< highlight csharp >}}
 <Line Name="line1">
    <Style>
      ......
    </style>
    <CustomProperties>
      <CustomProperty>
        <Name>HasArrowAtStart</Name>
        <Value>True</Value>
      </CustomProperty>
    </CustomProperties>
</Line>
......
<Line Name="line2">
    <Style>
      ......
    </style>
    <CustomProperties>
      <CustomProperty>
        <Name>HasArrowAtStart</Name>
        <Value>True</Value>
      </CustomProperty>
<CustomProperty>
        <Name>HasArrowAtEnd</Name>
        <Value>True</Value>
      </CustomProperty>
    </CustomProperties>
</Line>

{{< /highlight >}}
{{% /alert %}}

