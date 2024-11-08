---
title: تحديد أسماء حقول النماذج
type: docs
weight: 10
url: /ar/net/identifying-form-fields-names/
description: تتيح لك Aspose.PDF.Facades تحديد أسماء حقول النماذج باستخدام فئة النموذج.
lastmod: "2021-06-05"
draft: false
---

[Aspose.PDF for .NET](/pdf/ar/net/) توفر القدرة على إنشاء وتحرير وملء النماذج المكونة بالفعل. تحتوي مساحة الأسماء [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) على فئة [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form)، والتي تحتوي على وظيفة تسمى [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index) وتأخذ وسيطين وهما اسم الحقل وقيمة الحقل. لذلك، من أجل ملء حقول النموذج، يجب أن تكون على دراية بالاسم الدقيق لحقل النموذج.

## تفاصيل التنفيذ

غالبًا ما نصادف سيناريو حيث نحتاج إلى ملء النموذج الذي تم إنشاؤه في بعض الأدوات أي. 
Adobe Designer، ولسنا متأكدين من أسماء حقول النموذج. لذا لملء حقول النموذج، أولاً نحتاج إلى قراءة أسماء جميع حقول نموذج Pdf. توفر فئة [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) خاصية تسمى [FieldNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/properties/fieldnames) والتي تعيد جميع أسماء الحقول وتعيد القيمة null إذا لم يحتوي PDF على أي حقل. ومع ذلك، عند استخدام هذه الخاصية، نحصل على أسماء جميع الحقول في نموذج PDF وقد لا نكون متأكدين من أي اسم يتوافق مع أي حقل في النموذج.

كحل لهذه المشكلة، سنستخدم سمات المظهر لكل حقل.
``` 
Form class has a function named [GetFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getfieldfacade) والتي تُرجع السمات، بما في ذلك الموقع، اللون، نمط الحدود، الخط، عنصر القائمة وهكذا. لحفظ هذه القيم نحتاج لاستخدام فئة [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormFieldFacade)، والتي تُستخدم لتسجيل السمات المرئية للحقول. بمجرد أن نحصل على هذه السمات يمكننا إضافة حقل نصي تحت كل حقل يعرض اسم الحقل.

{{% alert color="primary" %}}
في هذه المرحلة، يبرز سؤال "كيف سنحدد الموقع لإضافة الحقل النصي؟"
{{% /alert %}}

{{% alert color="primary" %}}
الحل لهذه المشكلة هو خاصية Box في فئة [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormFieldFacade)، والتي تحمل موقع الحقل.
{{% /alert %}}
``` نحتاج إلى حفظ هذه القيم في مصفوفة من نوع المستطيل واستخدام هذه القيم لتحديد الموضع حيث سنضيف حقول النص الجديدة.

في مساحة الأسماء [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) لدينا فئة تسمى [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) والتي توفر القدرة على التعامل مع نماذج PDF. افتح نموذج PDF؛ أضف حقل نص أسفل كل حقل نموذج موجود واحفظ نموذج PDF باسم جديد.