---
title: Adicionando Propriedades Personalizadas
type: docs
weight: 10
url: /reportingservices/adding-custom-properties/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Você pode adicionar propriedades personalizadas para alguns itens de relatório para expandir seu uso, como Índice, setas de linha e assim por diante. Esta seção descreve este processo.

{{% /alert %}}

{{% alert color="primary" %}}

Você pode adicionar propriedades personalizadas para alguns itens de relatório para expandir seu uso, como Índice, setas de linha e assim por diante. Esta seção descreve este processo.

Para adicionar propriedades personalizadas, você precisa editar o arquivo de código do documento RDL nos seguintes passos:

1. Como na figura a seguir, abra seu projeto, navegue até o explorador de soluções e clique com o botão direito no arquivo de relatório selecionado, depois selecione o item de menu 'Ver Código'.

![todo:image_alt_text](adding-custom-properties_1.png)

2. Edite o arquivo de código XML. Por exemplo, se você quiser adicionar uma propriedade personalizada para um item de relatório de gráfico, você precisa adicionar o código semelhante ao texto em vermelho no exemplo a seguir.

**Example**

{{< highlight csharp >}}

<chart Name="chart1">
    <Left>5.5cm</Left>
    <Top>0.5cm</Top>
      ......
    <Style>
      ......
    </style>     
    <CustomProperties>
      <CustomProperty>
        <Name>IsInList</Name>
        <Value>True</Value>
      </CustomProperty>
    </CustomProperties>
</chart> 

{{< /highlight >}}

Neste exemplo de fragmento de código, o nome da propriedade personalizada é IsInList, e o valor é 'True'.

{{% /alert %}}