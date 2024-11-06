title: Setas de Linha
type: docs
weight: 20
url: pt/reportingservices/line-arrows/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

A especificação RDL não especifica as setas sobre o elemento de linha, portanto, o construtor de relatórios não suporta a configuração de setas para linha. Com Aspose.Pdf para Reporting Services, você pode fazer isso facilmente.

{{% /alert %}}

{{% alert color="primary" %}}

Atualmente, o renderizador Aspose.PDF suporta a adição de setas no início ou no final das linhas, adicionando propriedades personalizadas.

Adicionar Seta no Início da Linha  
**Nome da Propriedade Personalizada**: HasArrowAtStart  
**Valor da Propriedade Personalizada**: True  

Adicionar Seta no Final da Linha  
**Nome da Propriedade Personalizada**: HasArrowAtEnd  
**Valor da Propriedade Personalizada**: True  

Por exemplo, existem duas linhas chamadas 'line1' e 'line2' no arquivo de relatório atual, e line1 tem a seta inicial, line2 tem as setas inicial e final. Para satisfazer esses requisitos, você pode adicionar propriedades personalizadas conforme no fragmento de código a seguir.

**Exemplo**

{{< highlight csharp >}}

 <Line Name="line1">
```

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
```