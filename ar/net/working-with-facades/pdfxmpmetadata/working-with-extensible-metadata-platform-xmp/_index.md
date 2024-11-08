---

title: Extensible Metadata Platform - XMP

type: docs

weight: 10

url: /ar/net/working-with-extensible-metadata-platform-xmp/

description: يشرح هذا القسم كيفية العمل مع منصة البيانات التعريفية الممتدة - XMP باستخدام فئة PdfXmpMetadata.

lastmod: "2021-06-05"

draft: false

---

{{% alert color="primary" %}}

منصة البيانات التعريفية الممتدة (XMP) هي معيار أنشأته شركة Adobe Systems Inc. تم تطوير هذا المعيار لمعالجة وتخزين البيانات التعريفية القياسية والملكية. يمكن تضمين هذه البيانات التعريفية في تنسيقات ملفات مختلفة، ولكن في هذه المقالة سنركز فقط على تنسيق ملف PDF. سنرى كيف يمكننا تضمين البيانات التعريفية في ملف PDF باستخدام مساحة الأسماء Aspose.Pdf.Facades في Aspose.PDF لـ .NET. سنستخدم فئة [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) للتعامل مع XMP في مستند PDF.

{{% /alert %}}

## الخلفية

يمر ملف PDF بالعديد من المراحل خلال فترة حياته. نحن نقوم بإنشاء مستند PDF ثم نقوم بإرساله إلى أشخاص أو أقسام أخرى لمزيد من المعالجة. ومع ذلك، خلال هذه العملية نحتاج إلى تتبع الجوانب المختلفة للتغييرات التي تم إجراؤها. XMP يخدم هذا الغرض من تتبع التغييرات أو المعلومات الأخرى حول البيانات في الملف.

## الشرح

من أجل معالجة XMP باستخدام Aspose.Pdf.Facades، سنستخدم فئة [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class). سنستخدم هذه الفئة لمعالجة خصائص البيانات الوصفية المعرفة مسبقًا. فئة [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class) تضيف هذه الخصائص إلى ملف PDF. كما أنها تساعد في فتح وحفظ ملفات PDF التي نقوم بإضافة البيانات الوصفية إليها. لذا، باستخدام فئة [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class)، يمكننا بسهولة معالجة XMP في ملف PDF.

سيُساعدك الرمز التالي في فهم كيفية استخدام فئة [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) للعمل مع XMP:
{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ExtensibleMetadataPlatform-ExtensibleMetadataPlatform.cs" >}}

## الخاتمة

{{% alert color="primary" %}}
في هذه المقالة، رأينا كيف يمكننا العمل مع XMP باستخدام Aspose.Pdf.Facades. [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class)، المستخدم في هذه المقالة، يجعل من السهل جدًا على المستخدم التلاعب بالبيانات الوصفية في مستند PDF. إذا تم استخدام فئة [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class) بشكل صحيح، فسيكون من السهل جدًا دمج الذكاء في ملفات PDF، وجعل الويب الدلالي أقرب قليلاً إلى التحقيق.
{{% /alert %}}