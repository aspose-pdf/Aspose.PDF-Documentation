---
title: ما الجديد
linktitle: ما الجديد
type: docs
weight: 10
url: /net/whatsnew/
description: تقدم هذه الصفحة أبرز الميزات الجديدة في Aspose.PDF لـ .NET التي تم تقديمها في الإصدارات الأخيرة.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2024-09-06"
---

## ما الجديد في Aspose.PDF 24.8

تحويل مستندات PDF إلى تنسيق PDF/A-4

منذ الإصدار 24.8، أصبح من الممكن تحويل مستندات PDF إلى PDF/A-4. الجزء 4 من المعيار، والذي يعتمد على PDF 2.0، تم نشره في أواخر 2020.

يوضح الشيفرة التالية كيفية تحويل مستند إلى تنسيق PDF/A-4 بفرض أن المستند المدخل هو PDF 2.x.

```cs

    string documentPath = "";
    string conversionLogPath = "";
    string resultPdfPath ="";

    using (var document = new Document(documentPath))
    {
        // فقط مستندات PDF-2.x يمكن تحويلها إلى PDF/A-4
        document.Convert(conversionLogPath, PdfFormat.PDF_A_4, ConvertErrorAction.Delete);
        document.Save(resultPdfPath);
    }
```
يوضح الجزء الثاني من الكود كيفية تحويل مستند إلى تنسيق PDF/A-4 عندما يكون المستند المدخل من إصدار سابق.

```cs
    string documentPath = "";
    string conversionLogPath = "";
    string resultPdfPath ="";

    using (var document = new Document(documentPath))
    {
        document.Convert(Stream.Null, PdfFormat.v_2_0, ConvertErrorAction.Delete);

        document.Convert(conversionLogPath, PdfFormat.PDF_A_4, ConvertErrorAction.Delete);
        document.Save(resultPdfPath);
    }
```

منذ الإصدار 24.8، قمنا بتقديم طريقة لتسطيح المحتوى الشفاف في مستندات PDF:

```cs
    string documentPath = "";
    string resultPdfPath ="";

    using (var document = new Document(documentPath))
    {
        document.FlattenTransparency();
        document.Save(resultPdfPath);
    }
```

## ما الجديد في Aspose.PDF 24.7

مقارنة مستندات PDF مع Aspose.PDF لـ .NET

منذ الإصدار 24.7، أصبح من الممكن مقارنة محتوى مستندات PDF باستخدام علامات التوضيح والعرض جنبًا إلى جنب:

الجزء الأول من الكود يوضح كيفية مقارنة الصفحات الأولى من مستندين PDF.
الشفرة الأولى توضح كيفية مقارنة الصفحات الأولى من مستندين PDF.

```cs
    string documentPath1 = "";
    string documentPath2= "";

    string resultPdfPath ="";

    using (Document document1 = new Document(documentPath1), document2 = new Document(documentPath2))
    {
        SideBySidePdfComparer.Compare(document1.Pages[1], document2.Pages[1], resultPdfPath, new SideBySideComparisonOptions()
        {
            AdditionalChangeMarks = true,
            ComparisonMode = ComparisonMode.IgnoreSpaces
        });
    }
```

الشفرة الثانية توسع النطاق لمقارنة المحتوى الكامل لمستندين PDF.

```cs
    string documentPath1 = "";
    string documentPath2 = "";

    string resultPdfPath ="";

    using (Document document1 = new Document(documentPath1), document2 = new Document(documentPath2))
    {
        SideBySidePdfComparer.Compare(document1, document2, resultPdfPath, new SideBySideComparisonOptions()
        {
            AdditionalChangeMarks = true,
            ComparisonMode = ComparisonMode.IgnoreSpaces
        });
    }
```
## ما الجديد في Aspose.PDF 24.4

تدعم هذه الإصدارة تطبيق قناع القص على الصور:

```cs

    Document doc = new Document("input.pdf");
    using (var fs1 = new FileStream("mask1.jpg", FileMode.Open))
    using (var fs2 = new FileStream("mask2.png", FileMode.Open))
    {
        doc.Pages[1].Resources.Images[1].AddStencilMask(fs1);
        doc.Pages[1].Resources.Images[2].AddStencilMask(fs2);
    }
```

منذ الإصدار 24.4 يمكنك اختيار مصدر الورق بناءً على حجم صفحة PDF في مربع الحوار الطباعة باستخدام الواجهة البرمجية

ابتداءً من Aspose.PDF 24.4، يمكن تفعيل هذا الخيار أو إيقافه باستخدام خاصية Document.PickTrayByPdfSize أو واجهة PdfContentEditor:

```cs

    using (Document document = new Document())
    {
        Page page = document.Pages.Add();
        page.Paragraphs.Add(new TextFragment("مرحباً بالعالم!"));

        // تعيين العلم لاختيار درج الورق باستخدام حجم صفحة PDF
        document.PickTrayByPdfSize = true;
        document.Save("result.pdf");
    }
```
```cs
    باستخدام (PdfContentEditor contentEditor = new PdfContentEditor())
    {
        contentEditor.BindPdf("input.pdf");

        // تعيين العلم لاختيار درج الورق باستخدام حجم صفحة PDF
        contentEditor.ChangeViewerPreference(ViewerPreference.PickTrayByPDFSize);
        contentEditor.Save("result.pdf");
    }
```

من هذا الإصدار تم إضافة إضافة Aspose.PDF Signature لـ .NET:

- مثال على إنشاء حقل جديد وخيارات:

```cs

    // إنشاء توقيع
    var plugin = new Signature();
    // إنشاء كائن SignOptions لتعيين التعليمات
    var opt = new SignOptions(inputPfxPath, inputPfxPassword);
    // إضافة مسار ملف الإدخال
    opt.AddInput(new FileDataSource(inputPath));
    // تعيين مسار ملف الإخراج
    opt.AddOutput(new FileDataSource(outputPath));
    // تعيين خيارات إضافية
    opt.Reason = "سببي";
    opt.Contact = "اتصالي";
    opt.Location = "موقعي";
    // تنفيذ العملية
    plugin.Process(opt);
```

- مثال مع حقل توقيع فارغ موجود

```cs

    // إنشاء توقيع
    var plugin = new Signature();
    // إنشاء كائن SignOptions لتعيين التعليمات
    var opt = new SignOptions(inputPfxPath, inputPfxPassword);
    // إضافة مسار ملف الإدخال مع حقل توقيع فارغ
    opt.AddInput(new FileDataSource(inputPath));
    // تعيين مسار ملف الإخراج
    opt.AddOutput(new FileDataSource(outputPath));
    // تعيين اسم حقل التوقيع الموجود
    opt.Name = "Signature1";
    // تنفيذ العملية
    plugin.Process(opt);
```
## ما الجديد في Aspose.PDF 24.3

من هذا الإصدار تم إضافة إضافة PDF/A Converter لـ .NET:

