---

title: التثبيت على خادم التقارير  
type: docs  
weight: 10  
url: /ar/reportingservices/install-to-report-server/  
lastmod: "2021-06-05"  

---

{{% alert color="primary" %}}

تحتاج فقط إلى اتباع هذه الخطوات إذا قمت بتثبيت Aspose.PDF لـ Reporting Services يدويًا، وليس باستخدام مثبت MSI. يقوم مثبت MSI بتنفيذ جميع عمليات التثبيت والتسجيل اللازمة تلقائيًا.

{{% /alert %}}

في الخطوات التالية، ستحتاج إلى نسخ وتعديل الملفات في الدليل حيث تم تثبيت Microsoft SQL Server Reporting Services. تقع مجموعة SSRS 2016 في دليل \Bin\SSRS2016 في حزمة zip؛ وتقع مجموعة SSRS 2017 في دليل \Bin\SSRS2017؛ وتقع مجموعة SSRS 2019 في دليل \Bin\SSRS2019؛ وتقع مجموعة SSRS 2022 في دليل \Bin\SSRS2022؛ وتقع مجموعة Power BI Report Server في دليل \Bin\PowerBI.

{{% alert color="primary" %}}

**الخطوة 1.** حدد موقع دليل تثبيت خادم التقارير. الدليل الجذري لـ Microsoft SQL Server هو عادة C:\Program Files\Microsoft SQL Server. العملية التالية تختلف قليلاً بين Reporting Services 2016 و Reporting Services 2017 وما بعده و Power BI Report Server:

- يتم تثبيت Report Server 2016 بشكل افتراضي في الدليل C:\Program Files\Microsoft SQL Server\MSRS13.MSSQLSERVER\Reporting Services\ReportServer. إذا كنت تستخدم مثيلات مخصصة بدلاً من المثيل الافتراضي، سيكون المسار الافتراضي C:\Program Files\Microsoft SQL Server\MSRS13.[SSRSInstanceName]\Reporting Services\ReportServer
- يتم تثبيت Report Server 2017 وما بعده بشكل افتراضي في الدليل C:\Program Files\Microsoft SQL Server Reporting Services\SSRS\ReportServer.
- يتم تثبيت Power BI Report Server بشكل افتراضي في الدليل C:\Program Files\Microsoft Power BI Report Server\PBIRS\ReportServer.

في النص التالي سيتم الإشارة إلى دليل تثبيت خدمات التقارير (أحد المسارات المذكورة أعلاه) كـ ```<Instance>```.
{{% /alert %}}


{{% alert color="primary" %}}**الخطوة 2.** انسخ Aspose.Pdf.ReportingServices.dll للإصدار المقابل من SSRS إلى مجلد ```<Instance>```\bin.
{{% /alert %}}

{{% alert color="primary" %}}
**الخطوة 3.** سجل Aspose.Pdf لخدمات إعداد التقارير كامتداد عرض. افتح ملف ```<Instance>```\rsreportserver.config وأضف السطور التالية إلى عنصر ```<Render>```:
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
**الخطوة 4.** امنح Aspose.Pdf لخدمات إعداد التقارير الأذونات لتنفيذ. افتح ملف ```<Instance>```\rssrvpolicy.config وأضف النص التالي كآخر عنصر في عنصر ```<CodeGroup>``` الثاني من الخارج (والذي يجب أن يكون ```<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. ">):```

{{% /alert %}}

**Example**

{{< highlight csharp >}}

<CodeGroup>
...

<CodeGroup>
...

<!--ابدأ هنا.-->

<CodeGroup class="UnionCodeGroup" version="1" PermissionSetName="FullTrust"

Name="Aspose.Pdf_for_Reporting_Services" Description="تمنح مجموعة التعليمات البرمجية هذه الثقة الكاملة لتجميع AP4SSRS.">

<IMembershipCondition class="StrongNameMembershipCondition" version="1" PublicKeyBlob="00240000048000009400000006020000002400005253413100040000010001005542e99cecd28842dad186257b2c7b6ae9b5947e51e0b17b4ac6d8cecd3e01c4d20658c5e4ea1b9a6c8f854b2d796c4fde740dac65e834167758cff283eed1be5c9a812022b015a902e0b97d4e95569eb8c0971834744e633d9cb4c4a6d8eda03c12f486e13a1a0cb1aa101ad94943236384cbbf5c679944b994de9546e493bf " />

</CodeGroup>

<!--انته هنا. -->

</CodeGroup>

</CodeGroup>

{{< /highlight >}}

{{% alert color="primary" %}}
**Step 5.** تحقق من تثبيت Aspose.Pdf لخدمات التقارير بنجاح. افتح بوابة خدمات التقارير على الويب وتحقق من قائمة تنسيقات التصدير المتاحة لتقرير. يمكنك تشغيل بوابة الويب عن طريق بدء متصفح الويب وكتابة عنوان URL الخاص ببوابة خدمات التقارير في شريط العنوان (افتراضيًا هو http://```<Reporting_Services_server_name>```/reports/). حدد أحد التقارير المتوفرة في بوابة الويب الخاصة بك واسحب قائمة التصدير المنسدلة. يجب أن ترى قائمة بتنسيقات التصدير بما في ذلك تلك التي يوفرها امتداد Aspose.Pdf لخدمات التقارير. حدد عنصر PDF عبر Aspose.PDF.
{{% /alert %}}

![todo:image_alt_text](install-to-report-server_1.png)

انقر على العنصر المحدد. سيقوم بإنشاء التقرير بالتنسيق المحدد، وإرساله إلى العميل، واعتمادًا على إعدادات متصفح الويب الخاص بك، إما أن يعرض لك مربع حوار حفظ الملف لاختيار مكان حفظ التقرير المُصدر، أو يقوم تلقائيًا بتنزيل الملف إلى مجلد التنزيلات لديك.

