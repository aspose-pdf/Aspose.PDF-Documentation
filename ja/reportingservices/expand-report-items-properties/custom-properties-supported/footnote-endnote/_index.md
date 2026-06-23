---
title: 脚注 エンドノート
linktitle: 脚注 エンドノート
type: docs
weight: 30
url: /ja/reportingservices/footnote-endnote/
description: Aspose.PDF for Reporting Services を使用して PDF レポートに脚注とエンドノートを追加します。詳細な文書参照を提供します。
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Report Builder はテキストボックスに脚注またはエンドノートを設定できません。Aspose.PDF for Reporting Services を使用すれば、カスタム プロパティを追加するだけで簡単に実行できます。

{{% /alert %}}

{{% alert color="primary" %}}
脚注
**Custom Property** **Name**: 脚注
**Custom Property Value**: *その* *値* *は* *なる* *1つの* *文字列*

エンドノート
**Custom Property** **Name**: エンドノート
**Custom Property Value**: *その* *値* *は* *なる* *1つの* *文字列*

{{% alert color="primary" %}}
以下の例では、レポートに値 'AsposePdf4RS' を持つテキストボックスが含まれており、脚注の形で "An optional PDF renderer for SSRS from Aspose Pty. Ltd." というテキストの補足説明を追加したいです。
{{% /alert %}}

**例**

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

