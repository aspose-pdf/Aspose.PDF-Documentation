---
title: Выровнять полное выравнивание текста
linktitle: Выровнять полное выравнивание текста
type: docs
weight: 40
url: /reportingservices/justify-fulljustify-text-alignment/
description: Добейтесь идеального выравнивания текста в отчетах PDF с помощью Aspose.PDF для Reporting Services. Поддержка параметров выравнивания и полного выравнивания.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Построитель отчетов не поддерживает возможность указать выравнивание текста для текстового поля. `Justify` и `FullJustify`. С помощью Aspose.PDF for Reporting Services вы можете легко сделать это, добавив пользовательские свойства.

{{% /alert %}}

```text
Custom Property `Name`: TextAlignment  
Custom Property `Type`: String  
Custom Property `Values`: Justify, FullJustify  
```

В отчете код должен выглядеть следующим образом:

## Пример

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
