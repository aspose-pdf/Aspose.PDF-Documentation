---
title: Justify FullJustify Выравнивание текста
linktitle: Justify FullJustify Выравнивание текста
type: docs
weight: 40
url: /ru/reportingservices/justify-fulljustify-text-alignment/
description: Достигните идеального выравнивания текста в PDF‑отчетах с помощью Aspose.PDF for Reporting Services. Поддержка опций justify и full justify.
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Report builder не поддерживает возможность задавать выравнивание текста для текстового поля «Justify» и «FullJustify». С помощью Aspose.PDF for Reporting Services можно легко сделать это, добавив пользовательские свойства.

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
     <Name>Выравнивание текста</Name>
     <Value>Выровнять</Value>
   </CustomProperty>
  </CustomProperties>
</Textbox>
{{< /highlight >}}
{{% /alert %}}
