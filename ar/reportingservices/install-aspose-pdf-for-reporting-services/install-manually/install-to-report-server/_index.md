---
title: تثبيت إلى خادم التقارير
linktitle: تثبيت إلى خادم التقارير
type: docs
weight: 10
url: /ar/reportingservices/install-to-report-server/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

ما عليك إلا اتباع هذه الخطوات إذا قمت بتثبيت Aspose.PDF لخدمات التقارير يدويًا، دون استخدام مثبت MSI. يقوم مثبت MSI بتنفيذ جميع إجراءات التثبيت والتسجيل اللازمة تلقائيًا.

{{% /alert %}}

في الخطوات التالية، ستحتاج إلى نسخ وتعديل الملفات في الدليل حيث تم تثبيت Microsoft SQL Server Reporting Services. تجميع SSRS 2016 موجود في دليل \Bin\SSRS2016 داخل حزمة zip؛ تجميع SSRS 2017 موجود في دليل \Bin\SSRS2017؛ تجميع SSRS 2019 موجود في دليل \Bin\SSRS2019؛ تجميع SSRS 2022 موجود في دليل \Bin\SSRS2022؛ تجميع Power BI Report Server موجود في دليل \Bin\PowerBI. 

{{% alert color="primary" %}}

**Step 1.** حدد دليل تثبيت Report Server. الدليل الجذر لـ Microsoft SQL Server عادةً هو C:\Program Files\Microsoft SQL Server. العملية اللاحقة تختلف قليلاً بالنسبة لـ Reporting Services 2016 وReporting Services 2017 وما بعدها، وPower BI Report Server:

- يتم تثبيت Report Server 2016 افتراضيًا في الدليل C:\Program Files\Microsoft SQL Server\MSRS13.MSSQLSERVER\Reporting Services\ReportServer. إذا كنت تستخدم مثيلات مسماة مخصصًا بدلاً من المثيل الافتراضي، فسيكون المسار الافتراضي هو C:\Program Files\Microsoft SQL Server\MSRS13.[SSRSInstanceName]\Reporting Services\ReportServer
- يتم تثبيت Report Server 2017 وما بعده افتراضيًا في الدليل C:\Program Files\Microsoft SQL Server Reporting Services\SSRS\ReportServer.
- يتم تثبيت Power BI Report Server افتراضيًا في الدليل C:\Program Files\Microsoft Power BI Report Server\PBIRS\ReportServer.

في النص التالي سيتم الإشارة إلى دليل تثبيت Reporting Services (أحد المسارات المذكورة أعلاه) على أنه ```<Instance>```.
{{% /alert %}}

{{% alert color="primary" %}}
**الخطوة 2.** نسخ Aspose.Pdf.ReportingServices.dll للإصدار المقابل من SSRS إلى المجلد ```<Instance>```\bin.
{{% /alert %}}

{{% alert color="primary" %}}
**الخطوة 3.** تسجيل Aspose.Pdf لـ Reporting Services كملحق عرض. افتح ملف ```<Instance>```\rsreportserver.config وأضف الأسطر التالية إلى العنصر ```<Render>```:
{{% /alert %}}

**مثال**

{{< highlight csharp >}}

 <Render>
...
<!--Start here.-->

<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices"/>

</Render>

{{< /highlight >}}

{{% alert color="primary" %}}
**الخطوة 4.** قدم Aspose.Pdf لخدمات التقارير مع الأذونات للتنفيذ. افتح ملف ```<Instance>```\\rssrvpolicy.config وأضف النص التالي كآخر عنصر في العنصر ```<CodeGroup>``` الثاني إلى الخارجي (يجب أن يكون ```<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. ">):```
{{% /alert %}}

**مثال**

{{< highlight csharp >}}

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

{{< /highlight >}}

{{% alert color="primary" %}}
**الخطوة 5.** تحقق من أن Aspose.Pdf for Reporting Services تم تثبيته بنجاح. افتح بوابة الويب لخدمات التقارير وتحقق من قائمة صيغ التصدير المتاحة لتقرير. يمكنك تشغيل بوابة الويب ببدء متصفح ويب وكتابة عنوان URL لبوابة الويب لخدمات التقارير في شريط العنوان (بشكل افتراضي هو http://```<Reporting_Services_server_name>```/reports/). اختر أحد التقارير المتوفرة في بوابة الويب الخاصة بك واسحب قائمة التصدير من القائمة المنسدلة. يجب أن ترى قائمة صيغ التصدير بما في ذلك تلك التي يوفرها ملحق Aspose.Pdf for Reporting Services. اختر العنصر PDF via Aspose.PDF.

 
{{% /alert %}}

![todo:image_alt_text](install-to-report-server_1.png)

انقر على العنصر المحدد. سيولد التقرير بالتنسيق المختار، ويرسله إلى العميل، واعتمادًا على إعدادات متصفح الويب الخاص بك، إما أن يعرض لك مربع حوار حفظ الملف لاختيار مكان حفظ التقرير المُصدَّر، أو يقوم بتنزيل الملف تلقائيًا إلى مجلد التنزيلات الخاص بك.

{{% alert color="primary" %}}
تهانينا، لقد قمت بتثبيت Aspose.Pdf for Reporting Services بنجاح وتصدير تقرير كملف PDF!
{{% /alert %}}


