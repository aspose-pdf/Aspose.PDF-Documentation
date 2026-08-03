---
title: 脚注尾注
linktitle: 脚注尾注
type: docs
weight: 30
url: /reportingservices/footnote-endnote/
description: 使用 Aspose.PDF for Reporting Services 将脚注和尾注添加到 PDF 报告中。提供详细的文档参考。
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

报表生成器无法设置文本框的脚注或尾注。借助 Aspose.PDF for Reporting Services，您可以通过添加自定义属性轻松实现这一点。

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

在下面的示例中，报告包含一个值为 `AsposePdf4RS` 的文本框，我们希望以脚注的形式添加补充说明，其中包含文本“Aspose Pty. Ltd. 的 SSRS 的可选 PDF 渲染器”。

## 例子

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
