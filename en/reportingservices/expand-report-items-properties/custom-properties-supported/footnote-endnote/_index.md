---
title: Footnote Endnote
linktitle: Footnote Endnote
type: docs
weight: 30
url: /reportingservices/footnote-endnote/
description: Add footnotes and endnotes to your PDF reports with Aspose.PDF for Reporting Services. Provide detailed document references.
lastmod: "2026-08-31"
---

{{% alert color="primary" %}}

Report Builder cannot set the footnote or endnote for textboxes. With Aspose.PDF for Reporting Services, you can do that easily by adding custom properties.

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

In the following example, the report contains a Textbox with the value `AsposePdf4RS`, and we want to add a supplementary description in the form of a footnote with text "An optional PDF renderer for SSRS from Aspose Pty. Ltd.".

## Example

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
