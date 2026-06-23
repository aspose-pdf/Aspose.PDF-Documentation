---
title: تنسيق HTML
linktitle: تنسيق HTML
type: docs
weight: 20
url: /ar/reportingservices/html-formatting/
description: تمكين تنسيق HTML في تقارير PDF باستخدام Aspose.PDF لخدمات التقارير. أضف الأنماط والهيكل بسهولة.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

أحيانًا قد ترغب في تصدير النص الموجود في صناديق النص مع التنسيق. للأسف، لا تدعم خدمات التقارير هذا. ومع ذلك، لا يزال بإمكانك تنفيذه باستخدام Aspose.PDF لخدمات التقارير. فقط قم بتمكين وضع خاص تُعامل فيه جميع النصوص داخل صناديق النص كـHTML وضع علامات HTML اللازمة لتنسيق النص في مستند الإخراج. على سبيل المثال، للحصول على نص عادي وعريض ومائل في نفس صندوق النص، أدخل القيمة التالية لصندوق النص:

بعض هذا النص هو ```<b>bold</b>``` ونص آخر هو ```<i>italic</i>```.

عند التصدير، سيظهر النص كما أن بعض هذا النص هو **عريض** والنص الآخر هو *مائل*.

يرجى ملاحظة أن لهذه المقاربة بعض القيود

{{% /alert %}}

{{% alert color="primary" %}}

- التنسيق غير مرئي في وقت التصميم (في Report Builder، بوابة ويب Reporting Services وغيرها). بدلاً من ذلك، سترى نص HTML على شكل نص عادي مع العلامات.
- امتداد العرض Aspose.PDF for Reporting Services يتعرف على شفرة HTML في مربعات النص ويقوم بتنسيقها بشكل صحيح. مُعالج PDF الافتراضي في Reporting Services سيصدّر هذا الترميز كنص عادي.

**اسم المعامل**: IsHtmlTagSupported  
**نوع البيانات**: Boolean  
**القيم المدعومة**: True, False (default)   

**مثال**

{{< highlight csharp >}}

 <Render>
...
    <Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices ">
    <Configuration>
    <IsHtmlTagSupported >True</IsHtmlTagSupported>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

إذا كنت ترغب في إضافة هذا المعامل في مصمم التقرير، استخدم نوع البيانات 'Boolean'.

 
حاليًا يدعم Aspose.Pdf for Reporting Services مجموعة فرعية من جميع وسوم HTML. يمكنك العثور على مزيد من المعلومات في Aspose.PDF [توثيق](https://docs.aspose.com/pdf/net/add-text-to-pdf-file/#add-html-string-using-dom).

{{% /alert %}}

