---
title: معلومات التصحيح
linktitle: معلومات التصحيح
type: docs
weight: 90
url: /ar/reportingservices/debug-information/
description: الوصول إلى معلومات التصحيح وتحليلها لتصيير PDF في Aspose.PDF لخدمات التقارير من أجل استكشاف المشكلات بشكل فعال.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

من غير الممكن تجنّب وجود شيء خاطئ في عملية التصيير أو النتيجة المصورة. لأسباب مثل السرية أو الخصوصية، لا يمكننا الحصول على مصدر البيانات المستخدم في تقرير المستخدم، وبالتالي لا يمكننا إعادة إنتاج الخطأ في التقرير. لتسهيل وتحسين التواصل بين العملاء والمطورين، نضيف هذا المعامل. إذا واجهت مشاكل عند تصيير تقريرك باستخدام Aspose.PDF لخدمات التقارير، يرجى ضبط هذا المعامل في التقرير، ثم ستحصل على المستند المصور بصيغة XML. بعد ذلك، يرجى نشر ملف XML لنا في منتدى المنتج.

{{% /alert %}}

{{% alert color="primary" %}}
**اسم المعامل**: SavingXmlFormat  
**نوع التاريخ**: منطقي  
**القيم المدعومة**: True, False (default)  

**مثال**
{{< highlight csharp >}}

<Render>
...
<Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices">
<Configuration>
<SavingXmlFormat > True </SavingXmlFormat>
</Configuration>
</Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}

