---
title: حاشية سفلية
linktitle: حاشية سفلية
type: docs
weight: 30
url: /reportingservices/footnote-endnote/
description: أضف الحواشي السفلية والتعليقات الختامية إلى تقارير PDF الخاصة بك باستخدام Aspose.PDF لخدمات التقارير. توفير مراجع وثيقة مفصلة.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

لا يمكن لمنشئ التقرير تعيين الحاشية السفلية أو التعليق الختامي لمربعات النص. باستخدام Aspose.PDF لخدمات التقارير، يمكنك القيام بذلك بسهولة عن طريق إضافة خصائص مخصصة.

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

في المثال التالي، يحتوي التقرير على مربع نص بالقيمة `AsposePdf4RS`، ونريد إضافة وصف تكميلي في شكل حاشية سفلية مع النص "عارض PDF اختياري لـ SSRS من Aspose Pty. Ltd.".

## مثال

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
