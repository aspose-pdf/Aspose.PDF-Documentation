---
title: تحرير الصفحات الفردية في ملف PDF
type: docs
weight: 20
url: /ar/net/editing-a-pdf-s-individual-pages-using-pdfpageeditor-class/
description: يشرح هذا القسم كيفية تحرير الصفحات الفردية في ملف PDF باستخدام فئة PdfPageEditor.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

تسمح مساحة الأسماء Aspose.Pdf.Facades في [Aspose.PDF for .NET](/pdf/ar/net/) لك بالتعامل مع الصفحات الفردية في ملف PDF. تساعدك هذه الميزة على العمل مع عرض الصفحة، المحاذاة، والانتقال إلخ. تساعد فئة PdfPageEditor في تحقيق هذه الوظيفة. في هذه المقالة، سننظر في الخصائص والطرق المقدمة من قبل هذه الفئة وعمل هذه الطرق أيضًا.

{{% /alert %}}

## التفسير

فئة [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) تختلف عن فئة [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) و [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). 
أولاً نحتاج إلى فهم الفرق، ومن ثم سنكون قادرين على فهم فئة PdfPageEditor بشكل أفضل. تتيح لك فئة PdfFileEditor التلاعب بجميع الصفحات في ملف مثل الإضافة، الحذف، أو دمج الصفحات وما إلى ذلك، بينما تساعدك فئة PdfContentEditor في التلاعب بمحتويات الصفحة أي النصوص والكائنات الأخرى وما إلى ذلك. بينما، تعمل فئة PdfPageEditor فقط مع الصفحة الفردية نفسها مثل التدوير، التكبير، ومحاذاة الصفحة وما إلى ذلك.

يمكننا تقسيم الميزات التي تقدمها هذه الفئة إلى ثلاث فئات رئيسية وهي الانتقال، المحاذاة، والعرض. سوف نناقش هذه الفئات أدناه:

### الانتقال

تحتوي هذه الفئة على خاصيتين تتعلقان بالانتقال أي.
``` [TransitionType](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/transitiontype) و [TransitionDuration](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/transitionduration). يحدد TransitionType نمط الانتقال الذي سيتم استخدامه عند الانتقال إلى هذه الصفحة من صفحة أخرى أثناء العرض التقديمي. يحدد TransitionDuration مدة العرض للصفحات.

### المحاذاة

تدعم فئة PdfPageEditor المحاذاة الأفقية والعمودية. 
يوفر خاصيتين لخدمة الغرض وهما [Alignment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/alignment) و [VerticalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/VerticalAlignment). تُستخدم خاصية Alignment لمحاذاة المحتويات أفقيًا. تأخذ خاصية Alignment قيمة من نوع AlignmentType، والتي تحتوي على ثلاثة خيارات وهي Center، Left، و Right. تأخذ خاصية VerticalAlignment قيمة من نوع VerticalAlignmentType، والتي تحتوي على ثلاثة خيارات وهي Bottom، Center، و Top.

### العرض

تحت فئة العرض يمكننا تضمين خصائص مثل PageSize، Rotation، Zoom، و DisplayDuration.
``` 
PageSize property specifies the size of individual page in the file. This property takes PageSize object as an input, which encapsulates predefined page size like A0, A1, A2, A3, A4, A5, A6, B5, Letter, Ledger, and P11x17. Rotation property is used to set the rotation of an individual page. It can take values 0, 90, 180, or 270. Zoom property sets the zoom coefficient for the page, and it takes a float value as an input. This class also provides method to get page size and page rotation of the individual page in the file.

يمكنك العثور على أمثلة للطرق المذكورة أعلاه في مقتطف الشيفرة أدناه:



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-EditPdfPages-EditPdfPages.cs" >}}

## الاستنتاج

{{% alert color="primary" %}}
في هذه المقالة، ألقينا نظرة فاحصة على فئة [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor).
``` We have elaborated the properties and methods provided by this class. It makes the manipulation of individual pages in a class a very easy and simple task.  
لقد قمنا بتوضيح الخصائص والطرق التي توفرها هذه الفئة. يجعل التعامل مع الصفحات الفردية في فئة مهمة سهلة وبسيطة للغاية.  
{{% /alert %}}