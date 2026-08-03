---
title: معلومات التصحيح
linktitle: معلومات التصحيح
type: docs
weight: 90
url: /reportingservices/debug-information/
description: قم بالوصول إلى معلومات التصحيح وتحليلها لعرض PDF في Aspose.PDF لخدمات التقارير لاستكشاف المشكلات وإصلاحها بشكل فعال.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

لا يمكن تجنب وجود خطأ ما في العرض أو النتيجة المقدمة. لبعض الأسباب مثل السرية أو الخصوصية، لم نتمكن من الحصول على مصدر البيانات المستخدم في تقرير المستخدم، لذلك لم نتمكن من إعادة إنتاج الخطأ في التقرير. لجعل التواصل بين العملاء والمطورين أسهل وأكثر سلاسة، أضفنا هذه المعلمة. إذا واجهت مشكلات عند تقديم تقريرك باستخدام Aspose.PDF لخدمات التقارير، فيرجى تعيين معلمة التقرير هذه، ثم ستحصل على المستند المقدم بتنسيق XML. وبعد ذلك، يرجى نشر ملف XML لنا في منتدى المنتج.

{{% /alert %}}

{{% alert color="primary" %}}

```txt
Parameter Name: SavingXmlFormat
Date Type: Boolean  
Values supported**: True, False (default)
```

## مثال

```xml
<Render>
...
<Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices">
<Configuration>
<SavingXmlFormat > True </SavingXmlFormat>
</Configuration>
</Extension>
</Render>
```

{{% /alert %}}
