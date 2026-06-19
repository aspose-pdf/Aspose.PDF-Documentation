---
title: 脚注 尾注
linktitle: 脚注 尾注
type: docs
weight: 30
url: /zh/reportingservices/footnote-endnote/
description: 使用 Aspose.PDF for Reporting Services 为您的 PDF 报告添加脚注和尾注。提供详细的文档引用。
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Report Builder 无法为文本框设置脚注或尾注。使用 Aspose.Pdf for Reporting Services，您可以通过添加自定义属性轻松实现。

{{% /alert %}}

{{% alert color="primary" %}}
脚注
**Custom Property** **Name**: 脚注
**Custom Property Value**: *值* *应该* *是* *一个* *字符串*

尾注
**Custom Property** **Name**: 尾注
**Custom Property Value**: *值* *应该* *是* *一个* *字符串*

{{% alert color="primary" %}}
在下面的示例中，报表包含一个值为 'AsposePdf4RS' 的文本框，我们想要以脚注的形式添加补充说明，文本为 "An optional PDF renderer for SSRS from Aspose Pty. Ltd."。
{{% /alert %}}

**示例**

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

