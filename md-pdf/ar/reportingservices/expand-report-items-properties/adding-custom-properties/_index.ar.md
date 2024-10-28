---
title: Adding Custom Properties
type: docs
weight: 10
url: /reportingservices/adding-custom-properties/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

يمكنك إضافة خصائص مخصصة لبعض عناصر التقرير لتوسيع استخدامها، مثل جدول المحتويات، والأسهم الخطية وهكذا. يصف هذا القسم هذه العملية.

{{% /alert %}}

{{% alert color="primary" %}}

يمكنك إضافة خصائص مخصصة لبعض عناصر التقرير لتوسيع استخدامها، مثل جدول المحتويات، والأسهم الخطية وهكذا. يصف هذا القسم هذه العملية.

لإضافة خصائص مخصصة، تحتاج إلى تحرير ملف الكود لوثيقة RDL بالخطوات التالية:

1. كما في الشكل التالي، افتح مشروعك، وانتقل إلى مستكشف الحلول، وانقر بزر الماوس الأيمن على ملف التقرير المحدد، ثم اختر عنصر القائمة 'عرض الكود'.

![todo:image_alt_text](adding-custom-properties_1.png)

2. قم بتحرير ملف كود XML. على سبيل المثال، إذا كنت تريد إضافة خاصية مخصصة لعنصر تقرير المخطط البياني، تحتاج إلى إضافة الكود المشابه للنص الأحمر في المثال التالي.

**Example**

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

في مثال جزء الشيفرة هذا، اسم الخاصية المخصصة هو IsInList، والقيمة هي 'True'.