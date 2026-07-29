---
title: Setas de Linha
linktitle: Setas de Linha
type: docs
weight: 20
url: /pt/reportingservices/line-arrows/
description: Aprenda a adicionar setas de linha em relatórios PDF usando Aspose.PDF for Reporting Services. Melhore os visuais dos relatórios sem esforço.
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

A especificação RDL não define as setas para o elemento de linha, portanto o construtor de relatórios não suporta a configuração de setas para linhas. Com o Aspose.PDF for Reporting Services você pode fazer isso facilmente.

{{% /alert %}}

{{% alert color="primary" %}}

Atualmente, o renderizador Aspose.PDF suporta a adição de setas no início ou no final das linhas, adicionando propriedades personalizadas.

Adicionar seta de início para a linha  
**Propriedade Personalizada** **Nome**: HasArrowAtStart  
**Valor da Propriedade Personalizada**: True  

Adicionar seta de fim para a linha  
**Propriedade Personalizada** **Nome**: HasArrowAtEnd  
**Valor da Propriedade Personalizada**: True  

Por exemplo, há duas linhas chamadas 'line1' e 'line2' no arquivo de relatório atual, e line1 tem a seta de início, line2 tem as setas de início e fim; para atender a esses requisitos, você pode adicionar propriedades personalizadas como no fragmento de código a seguir.

**Exemplo**

{{< highlight csharp >}}
 <Line Name="line1">
    <Style>
      ......
    </style>
    <CustomProperties>
      <CustomProperty>
        <Name>TemSetaNoInício</Name>
        <Value>Verdadeiro</Value>
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
        <Name>TemSetaNoInício</Name>
        <Value>Verdadeiro</Value>
      </CustomProperty>
<CustomProperty>
        <Name>TemSetaNoFim</Name>
        <Value>Verdadeiro</Value>
      </CustomProperty>
    </CustomProperties>
</Line>

{{< /highlight >}}
{{% /alert %}}
