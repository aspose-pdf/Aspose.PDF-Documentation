---
title: التثبيت على خادم التقرير
linktitle: التثبيت على خادم التقرير
type: docs
weight: 10
url: /reportingservices/install-to-report-server/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

ما عليك سوى اتباع هذه الخطوات إذا قمت بتثبيت Aspose.PDF لخدمات التقارير يدويًا، وليس باستخدام مثبت MSI. يقوم برنامج تثبيت MSI بتنفيذ جميع إجراءات التثبيت والتسجيل اللازمة تلقائيًا.

{{% /alert %}}

في الخطوات التالية، ستحتاج إلى نسخ الملفات وتعديلها في الدليل المثبت عليه Microsoft SQL Server Reporting Services. يقع تجميع SSRS 2016 في الدليل \Bin\SSRS2016 الخاص بالحزمة المضغوطة؛ يقع تجميع SSRS 2017 في الدليل \Bin\SSRS2017؛ يقع تجميع SSRS 2019 في الدليل \Bin\SSRS2019؛ يقع تجميع SSRS 2022 في الدليل \Bin\SSRS2022؛ يقع تجميع Power BI Report Server في الدليل \Bin\PowerBI.

**الخطوة 1.** حدد موقع دليل تثبيت خادم التقارير. عادةً ما يكون الدليل الجذر لـ Microsoft SQL Server هو C:\Program Files\Microsoft SQL Server. تختلف العملية الإضافية قليلاً بالنسبة إلى Reporting Services 2016 وReporting Services 2017 والإصدارات الأحدث وPower BI Report Server:

- يتم تثبيت Report Server 2016 افتراضيًا في الدليل C:\Program Files\Microsoft SQL Server\MSRS13.MSSQLSERVER\Reporting Services\ReportServer. إذا كنت تستخدم مثيلات مسماة مخصصة بدلاً من المثيل الافتراضي، فسيكون المسار الافتراضي هو C:\Program Files\Microsoft SQL Server\MSRS13.[SSRSInstanceName]\Reporting Services\ReportServer
- يتم تثبيت Report Server 2017 والإصدارات الأحدث بشكل افتراضي في الدليل C:\Program Files\Microsoft SQL Server Reporting Services\SSRS\ReportServer.
- يتم تثبيت Power BI Report Server افتراضيًا في الدليل C:\Program Files\Microsoft Power BI Report Server\PBIRS\ReportServer.

في النص التالي، سيتم الإشارة إلى دليل تثبيت خدمات التقارير (أحد المسارات المذكورة أعلاه) باسم `<Instance>`.

**الخطوة 2.** انسخ Aspose.Pdf.ReportingServices.dll لإصدار SSRS المقابل إلى المجلد `<Instance>\bin`.

**الخطوة 3.** قم بتسجيل Aspose.PDF لخدمات التقارير كملحق للعرض. افتح الملف `<Instance>\rsreportserver.config` وأضف الأسطر التالية إلى العنصر `<Render>`:

## مثال

```xml
<Render>
...
<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices"/>
</Render>
```

**الخطوة 4.** قم بتوفير Aspose.PDF لخدمات التقارير مع أذونات التنفيذ. افتح الملف `<Instance>\rssrvpolicy.config` وأضف النص التالي باعتباره العنصر الأخير في العنصر الثاني إلى العنصر الخارجي `<CodeGroup>` والذي يجب أن يكون `<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. ">):`

## مثال

```xml

 <CodeGroup>
...

<CodeGroup>
...

<!--Start here.-->

<CodeGroup class="UnionCodeGroup" version="1" PermissionSetName="FullTrust"

Name="Aspose.Pdf_for_Reporting_Services" Description="This code group grants full trust to the AP4SSRS assembly.">

<IMembershipCondition class="StrongNameMembershipCondition" version="1" PublicKeyBlob="00240000048000009400000006020000002400005253413100040000010001005542e99cecd28842dad186257b2c7b6ae9b5947e51e0b17b4ac6d8cecd3e01c4d20658c5e4ea1b9a6c8f854b2d796c4fde740dac65e834167758cff283eed1be5c9a812022b015a902e0b97d4e95569eb8c0971834744e633d9cb4c4a6d8eda03c12f486e13a1a0cb1aa101ad94943236384cbbf5c679944b994de9546e493bf " />

</CodeGroup>

<!--End here. -->

</CodeGroup>

</CodeGroup>
```

**الخطوة 5.** تأكد من تثبيت Aspose.PDF for Reporting Services بنجاح. افتح بوابة الويب الخاصة بخدمات التقارير وتحقق من قائمة تنسيقات التصدير المتاحة للتقرير. يمكنك تشغيل بوابة الويب عن طريق تشغيل متصفح ويب وكتابة عنوان URL لبوابة الويب الخاصة بخدمات التقارير في شريط العناوين (افتراضيًا هو `http://<Reporting_Services_server_name>/reports/`). حدد أحد التقارير المتوفرة في بوابة الويب الخاصة بك واسحب القائمة المنسدلة "تصدير". يجب أن تشاهد قائمة تنسيقات التصدير بما في ذلك تلك التي يوفرها ملحق Aspose.PDF لخدمات التقارير. حدد PDF عبر عنصر Aspose.PDF.

![Install to report server](install-to-report-server_1.png)

انقر فوق العنصر المحدد. سيقوم بإنشاء التقرير بالتنسيق المحدد، وإرساله إلى العميل، ووفقًا لإعدادات متصفح الويب الخاص بك، إما أن يعرض لك مربع حوار حفظ الملف لاختيار مكان حفظ التقرير الذي تم تصديره، أو تنزيل الملف تلقائيًا إلى مجلد التنزيلات الخاص بك.

تهانينا، لقد نجحت في تثبيت Aspose.PDF لخدمات التقارير وتصدير تقرير كمستند PDF!


