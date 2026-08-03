---
title: 脚注 文末脚注
linktitle: 脚注 文末脚注
type: docs
weight: 30
url: /reportingservices/footnote-endnote/
description: Aspose.PDF for Reporting Services を使用して、PDF レポートに脚注と文末脚注を追加します。詳細なドキュメント参照を提供します。
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

レポート ビルダーは、テキストボックスの脚注または文末脚注を設定できません。 Aspose.PDF for Reporting Services を使用すると、カスタム プロパティを追加することでこれを簡単に行うことができます。

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

次の例では、レポートに次の値を含むテキストボックスが含まれています。 `AsposePdf4RS`、「Aspose Pty. Ltd. の SSRS 用のオプションの PDF レンダラー」というテキストを含む脚注の形式で補足説明を追加したいと考えています。

## 例

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
