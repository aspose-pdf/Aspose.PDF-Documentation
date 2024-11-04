---
title: الأسهم الخطية
type: docs
weight: 20
url: /reportingservices/line-arrows/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

مواصفات RDL لا تحدد الأسهم حول عنصر الخط، لذا فإن مُنشئ التقارير لا يدعم إعداد الأسهم للخط. باستخدام Aspose.Pdf لخدمات التقارير يمكنك القيام بذلك بسهولة.

{{% /alert %}}

{{% alert color="primary" %}}

حاليًا، يدعم عارض Aspose.PDF إضافة الأسهم في البداية أو النهاية للخطوط عن طريق إضافة خصائص مخصصة.

إضافة سهم بداية للخط  
**اسم الخاصية المخصصة**: HasArrowAtStart  
**قيمة الخاصية المخصصة**: True  

إضافة سهم نهاية للخط  
**اسم الخاصية المخصصة**: HasArrowAtEnd  
**قيمة الخاصية المخصصة**: True  

على سبيل المثال، هناك خطين باسم 'line1' و 'line2' في ملف التقرير الحالي، و line1 لديه سهم بداية، و line2 لديه سهم بداية ونهاية، لتلبية هذه المتطلبات، يمكنك إضافة خصائص مخصصة كما هو موضح في جزء الكود التالي.

**مثال**

{{< highlight csharp >}}

 <Line Name="line1">
```

<Style>
  ......
</style>
<CustomProperties>
  <CustomProperty>
    <Name>HasArrowAtStart</Name>
    <Value>True</Value>
  </CustomProperty>
</CustomProperties>
</Line>
......
<Line Name="line2">
<Style>
  ......
</style>
<CustomProperties>
  <CustomProperty>
    <Name>HasArrowAtStart</Name>
    <Value>True</Value>
  </CustomProperty>
  <CustomProperty>
    <Name>HasArrowAtEnd</Name>
    <Value>True</Value>
  </CustomProperty>
</CustomProperties>
</Line>

{{< /highlight >}}
{{% /alert %}}
```