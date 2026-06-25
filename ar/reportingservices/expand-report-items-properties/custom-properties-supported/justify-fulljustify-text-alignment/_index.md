---
title: محاذاة النص مبرر ومبرر بالكامل
linktitle: محاذاة النص مبرر ومبرر بالكامل
type: docs
weight: 40
url: /ar/reportingservices/justify-fulljustify-text-alignment/
description: تحقق من محاذاة النص المثالية في تقارير PDF باستخدام Aspose.PDF لخدمات التقارير. يدعم خيارات المبرر والمبرر بالكامل.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

لا يدعم مُنشئ التقارير القدرة على تحديد محاذاة النص لصندوق النص “Justify” و “FullJustify”. باستخدام Aspose.Pdf لخدمات التقارير، يمكنك القيام بذلك بسهولة عن طريق إضافة خصائص مخصصة.

{{% /alert %}}

{{% alert color="primary" %}}
**اسم الخاصية المخصصة** : محاذاة النص  
**نوع الخاصية المخصصة** : String  
**قيم الخاصية المخصصة** : Justify, FullJustify  

في التقرير يجب أن يكون الكود كما يلي:

**مثال**

{{< highlight csharp >}}
<Textbox Name="textbox1">
<value> AsposePdf4RS </value>     
  <CustomProperties>
   <CustomProperty>
     <Name>TextAlignment</Name>
     <Value>Justify</Value>
   </CustomProperty>
  </CustomProperties>
</Textbox>
{{< /highlight >}}
{{% /alert %}}

