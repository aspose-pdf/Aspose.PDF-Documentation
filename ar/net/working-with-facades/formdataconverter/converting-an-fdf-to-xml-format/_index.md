---
title: تحويل FDF إلى صيغة XML
type: docs
weight: 10
url: /ar/net/converting-an-fdf-to-xml-format/
description: يوضح هذا القسم كيفية تحويل FDF إلى صيغة XML باستخدام فئة FormDataConverter.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

يدعم النطاق [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) في [Aspose.PDF for .NET](/pdf/ar/net/) AcroForms بشكل جيد. كما يدعم استيراد وتصدير بيانات النماذج إلى صيغ ملفات مختلفة مثل FDF وXFDF وXML. ومع ذلك، في بعض الأحيان قد يحتاج المطورون إلى تحويل صيغة إلى أخرى. تنظر هذه المقالة في الميزة التي تحول FDF إلى XML.

{{% /alert %}}

## التفاصيل

FDF يرمز إلى صيغة بيانات النماذج، وملف FDF يحتوي على قيم النماذج في زوج مفتاح/قيمة.
``` نحن نعلم أيضًا أن ملف XML يحتوي على القيم كعلامات. حيث يتم تمثيل المفتاح غالبًا كاسم العلامة ويتم تمثيل القيمة كالقيمة داخل تلك العلامة. الآن، يوفر لنا [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) المرونة لتحويل تنسيق ملف FDF إلى تنسيق XML.

يمكننا استخدام فئة [FormDataConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formdataconverter) لهذا الغرض. توفر لنا هذه الفئة طرقًا مختلفة لتحويل تنسيق بيانات واحد إلى تنسيق آخر. في هذه المقالة، سنستخدم فقط طريقة واحدة تسمى [ConvertFdfToXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formdataconverter/methods/convertfdftoxml). تأخذ هذه الطريقة ملف FDF كمدخل أو تيار مصدر وتحفظه بتنسيق XML.

يظهر لك مقطع الشيفرة التالي كيفية تحويل ملف FDF إلى ملف XML: 

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConvertPdfToXML-ConvertPdfToXML.cs" >}}