---
title: إعداد الأمان
linktitle: إعداد الأمان
type: docs
weight: 30
url: /reportingservices/security-setting/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

لقد كان الأمن دائمًا هو القضية الأكثر أهمية في كل مجال، سواء كان ذلك حماية الشبكة أو مستند PDF. يتم جعل المستندات آمنة لعدة أسباب محتملة: قد يرغب كاتب المستند في الحفاظ على محتوى المستند آمنًا ولا يريد السماح للآخرين بتغييره، وما إلى ذلك.

لقد اهتمت Aspose.PDF لخدمات التقارير كثيرًا بهذه الجوانب الأمنية من خلال توفير هذه الميزات للمطورين والتي يمكن أن تكون مفيدة لهم لحماية مستندات PDF الخاصة بهم. لذلك، فهو يحتوي على عدد من المعلمات التي تسمح للمطورين بتطبيق إجراءات أمنية مختلفة على مستندات PDF.

أحد هذه الإجراءات هو حماية مستند PDF بكلمة مرور أثناء التشفير. يمكنك أيضًا تقييد أو السماح بتعديل المحتويات، أو نسخ المحتوى، أو طباعة المستندات، أو السماح/تعطيل ملء النماذج. هذه الميزات غير مدعومة في الوقت الحالي بواسطة SQL Reporting Services PDF Exporter الافتراضي، ولكن يمكنك تنفيذ هذه الميزات باستخدام Aspose.PDF لخدمات التقارير. ما عليك سوى إضافة معلمات الأمان المقابلة إلى تقرير أو ملف تكوين خادم التقارير، وستكون قادرًا على إنشاء مستندات PDF آمنة بامتيازات محدودة.

حاليًا، يدعم عارض Aspose.PDF لخدمات التقارير سمات الأمان التالية:

{{% /alert %}}

```text
Parameter Name: User Password  
Date Type: String  
Values supported: Any plain text
```

```text
Parameter Name: Master Password  
Date Type: String  
Values supported: Any plain text 
```

```text
Parameter Name: IsCopyingAllowed  
Date Type: Boolean  
Values supported: True, False (default) 
```

```text
Parameter Name: IsPrintingAllowed  
Date Type: Boolean  
Values supported: True, False (default)  
```

```text
Parameter Name: IsContentsModifyingAllowed  
Date Type: Boolean  
Values supported: True, False (default) 
```

```text
Parameter Name: IsFormFillingAllowed  
Date Type: Boolean  
Values supported: True, False (default)  
```

## مثال

```xml
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
```

