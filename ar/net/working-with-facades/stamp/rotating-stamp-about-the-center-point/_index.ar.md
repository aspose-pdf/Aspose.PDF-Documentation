---
title: تدوير الختم حول نقطة المركز
type: docs
weight: 10
url: /net/rotating-stamp-about-the-center-point/
description: يشرح هذا القسم كيفية تدوير الختم حول نقطة المركز باستخدام فئة Stamp.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

تسمح لك [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) في [Aspose.PDF for .NET](/pdf/net/) بإضافة ختم في ملف PDF موجود. في بعض الأحيان، يحتاج المستخدمون إلى تدوير الختم. في هذه المقالة، سنرى كيفية تدوير الختم حول نقطة مركزه.

{{% /alert %}}

## تفاصيل التنفيذ

تسمح [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) class لك بإضافة علامة مائية في ملف PDF. 
يمكنك تحديد الصورة ليتم إضافتها كختم باستخدام طريقة [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.stamp/bindimage/methods/1). تسمح لك طريقة [SetOrigin](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/setorigin) بتعيين أصل الختم المضاف؛ هذا الأصل هو الإحداثيات السفلية اليسرى للختم. يمكنك أيضًا تعيين حجم الصورة باستخدام طريقة [SetImageSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/setimagesize).

الآن، نرى كيف يمكن تدوير الختم حول مركز الختم.
``` [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) توفر فئة خاصية تدعى Rotation. تقوم هذه الخاصية بتعيين أو الحصول على الدوران من 0 إلى 360 لمحتوى الختم. يمكننا تحديد أي قيمة دوران من 0 إلى 360. من خلال تحديد قيمة الدوران يمكننا تدوير الختم حول نقطة مركزه. إذا كان الختم كائنًا من نوع Stamp فيمكن تحديد قيمة الدوران كالتالي aStamp.Rotation = 90. في هذه الحالة سيتم تدوير الختم بزاوية 90 درجة حول مركز محتوى الختم. يوضح لك مقطع الكود التالي كيفية تدوير الختم حول نقطة المركز:



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-RotatingStamp-RotatingStamp.cs" >}}