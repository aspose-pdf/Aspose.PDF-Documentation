---
title: ضبط محاذاة النص كاملة
type: docs
weight: 40
url: ar/reportingservices/justify-fulljustify-text-alignment/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

لا يدعم منشئ التقارير القدرة على تحديد محاذاة النص لصندوق النص "ضبط" و "ضبط كامل". باستخدام Aspose.Pdf لخدمات التقارير، يمكنك القيام بذلك بسهولة عن طريق إضافة خصائص مخصصة.

{{% /alert %}}

{{% alert color="primary" %}}
**اسم الخاصية المخصصة** : TextAlignment  
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
```