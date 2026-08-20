---
title: Выравнивание текста Justify FullJustify
linktitle: Выравнивание текста Justify FullJustify
type: docs
weight: 40
url: /ru/reportingservices/justify-fulljustify-text-alignment/
description: Достигните идеального выравнивания текста в PDF‑отчётах с Aspose.PDF for Reporting Services. Поддержка опций justify и full justify.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Report builder не поддерживает возможность задавать выравнивание текста для текстового поля «Justify» и «FullJustify». С Aspose.Pdf for Reporting Services вы можете легко сделать это, добавив пользовательские свойства.

{{% /alert %}}

{{% alert color="primary" %}}

```text
Custom Property `Name`: TextAlignment  
Custom Property `Type`: String  
Custom Property `Values`: Justify, FullJustify  
```

В отчете код должен выглядеть следующим образом:

**Пример**

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

{{% /alert %}}