---
title: 脚注 尾注
type: docs
weight: 30
url: /reportingservices/footnote-endnote/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Report Builder 无法为文本框设置脚注或尾注。使用 Aspose.Pdf for Reporting Services，您可以通过添加自定义属性轻松实现。

{{% /alert %}}

{{% alert color="primary" %}}
脚注
**自定义属性** **名称**: Footnote
**自定义属性值**: *值应该是一个字符串*

尾注
**自定义属性** **名称**: Endnote
**自定义属性值**: *值应该是一个字符串*

{{% alert color="primary" %}}
在以下示例中，报告包含一个值为 'AsposePdf4RS' 的文本框，我们希望以脚注的形式添加补充说明，文本为 "An optional PDF renderer for SSRS from Aspose Pty. Ltd."。
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