---
title: Justify FullJustify Alinhamento de Texto
linktitle: Justify FullJustify Alinhamento de Texto
type: docs
weight: 40
url: /pt/reportingservices/justify-fulljustify-text-alignment/
description: Alcance um alinhamento de texto perfeito em relatórios PDF com Aspose.PDF for Reporting Services. Suporte para as opções justify e full justify.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

O construtor de relatórios não suporta a capacidade de especificar o alinhamento de texto para a caixa de texto “Justify” e “FullJustify”. Com Aspose.Pdf for Reporting Services, você pode fazer isso facilmente adicionando propriedades personalizadas.

{{% /alert %}}

{{% alert color="primary" %}}
**Nome da Propriedade Personalizada** : TextAlignment  
**Tipo de Propriedade Personalizada** : String  
**Valores da Propriedade Personalizada** : Justify, FullJustify  

No relatório, o código deve ser como o seguinte:

**Exemplo**

{{< highlight csharp >}}
<Textbox Name="textbox1">
<value> AsposePdf4RS </value>     
  <CustomProperties>
   <CustomProperty>
     <Name>TextAlignment</Name>
     <Value>Justify</Value>
   </CustomProperty>
  </CustomProperties>
</Textbox>
{{< /highlight >}}
{{% /alert %}}

