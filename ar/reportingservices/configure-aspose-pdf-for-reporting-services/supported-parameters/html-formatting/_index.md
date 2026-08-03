---
title: تنسيق HTML
linktitle: تنسيق HTML
type: docs
weight: 20
url: /reportingservices/html-formatting/
description: تمكين تنسيق HTML في تقارير PDF باستخدام Aspose.PDF لخدمات التقارير. أضف الأنماط والبنية بسهولة.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

في بعض الأحيان قد ترغب في تصدير النص في مربعات النص ذات التنسيق. لسوء الحظ، لا تدعم خدمات التقارير هذا. ومع ذلك، لا يزال بإمكانك تنفيذ ذلك باستخدام Aspose.PDF لخدمات التقارير. ما عليك سوى تمكين وضع خاص يتم فيه التعامل مع كل النص الموجود في مربعات النص على أنه HTML ووضع علامات HTML الضرورية لتنسيق النص في مستند الإخراج. على سبيل المثال، للحصول على نص عادي وغامق ومائل في نفس مربع النص، أدخل قيمة مربع النص التالي:

بعض هذا النص هو `<b>bold</b>` والنص الآخر هو `<i>italic</i>`.

عند التصدير، سيبدو النص كما يلي: بعض هذا النص **غامق** والنص الآخر *مائل*.

يرجى ملاحظة أن هذا النهج له بعض القيود

{{% /alert %}}

{{% alert color="primary" %}}

- لا يكون التنسيق مرئيًا في وقت التصميم (في Report Builder، وبوابة الويب الخاصة بخدمات التقارير، وما إلى ذلك). بدلاً من ذلك، ستشاهد نص HTML في شكل نص عادي مع العلامات.
- يتعرف ملحق العرض Aspose.PDF for Reporting Services على تعليمات HTML البرمجية ويقوم بتنسيقها بشكل صحيح في مربعات النص. سيقوم عارض PDF الافتراضي لخدمات التقارير بتصدير هذا الترميز كنص عادي.

```text
Parameter Name: IsHtmlTagSupported  
Date Type: Boolean  
Values supported: True, False (default)   
```

## مثال

```xml
<Render>
...
    <Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices ">
    <Configuration>
    <IsHtmlTagSupported >True</IsHtmlTagSupported>
    </Configuration>
    </Extension>
</Render>
```

إذا كنت تريد إضافة هذه المعلمة في مصمم التقارير، استخدم نوع البيانات `Boolean`.

حاليًا، يدعم Aspose.Pdf for Reporting Services مجموعة فرعية من كافة علامات HTML. قد تجد المزيد من المعلومات في Aspose.PDF [الوثائق](https://docs.aspose.com/pdf/net/add-text-to-pdf-file/#add-html-string-using-dom).

{{% /alert %}}
