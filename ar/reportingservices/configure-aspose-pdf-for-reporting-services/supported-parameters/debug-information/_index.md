---
title: معلومات تصحيح الأخطاء
type: docs
weight: 90
url: /ar/reportingservices/debug-information/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

من المحتم أن يكون هناك خطأ ما في العرض أو النتيجة المعروضة. لأسباب مثل السرية أو الخصوصية، لا يمكننا الحصول على مصدر البيانات المستخدم في تقرير المستخدم، لذلك لا يمكننا إعادة إنتاج الخطأ في التقرير. لتسهيل وتحسين التواصل بين العملاء والمطورين، قمنا بإضافة هذه المعلمة. إذا واجهت مشاكل عند عرض تقريرك باستخدام Aspose.PDF لخدمات التقارير، يرجى ضبط هذه المعلمة في التقرير، ثم ستحصل على المستند المعروض بصيغة XML. بعد ذلك، يرجى نشر ملف XML لنا في منتدى المنتج.

{{% /alert %}}

{{% alert color="primary" %}}
**اسم المعلمة**: SavingXmlFormat  
**نوع البيانات**: Boolean  
**القيم المدعومة**: True, False (افتراضي)  

**مثال**
{{< highlight csharp >}}

<Render>
...

<Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices">
```

<Configuration>
<SavingXmlFormat > True </SavingXmlFormat>
</Configuration>
</Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
```