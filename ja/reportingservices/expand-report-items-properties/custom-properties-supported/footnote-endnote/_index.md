---
title: 脚注 エンドノート
linktitle: 脚注 エンドノート
type: docs
weight: 30
url: /ja/reportingservices/footnote-endnote/
description: Aspose.PDF for Reporting Services を使用して PDF レポートに脚注とエンドノートを追加します。詳細な文書参照を提供します。
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Report Builder ではテキストボックスに対して脚注またはエンドノートを設定できません。Aspose.PDF for Reporting Services を使用すれば、カスタム プロパティを追加するだけで簡単に設定できます。

{{% /alert %}}

{{% alert color="primary" %}}
脚注
**Custom Property** **Name**: 脚注
**Custom Property Value**: *その* *値* *は* *文字列* *である* *必要があります*

エンドノート
**Custom Property** **Name**: エンドノート
**Custom Property Value**: *その* *値* *は* *文字列* *である* *必要があります*

{{% alert color="primary" %}}
次の例では、レポートに 'AsposePdf4RS' という値を持つテキストボックスが含まれており、フットノートとしてテキスト "An optional PDF renderer for SSRS from Aspose Pty. Ltd." を付加した補足説明を追加したいです。
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
