---
title: دمج مستندات PDF في C#
linktitle: دمج مستندات PDF
type: docs
weight: 20
url: /ar/net/concatenate-pdf-documents/
description: يوضح هذا القسم كيفية دمج مستندات PDF باستخدام Aspose.PDF Facades باستخدام فئة PdfFileEditor.
lastmod: "2021-06-05"
---

## **نظرة عامة**

تشرح هذه المقالة كيفية دمج أو توحيد أو دمج ملفات PDF مختلفة في ملف PDF واحد باستخدام C#. وتغطي مواضيع مثل

- [دمج ملفات PDF باستخدام C#](#concatenate-pdf-files-using-file-paths)
- [توحيد ملفات PDF باستخدام C#](#concatenate-pdf-files-using-file-paths)

- [دمج ملفات PDF متعددة في ملف واحد باستخدام C#](#concatenate-array-of-pdf-files-using-file-paths)
- [C# دمج ملفات PDF متعددة في ملف PDF واحد](#concatenate-array-of-pdf-files-using-file-paths)
- [C# دمج جميع ملفات PDF في مجلد](#concatenating-all-pdf-files-in-particular-folder)
- [C# دمج جميع ملفات PDF في مجلد](#concatenating-all-pdf-files-in-particular-folder)
- [C# دمج ملفات PDF باستخدام مسارات الملفات](#concatenate-pdf-files-using-file-paths)
- [C# دمج ملفات PDF باستخدام التدفقات](#concatenate-array-of-pdf-files-using-streams)
- [C# دمج جميع ملفات PDF في المجلد](#concatenate-pdf-files-in-folder)

## دمج ملفات PDF باستخدام مسارات الملفات

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) هي الفئة في [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) التي تتيح لك دمج ملفات PDF متعددة. يمكنك ليس فقط دمج الملفات باستخدام FileStreams ولكن أيضًا باستخدام MemoryStreams أيضًا. في هذه المقالة، سيتم شرح عملية دمج الملفات باستخدام MemoryStreams ثم عرضها باستخدام مقتطف الكود.

يمكن استخدام طريقة [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) من فئة [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) لدمج ملفي PDF. تتيح لك طريقة [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) تمرير ثلاث معلمات: ملف PDF المدخل الأول، ملف PDF المدخل الثاني، وملف PDF الناتج. يحتوي ملف PDF الناتج النهائي على كلا ملفي PDF المدخلين.

يوضح لك مقتطف الكود C# التالي كيفية دمج ملفات PDF باستخدام مسارات الملفات.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateUsingPath-ConcatenateUsingPath.cs" >}}

في بعض الحالات، عندما يكون هناك الكثير من المخططات، قد يقوم المستخدمون بتعطيلها من خلال تعيين CopyOutlines إلى false وتحسين أداء الدمج.
{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateUsingPath-CopyOutline.cs" >}}

## دمج ملفات PDF متعددة باستخدام MemoryStreams

طريقة [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) من فئة [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) تأخذ ملفات PDF المصدر وملف PDF الوجهة كمعاملات. يمكن أن تكون هذه المعاملات إما مسارات لملفات PDF على القرص أو يمكن أن تكون MemoryStreams. الآن، في هذا المثال، سنقوم أولاً بإنشاء تدفقين للملفات لقراءة ملفات PDF من القرص. ثم سنقوم بتحويل هذه الملفات إلى مصفوفات بايت. سيتم تحويل هذه المصفوفات البايتية لملفات PDF إلى MemoryStreams. بمجرد حصولنا على MemoryStreams من ملفات PDF، سنكون قادرين على تمريرها إلى طريقة الدمج والدمج في ملف إخراج واحد.

يظهر لك مقتطف الكود C# التالي كيفية دمج ملفات PDF متعددة باستخدام MemoryStreams:

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenateMultiplePDFUsingMemoryStream-ConcatenateMultiplePDFUsingMemoryStream.cs" >}}

## دمج مجموعة من ملفات PDF باستخدام مسارات الملفات

إذا كنت تريد دمج ملفات PDF متعددة، يمكنك استخدام التحميل الزائد لطريقة [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index)، والتي تسمح لك بتمرير مصفوفة من ملفات PDF. يتم حفظ الناتج النهائي كملف مدمج تم إنشاؤه من جميع الملفات في المصفوفة. يظهر لك مقتطف الشيفرة C# التالي كيفية دمج مجموعة من ملفات PDF باستخدام مسارات الملفات.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateArrayOfFilesWithPath-ConcatenateArrayOfFilesWithPath.cs" >}}

## دمج مجموعة من ملفات PDF باستخدام التدفقات

دمج مجموعة من ملفات PDF لا يقتصر فقط على الملفات الموجودة على القرص. يمكنك أيضًا دمج مجموعة من ملفات PDF من التدفقات. إذا كنت ترغب في دمج ملفات PDF متعددة، يمكنك استخدام التحميل الزائد المناسب لطريقة [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index). أولاً، تحتاج إلى إنشاء مجموعة من تدفقات الإدخال وتدفق واحد لملف PDF الناتج، ثم استدعاء طريقة [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index). سيتم حفظ الناتج في تدفق الإخراج. يوضح لك جزء الشفرة C# التالي كيفية دمج مجموعة من ملفات PDF باستخدام التدفقات.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateArrayOfPdfUsingStreams-ConcatenateArrayOfPdfUsingStreams.cs" >}}

## دمج جميع ملفات Pdf في مجلد معين

يمكنك حتى قراءة جميع ملفات Pdf في مجلد معين أثناء وقت التشغيل ودمجها، دون حتى معرفة أسماء الملفات. قدم مسار الدليل الذي يحتوي على مستندات PDF التي ترغب في دمجها.

يرجى تجربة استخدام جزء الكود C# التالي لتحقيق هذه الوظيفة.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatingAllPdfFiles-ConcatenatingAllPdfFiles.cs" >}}

## دمج نماذج PDF والحفاظ على أسماء الحقول فريدة

توفر فئة [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) في [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) القدرة على دمج ملفات PDF. الآن، إذا كانت ملفات Pdf التي سيتم دمجها تحتوي على حقول نموذج بأسماء حقول مشابهة، يوفر Aspose.PDF ميزة الحفاظ على الحقول في ملف Pdf الناتج كفريدة كما يمكنك تحديد اللاحقة لجعل أسماء الحقول فريدة. خاصية [KeepFieldsUnique](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/properties/keepfieldsunique) الخاصة بـ [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) كـ true ستجعل أسماء الحقول فريدة عند دمج نماذج Pdf. أيضًا، يمكن استخدام خاصية [UniqueSuffix](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/properties/uniquesuffix) الخاصة بـ PdfFileEditor لتحديد تنسيق اللاحقة الذي يحدده المستخدم والذي يضاف إلى اسم الحقل لجعله فريدًا عند دمج النماذج. يجب أن تحتوي هذه السلسلة على الجزء الفرعي `%NUM%` والذي سيتم استبداله بالأرقام في الملف الناتج.

يرجى الاطلاع على مقتطف الكود البسيط التالي لتحقيق هذه الوظيفة.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePDFForms-ConcatenatePDFForms.cs" >}}
## دمج ملفات PDF وإنشاء جدول المحتويات

## دمج ملفات PDF

يرجى الإطلاع على مقتطف الشيفرة التالية للحصول على معلومات حول كيفية دمج ملفات PDF.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-ConcatenatePdfFilesAndCreateTOC.cs" >}}

### إدراج صفحة فارغة

بمجرد دمج ملفات PDF، يمكننا إدراج صفحة فارغة في بداية المستند حيث يمكننا إنشاء جدول المحتويات. لتحقيق هذا المتطلب، يمكننا تحميل الملف المدمج في كائن **Document** ونحتاج إلى استدعاء طريقة Page.Insert(...) لإدراج صفحة فارغة.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-InsertBlankPage.cs" >}}

### إضافة طوابع نصية

لإنشاء جدول محتويات، نحتاج إلى إضافة طوابع نصية في الصفحة الأولى باستخدام كائنات [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) و[Stamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp). 
توفر فئة Stamp طريقة `BindLogo(...)` لإضافة [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) ويمكننا أيضًا تحديد الموقع لإضافة هذه الأختام النصية باستخدام طريقة `SetOrigin(..)`. في هذه المقالة، نحن نقوم بدمج ملفي PDF، لذلك نحتاج إلى إنشاء كائنين لختم النص يشيران إلى هذه المستندات الفردية.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-AddTextStamps.cs" >}}

### إنشاء روابط محلية

الآن نحن بحاجة إلى إضافة روابط نحو الصفحات داخل الملف المدمج. لتحقيق هذا المتطلب، يمكننا استخدام طريقة `CreateLocalLink(..)` لفئة [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). في مقطع الكود التالي، قمنا بتمرير Transparent كحجة رابعة بحيث لا يظهر المستطيل حول الرابط.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-CreateLocalLinks.cs" >}}
```
### الشيفرة الكاملة

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-CompletedCode.cs" >}}

## دمج ملفات PDF في مجلد

فئة [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) في مساحة الأسماء Aspose.Pdf.Facades تقدم لك القدرة على دمج ملف PDF. يمكنك حتى قراءة جميع ملفات Pdf في مجلد معين أثناء وقت التشغيل ودمجها، دون حتى معرفة أسماء الملفات. ببساطة قم بتوفير مسار الدليل الذي يحتوي على مستندات PDF التي ترغب في دمجها.

يرجى محاولة استخدام مقتطف الشيفرة C# التالي لتحقيق هذه الوظيفة من Aspose.PDF:

```csharp
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

// استرجاع أسماء جميع ملفات Pdf في دليل معين
string[] fileEntries = Directory.GetFiles(dataDir, "*.pdf");

// الحصول على التاريخ الحالي للنظام وتعيين تنسيقه
string date = DateTime.Now.ToString("MM-dd-yyyy");
// الحصول على الوقت الحالي للنظام وتعيين تنسيقه
string hoursSeconds = DateTime.Now.ToString("hh-mm");
// تعيين القيمة للمستند النهائي الناتج Pdf
string masterFileName = date + "_" + hoursSeconds + "_out.pdf";

// إنشاء كائن PdfFileEditor
Aspose.Pdf.Facades.PdfFileEditor pdfEditor = new PdfFileEditor();

// استدعاء طريقة Concatenate لكائن PdfFileEditor لدمج جميع الملفات المدخلة
// في ملف إخراج واحد
pdfEditor.Concatenate(fileEntries, dataDir + masterFileName);
```