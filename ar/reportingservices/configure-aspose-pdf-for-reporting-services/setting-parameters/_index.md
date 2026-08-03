---
title: إعداد المعلمات
linktitle: إعداد المعلمات
type: docs
weight: 10
url: /reportingservices/setting-parameters/
description: تعرف على كيفية تعيين المعلمات لعرض PDF في Aspose.PDF لخدمات التقارير. تحقيق التحكم الدقيق في الإخراج.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

يمكنك تحديد معلمات تكوين معينة تؤثر على كيفية قيام Aspose.PDF for Reporting Services بإنشاء المستندات. يصف هذا القسم هذه العملية.

{{% /alert %}}

لتكوين Aspose.Pdf لخدمات التقارير، تحتاج إلى تحرير الملف `C:\Program Files\Microsoft SQL Server\<Instance>\Reporting Services\ReportServer\rsreportserver.config`. هذا ملف XML وتكوين العارض موجود داخل العنصر `<Extension>` المطابق لعارض Aspose.PDF.

## مثال

```xml
<Render>
…
<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
<!--Insert configuration elements for exporting to PDF here. The following is an example
For PageOrientation -->
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
</Extension>
</Render>
```

{{% alert color="primary" %}}

إذا كنت تريد تعيين معلمات لملف تقرير معين ولكن ليس لكل تقرير على الخادم، فيمكنك إضافة معلمة تقرير لتقرير معين في أداة إنشاء التقارير بالخطوات التالية (على سبيل المثال، سنضيف معلمة "IsLandscape" الموضحة سابقًا):

1. افتح التقرير في مصمم التقارير، وانقر بزر الماوس الأيمن على مجلد "المعلمات" في جزء "بيانات التقرير"، وحدد "إضافة معلمة..." (أو، بدلاً من ذلك، اسحب القائمة "جديد" للأسفل وحدد "معلمة...").

![Parameters set up. Step 1](setting-parameters_1.png)

1. في مربع الحوار "خصائص معلمة التقرير"، قم بإنشاء المعلمة المسماة "IsLandscape"، بنوع البيانات المنطقية، وأضف القيمة True في علامة التبويب "القيم الافتراضية".

![Parameters set up. Step 2](setting-parameters_2.png)

{{% /alert %}}
