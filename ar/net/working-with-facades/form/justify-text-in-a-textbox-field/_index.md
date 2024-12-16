---
title: ضبط النص في حقل مربع النص
type: docs
weight: 20
url: /ar/net/justify-text-in-a-textbox-field/
description: توضح هذه المقالة كيفية ضبط النص في حقل مربع النص باستخدام فئة النموذج.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

في هذه المقالة، سنوضح لك كيفية ضبط النص في حقل مربع النص في ملف PDF.

{{% /alert %}}

## تفاصيل التنفيذ

يوفر فئة [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) في [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) القدرة على تزيين حقل نموذج PDF. الآن، إذا كانت متطلباتك تبرير النص في حقل مربع النص، يمكنك تحقيق ذلك بسهولة باستخدام قيمة [AlignJustified](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade/fields/alignjustified) من تعداد [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) واستدعاء طريقة [FormEditor.DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield/index). في المثال أدناه، سنقوم أولاً بملء حقل مربع النص باستخدام طريقة [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index) من فئة [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form). بعد ذلك سنستخدم فئة FormEditor لتبرير النص في حقل مربع النص. يوضح لك مقطع الكود التالي كيفية تبرير النص في حقل مربع النص.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-JustifyText-JustifyText.cs" >}}
```
يرجى ملاحظة أن المحاذاة المضبوطة غير مدعومة من قبل PDF ولهذا السبب سيتم محاذاة النص إلى اليسار عندما تقوم بإدخال النص في حقل النص. ولكن عندما لا يكون الحقل نشطًا، يكون النص مضبوطًا.
```