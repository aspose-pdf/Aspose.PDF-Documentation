---
title: الحاشية السفلية النهاية
type: docs
weight: 30
url: ar/reportingservices/footnote-endnote/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

لا يمكن لـ Report Builder تعيين الحاشية السفلية أو النهاية لمربعات النص. مع Aspose.Pdf لخدمات التقارير، يمكنك القيام بذلك بسهولة عن طريق إضافة خصائص مخصصة.

{{% /alert %}}

{{% alert color="primary" %}}
الحاشية السفلية
**اسم الخاصية المخصصة**: الحاشية السفلية
**قيمة الخاصية المخصصة**: *يجب أن تكون القيمة سلسلة نصية*

النهاية
**اسم الخاصية المخصصة**: النهاية
**قيمة الخاصية المخصصة**: *يجب أن تكون القيمة سلسلة نصية*

{{% alert color="primary" %}}
في المثال التالي، يحتوي التقرير على مربع نص بالقيمة 'AsposePdf4RS' ونريد إضافة وصف تكميلي في شكل حاشية سفلية بالنص "محرك PDF اختياري لـ SSRS من Aspose Pty. Ltd.".
{{% /alert %}}

**مثال**

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