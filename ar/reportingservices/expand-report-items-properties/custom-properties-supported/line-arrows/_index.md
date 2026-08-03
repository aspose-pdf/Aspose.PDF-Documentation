---
title: سهام الخط
linktitle: سهام الخط
type: docs
weight: 20
url: /reportingservices/line-arrows/
description: تعرف على كيفية إضافة أسهم سطرية في تقارير PDF باستخدام Aspose.PDF لخدمات التقارير. تعزيز صور التقرير دون عناء.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

لا تحدد مواصفات RDL الأسهم الخاصة بعنصر السطر، لذا لا يدعم منشئ التقارير إعداد الأسهم للخط. مع Aspose.PDF لخدمات التقارير، يمكنك القيام بذلك بسهولة.

{{% /alert %}}

حاليًا، يدعم عارض Aspose.PDF إضافة أسهم في بداية أو نهاية الخطوط عن طريق إضافة خصائص مخصصة.

```text
Add Start Arrow for Line  
Custom Property `Name`: HasArrowAtStart  
Custom Property `Value`: True  
```

```text
Add End Arrow for Line  
Custom Property `Name`: HasArrowAtEnd  
Custom Property `Value`: True  
```

على سبيل المثال، هناك سطرين اسمه `line1` و `line2` في ملف التقرير الحالي، والسطر 1 يحتوي على سهم البداية، والسطر 2 يحتوي على أسهم البداية والنهاية، لتلبية هذه المتطلبات، يمكنك إضافة خصائص مخصصة كما في جزء التعليمات البرمجية التالي.

## مثال

```xml
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
```

