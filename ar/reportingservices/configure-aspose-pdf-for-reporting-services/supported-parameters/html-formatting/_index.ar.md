---
title: HTML Formatting
type: docs
weight: 20
url: /reportingservices/html-formatting/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

أحيانًا قد ترغب في تصدير النص في مربعات النص مع التنسيق. لسوء الحظ، لا تدعم خدمات التقارير ذلك. ومع ذلك، لا يزال بإمكانك تنفيذ ذلك باستخدام Aspose.PDF لخدمات التقارير. فقط قم بتمكين وضع خاص يتم فيه التعامل مع جميع النصوص في مربعات النص على أنها HTML وضع العلامات HTML الضرورية لتنسيق النص في المستند الناتج. على سبيل المثال، للحصول على نص عادي، ونص غامق ومائل في نفس مربع النص، أدخل القيمة التالية لمربع النص:

بعض هذا النص هو ```<b>غامق</b>``` والنص الآخر هو ```<i>مائل</i>```.

عند التصدير، سيبدو النص كما لو أن بعض هذا النص هو **غامق** والنص الآخر هو *مائل*.

يرجى ملاحظة أن هذا النهج له بعض القيود

{{% /alert %}}

{{% alert color="primary" %}}

- التنسيق غير مرئي في وقت التصميم (في منشئ التقارير، بوابة خدمات التقارير على الويب إلخ.).
 بدلاً من ذلك، سترى نص HTML في شكل نص عادي مع العلامات.  
- يتعرف ملحق تصيير Aspose.PDF لخدمات التقارير ويقوم بتنسيق كود HTML بشكل صحيح في صناديق النصوص. سيقوم محول PDF الافتراضي لخدمات التقارير بتصدير هذه العلامة كنص عادي.
{{% /alert %}}

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

إذا كنت تريد إضافة هذا المعامل في مصمم التقارير، استخدم نوع البيانات 'Boolean'.

حاليًا، يدعم Aspose.Pdf لخدمات التقارير مجموعة فرعية من جميع علامات HTML. يمكنك العثور على مزيد من المعلومات في [التوثيق](https://docs.aspose.com/pdf/net/add-text-to-pdf-file/#add-html-string-using-dom) الخاص بـ Aspose.PDF.