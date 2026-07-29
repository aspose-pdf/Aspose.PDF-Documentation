---
title: Alinhamento de Texto Justify FullJustify
linktitle: Alinhamento de Texto Justify FullJustify
type: docs
weight: 40
url: /pt/reportingservices/justify-fulljustify-text-alignment/
description: Alcance o alinhamento de texto perfeito em relatórios PDF com Aspose.PDF for Reporting Services. Suporte para as opções de justificar e justificar totalmente.
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

O construtor de relatórios não oferece suporte à capacidade de especificar o alinhamento de texto para a caixa de texto “Justify” e “FullJustify”. Com Aspose.PDF for Reporting Services, você pode fazer isso facilmente adicionando propriedades personalizadas.

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
     <Name>AlinhamentoDeTexto</Name>
     <Value>Justificar</Value>
   </CustomProperty>
  </CustomProperties>
</Textbox>
{{< /highlight >}}
{{% /alert %}}