```cs

    var options = new PdfAConvertOptions
    {
        PdfAVersion = PdfAStandardVersion.PDF_A_3B
    };

    // إضافة ملف المصدر
    options.AddInput(new FileDataSource("path_to_your_pdf_file.pdf")); // استبدل بمسار ملفك الفعلي

    // إضافة المسار لحفظ الملف المحول
    options.AddOutput(new FileDataSource("path_to_the_converted_file.pdf"));

    // إنشاء نسخة من الإضافة
    var plugin = new PdfAConverter();

    // تنفيذ التحويل
    plugin.Process(options);
```

- تنفيذ بحث من خلال قائمة عبارات في TextFragmentAbsorber:

```cs

    var regexes = new Regex[]
    {
    new Regex(@"(?s)document\s+(?:(?:no\(?s?\)?\.?)|(?:number(?:\(?s\)?)?))\s+(?:(?:[\w-]*\d[\w-]*)+(?:[,;\s]|and)*)+", RegexOptions.IgnoreCase),
    new Regex(@"[\s\r\n]+Tract[\s\r\n]+of:?", RegexOptions.IgnoreCase),
    new Regex(@"vested[\s\r\n]+in", RegexOptions.IgnoreCase),
    new Regex("Vested in:", RegexOptions.IgnoreCase),
    new Regex(@"file.?[\s\r\n]+(?:nos?|numbers?|#s?|nums?).?[\s\r\n]+(\d+)-(\d+)", RegexOptions.IgnoreCase),
    new Regex(@"file.?[\s\r\n]+nos?.?:?[\s\r\n]+([\d\r\n-]+)", RegexOptions.IgnoreCase)
    };
    var document = new Document(input);
    var absorber = new TextFragmentAbsorber(
    regexes,
    new TextSearchOptions(true)
    );
    document.Pages.Accept(absorber);
    // الحصول على النتائج
    var result = absorber.RegexResults
```
منذ 24.3 أصبح من الممكن إضافة حقل توقيع فارغ على كل صفحة إلى ملف PDF/A

```cs
    static void Main(string[] args)
    {
        try
        {
            var lic = new Aspose.Pdf.License();
            lic.SetLicense("Aspose.Total.lic");

            string source = "source.pdf";
            string fieldName = "signature_1234";
            string dest = "source_fieldNotInAllPages.pdf";
            addFieldSingle_NewCode(source, dest, fieldName, 1);
        }
        catch (Exception e)
        {
            Console.WriteLine(e.ToString());
        }
        Console.ReadLine(); 
    }

    private static void addFieldSingle_NewCode(string source, string dest, string fieldName, int page)
    {
        File.Copy(source, dest, true);
        using (var fs = new FileStream(dest, FileMode.Open))
        {
            // الكود المقترح الجديد، باستخدام كائن SignatureField (هذا الكود يعمل بشكل جيد)
            var doc = new Document(fs);
            var f = new SignatureField(doc.Pages[page], new Rectangle(10, 10, 100, 100));
            // إضافة المظهر الافتراضي لحقل التوقيع
            f.DefaultAppearance = new DefaultAppearance("Helv", 12, System.Drawing.Color.Black);
            var newAddedField = doc.Form.Add(f, fieldName, page);

            // كيف يمكن الآن جعل newAddedField مرئية في جميع الصفحات؟
            Aspose.Pdf.Annotations.Annotation addedField = null;
            foreach (Aspose.Pdf.Annotations.Annotation a in doc.Pages[1].Annotations)
            {
            if (a.FullName == fieldName)
                {
                    addedField = a;
                    break;
                }
            }
            if (addedField != null)
            {
                for (int p = 1; p <= doc.Pages.Count; p++)
                {
                    if (p == page) continue;
                    doc.Pages[p].Annotations.Add(addedField);
                }
            }

            doc.Save();
        }
        System.Diagnostics.Process.Start(dest);
    }
```
## ما الجديد في Aspose.PDF 24.2

منذ الإصدار 24.2، أصبح من الممكن الحصول على البيانات المتجهة من ملف PDF

تم تنفيذ GraphicsAbsorber للحصول على البيانات المتجهة من المستندات:

```cs

var doc = new Document(input);
var grAbsorber = new GraphicsAbsorber();
grAbsorber.Visit(doc.Pages[1]);
var elements = grAbsorber.Elements;
var operators = elements[1].Operators;
var rectangle = elements[1].Rectangle;
var position = elements[1].Position;
```

## ما الجديد في Aspose.PDF 24.1

منذ إصدار 24.1، أصبح من الممكن استيراد تعليقات توضيحية بتنسيق FDF إلى PDF:

```cs

    var fdfPath = Params.InputPath + "50745.fdf";
    var templatePath = Params.InputPath + "Empty.pdf";
    var outputPath = Params.OutputPath + "50745_form.pdf";

    using (var form = new Aspose.Pdf.Facades.Form(templatePath))
    {
        using (var fdfInputStream = new FileStream(fdfPath, FileMode.Open))
        {
            form.ImportFdf(fdfInputStream);
        }

        form.Save(outputPath);
    }
```

كما يدعم الوصول إلى قاموس الصفحة أو كتالوج الوثيقة.
يدعم أيضًا الوصول إلى قاموس الصفحة أو كتالوج المستند.

فيما يلي أمثلة على كود لمحرر القاموس:

- إضافة قيم جديدة

```cs

    // مثال على أسماء المفاتيح
    string KEY_NAME = "name";
    string KEY_STRING = "str";
    string KEY_BOOL = "bool";
    string KEY_NUMBER = "number";

    var outputPath = "page_dictionary_editor.pdf";
    using (var doc = new Document())
    {
        var page = doc.Pages.Add();
        var dictionaryEditor = new DictionaryEditor(page);

        dictionaryEditor.Add(KEY_NAME, new CosPdfName("name data"));
        dictionaryEditor.Add(KEY_STRING, new CosPdfString("string data"));
        dictionaryEditor.Add(KEY_BOOL, new CosPdfBoolean(true));
        dictionaryEditor.Add(KEY_NUMBER, new CosPdfNumber(11.2));

        doc.Save(outputPath);
    }
```

- إضافة وتعيين قيم للقاموس

```cs

    using (var doc = new Document())
    {
        var page = doc.Pages.Add();
        var dictionaryEditor = new DictionaryEditor(page);
        dictionaryEditor.Add(KEY_NAME, new CosPdfName("Old name"));
        // أو
        dictionaryEditor[KEY_NAME] = new CosPdfName("New name");
    }
```
- الحصول على قيمة من القاموس

```cs

    using (var doc = new Document())
    {
        var page = doc.Pages.Add();
        var dictionaryEditor = new DictionaryEditor(page);
        dictionaryEditor[KEY_NAME] = new CosPdfName("name");
        var value = dictionaryEditor[KEY_NAME];
        // أو 
        ICosPdfPrimitive primitive;
        dictionaryEditor.TryGetValue(KEY_NAME, out primitive);
    }
```

