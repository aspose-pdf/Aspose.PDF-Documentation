---
title: Сноска
linktitle: Сноска
type: docs
weight: 30
url: /reportingservices/footnote-endnote/
description: Добавляйте сноски и концевые сноски в свои отчеты в формате PDF с помощью Aspose.PDF for Reporting Services. Предоставьте подробные ссылки на документы.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Построитель отчетов не может установить сноску или концевую сноску для текстовых полей. С помощью Aspose.PDF for Reporting Services вы можете легко сделать это, добавив пользовательские свойства.

{{% /alert %}}

```text
Footnote
Custom Property `Name`: Footnote
Custom Property Value: `the` `value` `should` `be` `a` `string`
```

```text
Endnote
Custom Property `Name`: Endnote
Custom Property Value: `the` `value` `should` `be` `a` `string`
```

В следующем примере отчет содержит текстовое поле со значением `AsposePdf4RS`, и мы хотим добавить дополнительное описание в виде сноски с текстом «Дополнительный модуль визуализации PDF для SSRS от Aspose Pty. Ltd.».

## Пример

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
