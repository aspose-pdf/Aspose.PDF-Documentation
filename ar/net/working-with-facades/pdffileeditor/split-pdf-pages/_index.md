---
title: تقسيم صفحات PDF
type: docs
weight: 60
url: /ar/net/split-pdf-pages/
description: يشرح هذا القسم كيفية تقسيم صفحات PDF باستخدام Aspose.PDF Facades باستخدام فئة PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

## تقسيم صفحات PDF من البداية باستخدام مسارات الملفات

تسمح لك طريقة [SplitFromFirst](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) لفئة [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor) بتقسيم ملف PDF بدءًا من الصفحة الأولى وانتهاءً برقم الصفحة المحدد. إذا كنت ترغب في معالجة ملفات PDF من القرص، يمكنك تمرير مسارات الملفات لملفات PDF المدخلة والمخرجة إلى هذه الطريقة. يظهر لك مقتطف الكود التالي كيف يتم تقسيم صفحات PDF من البداية باستخدام مسارات الملفات.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesUsingPaths-SplitPagesUsingPaths.cs" >}}

## تقسيم صفحات PDF من البداية باستخدام تدفقات الملفات


[SplitFromFirst](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) طريقة من فئة [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor) تسمح لك بتقسيم ملف PDF بدءًا من الصفحة الأولى وانتهاءً برقم الصفحة المحدد. إذا كنت تريد معالجة ملفات PDF من التدفقات، يمكنك تمرير تدفقات PDF المدخلة والمخرجة إلى هذه الطريقة. يوضح لك المثال التالي كيفية تقسيم صفحات PDF من الأولى باستخدام تدفقات الملفات.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesUsingStreams-SplitPagesUsingStreams.cs" >}}

## تقسيم صفحات PDF إلى مجموعات باستخدام مسارات الملفات

طريقة [SplitToBulks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/methods/splittobulks/index) من فئة [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor) تسمح لك بتقسيم ملف PDF إلى مجموعات متعددة من الصفحات. في هذا المثال، نحتاج إلى مجموعتين من الصفحات (1، 2) و(5، 6). إذا كنت ترغب في الوصول إلى ملف PDF من القرص، تحتاج إلى تمرير ملف PDF المدخل كمسار ملف. تعيد هذه الطريقة مصفوفة من MemoryStream. يمكنك التنقل خلال هذه المصفوفة وحفظ المجموعات الفردية من الصفحات كملفات منفصلة. يُظهر لك مقطع الكود التالي كيفية تقسيم صفحات PDF إلى مجموعات باستخدام مسارات الملفات.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToBulkUsingPaths-SplitPagesToBulkUsingPaths.cs" >}}

## تقسيم صفحات PDF إلى مجموعات باستخدام التدفقات

طريقة [SplitToBulks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittobulks/index) من فئة [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) تتيح لك تقسيم ملف PDF إلى مجموعات متعددة من الصفحات. في هذا المثال، نحتاج إلى مجموعتين من الصفحات (1, 2) و(5, 6). يمكنك تمرير تدفق إلى هذه الطريقة بدلاً من الوصول إلى الملف من القرص. تُرجع هذه الطريقة مصفوفة من MemoryStream. يمكنك التجول عبر هذه المصفوفة وحفظ مجموعات الصفحات الفردية كملفات منفصلة. يوضح لك مقتطف الشيفرة التالي كيفية تقسيم صفحات PDF إلى حجم باستخدام التدفقات.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToBulkUsingStreams-SplitPagesToBulkUsingStreams.cs" >}}

## تقسيم صفحات PDF إلى النهاية باستخدام مسارات الملفات

طريقة [SplitToEnd](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittoend/index) في فئة [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) تتيح لك تقسيم ملف PDF من رقم الصفحة المحدد إلى نهاية ملف PDF وحفظه كملف PDF جديد. من أجل القيام بذلك، باستخدام مسارات الملفات، تحتاج إلى تمرير مسارات ملفات الإدخال والإخراج ورقم الصفحة التي يجب أن يبدأ منها الانقسام. سيتم حفظ ملف PDF الناتج على القرص. يُظهر لك جزء الشيفرة التالي كيفية تقسيم صفحات PDF إلى النهاية باستخدام مسارات الملفات.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToEndUsingPaths-SplitPagesToEndUsingPaths.cs" >}}

## تقسيم صفحات PDF إلى النهاية باستخدام التدفقات

طريقة [SplitToEnd](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittoend/index) الخاصة بفئة [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) تتيح لك تقسيم ملف PDF من رقم الصفحة المحددة إلى نهاية ملف PDF وحفظه كملف PDF جديد. من أجل القيام بذلك، باستخدام التدفقات، تحتاج إلى تمرير تدفقات الإدخال والإخراج ورقم الصفحة التي يجب بدء التقسيم منها. سيتم حفظ ملف PDF الناتج في تدفق الإخراج. يوضح لك مقتطف الكود التالي كيفية تقسيم صفحات PDF حتى النهاية باستخدام التدفقات.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToEndUsingStreams-SplitPagesToEndUsingStreams.cs" >}}

## تقسيم ملف PDF إلى صفحات فردية باستخدام مسارات الملفات

{{% alert color="primary" %}}

يمكنك محاولة تقسيم مستند PDF وعرض النتائج عبر الإنترنت من خلال هذا الرابط:

[products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter) {{% /alert %}}

من أجل تقسيم ملف PDF إلى صفحات فردية، تحتاج إلى تمرير ملف PDF كمسار ملف إلى طريقة [SplitToPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index). هذه الطريقة ستعيد مصفوفة من MemoryStream تحتوي على صفحات فردية من ملف PDF. يمكنك التجول عبر هذه المصفوفة من MemoryStream وحفظ الصفحات الفردية كملفات PDF منفصلة على القرص. يوضح لك مقطع الشيفرة التالي كيفية تقسيم ملف PDF إلى صفحات فردية باستخدام مسارات الملفات.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitToIndividualPagesUsingPaths-SplitToIndividualPagesUsingPaths.cs" >}}

## تقسيم ملف PDF إلى صفحات فردية باستخدام التدفقات

لتقسيم ملف PDF إلى صفحات فردية، تحتاج إلى تمرير ملف PDF كتيار إلى طريقة [SplitToPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index). هذه الطريقة ستعيد مصفوفة من MemoryStream تحتوي على صفحات فردية من ملف PDF. يمكنك التجول عبر هذه المصفوفة من MemoryStream وحفظ الصفحات الفردية كملفات PDF فردية على القرص، أو يمكنك الاحتفاظ بهذه الصفحات الفردية في ذاكرة التخزين المؤقت للاستخدام لاحقًا في تطبيقك. يظهر لك مقتطف الكود التالي كيفية تقسيم PDF إلى صفحات فردية باستخدام التدفقات.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitToIndividualPagesUsingStreams-SplitToIndividualPagesUsingStreams.cs" >}}