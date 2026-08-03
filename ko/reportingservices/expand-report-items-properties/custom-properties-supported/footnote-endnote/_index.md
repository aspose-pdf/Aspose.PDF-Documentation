---
title: 각주 미주
linktitle: 각주 미주
type: docs
weight: 30
url: /reportingservices/footnote-endnote/
description: Reporting Services용 Aspose.PDF를 사용하여 PDF 보고서에 각주와 미주를 추가하세요. 자세한 문서 참조를 제공하십시오.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

보고서 작성기는 텍스트 상자의 각주나 미주를 설정할 수 없습니다. Reporting Services용 Aspose.PDF를 사용하면 사용자 지정 속성을 추가하여 쉽게 수행할 수 있습니다.

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

다음 예에서 보고서에는 `AsposePdf4RS` 값이 있는 텍스트 상자가 포함되어 있으며 "Aspose Pty. Ltd.의 SSRS용 선택적 PDF 렌더러"라는 텍스트가 있는 각주 형식의 보충 설명을 추가하려고 합니다.

## 예

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
