---
title: Setas de linha
linktitle: Line Arrows
type: docs
weight: 20
url: /reportingservices/line-arrows/
description: Aprenda a adicionar setas de linha em relatórios PDF usando Aspose.PDF para Reporting Services. Aprimore o visual do relatório sem esforço.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

A especificação RDL não especifica as setas sobre o elemento de linha, portanto, o construtor de relatórios não suporta a configuração de setas para linha. Com Aspose.PDF for Reporting Services você pode fazer isso facilmente.

{{% /alert %}}

Atualmente, o renderizador Aspose.PDF oferece suporte à adição de setas no início ou no final das linhas, adicionando propriedades personalizadas.

```text
Add Start Arrow for Line  
Custom Property `Name`: HasArrowAtStart  
Custom Property `Value`: True  
```

```text
Add End Arrow for Line  
Custom Property `Name`: HasArrowAtEnd  
Custom Property `Value`: True  
```

Por exemplo, existem duas linhas nomeadas `line1` e `line2` no arquivo de relatório atual, e a linha1 possui a seta inicial, a linha2 possui as setas inicial e final. Para atender a esses requisitos, você pode adicionar propriedades customizadas como no fragmento de código a seguir.

## Exemplo

```xml
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
```

