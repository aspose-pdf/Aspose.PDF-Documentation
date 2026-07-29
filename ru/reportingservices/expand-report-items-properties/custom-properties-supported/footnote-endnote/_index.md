---
title: Сноска Концевая сноска
linktitle: Сноска Концевая сноска
type: docs
weight: 30
url: /ru/reportingservices/footnote-endnote/
description: Добавьте сноски и концевые сноски в свои PDF‑отчёты с помощью Aspose.PDF for Reporting Services. Предоставьте подробные ссылки на документы.
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Report Builder не может установить сноску или концевую сноску для текстовых полей. С помощью Aspose.PDF for Reporting Services вы можете легко сделать это, добавив пользовательские свойства.

{{% /alert %}}

{{% alert color="primary" %}}
Сноска
**Пользовательское свойство** **Имя**: Сноска
**Значение пользовательского свойства**: *это* *значение* *должно* *быть* *одна* *строка*

Концевая сноска
**Пользовательское свойство** **Имя**: Концевая сноска
**Значение пользовательского свойства**: *это* *значение* *должно* *быть* *одна* *строка*

{{% alert color="primary" %}}
В следующем примере отчёт содержит Textbox со значением 'AsposePdf4RS', и мы хотим добавить дополнительное описание в виде сноски с текстом "An optional PDF renderer for SSRS from Aspose Pty. Ltd.".
{{% /alert %}}

**Пример**

```cs
<Textbox Name="Textbox1">
...
<Paragraphs>
              <Paragraph>
                   <TextRuns>
                       <TextRun>
                            ......
                            <Value>AsposePdf4RS</Value>
                            <Style>
                               ......
                            </Style>
                    <CustomProperties>
                 <CustomProperty>
                      <Name>Footnote</Name>
                      <Value>An optional PDF renderer for SSRS from Aspose Pty. Ltd.</Value>
                      </CustomProperty>
                 </CustomProperties>
                       </TextRun>
                   </TextRuns>
</Paragraph>
</Paragraphs>
</Textbox>
```
{{% /alert %}}
