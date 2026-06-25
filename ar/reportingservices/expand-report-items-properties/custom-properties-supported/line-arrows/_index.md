---
title: أسهم الخط
linktitle: أسهم الخط
type: docs
weight: 20
url: /ar/reportingservices/line-arrows/
description: تعلم كيفية إضافة أسهم الخط في تقارير PDF باستخدام Aspose.PDF لخدمات التقارير. حسّن مظهر التقارير بسهولة.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

مواصفة RDL لا تحدد الأسهم لعناصر الخط، لذلك لا يدعم مُنشئ التقارير إعداد الأسهم للخط. باستخدام Aspose.Pdf لخدمات التقارير يمكنك القيام بذلك بسهولة.

{{% /alert %}}

{{% alert color="primary" %}}

حاليًا، يدعم مُعالج Aspose.PDF إضافة أسهم في بداية أو نهاية الخطوط عن طريق إضافة خصائص مخصصة.

إضافة سهم بداية للخط  
**خاصية مخصصة** **الاسم**: HasArrowAtStart  
**قيمة الخاصية المخصصة**: True  

إضافة سهم نهاية للخط  
**خاصية مخصصة** **الاسم**: HasArrowAtEnd  
**قيمة الخاصية المخصصة**: True  

على سبيل المثال، هناك خطان اسمهما 'line1' و 'line2' في ملف التقرير الحالي، والخط line1 يحتوي على سهم البداية، والخط line2 يحتوي على سهمي البداية والنهاية، لتلبية هذه المتطلبات، يمكنك إضافة الخصائص المخصصة كما هو موضح في المقتطف البرمجي التالي.

**مثال**

{{< highlight csharp >}}
 <Line Name="line1">
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

