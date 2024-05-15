---
title: Footnote Endnote
type: docs
weight: 30
url: /reportingservices/footnote-endnote/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Report Builder cannot set the footnote or endnote for textboxes. With Aspose.Pdf for Reporting Services, you can do that easily by adding custom properties.

{{% /alert %}}

{{% alert color="primary" %}}
Footnote
**Custom Property** **Name**: Footnote
**Custom Property Value**: *the* *value* *should* *be* *a* *string*

Endnote
**Custom Property** **Name**: Endnote
**Custom Property Value**: *the* *value* *should* *be* *a* *string*

{{% alert color="primary" %}}
In the following example, the report contains a Textbox with the value 'AsposePdf4RS', and we want to add a supplementary description in the form of a footnote with text "An optional PDF renderer for SSRS from Aspose Pty. Ltd.".
{{% /alert %}}

**Example**

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
