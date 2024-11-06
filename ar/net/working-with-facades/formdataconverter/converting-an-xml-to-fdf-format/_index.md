---
title: تحويل XML إلى تنسيق FDF
type: docs
weight: 20
url: ar/net/converting-an-xml-to-fdf-format/
description: يوضح هذا القسم كيفية تحويل XML إلى تنسيق FDF باستخدام FormDataConverter.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

يدعم النطاق [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) في [Aspose.PDF for .NET](/pdf/net/) نماذج AcroForms بشكل جيد جداً. كما يدعم استيراد وتصدير بيانات النماذج إلى تنسيقات ملفات مختلفة مثل FDF وXFDF وXML. ومع ذلك، في بعض الأحيان يحتاج المطور إلى تحويل تنسيق إلى آخر. في هذه المقالة، سوف نلقي نظرة على الميزة التي تسمح لنا بتحويل تنسيق FDF إلى XML.

{{% /alert %}}

## التفاصيل

يشير FDF إلى تنسيق بيانات النماذج، ويحتوي ملف FDF على قيم النماذج في شكل زوج مفتاح/قيمة. نعلم أيضًا أن ملف XML يحتوي على القيم كعلامات. حيث يتم تمثيل المفتاح في الغالب كاسم العلامة ويتم تمثيل القيمة كالقيمة داخل تلك العلامة. الآن، توفر [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) المرونة لتحويل تنسيق ملف XML إلى تنسيق FDF.

استخدم فئة [FormDataConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormDataConverter) لهذا الغرض. توفر هذه الفئة طرقًا مختلفة لتحويل صيغة بيانات إلى أخرى. توضح هذه المقالة كيفية استخدام إحدى الطرق، ConvertXmlToFdf(..)، التي تأخذ ملف FDF كمدخل أو تدفق مصدر وتحفظه في تنسيق XML. يوضح المقتطف البرمجي التالي كيفية تحويل ملف FDF إلى ملف XML.