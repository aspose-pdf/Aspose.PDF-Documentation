---
title: إعداد الأمان
linktitle: إعداد الأمان
type: docs
weight: 30
url: /ar/reportingservices/security-setting/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

الأمان كان دائمًا أهم قضية في كل مجال، سواء كان حماية شبكة أو مستند PDF. يتم تأمين المستندات لأسباب عديدة محتملة: قد يرغب كاتب المستند في الحفاظ على محتوى المستند آمنًا ولا يريد السماح للآخرين بتغييره، إلخ.

قامت Aspose.PDF for Reporting Services بالاهتمام الكبير بهذه الجوانب الأمنية من خلال توفير هذه الميزات للمطورين التي يمكن أن تكون مفيدة لهم لحماية مستندات PDF الخاصة بهم. وبالتالي، تحتوي على عدد من المعلمات التي تسمح للمطورين بتطبيق إجراءات أمنية مختلفة على مستندات PDF.

إحدى هذه الإجراءات هي حماية مستند PDF بكلمة مرور أثناء التشفير. يمكنك أيضًا تقييد أو السماح بتعديل المحتوى، نسخ المحتوى، طباعة المستند أو السماح/تعطيل ملء النماذج. هذه الميزات غير مدعومة في الوقت الحالي من قبل مُصدّر PDF الافتراضي في SQL Reporting Services، ولكن يمكنك تنفيذ هذه الميزات باستخدام Aspose.PDF for Reporting Services. فقط أضف معلمات الأمان المقابلة إلى تقرير أو ملف إعداد خادم التقارير، وستتمكن من إنشاء مستندات PDF آمنة مع امتيازات محدودة.

حاليًا، يدعم المكوّن Aspose.Pdf لخدمات التقارير السمات الأمنية التالية:

{{% /alert %}}

{{% alert color="primary" %}}

**Parameter Name**: كلمة مرور المستخدم  
**Date Type**: نص  
**Values supported**: أي نص عادي

**Parameter Name**: كلمة مرور المدير  
**Date Type**: نص  
**Values supported**: أي نص عادي 

**اسم المعامل**: IsCopyingAllowed  
**نوع البيانات**: منطقي  
**القيم المدعومة**: صحيح، خطأ (الافتراضي)  

**اسم المعامل**: IsPrintingAllowed  
**نوع البيانات**: منطقي  
**القيم المدعومة**: صحيح، خطأ (الافتراضي)  

**اسم المعامل**: IsContentsModifyingAllowed  
**نوع البيانات**: منطقي  
**القيم المدعومة**: صحيح، خطأ (الافتراضي)  

**اسم المعامل**: IsFormFillingAllowed  
**نوع البيانات**: منطقي  
**القيم المدعومة**: صحيح، خطأ (الافتراضي)  

**مثال**

{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <UserPassword>aspose</UserPassword>
    <IsCopyingAllowed>False</IsCopyingAllowed>
    <IsPrintingAllowed>False</IsPrintingAllowed>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}

