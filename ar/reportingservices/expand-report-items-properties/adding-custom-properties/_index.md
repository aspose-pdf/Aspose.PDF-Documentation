---
title: إضافة خصائص مخصصة
linktitle: إضافة خصائص مخصصة
type: docs
weight: 10
url: /ar/reportingservices/adding-custom-properties/
description: تعرف على كيفية إضافة خصائص مخصصة لتقارير PDF باستخدام Aspose.PDF for Reporting Services. قم بتخصيص مستنداتك بكفاءة.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

يمكنك إضافة خصائص مخصصة لبعض عناصر التقرير لتوسيع استخدامها، مثل ToC وأسهم الخط وغيرها. يصف هذا القسم العملية.

{{% /alert %}}

{{% alert color="primary" %}}

يمكنك إضافة خصائص مخصصة لبعض عناصر التقرير لتوسيع استخدامها، مثل جدول المحتويات وأسهم الخط وغيرها. يصف هذا القسم العملية.

لإضافة خصائص مخصصة، تحتاج إلى تحرير ملف الكود لوثيقة RDL في الخطوات التالية:

1. كما هو موضح في الشكل التالي، افتح مشروعك، انتقل إلى مستكشف الحلول، وانقر بزر الماوس الأيمن على ملف التقرير المحدد، ثم اختر عنصر القائمة 'View Code'.

![todo:image_alt_text](adding-custom-properties_1.png)

2. حرر ملف كود XML. على سبيل المثال، إذا كنت ترغب في إضافة خاصية مخصصة لعنصر تقرير المخطط، تحتاج إلى إضافة الكود المشابه للنص الأحمر في المثال التالي.

**مثال**

{{< highlight csharp >}}

<chart Name="chart1">
    <Left>5.5cm</Left>
    <Top>0.5cm</Top>
      ......
    <Style>
      ......
    </style>     
    <CustomProperties>
      <CustomProperty>
        <Name>IsInList</Name>
        <Value>True</Value>
      </CustomProperty>
    </CustomProperties>
</chart> 

{{< /highlight >}}

في مثال مقطع الشيفرة هذا، اسم الخاصية المخصصة هو IsInList، والقيمة هي 'True'.

{{% /alert %}}

