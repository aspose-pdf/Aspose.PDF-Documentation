---
title: Security Setting
type: docs
weight: 30
url: ar/reportingservices/security-setting/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

لطالما كانت الأمان هي القضية الأكثر أهمية في كل مجال، سواء كان ذلك لحماية الشبكة أو مستند PDF. يتم تأمين المستندات لأسباب عديدة محتملة: قد يرغب كاتب المستند في الحفاظ على محتوى المستند آمنًا ولا يريد السماح للآخرين بتغييره، إلخ.

لقد اهتم Aspose.Pdf for Reporting Services بالكثير من هذه الجوانب الأمنية من خلال توفير هذه الميزات للمطورين التي يمكن أن تكون مفيدة لهم لحماية مستندات PDF الخاصة بهم. لذلك، فإنه يحتوي على عدد من المعلمات التي تسمح للمطورين بتطبيق تدابير أمان مختلفة على مستندات PDF.

أحد هذه التدابير هو حماية مستند PDF بكلمة مرور أثناء التشفير. يمكنك أيضًا تقييد أو السماح بتعديل المحتوى، نسخ المحتوى، طباعة الوثيقة أو السماح/تعطيل تعبئة النماذج. هذه الميزات غير مدعومة حاليًا من قبل مُصدر PDF الافتراضي لخدمات تقارير SQL ولكن يمكنك تنفيذ هذه الميزات باستخدام Aspose.Pdf لخدمات التقارير. فقط أضف المعلمات الأمنية المقابلة إلى تقرير أو ملف تكوين خادم التقارير، وستتمكن من إنشاء مستندات PDF آمنة بامتيازات محدودة.

حاليًا، يدعم Aspose.Pdf لخدمات التقارير السمات الأمنية التالية:

{{% /alert %}}

{{% alert color="primary" %}}

**Parameter Name**: User Password  
**Date Type**: String  
**Values supported**: أي نص عادي

**Parameter Name**: Master Password  
**Date Type**: String  
**Values supported**: أي نص عادي 

**Parameter Name**: IsCopyingAllowed  
**Date Type**: Boolean  
**Values supported**: True, False (افتراضي)  

**Parameter Name**: IsPrintingAllowed  
**Date Type**: Boolean  

**Values supported**: True, False (افتراضي)  
**Parameter Name**: IsContentsModifyingAllowed  
**Date Type**: منطقي  
**Values supported**: صحيح، خطأ (افتراضي)  

**Parameter Name**: IsFormFillingAllowed  
**Date Type**: منطقي  
**Values supported**: صحيح، خطأ (افتراضي)  

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