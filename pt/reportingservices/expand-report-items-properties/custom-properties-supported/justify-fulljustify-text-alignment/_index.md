---
title: Justificar Alinhamento de Texto Completo
type: docs
weight: 40
url: /pt/reportingservices/justify-fulljustify-text-alignment/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

O construtor de relatórios não suporta a capacidade de especificar o alinhamento de texto para a caixa de texto “Justificar” e “Justificar Completo”. Com Aspose.Pdf para Serviços de Relatórios, você pode fazer isso facilmente adicionando propriedades personalizadas.

{{% /alert %}}

{{% alert color="primary" %}}
**Nome da Propriedade Personalizada** : TextAlignment  
**Tipo da Propriedade Personalizada** : String  
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