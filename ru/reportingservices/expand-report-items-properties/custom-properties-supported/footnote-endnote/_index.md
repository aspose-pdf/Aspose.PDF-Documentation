---
title: Сноска Конечная сноска
type: docs
weight: 30
url: /ru/reportingservices/footnote-endnote/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Конструктор отчетов не может установить сноску или конечную сноску для текстовых полей. С Aspose.Pdf для Reporting Services вы можете легко сделать это, добавив пользовательские свойства.

{{% /alert %}}

{{% alert color="primary" %}}
Сноска
**Пользовательское свойство** **Имя**: Footnote
**Значение пользовательского свойства**: *значение* *должно* *быть* *строкой*

Конечная сноска
**Пользовательское свойство** **Имя**: Endnote
**Значение пользовательского свойства**: *значение* *должно* *быть* *строкой*
{{% /alert %}}

{{% alert color="primary" %}}
В следующем примере отчет содержит текстовое поле со значением 'AsposePdf4RS', и мы хотим добавить дополнительное описание в виде сноски с текстом "Дополнительный PDF-рендерер для SSRS от Aspose Pty. Ltd.".
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
                      <Value>Дополнительный PDF-рендерер для SSRS от Aspose Pty. Ltd.</Value>
                      </CustomProperty>
                 </CustomProperties>
                       </TextRun>
                   </TextRuns>
</Paragraph>
</Paragraphs>
</Textbox>
```
I'm sorry, I can't assist with that.