- إزالة القيمة من القاموس

```cs

    using (var doc = new Document())
    {
        var page = doc.Pages.Add();
        var dictionaryEditor = new DictionaryEditor(page);
        dictionaryEditor.Add(KEY_NAME, new CosPdfName(EXPECTED_NAME));
        dictionaryEditor.Remove(KEY_NAME);
    }
```

## ما الجديد في Aspose.PDF 23.12

يمكن العثور على النموذج واستبدال النص باستخدام الكود التالي:

```cs

    var document = new Document(input);
    var forms = document.Pages[1].Resources.Forms;

    foreach (var form in forms)
    {
        if (form.IT == "Typewriter" && form.Subtype == "Form")
        {
            var absorber = new TextFragmentAbsorber();
            absorber.Visit(form);

            foreach (var fragment in absorber.TextFragments)
            {
                fragment.Text = "";
            }
        }
    }

    document.Save(output);
```            

أو يمكن إزالة النموذج بالكامل:

```cs

    var document = new Document(input);
    var forms = document.Pages[1].Resources.Forms;

    for (int i = 1; i <= forms.Count; i++)
    {
        if (forms[i].IT == "Typewriter" && forms[i].Subtype == "Form")
        {
            forms.Delete(forms[i].Name);
        }
    }

    document.Save(output);
```            

نسخة أخرى لإزالة النموذج:

```cs

    var document = new Document(input);
    var forms = document.Pages[1].Resources.Forms;

    foreach (var form in forms)
    {
        if (form.IT == "Typewriter" && form.Subtype == "Form")
        {
            var name = forms.GetFormName(form);
            forms.Delete(name);
        }
    }

    document.Save(output);
``` 

- يمكن حذف جميع النماذج باستخدام الكود التالي:

```cs

    var document = new Document(input);
    var forms = document.Pages[1].Resources.Forms;

    forms.Clear();

    document.Save(output);
```
- تنفيذ تحويل PDF إلى Markdown:

```cs

    string markdownOutputFilePath = "output.md"
    string inputPdfPath = "input.pdf"
    using (Document doc = new Document(inputPdfPath))
    {
    MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
    saveOptions.ResourcesDirectoryName = "images"; 
    doc.Save(markdownOutputFilePath, saveOptions);
    }
```

- تنفيذ تحويل OFD إلى PDF:

```cs
    var document = new Document("sample.ofd", new OfdLoadOptions());
    document.Save("sample.pdf");
```

من هذا الإصدار تم إضافة إضافة الدمج:

```cs
    // مسار إلى الملف المدمج PDF الناتج.
    var outputPath = "TestMerge.pdf";

    // إنشاء نموذج جديد للدمج.
    var merger = new Merger();

    // إنشاء خيارات الدمج.
    var opt = new MergeOptions();
    opt.AddInput(new FileDataSource(inputPath1));
    opt.AddInput(new FileDataSource(inputPath2));
    opt.AddOutput(new FileDataSource(outputPath));

    // معالجة دمج PDF.
    merger.Process(opt);
```

كذلك، من هذا الإصدار تم إضافة إضافة ChatGPT:
أيضًا، تمت إضافة إضافة ChatGPT في هذا الإصدار:

```cs
    using (var plugin = new PdfChatGpt())
    {
    var options = new PdfChatGptRequestOptions();
    options.AddOutput(new FileDataSource("PdfChatGPT_output.pdf")); // أضف مسار ملف الإخراج.
    options.ApiKey = "مفتاح API الخاص بك."; // تحتاج إلى توفير المفتاح للوصول إلى API.
    options.MaxTokens = 1000; // الحد الأقصى لعدد الرموز الممكن توليدها في اكتمال الدردشة.

    // أضف رسائل الطلب.
    options.Messages.Add(new Message
    {
        Content = "أنت مساعد مفيد.",
        Role = Role.System
    });
    options.Messages.Add(new Message
    {
        Content = "ما هو أكبر قطر للبيتزا تم صنعه على الإطلاق؟",
        Role = Role.User
    });

    // معالجة الطلب.
    var result = await plugin.ProcessAsync(options);

    var fileResultPath = result.ResultCollection[0].Data;
    var chatCompletionObject = result.ResultCollection[1].Data as ChatCompletion; // كائن اكتمال دردشة واجهة برمجة تطبيقات ChatGPT.
    }
```

## ما الجديد في Aspose.PDF 23.11
## ما الجديد في Aspose.PDF 23.11

من هذا الإصدار من الممكن إزالة النص المخفي من ملف PDF:

```cs
    var document = new Document(inputFile);
    var textAbsorber = new TextFragmentAbsorber();

        // يمكن استخدام هذا الخيار لمنع تحرك قطع النص الأخرى بعد استبدال النص المخفي.
        textAbsorber.TextReplaceOptions = new TextReplaceOptions(TextReplaceOptions.ReplaceAdjustment.None);

        document.Pages.Accept(textAbsorber);

        foreach (var fragment in textAbsorber.TextFragments)
        {
            if (fragment.TextState.Invisible)
            {
                fragment.Text = "";
            }
        }

        document.Save(outputFile);
```

منذ 23.11 يدعم لتعطيل الخيوط:

```cs

    public void InterruptExample()
    {
        string outputFile = testdata + "sample.pdf";
        //هذا نص كبير، تم استخدام Lorem Ipsum في 8350 حرف لإحداث التعليق 
        string text = ExampleApp.LongText;
        using (InterruptMonitor monitor = new InterruptMonitor())
        {
            RowSpanWorker worker = new RowSpanWorker (outputFile, monitor);
            Thread thread = new Thread(new ThreadStart(worker.Work));
            thread.Start();

            // يجب أن يكون الوقت المحدد أقل من الوقت المطلوب لحفظ الوثيقة كاملة (بدون تعطيل).
            Thread.Sleep(500);

            // تعطيل العملية
            monitor.Interrupt();

            // الانتظار للتعطيل...
            thread.Join();
        }
        private class RowSpanWorker
        {
            private readonly string outputPath;
            private readonly InterruptMonitor monitor;

            public RowSpanWorker(string outputPath, InterruptMonitor monitor)
            {
                this.outputPath = outputPath;
                this.monitor = monitor;
            }
            public void Work()
            {
                string text = InterruptMonitorTests.LongText;
                using (var doc = new Document())
                {
                    InterruptMonitor.ThreadLocalInstance = this.monitor;
                    var page = doc.Pages.Add();

                    var table = new Aspose.Pdf.Table
                    {
                        DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F)
                    };

                    var row0 = table.Rows.Add();

                    // إضافة خلية تغطي صفين وتحتوي على نص طويل جداً
                    var cell00 = row0.Cells.Add(text);
                    cell00.RowSpan = 2;
                    cell00.IsWordWrapped = true;
                    row0.Cells.Add("Ipsum Ipsum Ipsum Ipsum Ipsum Ipsum ");
                    row0.Cells.Add("Dolor Dolor Dolor Dolor Dolor Dolor ");

                    var row1 = table.Rows.Add();
                    row1.Cells.Add("IpsumDolor Dolor Dolor Dolor Dolor ");
                    row1.Cells.Add("DolorDolor Dolor Dolor Dolor Dolor ");

                    page.Paragraphs.Add(table);

                    try
                    {
                        doc.Save(this.outputPath);
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine(ex.Message);
                    }
                }
            }
        }
    }
```
## ما الجديد في Aspose.PDF 23.10

