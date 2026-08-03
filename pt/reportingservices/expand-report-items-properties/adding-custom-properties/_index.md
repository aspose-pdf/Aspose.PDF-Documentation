---
title: Adicionando propriedades personalizadas
linktitle: Adding Custom Properties
type: docs
weight: 10
url: /reportingservices/adding-custom-properties/
description: Aprenda como adicionar propriedades personalizadas a relatórios PDF com Aspose.PDF para Reporting Services. Personalize seus documentos com eficiência.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Você pode adicionar propriedades personalizadas a alguns itens de relatório para expandir seu uso, como ToC, setas de linha e assim por diante. Esta seção descreve esse processo.

{{% /alert %}}

Você pode adicionar propriedades personalizadas a alguns itens de relatório para expandir seu uso, como Índice, setas de linha e assim por diante. Esta seção descreve esse processo.

Para adicionar propriedades customizadas, você precisa editar o arquivo de código do documento RDL nas seguintes etapas:

1. Como na figura a seguir, abra seu projeto, navegue até o gerenciador de soluções, clique com o botão direito no arquivo de relatório selecionado e selecione o item de menu 'Exibir código'.

![Adicionar propriedades personalizadas](adding-custom-properties_1.png)

2. Edite o arquivo de código XML. Por exemplo, se desejar adicionar uma propriedade customizada para o item de relatório gráfico, será necessário adicionar o código semelhante ao texto em vermelho no exemplo a seguir.

## Exemplo

```xml
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
```

Neste exemplo de fragmento de código, o nome da propriedade customizada é IsInList e o valor é `True`.

