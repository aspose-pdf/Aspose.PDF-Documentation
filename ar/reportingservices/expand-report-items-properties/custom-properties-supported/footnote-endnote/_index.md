---
title: حاشية سفلية هامش نهائي
linktitle: حاشية سفلية هامش نهائي
type: docs
weight: 30
url: /ar/reportingservices/footnote-endnote/
description: أضف الحواشي السفلية والهوامش النهائية إلى تقارير PDF الخاصة بك باستخدام Aspose.PDF for Reporting Services. قدّم مراجع مستندات مفصلة.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

لا يمكن لبرنامج Report Builder تعيين الحاشية السفلية أو الهامش النهائي لمربعات النص. باستخدام Aspose.Pdf for Reporting Services، يمكنك القيام بذلك بسهولة عن طريق إضافة خصائص مخصصة.

{{% /alert %}}

{{% alert color="primary" %}}
حاشية سفلية
**خاصية مخصصة** **الاسم**: حاشية
**قيمة الخاصية المخصصة**: *ال* *قيمة* *يجب* *أن تكون* *سلسلة*

حاشية ختامية
**خاصية مخصصة** **الاسم**: حاشية ختامية
**قيمة الخاصية المخصصة**: *ال* *قيمة* *يجب* *أن تكون* *سلسلة*

{{% alert color="primary" %}}
في المثال التالي، يحتوي التقرير على مربع نص بالقيمة 'AsposePdf4RS'، ونريد إضافة وصف تكميلي على شكل حاشية بالنص "An optional PDF renderer for SSRS from Aspose Pty. Ltd.".
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

