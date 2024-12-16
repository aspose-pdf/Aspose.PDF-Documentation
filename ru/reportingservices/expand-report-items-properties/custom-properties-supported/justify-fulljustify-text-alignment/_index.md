---
title: Justify FullJustify Text Alignment
type: docs
weight: 40
url: /ru/reportingservices/justify-fulljustify-text-alignment/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Конструктор отчетов не поддерживает возможность указания выравнивания текста для текстового поля «Justify» и «FullJustify». С помощью Aspose.Pdf для служб отчетов вы можете легко это сделать, добавив пользовательские свойства.

{{% /alert %}}

{{% alert color="primary" %}}
**Имя пользовательского свойства** : TextAlignment  
**Тип пользовательского свойства** : String  
**Значения пользовательского свойства** : Justify, FullJustify  

В отчете код должен выглядеть следующим образом:

**Пример**

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