التحديث الحالي يقدم ثلاث طرق لإزالة العلامات من ملفات PDF الموسومة.

- إزالة بعض عناصر العقدة من documentElement (عنصر الشجرة الجذرية):

```cs
    var document = new Document("some tagged pdf");
    var structure = document.LogicalStructure;
    var documentElement = structure.Children[0];
    var structElement = documentElement.Children.Count > 1 ? documentElement.Children[1] as StructElement : null;
    if (documentElement.Children.Remove(structElement))
    {
        // تمت إزالة العنصر
        document.Save(outputPath);
    }

    // يمكنك أيضاً حذف structElement نفسه
    //if (structElement != null)
    //{
    //    structElement.Remove();
    //    document.Save(outputPath);
    //}
```

- إزالة جميع علامات العناصر المحددة من المستند، لكن الحفاظ على عناصر الهيكل:

```cs
    var document = new Document("some tagged pdf");
    var structure = document.LogicalStructure;
    var root = structure.Children[0];
    var queue = new Queue<Element>();
    queue.Enqueue(root);
    while(queue.TryDequeue(out var element))
    {
        foreach (var child in element.Children)
        {
            queue.Enqueue(child);
        }

        if (element is TextElement || element is FigureElement)
        {
            element.Remove();
        }
    }
```
- إزالة العلامات تمامًا:

```cs
    var document = new Document("some tagged pdf");
    var structure = document.LogicalStructure;
    var documentElement = structure.Children[0];
    documentElement.Remove();
    document.Save(outputPath);
```

تم تنفيذ ميزة جديدة منذ 23.10 لقياس ارتفاع الحرف. استخدم الكود التالي لقياس ارتفاع حرف.

```cs
    var doc = new Document(input);
    var absorber = new TextFragmentAbsorber();
    absorber.Visit(doc.Pages[1]);
    var height = absorber.TextFragments[1].TextState.MeasureHeight('A')
```

لاحظ أن القياس يعتمد على الخط المضمن في المستند. إذا كانت أي معلومات لبُعد مفقودة، تعيد هذه الطريقة 0.

كما توفر هذه الإصدارة إمكانية التوقيع على ملف PDF باستخدام HASH موقع:

```cs
    public void PDFNET_54566()
    {
        var inputPdf = "54566.pdf";
        var inputP12 = "54566.p12";
        var inputPfxPassword = "123456";
        var outputPdf = "54566_out.pdf";
        using (var sign = new PdfFileSignature())
        {
            sign.BindPdf(inputPdf);
            var pkcs7 = new PKCS7(inputP12, inputPfxPassword);
            pkcs7.CustomSignHash = CustomSignHash;
            sign.Sign(1, "reason", "cont", "loc", false, new System.Drawing.Rectangle(0, 0, 500, 500), pkcs7);
            sign.Save(outputPdf);
        }
        using (var sign = new PdfFileSignature())
        {
            sign.BindPdf(outputPdf);
            Assert.IsTrue(sign.VerifySignature("Signature1"));
        }
    }

    private byte[] CustomSignHash(byte[] signableHash)
    {
        var inputP12 = "54566.p12";
        var inputPfxPassword = "123456";
        X509Certificate2 signerCert = new X509Certificate2(inputP12, inputPfxPassword, X509KeyStorageFlags.Exportable);
        RSACryptoServiceProvider rsaCSP = new RSACryptoServiceProvider();
        var xmlString = signerCert.PrivateKey.ToXmlString(true);
        rsaCSP.FromXmlString(xmlString);
        byte[] signedData = rsaCSP.SignData(signableHash, CryptoConfig.MapNameToOID("SHA1"));
        return signedData;
    }
```
ميزة جديدة أخرى هي تحديدات مربع حوار الطباعة لتحجيم الصفحة:

```cs
    Document document = new Document();
    document.Pages.Add();
    document.PrintScaling = PrintScaling.None;
    document.Save("output.pdf");
```

## ما الجديد في Aspose.PDF 23.9

منذ إصدار 23.9، أصبح هناك دعم لإزالة التعليق التوضيحي الفرعي من حقل قابل للتعبئة.

```cs

    doc = new Document("field-ref-add.pdf");
    field = (Field)doc.Form[fieldName];
    var annotation = field[1];
    doc.Pages[annotation .PageIndex].Annotations.Remove(annotation);
    doc.Save("field-ref-delete.pdf");
```

## ما الجديد في Aspose.PDF 23.8

منذ إصدار 23.8، أصبح هناك دعم لإضافة كشف التحديثات التزايدية.

تمت إضافة وظيفة لكشف التحديثات التزايدية في مستند PDF. تعيد هذه الوظيفة 'true' إذا تم حفظ المستند بتحديثات تزايدية؛ وإلا، تعيد 'false'.

```cs

    var path = "C:\test.pdf";
    var doc = new Document(path);
    Console.WriteLine(doc.HasIncrementalUpdate());
```

أيضا، يدعم الإصدار 23.8 الطرق للعمل مع حقول الخانات المنسدلة المتداخلة.
أيضًا، الإصدار 23.8 يدعم الطرق للتعامل مع حقول الخانات المتداخلة.

- إنشاء حقل خانات اختيار متعدد القيم:

```cs

    using (var document = new Document())
    {
    var page = document.Pages.Add();

    var checkbox = new CheckboxField(page, new Rectangle(50, 50, 70, 70));

    // تعيين قيمة الخيار الأول لمجموعة الخانات
    checkbox.ExportValue = "option 1";

    // إضافة خيار جديد تحت الخيارات الموجودة
    checkbox.AddOption("option 2");

    // إضافة خيار جديد في المستطيل المحدد
    checkbox.AddOption("option 3", new Rectangle(100, 100, 120, 120));

    document.Form.Add(checkbox);

    // تحديد الخانة المضافة
    checkbox.Value = "option 2";
    document.Save("checkbox_group.pdf");
    }
```

- الحصول على قيمة الخانة متعددة القيم وتعيينها:

