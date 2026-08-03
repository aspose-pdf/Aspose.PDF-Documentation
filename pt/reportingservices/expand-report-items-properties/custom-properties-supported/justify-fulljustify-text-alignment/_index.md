---
title: Justificar FullJustify Alinhamento de Texto
linktitle: Justify FullJustify Text Alignment
type: docs
weight: 40
url: /reportingservices/justify-fulljustify-text-alignment/
description: Obtenha alinhamento de texto perfeito em relatórios PDF com Aspose.PDF for Reporting Services. Suporte para opções de justificação e justificação completa.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

O construtor de relatórios não suporta a capacidade de especificar o alinhamento de texto para caixa de texto `Justify` e `FullJustify`. Com Aspose.PDF for Reporting Services, você pode fazer isso facilmente adicionando propriedades personalizadas.

{{% /alert %}}

```text
Custom Property `Name`: TextAlignment  
Custom Property `Type`: String  
Custom Property `Values`: Justify, FullJustify  
```

No relatório o código deve ficar assim:

## Exemplo

```xml
<Textbox Name="textbox1">
<value> AsposePdf4RS </value>     
  <CustomProperties>
   <CustomProperty>
     <Name>TextAlignment</Name>
     <Value>Justify</Value>
   </CustomProperty>
  </CustomProperties>
</Textbox>
```
