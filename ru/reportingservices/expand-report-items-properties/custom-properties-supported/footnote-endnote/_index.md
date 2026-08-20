---
title: Сноска Конец сноски
linktitle: Сноска Конец сноски
type: docs
weight: 30
url: /ru/reportingservices/footnote-endnote/
description: Добавьте сноски и конечные сноски в ваши PDF‑отчёты с помощью Aspose.PDF for Reporting Services. Предоставьте детальные ссылки на документы.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Report Builder не может установить сноску или конец сноски для текстовых полей. С помощью Aspose.Pdf for Reporting Services вы можете легко сделать это, добавив пользовательские свойства.

{{% /alert %}}

{{% alert color="primary" %}}

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

{{% alert color="primary" %}}
В следующем примере отчет содержит Textbox со значением 'AsposePdf4RS', и мы хотим добавить дополнительное описание в виде сноски с текстом "An optional PDF renderer for SSRS from Aspose Pty. Ltd.".
{{% /alert %}}

**Пример**

```xml
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

