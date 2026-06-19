---
title: Adicionando Propriedades Personalizadas
linktitle: Adicionando Propriedades Personalizadas
type: docs
weight: 10
url: /pt/reportingservices/adding-custom-properties/
description: Aprenda como adicionar propriedades personalizadas a relatórios PDF com Aspose.PDF for Reporting Services. Personalize seus documentos de forma eficiente.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Você pode adicionar propriedades personalizadas para alguns itens de relatório para expandir seu uso, como ToC, setas de linha e assim por diante. Esta seção descreve esse processo.

{{% /alert %}}

{{% alert color="primary" %}}

Você pode adicionar propriedades personalizadas para alguns itens de relatório para expandir seu uso, como Índice, setas de linha e assim por diante. Esta seção descreve esse processo.

Para adicionar propriedades personalizadas, você precisa editar o arquivo de código do documento RDL nas seguintes etapas:

1. Conforme na figura a seguir, abra seu projeto, navegue até o Solution Explorer e clique com o botão direito no arquivo de relatório selecionado, então selecione o item de menu 'View Code'.

![todo:image_alt_text](adding-custom-properties_1.png)

2. Edite o arquivo de código XML. Por exemplo, se você quiser adicionar uma propriedade personalizada para o item de relatório de gráfico, você precisa adicionar o código semelhante ao texto em vermelho no exemplo a seguir.

**Exemplo**

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

Neste exemplo de fragmento de código, o nome da propriedade personalizada é IsInList e o valor é 'True'.

{{% /alert %}}