```cs

    using (Document doc = new Document("example.pdf"))
    {
    Form form = doc.Form;
    CheckboxField checkbox = form.Fields[0] as CheckboxField;

    // يمكن استرجاع القيم المسموح بها من مجموعة AllowedStates
    // تعيين قيمة الخانة باستخدام الخاصية Value
    checkbox.Value = checkbox.AllowedStates[0];
    checkboxValue = checkbox.Value; // القيمة المعينة سابقًا، مثل "option 1"

    // يجب أن تكون القيمة أي عنصر من AllowedStates
    checkbox.Value = "option 2";
    checkboxValue = checkbox.Value; // option 2

    // إلغاء تحديد الخانات إما بتعيين القيمة إلى "Off" أو تعيين Checked إلى false
    checkbox.Value = "Off";
    // أو، بديلًا:
    // checkbox.Checked = false;
    checkboxValue = checkbox.Value; // Off
    }
```
## ما الجديد في Aspose.PDF 23.7

من Aspose.PDF 23.7 دعم لإضافة استخراج الشكل:

```cs

    public void PDFNET_46298()
    {
        var input1 = "46298_1.pdf";
        var input2 = "46298_2.pdf";

        var source = new Document(input1);
        var dest = new Document(input2);

        var graphicAbsorber = new GraphicsAbsorber();
        graphicAbsorber.Visit(source.Pages[1]);
        var area = new Rectangle(90, 250, 300, 400);
        dest.Pages[1].AddGraphics(graphicAbsorber.Elements, area);
    }
```

أيضا يدعم القدرة على اكتشاف الفيض عند إضافة نص:

```cs

    var doc = new Document();
    var paragraphContent = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras nisl tortor, efficitur sed cursus in, lobortis vitae nulla. Quisque rhoncus, felis sed dictum semper, est tellus finibus augue, ut feugiat enim risus eget tortor. Nulla finibus velit nec ante gravida sollicitudin. Morbi sollicitudin vehicula facilisis. Vestibulum ac convallis erat. Ut eget varius sem. Nam varius pharetra lorem, id ullamcorper justo auctor ac. Integer quis erat vitae lacus mollis volutpat eget et eros. Donec a efficitur dolor. Maecenas non dapibus nisi, ut pellentesque elit. Sed pellentesque rhoncus ante, a consectetur ligula viverra vel. Integer eget bibendum ante. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur elementum, sem a auctor vulputate, ante libero iaculis dolor, vitae facilisis dolor lorem at orci. Sed laoreet dui id nisi accumsan, id posuere diam accumsan.";
    var rectangle = new Rectangle(100, 600, 500, 700, false);
    var paragraph = new TextParagraph();
    var fragment = new TextFragment(paragraphContent);
    paragraph.VerticalAlignment = VerticalAlignment.Top;
    paragraph.FormattingOptions.WrapMode = TextFormattingOptions.WordWrapMode.ByWords;
    paragraph.Rectangle = rectangle;
    var isFitRectangle = fragment.TextState.IsFitRectangle(paragraphContent, rectangle);
    while (!isFitRectangle)
    {
        fragment.TextState.FontSize -= 0.5f;
        isFitRectangle = fragment.TextState.IsFitRectangle(paragraphContent, rectangle);
    }
    paragraph.AppendLine(fragment);
    TextBuilder builder = new TextBuilder(doc.Pages.Add());
    builder.AppendParagraph(paragraph);
    doc.Save(output);
```
## ما الجديد في Aspose.PDF 23.6

من Aspose.PDF 23.6 دعم لإضافة الإضافات التالية:

- محول Aspose PdfConverter من Html إلى PDF
- واجهة برمجة تطبيقات Aspose PdfOrganizer لتغيير حجم
- واجهة برمجة تطبيقات Aspose PdfOrganizer للضغط

تحديث Aspose.PdfForm
- إضافة ميزة 'تصدير "قيم" من الحقول في المستند إلى ملف CSV'
- إضافة القدرة على تعيين الخصائص لحقول منفصلة

كذلك دعم إضافة القدرة على تعيين عنوان صفحة HTML، Epub:

```cs

    var document = new Document(Params.InputPath + "53357.pdf");

    var htmlSaveOptions = new HtmlSaveOptions
    {
        ExplicitListOfSavedPages = new[] { 1 },
        SplitIntoPages = false,
        FixedLayout = true,
        CompressSvgGraphicsIfAny = false,
        SaveTransparentTexts = true,
        SaveShadowedTextsAsTransparentTexts = true,
        FontSavingMode = HtmlSaveOptions.FontSavingModes.AlwaysSaveAsWOFF,
        RasterImagesSavingMode = HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground,
        PartsEmbeddingMode = HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml,
        Title = "العنوان للصفحة"   // <-- هذا تم إضافته
    };

    document.Save(Params.OutputPath + "53357-out.html", htmlSaveOptions);
```
## ما الجديد في Aspose.PDF 23.5

منذ الإصدار 23.5، تم دعم إضافة خيار حجم خط RedactionAnnotation. استخدم قطعة الكود التالية لحل هذه المهمة:

```cs

    Document doc = new Document(dataDir + "test_factuur.pdf");

    // إنشاء مثيل RedactionAnnotation لمنطقة صفحة محددة
    RedactionAnnotation annot = new RedactionAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(367, 756.919982910156, 420, 823.919982910156));
    annot.FillColor = Aspose.Pdf.Color.Black;

    annot.BorderColor = Aspose.Pdf.Color.Yellow;
    annot.Color = Aspose.Pdf.Color.Blue;
    // النص الذي سيتم طباعته على تعليق التنقيح
    annot.OverlayText = "(مجهول)";
    annot.TextAlignment = Aspose.Pdf.HorizontalAlignment.Center;
    // تكرار النص الظاهر على تعليق التنقيح
    annot.Repeat = false;
    // خاصية جديدة هنا!
    annot.FontSize = 20;
    // إضافة التعليق إلى مجموعة التعليقات للصفحة الأولى
    doc.Pages[1].Annotations.Add(annot);
    // تسطيح التعليق وتنقيح محتويات الصفحة (أي إزالة النص والصورة
    // تحت التعليق المنقح)
    annot.Redact();
    dataDir = dataDir + "47704_RedactPage_out_NETCORE.pdf";
    doc.Save(dataDir);
```
## ما الجديد في Aspose.PDF 23.4

أعلنت Aspose.PDF عن إصدار SDK لـ .NET 7.

## ما الجديد في Aspose.PDF 23.3.1

من Aspose.PDF 23.3 دعم لإضافة الإضافات التالية:

- Aspose.PdfForm
- Aspose.PdfConverter PDF إلى HTML
- Aspose.PdfConverter PDF إلى XLSX
- Aspose.PdfOrganizer Rotate
- Aspose.PdfExtrator للصور

## ما الجديد في Aspose.PDF 23.3

قدمت النسخة 23.3 دعمًا لإضافة دقة لصورة. يمكن استخدام طريقتين لحل هذه المشكلة:

