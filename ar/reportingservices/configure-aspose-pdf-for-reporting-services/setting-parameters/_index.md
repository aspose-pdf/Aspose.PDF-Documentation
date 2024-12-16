```
title: إعداد المعلمات
type: docs
weight: 10
url: /ar/reportingservices/setting-parameters/
lastmod: "2021-06-05"
```

{{% alert color="primary" %}}

يمكنك تحديد معلمات تكوين معينة تؤثر على كيفية توليد Aspose.Pdf لـ Reporting Services للوثائق. يصف هذا القسم هذه العملية.

{{% /alert %}}

لتكوين Aspose.Pdf لـ Reporting Services، تحتاج إلى تحرير ملف C:\Program Files\Microsoft SQL Server\<Instance>\Reporting Services\ReportServer\rsreportserver.config. هذا ملف XML وتكوين العارض موجود داخل عنصر ```<Extension>``` المقابل لعارض Aspose.PDF.

**مثال**

{{< highlight csharp >}}

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

{{< /highlight >}}


{{% alert color="primary" %}}

إذا كنت تريد إعداد معلمات لملف تقرير محدد ولكن ليس لكل تقرير على الخادم، يمكنك إضافة معلمة تقرير للتقرير المحدد في مُنشئ التقارير بالخطوات التالية (على سبيل المثال، سنضيف معلمة 'IsLandscape' الموضحة سابقًا):

1. افتح التقرير في مصمم التقارير، انقر بزر الماوس الأيمن على مجلد 'Parameters' في لوحة 'Report Data'، واختر 'Add Parameter…' (أو، بدلاً من ذلك، اسحب قائمة 'New' واختر 'Parameter…').

![todo:image_alt_text](setting-parameters_1.png)

1. في مربع الحوار 'Report Parameter Properties'، أنشئ المعلمة المسماة 'IsLandscape'، مع نوع البيانات Boolean، وأضف القيمة True في علامة تبويب 'Default Values'.

![todo:image_alt_text](setting-parameters_2.png)

{{% /alert %}}