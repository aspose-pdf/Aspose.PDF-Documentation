---
title: 각주 미주
linktitle: 각주 미주
type: docs
weight: 30
url: /ko/reportingservices/footnote-endnote/
description: Aspose.PDF for Reporting Services를 사용하여 PDF 보고서에 각주 및 미주를 추가하십시오. 자세한 문서 참조를 제공하십시오.
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Report Builder에서는 텍스트 상자에 각주 또는 미주를 설정할 수 없습니다. Aspose.PDF for Reporting Services를 사용하면 사용자 지정 속성을 추가하여 쉽게 수행할 수 있습니다.

{{% /alert %}}

{{% alert color="primary" %}}
각주
**맞춤 속성** **이름**: 각주
**맞춤 속성 값**: *그*\u00A0*값* *은*\u00A0*이어야*\u00A0*하나의*\u00A0*문자열*

미주
**맞춤 속성** **이름**: 미주
**맞춤 속성 값**: *그*\u00A0*값* *은*\u00A0*이어야* *하나의*\u00A0*문자열*

{{% alert color="primary" %}}
다음 예제에서는 보고서에 값이 'AsposePdf4RS'인 텍스트 상자가 포함되어 있으며, 여기서 텍스트 "An optional PDF renderer for SSRS from Aspose Pty. Ltd."를 각주의 형태로 보조 설명을 추가하고자 합니다.
{{% /alert %}}

**예제**

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