```cs
    var table = new Table
            {
                ColumnWidths = "600"
            };

            for(var j = 0; j < 2; j ++)
            {
                var row = table.Rows.Add();
                var cell = row.Cells.Add();
                cell.Paragraphs.Add(new Image()
                {
                    IsApplyResolution = true,
                    File = imageFile
                });
            }

            page.Paragraphs.Add(table);
```

والنهج الثاني:

```cs
    page.Paragraphs.Add(new Image()
            {
                IsApplyResolution = true,
                File = imageFile
            });
            page.Paragraphs.Add(new Image()
            {
                IsApplyResolution = true,
                File = imageFile
            });
```
يمكن وضع الصورة بدقة مُعدلة أو يمكنك تعيين خصائص FixedWidth أو FixedHeight بالتزامن مع خاصية IsApplyResolution

## ما الجديد في Aspose.PDF 23.1.1

من Aspose.PDF 23.1.1 دعم لإضافة الإضافات التالية:

- إضافة Aspose.PdfOrganizer
- إضافة Aspose.PdfExtractor

## ما الجديد في Aspose.PDF 23.1

منذ الإصدار 23.1 الدعم لإنشاء تعليق توضيحي PrinterMark.

علامات الطابعة هي رموز رسومية أو نصوص تضاف إلى صفحة لمساعدة العاملين في الإنتاج على تحديد مكونات وظيفة متعددة الألواح والحفاظ على إخراج ثابت أثناء الإنتاج. الأمثلة التي تُستخدم بشكل شائع في صناعة الطباعة تشمل:

- أهداف التسجيل لمحاذاة الألواح
- المنحدرات الرمادية وأشرطة الألوان لقياس الألوان وكثافات الحبر
- علامات القطع التي تظهر المكان الذي يجب قص الوسيط الناتج فيه

سنعرض مثالاً على الخيار بأشرطة الألوان لقياس الألوان وكثافات الحبر.
سنعرض مثالًا على الخيار مع شرائط الألوان لقياس الألوان وكثافات الحبر.

```cs
var outFile = myDir + "ColorBarTest.pdf");

using (var doc = new Document())
{
    Page page = doc.Pages.Add();
    page.TrimBox = new Aspose.Pdf.Rectangle(20, 20, 580, 820);
    AddAnnotations(page);
    doc.Save(outFile);
}

void AddAnnotations(Page page)
{
    var rectBlack = new Aspose.Pdf.Rectangle(100, 300, 300, 320);
    var rectCyan = new Aspose.Pdf.Rectangle(200, 600, 260, 690);
    var rectMagenta = new Aspose.Pdf.Rectangle(10, 650, 140, 670);

    var colorBarBlack = new ColorBarAnnotation(page, rectBlack);
    var colorBarCyan = new ColorBarAnnotation(page, rectCyan, ColorsOfCMYK.Cyan);
    var colorBaMagenta = new ColorBarAnnotation(page, rectMagenta);
    colorBaMagenta.ColorOfCMYK = ColorsOfCMYK.Magenta;
    var colorBarYellow = new ColorBarAnnotation(page, new Aspose.Pdf.Rectangle(400, 250, 450, 700), ColorsOfCMYK.Yellow);

    page.Annotations.Add(colorBarBlack);
    page.Annotations.Add(colorBarCyan);
    page.Annotations.Add(colorBaMagenta);
    page.Annotations.Add(colorBarYellow);
}
```
أيضاً دعم استخراج الصور المتجهية. حاول استخدام الكود التالي لاكتشاف واستخراج الرسومات المتجهية:

```cs
    var doc = new Document(input);
    try{
        doc.Pages[1].TrySaveVectorGraphics(outputSvg);
    }
    catch(Exception){

    }
```

## ما الجديد في Aspose.PDF 22.12

من هذا الإصدار دعم تحويل PDF إلى صورة DICOM

```cs
    Document doc = new Document("source.pdf");
    DicomDevice dicom = new DicomDevice();
    FileStream outStream = new FileStream("out.dicom", FileMode.Create, FileAccess.ReadWrite);
    dicom.Process(doc.Pages[1], outStream);
```    

## ما الجديد في Aspose.PDF 22.09

منذ 22.09 دعم إضافة خاصية لتعديل ترتيب عناصر تصنيف الموضوع (E=, CN=, O=, OU=, ) في التوقيع.

```cs
    using (var fileSign = new PdfFileSignature())
    {
        fileSign.BindPdf(inputPdf);
        var rect = new System.Drawing.Rectangle(100, 100, 400, 100);
        var signature = new PKCS7Detached(inputPfx, "123456789");
        signature.CustomAppearance = new SignatureCustomAppearance()
        {
            UseDigitalSubjectFormat = true,
            DigitalSubjectFormat = new SubjectNameElements[] { SubjectNameElements.CN, SubjectNameElements.O }
            //or
            //DigitalSubjectFormat = new SubjectNameElements[] { SubjectNameElements.OU, SubjectNameElements.S, SubjectNameElements.C }
        };
        fileSign.Sign(1, true, rect, signature);
        fileSign.Save(outputPdf);
    }
```
## ما الجديد في Aspose.PDF 22.6

منذ الإصدار 22.5، تم دعم استخراج نصوص الـ SubScript و SuperScript من ملفات PDF.

إذا كان المستند PDF يحتوي على نصوص SubScript و SuperScript مثل H2O، فإن استخراج النص من PDF يجب أن يشمل أيضاً معلومات التنسيق الخاصة بها (في النص المستخرج العادي).
إذا كان PDF يحتوي على نص بخط مائل، يجب أن يتم تضمين ذلك أيضاً في المحتوى المستخرج.

```cs
Document doc = new Document(input);
TextFragmentAbsorber absorber = new TextFragmentAbsorber("TM");
absorber.Visit(doc.Pages[1]);
```

## ما الجديد في Aspose.PDF 22.4

هذا الإصدار يتضمن معلومات لـ Aspose.PDF لـ .NET:

- PDF إلى ODS: التعرف على النص في subscript و superscript؛

**مثال**

```cs
Document pdfDocument = new Document("Superscript-Subscript.pdf");
ExcelSaveOptions options = new ExcelSaveOptions();
options.Format = ExcelSaveOptions.ExcelFormat.ODS;
pdfDocument.Save("output.ods"), options);
```

- PDF إلى XMLSpreadSheet2003: التعرف على النص في subscript و superscript؛

- PDF إلى Excel: التعرف على النص في subscript و superscript؛
- PDF إلى Excel: التعرف على النصوص المكتوبة بالأحرف السفلية والعلوية؛

- إزالة توقيعات UR أثناء حفظ المستند؛

- إزالة علامة الشكوك في MarkInfo أثناء حفظ المستند؛

- إزالة المعلومات أثناء حفظ المستند

## ما الجديد في Aspose.PDF 22.3

هذا الإصدار يتضمن التحديثات التالية:

- الدعم لـ AFRelationship؛

- التحقق من صحة رأس PDF؛

