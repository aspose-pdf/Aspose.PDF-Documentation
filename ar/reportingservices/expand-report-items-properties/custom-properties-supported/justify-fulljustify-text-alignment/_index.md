---
title: ضبط كاملضبط محاذاة النص
linktitle: ضبط كاملضبط محاذاة النص
type: docs
weight: 40
url: /reportingservices/justify-fulljustify-text-alignment/
description: حقق محاذاة مثالية للنص في تقارير PDF باستخدام Aspose.PDF لخدمات التقارير. دعم خيارات التبرير والتبرير الكامل.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

لا يدعم منشئ التقارير القدرة على تحديد محاذاة النص لمربع النص `Justify` و `FullJustify`. باستخدام Aspose.PDF لخدمات التقارير، يمكنك القيام بذلك بسهولة عن طريق إضافة خصائص مخصصة.

{{% /alert %}}

```text
Custom Property `Name`: TextAlignment  
Custom Property `Type`: String  
Custom Property `Values`: Justify, FullJustify  
```

يجب أن يكون الكود في التقرير كما يلي:

## مثال

```xml
<Textbox Name="textbox1">
<value> AsposePdf4RS </value>     
  <CustomProperties>
   <CustomProperty>
     <Name>TextAlignment</Name>
     <Value>Justify</Value>
   </CustomProperty>
  </CustomProperties>
</Textbox>
```