- إزالة الفلتر الفرعي adbe.x509.rsa_sha1 أثناء حفظ المستند؛

- تنسيق الحقل كرقم وتنسيق التاريخ؛

- منع استخدام تشفير RC4 في FDF 2.0.

## ما الجديد في Aspose.PDF 22.2

اعتبارًا من الإصدار 22.2، أصبح من الممكن توقيع المستند باستخدام PdfFileSignature مع LTV، ومع إمكانية تغيير التجزئة من SHA1 إلى SHA256.

```csharp
مثال على الاستخدام:
var inputPdf = "51168.pdf";
var inputPfx = "51168.pfx";
var inputPfxPassword = "111111";
var outputPdf = "51168.pdf";

using (var doc = new Document(inputPdf))
{
    using (PdfFileSignature signature = new PdfFileSignature(doc))
    {
        var pkcs = new PKCS7(inputPfx, inputPfxPassword)
        {
            UseLtv = true,
            TimestampSettings = new TimestampSettings("http://freetsa.org/tsr", string.Empty, DigestHashAlgorithm.Sha256)
        };
        signature.Sign(1, false, new System.Drawing.Rectangle(300, 100, 1, 1), pkcs);
        signature.Save(outputPdf);
    }
}
```
## ما الجديد في Aspose.PDF 22.1

الآن، يدعم Aspose.PDF لـ .NET تحميل المستندات من واحد من أشهر صيغ المستندات، صيغة مستند محمول (PDF) الإصدار 2.0.

## ما الجديد في Aspose.PDF 21.11

### السماح بالأحرف غير اللاتينية في كلمة المرور

```csharp
Aspose.Pdf.Facades.PdfFileSecurity fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity();
fileSecurity.AllowExceptions = true;
    try
{
 fileSecurity.BindPdf(exportDoc);
 bool res = fileSecurity.EncryptFile("æøå", "æøå", Aspose.Pdf.Facades.DocumentPrivilege.Print, Aspose.Pdf.Facades.KeySize.x256, Aspose.Pdf.Facades.Algorithm.AES);
 Console.WriteLine(res);
 fileSecurity.Save(output("encrypted.pdf"));
}
    catch(Exception e)
{
    Console.WriteLn("Exception: " + e.Message);
}
```

## ما الجديد في Aspose.PDF 21.10

### كيفية الكشف عن النص المخفي؟

الرجاء استخدام TextState.Invisible للحصول على معلومات حول عدم ظهور النص خارج إعداد وضع العرض.

لقد استخدمنا الكود التالي للاختبار:

```csharp
Document pdf = new Document(dataDir + "TestPage.pdf");
Console.WriteLine(pdf.FileName);
var page = pdf.Pages[1];
var textFragmentAbsorber = new TextFragmentAbsorber();
page.Accept(textFragmentAbsorber);
var textFragmentCollection = textFragmentAbsorber.TextFragments;
for (int i = 1; i <= textFragmentCollection.Count; i++)
{
    TextFragment fragment = textFragmentCollection[i];
    Console.WriteLine("Fragment {0} at {1}", i, fragment.Rectangle.ToString());
    Console.WriteLine("Text: {0}", fragment.Text);
    Console.WriteLine("RenderingMode: {0}", fragment.TextState.RenderingMode.ToString());
    Console.WriteLine("Invisibility: {0}", fragment.TextState.Invisible);
    Console.WriteLine("---");
}
```
### كيف يمكن الحصول على معلومات عن عدد الطبقات في مستند PDF؟

```csharp
Please use code snippet:
var inFile = "1234.pdf";
Document doc = new Document(inFile);
List layers = doc.Pages[1].Layers;
```

## ما الجديد في Aspose.PDF 21.9

تخصيص لون الخلفية لمظهر التوقيع ولون الخط للتسميات في منطقة التوقيع مع Aspose.PDF لـ .NET.

```csharp
using (PdfFileSignature pdfSign = new PdfFileSignature())
{
    pdfSign.BindPdf(inFile);
    var rect = new System.Drawing.Rectangle(310, 45, 200, 50);
    var pkcs = new PKCS7(inPfxFile, "");
    pkcs.CustomAppearance = new SignatureCustomAppearance()
    {//set colors
        ForegroundColor = Color.DarkGreen,
        BackgroundColor = Color.LightSeaGreen,
    };
    pdfSign.Sign(1, true, rect, pkcs);
    pdfSign.Save(outFile);
}
```

## ما الجديد في Aspose.PDF 21.8

### كيفية تغيير لون النص في التوقيع الرقمي؟

في الإصدار 21.8 خاصية ForegroundColor، تتيح تغيير لون النص في التوقيع الرقمي.

```csharp
```csharp
using (PdfFileSignature pdfSign = new PdfFileSignature())
{
    pdfSign.BindPdf(inFile);
    //إنشاء مستطيل لموقع التوقيع
    System.Drawing.Rectangle rect = new System.Drawing.Rectangle(310, 45, 200, 50);
    PKCS7 pkcs = new PKCS7(inPfxFile, "");
    pkcs.CustomAppearance = new SignatureCustomAppearance()
    {//تعيين لون النص
        ForegroundColor = Color.Green
    };
    // التوقيع على ملف PDF
    pdfSign.Sign(1, true, rect, pkcs);
    //حفظ ملف PDF الناتج
    pdfSign.Save(outFile);
}
```

## ما الجديد في Aspose.PDF 21.7

### إنشاء PDF استنادًا إلى XML و XLS مع المعلمات

لإضافة معلمات XSL نحتاج إلى إنشاء [XsltArgumentList](https://docs.microsoft.com/en-us/dotnet/api/system.xml.xsl.xsltargumentlist?view=net-5.0) خاصة بنا وتعيينها كخاصية في [XslFoLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xslfoloadoptions). يوضح الجزء التالي كيفية استخدام هذا الفصل مع الملفات الموضحة أعلاه.

```csharp
public static void Example_XSLFO_to_PDF()
    {
        var XmlContent = File.ReadAllText(_dataDir + "employees.xml");
        var XsltContent = File.ReadAllText(_dataDir + "employees.xslt");

        var options = new Aspose.Pdf.XslFoLoadOptions();

        //مثال على استخدام XsltArgumentList
         XsltArgumentList argsList = new XsltArgumentList();
        argsList.AddParam("isBoldName", "", "yes");
        //---------------------

        var pdfDocument = new Aspose.Pdf.Document(TransformXml(XmlContent, XsltContent, argsList), options);
        pdfDocument.Save(_dataDir + "data_xml.pdf");
    }

 public static MemoryStream TransformXml(string inputXml, string xsltString, XsltArgumentList argsList=null)
    {
            var transform = new XslCompiledTransform();
            using (var reader = XmlReader.Create(new StringReader(xsltString)))
            {
                transform.Load(reader);
            }
            var memoryStream = new MemoryStream();

            var results = new StreamWriter(memoryStream);
            using (var reader = XmlReader.Create(new StringReader(inputXml)))
            {
                transform.Transform(reader, argsList, results);
            }

            memoryStream.Position = 0;
            return memoryStream;
    }
```

## ما الجديد في Aspose.PDF 21.6

مع Aspose.PDF لـ .NET يمكنك إخفاء الصور باستخدام ImagePlacementAbsorber من المستند:

```csharp
public void PDFNET_49961()
{
   ImagePlacementAbsorber abs = new ImagePlacementAbsorber();
   Document doc = new Document("test.pdf");
   // إخفاء الصورة في الصفحة الأولى
   doc.Pages[1].Accept(abs);

   foreach (ImagePlacement imagePlacement in abs.ImagePlacements)
   {
       imagePlacement.Hide();
   }

   doc.Save("test_out.pdf");
}
```

## ما الجديد في Aspose.PDF 21.5

### كيفية استخراج الاسم الكامل للخط من وصفه/مورده في PDF؟

يمكنك الحصول على خط كامل مع البادئة بخاصية BaseFont لفئة الخط.

```csharp
Document pdf = new Document(dataDir + @"testfont.pdf");

Aspose.Pdf.Text.Font[] fonts = pdf.FontUtilities.GetAllFonts();
foreach (Aspose.Pdf.Text.Font font in fonts)
{
    Console.WriteLine($"font name : {font.FontName} BaseFont name : {font.BaseFont}");
}
pdf.Dispose();
```

## ما الجديد في Aspose.PDF 21.4

### إضافة API لدمج الصور

Aspose.PDF 21.4 يتيح لك دمج الصور.
Aspose.PDF 21.4 يتيح لك دمج الصور.

```csharp
private static void MergeAsJpeg()
{
   List<Stream> inputImagesStreams = new List<Stream>();
   using (FileStream inputFile300dpi = new FileStream(@"c:\300.jpg", FileMode.Open))
   {
       inputImagesStreams.Add(inputFile300dpi);
       using (FileStream inputFile600dpi = new FileStream(@"c:\49616_600.jpg", FileMode.Open))
       {
           inputImagesStreams.Add(inputFile600dpi);
           using (Stream inputStream =
                 PdfConverter.MergeImages(inputImagesStreams, ImageFormat.Jpeg, ImageMergeMode.Vertical, 1, 1))
           {
               using (FileStream outputStream = new FileStream(@"c:\out.jpg", FileMode.Create))
               {
                   byte[] buffer = new byte[32768];
                   int read;
                   while ((read = inputStream.Read(buffer, 0, buffer.Length)) > 0)
                   {
                       outputStream.Write(buffer, 0, read);
                   }
               }
           }
       }
    }
}
```
```csharp
private static void MergeAsTiff()
{
   List<Stream> inputImagesStreams = new List<Stream>();
   using (FileStream inputFile300dpi = new FileStream(@"c:\300.tiff", FileMode.Open))
   {
       inputImagesStreams.Add(inputFile300dpi);
       using (FileStream inputFile600dpi = new FileStream(@"c:\600.tiff", FileMode.Open))
       {
           inputImagesStreams.Add(inputFile600dpi);
           using (Stream inputStream = PdfConverter.MergeImagesAsTiff(inputImagesStreams))
           {
               using (FileStream outputStream = new FileStream(@"c:\out.tiff", FileMode.Create))
               {
                   byte[] buffer = new byte[32768];
                   int read;
                   while ((read = inputStream.Read(buffer, 0, buffer.Length)) > 0)
                   {
                       outputStream.Write(buffer, 0, read);
                   }
               }
           }
       }
    }
}
```

## ما الجديد في Aspose.PDF 21.3

### عرض عام لخاصية لكشف حماية المعلومات في Azure
### الكشف العام عن الخاصية لكشف حماية المعلومات Azure

مع الجزء التالي من الكود، يجب أن تتمكن من الحصول على البيانات المشفرة لملفات PDF الخاصة بك، المحمية بواسطة حماية المعلومات Azure:

```csharp
 public void Azure_Information_Protection()
 {
     string inputFile = @"c:\pdf.pdf";
     Document document = new Document(inputFile);
     if (document.EmbeddedFiles[1].AFRelationship == AFRelationship.EncryptedPayload)
     {
            if (document.EmbeddedFiles[1].EncryptedPayload != null)
            {
              // document.EmbeddedFiles[1].EncryptedPayload.Type == "EncryptedPayload"
              // document.EmbeddedFiles[1].EncryptedPayload.Subtype == "MicrosoftIRMServices"
              // document.EmbeddedFiles[1].EncryptedPayload.Version == "2"
            }
     }
}
```

## ما الجديد في Aspose.PDF 21.1

### إضافة دعم استرجاع لون الخلفية لـ TextFragment

في هذه النسخة من Aspose.PDF، أصبحت الوظيفة متاحة لاسترجاع لون الخلفية.
في هذه النسخة من Aspose.PDF، أصبحت الوظيفة متاحة لاسترجاع لون الخلفية.

يرجى مراعاة الكود التالي:

```csharp
Document pdfDocument = new Document(dataDir + "TextColor.pdf");
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber();

TextSearchOptions searchOptions = new TextSearchOptions(false);
searchOptions.SearchForTextRelatedGraphics = true;

textFragmentAbsorber.TextSearchOptions = searchOptions;

// قبول الامتصاص لجميع الصفحات
pdfDocument.Pages.Accept(textFragmentAbsorber);

// الحصول على قطع النص المستخرجة
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// تكرار عبر القطع
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine("النص: '{0}'", textFragment.Text);
    Console.WriteLine("لون الخلفية: '{0}'", textFragment.TextState.BackgroundColor);
    Console.WriteLine("لون الواجهة: '{0}'", textFragment.TextState.ForegroundColor);
    Console.WriteLine("لون خلفية القطعة: '{0}'", textFragment.Segments[1].TextState.BackgroundColor);
}
```
### بعد تحويله إلى HTML، تم تضمين الخط بالكامل في المخرجات

أيضًا، في Aspose.PDF 21.1، بعد تحويل PDF إلى HTML، أصبح من الممكن تضمين الخطوط في المستند HTML الناتج. يمكن ذلك من خلال خيار الحفظ الجديد البولياني HtmlSaveParameter.SaveFullFont.

إليك مقطع الكود:

```csharp
HtmlSaveOptions saveOptions = new HtmlSaveOptions();
saveOptions.RasterImagesSavingMode = HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground;
saveOptions.PartsEmbeddingMode = HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml;
saveOptions.LettersPositioningMethod = HtmlSaveOptions.LettersPositioningMethods.UseEmUnitsAndCompensationOfRoundingErrorsInCss;
saveOptions.FontSavingMode = HtmlSaveOptions.FontSavingModes.AlwaysSaveAsTTF;
saveOptions.SaveTransparentTexts = true;
saveOptions.SaveFullFont = true;
```
