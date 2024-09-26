---
title: מה חדש
linktitle: מה חדש
type: docs
weight: 10
url: /net/whatsnew/
description: בדף זה מוצגות התכונות החדשות הפופולריות ביותר ב-Aspose.PDF עבור .NET שהוצגו בשחרורים האחרונים.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2024-09-06"
---

## מה חדש ב-Aspose.PDF 24.8

המרת מסמכי PDF לפורמט PDF/A-4

החל מגרסה 24.8, ניתן להמיר מסמכי PDF ל-PDF/A-4. חלק 4 של התקן, המבוסס על PDF 2.0, פורסם בסוף 2020.

הקטע הבא מדגים איך להמיר מסמך לפורמט PDF/A-4, בהנחה שהמסמך הקלט הוא PDF 2.x.

```cs

    string documentPath = "";
    string conversionLogPath = "";
    string resultPdfPath ="";

    using (var document = new Document(documentPath))
    {
        // רק מסמכי PDF-2.x ניתנים להמרה ל-PDF/A-4
        document.Convert(conversionLogPath, PdfFormat.PDF_A_4, ConvertErrorAction.Delete);
        document.Save(resultPdfPath);
    }
```
הדוגמה השנייה מדגימה כיצד להמיר מסמך לפורמט PDF/A-4 כאשר המסמך הקלט הוא מגרסה קודמת.

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

מאז 24.8 הצגנו שיטה להחלקת תוכן שקוף במסמכי PDF:

```cs

    string documentPath = "";
    string resultPdfPath ="";

    using (var document = new Document(documentPath))
    {
        document.FlattenTransparency();
        document.Save(resultPdfPath);
    }
```

## מה חדש ב-Aspose.PDF 24.7

השוואת מסמכי PDF עם Aspose.PDF עבור .NET

מאז 24.7 ניתן להשוות תוכן מסמכי PDF עם סימוני אנוטציה ופלט צד לצד:

הדוגמה הראשונה מדגימה כיצד להשוות את הדפים הראשונים של שני מסמכי PDF.
הדגמה הראשונה מדגימה כיצד להשוות את הדפים הראשונים של שני מסמכי PDF.

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

הדגמה השנייה מרחיבה את ההיקף להשוואה של כל התוכן בשני מסמכי PDF.

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
## מה חדש ב-Aspose.PDF 24.4

גרסה זו תומכת בהחלת מסכת גזירה על תמונות:

```cs

    Document doc = new Document("input.pdf");
    using (var fs1 = new FileStream("mask1.jpg", FileMode.Open))
    using (var fs2 = new FileStream("mask2.png", FileMode.Open))
    {
        doc.Pages[1].Resources.Images[1].AddStencilMask(fs1);
        doc.Pages[1].Resources.Images[2].AddStencilMask(fs2);
    }
```

מאז 24.4 ניתן לבחור את מקור הנייר לפי גודל הדף ב-PDF בדיאלוג ההדפסה באמצעות ה-API

החל מ-Aspose.PDF 24.4 ניתן להפעיל ולכבות את ההעדפה הזו באמצעות התכונה Document.PickTrayByPdfSize או חזית PdfContentEditor:

```cs

    using (Document document = new Document())
    {
        Page page = document.Pages.Add();
        page.Paragraphs.Add(new TextFragment("Hello world!"));

        // הגדר את הדגל לבחירת מגש נייר באמצעות גודל דף ה-PDF
        document.PickTrayByPdfSize = true;
        document.Save("result.pdf");
    }
```
מה שחרור זה נוסף התוסף Aspose.PDF Signature עבור .NET:

- דוגמה עם יצירת שדה חדש ואפשרויות:

```cs

    // יצירת חתימה
    var plugin = new Signature();
    // יצירת אובייקט SignOptions כדי להגדיר הוראות
    var opt = new SignOptions(inputPfxPath, inputPfxPassword);
    // הוספת נתיב קובץ קלט
    opt.AddInput(new FileDataSource(inputPath));
    // הגדרת נתיב קובץ פלט
    opt.AddOutput(new FileDataSource(outputPath));
    // הגדרת אפשרויות נוספות
    opt.Reason = "הסיבה שלי";
    opt.Contact = "הקשר שלי";
    opt.Location = "המיקום שלי";
    // ביצוע התהליך
    plugin.Process(opt);
```

- דוגמה עם שדה חתום ריק קיים

```cs

    // יצירת חתימה
    var plugin = new Signature();
    // יצירת אובייקט SignOptions כדי להגדיר הוראות
    var opt = new SignOptions(inputPfxPath, inputPfxPassword);
    // הוספת נתיב קובץ קלט עם שדה חתימה ריק
    opt.AddInput(new FileDataSource(inputPath));
    // הגדרת נתיב קובץ פלט
    opt.AddOutput(new FileDataSource(outputPath));
    // הגדרת שם של שדה חתימה קיים
    opt.Name = "Signature1";
    // ביצוע התהליך
    plugin.Process(opt);
```
## מה חדש ב-Aspose.PDF 24.3

מהמהדורה הזו נוסף התוסף PDF/A Converter עבור .NET:

```cs

    var options = new PdfAConvertOptions
    {
        PdfAVersion = PdfAStandardVersion.PDF_A_3B
    };

    // הוסף את קובץ המקור
    options.AddInput(new FileDataSource("path_to_your_pdf_file.pdf")); // החלף בנתיב הקובץ הממשי שלך

    // הוסף את הנתיב לשמירת הקובץ המומר
    options.AddOutput(new FileDataSource("path_to_the_converted_file.pdf"));

    // צור מופע של התוסף
    var plugin = new PdfAConverter();

    // הרץ את ההמרה
    plugin.Process(options);
```

- יישום חיפוש דרך רשימת ביטויים ב-TextFragmentAbsorber:

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
    // קבל תוצאה
    var result = absorber.RegexResults
```
מאז 24.3 ניתן להוסיף שדה חתימה ריק בכל דף לקובץ PDF/A

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
            // הקוד המוצע החדש, באמצעות אובייקט SignatureField (קוד זה עובד כראוי)
            var doc = new Document(fs);
            var f = new SignatureField(doc.Pages[page], new Rectangle(10, 10, 100, 100));
            // הוספת המראה המוגדר כברירת מחדל לשדה החתימה
            f.DefaultAppearance = new DefaultAppearance("Helv", 12, System.Drawing.Color.Black);
            var newAddedField = doc.Form.Add(f, fieldName, page);

            // איך ניתן כעת להפוך את newAddedField לנראה בכל הדפים?
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

## מה חדש ב-Aspose.PDF 24.2

מאז גרסה 24.2 ניתן לקבל נתוני וקטור מקובץ PDF

הוטמע GraphicsAbsorber כדי לקבל נתוני וקטור ממסמכים:

```cs

var doc = new Document(input);
var grAbsorber = new GraphicsAbsorber();
grAbsorber.Visit(doc.Pages[1]);
var elements = grAbsorber.Elements;
var operators = elements[1].Operators;
var rectangle = elements[1].Rectangle;
var position = elements[1].Position;
```

## מה חדש ב-Aspose.PDF 24.1

מאז שחרור 24.1 ניתן לייבא הערות בפורמט FDF ל-PDF:

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

כמו כן, תומך בגישה למילון הדף או לקטלוג המסמכים.
גם תומך בגישה למילון הדפים או לקטלוג המסמכים.

הנה דוגמאות לקוד עבור DictionaryEditor:

- הוספת ערכים חדשים

```cs

    // דוגמה לשמות מפתח
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

- הוספה והגדרת ערכים במילון

```cs

    using (var doc = new Document())
    {
        var page = doc.Pages.Add();
        var dictionaryEditor = new DictionaryEditor(page);
        dictionaryEditor.Add(KEY_NAME, new CosPdfName("Old name"));
        // או 
        dictionaryEditor[KEY_NAME] = new CosPdfName("New name");
    }
```
- קבלת ערך ממילון

```cs

    using (var doc = new Document())
    {
        var page = doc.Pages.Add();
        var dictionaryEditor = new DictionaryEditor(page);
        dictionaryEditor[KEY_NAME] = new CosPdfName("name");
        var value = dictionaryEditor[KEY_NAME];
        // או 
        ICosPdfPrimitive primitive;
        dictionaryEditor.TryGetValue(KEY_NAME, out primitive);
    }
```

- הסרת ערך ממילון

```cs

    using (var doc = new Document())
    {
        var page = doc.Pages.Add();
        var dictionaryEditor = new DictionaryEditor(page);
        dictionaryEditor.Add(KEY_NAME, new CosPdfName(EXPECTED_NAME));
        dictionaryEditor.Remove(KEY_NAME);
    }
```

## מה חדש ב-Aspose.PDF 23.12

הטופס ניתן למציאה והטקסט ניתן להחלפה באמצעות הקטע הבא:

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

או, ניתן להסיר את הטופס לחלוטין:

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

וריאנט נוסף להסרת הטופס:

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

- ניתן למחוק את כל הטפסים באמצעות הקטע הבא:

```cs

    var document = new Document(input);
    var forms = document.Pages[1].Resources.Forms;

    forms.Clear();

    document.Save(output);
```
- מימוש המרת PDF ל-Markdown:

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

- מימוש המרת OFD ל-PDF:

```cs
    var document = new Document("sample.ofd", new OfdLoadOptions());
    document.Save("sample.pdf");
```

מהגרסה הזו נוסף התוסף Merger:

```cs
    // נתיב לקובץ PDF הממוזג.
    var outputPath = "TestMerge.pdf";

    // יצירת מופע חדש של Merger.
    var merger = new Merger();

    // יצירת MergeOptions.
    var opt = new MergeOptions();
    opt.AddInput(new FileDataSource(inputPath1));
    opt.AddInput(new FileDataSource(inputPath2));
    opt.AddOutput(new FileDataSource(outputPath));

    // תהליך מיזוג ה-PDF.
    merger.Process(opt);
```

כמו כן, מהגרסה הזו נוסף התוסף ChatGPT:
גם בגרסה זו נוסף התוסף של ChatGPT:

```cs
    using (var plugin = new PdfChatGpt())
    {
    var options = new PdfChatGptRequestOptions();
    options.AddOutput(new FileDataSource("PdfChatGPT_output.pdf")); // הוסף את נתיב קובץ הפלט.
    options.ApiKey = "Your API key."; // עליך לספק את המפתח לגישה ל-API.
    options.MaxTokens = 1000; // מספר האסימונים המרבי ליצירה בהשלמת הצ'אט.

    // הוסף את הודעות הבקשה.
    options.Messages.Add(new Message
    {
        Content = "אתה עוזר מועיל.",
        Role = Role.System
    });
    options.Messages.Add(new Message
    {
        Content = "מהו קוטר הפיצה הגדול ביותר שנעשה אי פעם?",
        Role = Role.User
    });

    // עבד את הבקשה.
    var result = await plugin.ProcessAsync(options);

    var fileResultPath = result.ResultCollection[0].Data;
    var chatCompletionObject = result.ResultCollection[1].Data as ChatCompletion; // אובייקט השלמת הצ'אט של ממשק ה-API של ChatGPT.
    }
```

## מה חדש ב-Aspose.PDF 23.11
## מה חדש ב-Aspose.PDF 23.11

מהגרסה הזו אפשר להסיר טקסט מוסתר מקובץ PDF:

```cs
    var document = new Document(inputFile);
    var textAbsorber = new TextFragmentAbsorber();

        // אפשרות זו יכולה לשמש כדי למנוע הזזת קטעי טקסט אחרים לאחר החלפת טקסט מוסתר.
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

מ-23.11 נתמך הפסקת תהליך באמצעות ניטור:

```cs

    public void InterruptExample()
    {
        string outputFile = testdata + "sample.pdf";
        //זהו טקסט ארוך, שימוש ב-Lorem Ipsum ב-8350 תווים כדי לגרום להשהיה
        string text = ExampleApp.LongText;
        using (InterruptMonitor monitor = new InterruptMonitor())
        {
            RowSpanWorker worker = new RowSpanWorker (outputFile, monitor);
            Thread thread = new Thread(new ThreadStart(worker.Work));
            thread.Start();

            // ההשהיה צריכה להיות קצרה יותר מהזמן הנדרש לשמירת המסמך המלאה (ללא הפסקה).
            Thread.Sleep(500);

            // הפסק את התהליך
            monitor.Interrupt();

            // המתן להפסקה...
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

                    // הוסף תא שכולל טקסט ארוך שנמשך לשני שורות
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
## מה חדש ב-Aspose.PDF 23.10

העדכון הנוכחי מציג שלוש גרסאות של הסרת תגים מ-PDF מתויג.

- הסרת כמה אלמנטים של עץ מאלמנט המסמך (אלמנט השורש):

```cs
    var document = new Document("some tagged pdf");
    var structure = document.LogicalStructure;
    var documentElement = structure.Children[0];
    var structElement = documentElement.Children.Count > 1 ? documentElement.Children[1] as StructElement : null;
    if (documentElement.Children.Remove(structElement))
    {
        // element removed
        document.Save(outputPath);
    }

    // You can also delete the structElement itself
    //if (structElement != null)
    //{
    //    structElement.Remove();
    //    document.Save(outputPath);
    //}
```

- הסרת כל תגי האלמנטים המסומנים מהמסמך, אך שמירה על אלמנטי המבנה:

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
- הסר תגיות לגמרי:

```cs
    var document = new Document("some tagged pdf");
    var structure = document.LogicalStructure;
    var documentElement = structure.Children[0];
    documentElement.Remove();
    document.Save(outputPath);
```

מאז 23.10 הוטמעה תכונה חדשה למדידת גובה תו. השתמש בקוד הבא כדי למדוד את גובה התו.

```cs
    var doc = new Document(input);
    var absorber = new TextFragmentAbsorber();
    absorber.Visit(doc.Pages[1]);
    var height = absorber.TextFragments[1].TextState.MeasureHeight('A')
```

שים לב שהמדידה מבוססת על הגופן המוטמע במסמך. אם חסרה מידע למימד, השיטה זו מחזירה 0.

כמו כן, בשחרור זה מוצעת האפשרות לחתום על PDF באמצעות HASH חתום:

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
עוד תכונה חדשה היא דף הגדרות תצורת הדפסה:

```cs
    Document document = new Document();
    document.Pages.Add();
    document.PrintScaling = PrintScaling.None;
    document.Save("output.pdf");
```

## מה חדש ב-Aspose.PDF 23.9

מאז 23.9 תומך בהסרת אנוטציה צאצא משדה מילוי.

```cs

    doc = new Document("field-ref-add.pdf");
    field = (Field)doc.Form[fieldName];
    var annotation = field[1];
    doc.Pages[annotation .PageIndex].Annotations.Remove(annotation);
    doc.Save("field-ref-delete.pdf");
```

## מה חדש ב-Aspose.PDF 23.8

מאז 23.8 תומך בהוספת זיהוי עדכונים מדרגתיים.

הפונקציה לזיהוי עדכונים מדרגתיים במסמך PDF נוספה. הפונקציה מחזירה 'true' אם מסמך נשמר עם עדכונים מדרגתיים; אחרת, היא מחזירה 'false'.

```cs

    var path = "C:\test.pdf";
    var doc = new Document(path);
    Console.WriteLine(doc.HasIncrementalUpdate());
```

כמו כן, 23.8 תומך בדרכים לעבוד עם שדות תיבת סימון מקוננים.
גם 23.8 תומך בדרכים לעבוד עם שדות תיבת סימון מקוננים.

- צור שדה תיבת סימון עם ערכים מרובים:

```cs
    using (var document = new Document())
    {
    var page = document.Pages.Add();

    var checkbox = new CheckboxField(page, new Rectangle(50, 50, 70, 70));

    // הגדר את ערך אפשרות הקבוצה הראשונה
    checkbox.ExportValue = "option 1";

    // הוסף אפשרות חדשה ממש מתחת לקיימות
    checkbox.AddOption("option 2");

    // הוסף אפשרות חדשה במלבן הנתון
    checkbox.AddOption("option 3", new Rectangle(100, 100, 120, 120));

    document.Form.Add(checkbox);

    // בחר בתיבת הסימון שנוספה
    checkbox.Value = "option 2";
    document.Save("checkbox_group.pdf");
    }
```

- קבל והגדר ערך של תיבת סימון עם ערכים מרובים:

```cs
    using (Document doc = new Document("example.pdf"))
    {
    Form form = doc.Form;
    CheckboxField checkbox = form.Fields[0] as CheckboxField;

    // ערכים מותרים ניתן לאחזר מאוסף ה-AllowedStates
    // הגדר את ערך תיבת הסימון באמצעות התכונה Value
    checkbox.Value = checkbox.AllowedStates[0];
    checkboxValue = checkbox.Value; // הערך שהוגדר קודם, למשל "option 1"

    // הערך צריך להיות כל אלמנט מתוך AllowedStates
    checkbox.Value = "option 2";
    checkboxValue = checkbox.Value; // option 2

    // בטל סימון תיבות על ידי הגדרת Value ל-"Off" או הגדרת Checked ל-false
    checkbox.Value = "Off";
    // או, בחלופין:
    // checkbox.Checked = false;
    checkboxValue = checkbox.Value; // Off
    }
```
## מה חדש ב-Aspose.PDF 23.7

מ-Aspose.PDF 23.7 תומך בהוספת חילוץ צורות:

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

גם תומך ביכולת לזהות גלישה כאשר מוסיפים טקסט:

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

## מה חדש ב-Aspose.PDF 23.6

מ-Aspose.PDF 23.6 תמיכה להוסיף את התוספים הבאים:

- Aspose PdfConverter Html ל-PDF
- Aspose PdfOrganizer Resize API
- Aspose PdfOrganizer Compress API

עדכון ה-Aspose.PdfForm
- הוספת תכונה 'יצוא "ערכים משדות במסמך לקובץ CSV"'
- הוספת היכולת להגדיר תכונות לשדות נפרדים

כמו כן תמיכה בהוספת היכולת להגדיר את כותרת הדף של HTML, Epub:

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
        Title = "Title for page"   // <-- this added
    };

    document.Save(Params.OutputPath + "53357-out.html", htmlSaveOptions);
```
## מה חדש ב-Aspose.PDF 23.5

מאז גרסה 23.5 נוספה תמיכה להוספת אפשרות גודל גופן ל-RedactionAnnotation. השתמש בקטע הקוד הבא כדי לפתור משימה זו:

```cs
    Document doc = new Document(dataDir + "test_factuur.pdf");

    // יצירת מופע של RedactionAnnotation לאזור מסוים בדף
    RedactionAnnotation annot = new RedactionAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(367, 756.919982910156, 420, 823.919982910156));
    annot.FillColor = Aspose.Pdf.Color.Black;

    annot.BorderColor = Aspose.Pdf.Color.Yellow;
    annot.Color = Aspose.Pdf.Color.Blue;
    // טקסט להדפסה על האנוטציה
    annot.OverlayText = "(לא ידוע)";
    annot.TextAlignment = Aspose.Pdf.HorizontalAlignment.Center;
    // חזרה על טקסט הכיסוי מעל האנוטציה
    annot.Repeat = false;
    // מאפיין חדש כאן!
    annot.FontSize = 20;
    // הוספת האנוטציה לאוסף האנוטציות של הדף הראשון
    doc.Pages[1].Annotations.Add(annot);
    // החלקת האנוטציה והסתרת תוכן הדף (כלומר הסרת טקסט ותמונה
    // מתחת לאנוטציה המוחקת)
    annot.Redact();
    dataDir = dataDir + "47704_RedactPage_out_NETCORE.pdf";
    doc.Save(dataDir);
```
## מה חדש ב-Aspose.PDF 23.4

Aspose.PDF הכריזה על שחרור SDK של .NET 7.

## מה חדש ב-Aspose.PDF 23.3.1

מ-Aspose.PDF 23.3 תומך בהוספת התוספים הבאים:

- Aspose.PdfForm
- Aspose.PdfConverter PDF ל-HTML
- Aspose.PdfConverter PDF ל-XLSX
- Aspose.PdfOrganizer Rotate
- Aspose.PdfExtrator לתמונות

## מה חדש ב-Aspose.PDF 23.3

גרסה 23.3 הציגה תמיכה בהוספת רזולוציה לתמונה. ניתן להשתמש בשתי שיטות לפתרון הבעיה:

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

והשיטה השנייה:

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
תמונה תוצב עם רזולוציה מותאמת או שתוכלו להגדיר את התכונות FixedWidth או FixedHeight בשילוב עם IsApplyResolution

## מה חדש ב-Aspose.PDF 23.1.1

מגרסת Aspose.PDF 23.1.1 ניתן להוסיף את התוספים הבאים:

- תוסף Aspose.PdfOrganizer
- תוסף Aspose.PdfExtractor

## מה חדש ב-Aspose.PDF 23.1

מגרסה 23.1 נתמך יצירת אנוטציה של סימני מדפסת.

סימני מדפסת הם סמלים גרפיים או טקסט הנוספים לדף כדי לסייע לצוות ההפקה לזהות את רכיבי העבודה המרובי צלחות ולשמור על פלט עקבי במהלך הייצור. דוגמאות שנפוצות בתעשיית ההדפסה כוללות:

- מטרות רישום ליישור צלחות
- מדרגות אפורות וסרגלי צבע למדידת צבעים וצפיפויות דיו
- סימני חיתוך המציינים היכן שהתקשורת המוצאת צריכה להיות מוגזמת

נראה דוגמה לאפשרות עם סרגלי צבע למדידת צבעים וצפיפויות דיו.
נראה דוגמה לאפשרות עם פסי צבע למדידת צבעים וריכוזי דיו.

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
גם תומך בחילוץ תמונות וקטוריות. נסה להשתמש בקוד הבא לזיהוי וחילוץ גרפיקה וקטורית:

```cs
    var doc = new Document(input);
    try{
        doc.Pages[1].TrySaveVectorGraphics(outputSvg);
    }
    catch(Exception){

    }
```

## מה חדש ב-Aspose.PDF 22.12

מהגרסה הזו תומך בהמרת PDF לתמונת DICOM

```cs
    Document doc = new Document("source.pdf");
    DicomDevice dicom = new DicomDevice();
    FileStream outStream = new FileStream("out.dicom", FileMode.Create, FileAccess.ReadWrite);
    dicom.Process(doc.Pages[1], outStream);
```

## מה חדש ב-Aspose.PDF 22.09

מאז 22.09 תומך בהוספת תכונה לשינוי סדר רובריקות הנושא (E=, CN=, O=, OU=, ) בחתימה.

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
## מה חדש ב-Aspose.PDF 22.6

מאז 22.5 תמיכה לחילוץ טקסט תת-כתב ועילוי ממסמכי PDF.

אם המסמך PDF מכיל טקסט תת-כתב ועילוי כמו H2O, אזי לחילוץ הטקסט מה-PDF יש לחלץ גם את מידע העיצוב שלהם (בטקסט הנקי שנחלץ).
אם ה-PDF מכיל טקסט בכתב נטוי, עליו גם להיכלל בתוכן שנחלץ.

```cs
Document doc = new Document(input);
TextFragmentAbsorber absorber = new TextFragmentAbsorber("TM");
absorber.Visit(doc.Pages[1]);
```

## מה חדש ב-Aspose.PDF 22.4

גרסה זו כוללת מידע עבור Aspose.PDF עבור .NET:

- PDF ל-ODS: זיהוי טקסט בתת-כתב ועילוי;

**דוגמה**

```cs
Document pdfDocument = new Document("Superscript-Subscript.pdf");
ExcelSaveOptions options = new ExcelSaveOptions();
options.Format = ExcelSaveOptions.ExcelFormat.ODS;
pdfDocument.Save("output.ods"), options);
```

- PDF ל-XMLSpreadSheet2003: זיהוי טקסט בתת-כתב ועילוי;

- PDF ל-Excel: זיהוי טקסט בתת-כתב ועילוי;
- PDF ל-Excel: זיהוי טקסט בכתב תחתון וכתב עילי;

- הסרת חתימות UR בעת שמירת מסמך;

- הסרת דגל Suspects ב-MarkInfo בעת שמירת מסמך;

- הסרת מידע בעת שמירת מסמך

## מה חדש ב-Aspose.PDF 22.3

הגרסה כוללת את העדכונים הבאים:

- תמיכה ב-AFRelationship;

- אימות כותרת PDF;

- הסרת תת-מסנן adbe.x509.rsa_sha1 בעת שמירת מסמך;

- עיצוב שדה כמספר ותבנית תאריך;

- איסור על שימוש בהצפנת RC4 ב-FDF 2.0.

## מה חדש ב-Aspose.PDF 22.2

מגרסה 22.2 ניתן לחתום על מסמך באמצעות PdfFileSignature עם LTV, ועם היכולת לשנות את אלגוריתם הגיבוב מ-SHA1 ל-SHA256.

```csharp
דוגמה לשימוש:
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
## מה חדש ב-Aspose.PDF 22.1

כעת, Aspose.PDF עבור .NET תומך בטעינת מסמכים מאחד מפורמטי המסמכים הפופולריים ביותר, פורמט מסמך נייד (PDF) גרסה 2.0.

## מה חדש ב-Aspose.PDF 21.11

### אפשר תווים שאינם לטיניים בסיסמה

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

## מה חדש ב-Aspose.PDF 21.10

### איך לזהות טקסט נסתר?

אנא השתמש ב-TextState.Invisible כדי לקבל מידע על חוסר נראות של טקסט מחוץ להגדרת מצב ההדפסה.

השתמשנו בקוד הבא לבדיקה:

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
### כיצד לקבל מידע על מספר השכבות במסמך PDF?

```csharp
Please use code snippet:
var inFile = "1234.pdf";
Document doc = new Document(inFile);
List layers = doc.Pages[1].Layers;
```

## מה חדש ב-Aspose.PDF 21.9

התאמת צבע הרקע להופעת החתימה וצבע הגופן של התוויות באזור החתימה עם Aspose.PDF עבור .NET.

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

## מה חדש ב-Aspose.PDF 21.8

### כיצד לשנות את צבע הטקסט בחתימה דיגיטלית?

בגרסה 21.8 תכונת ForegroundColor מאפשרת לשנות את צבע הטקסט בחתימה דיגיטלית.

```csharp

```csharp
using (PdfFileSignature pdfSign = new PdfFileSignature())
{
    pdfSign.BindPdf(inFile);
    //יצירת מלבן למיקום החתימה
    System.Drawing.Rectangle rect = new System.Drawing.Rectangle(310, 45, 200, 50);
    PKCS7 pkcs = new PKCS7(inPfxFile, "");
    pkcs.CustomAppearance = new SignatureCustomAppearance()
    {//הגדרת צבע הטקסט
        ForegroundColor = Color.Green
    };
    // חתימה על קובץ ה-PDF
    pdfSign.Sign(1, true, rect, pkcs);
    //שמירת קובץ PDF הפלט
    pdfSign.Save(outFile);
}
```

## מה חדש ב-Aspose.PDF 21.7

### יצירת PDF מבוססת על XML ו-XLS עם פרמטרים

להוספת פרמטרים ל-XSL עלינו ליצור [XsltArgumentList](https://docs.microsoft.com/en-us/dotnet/api/system.xml.xsl.xsltargumentlist?view=net-5.0) משלנו ולהגדיר אותו כתכונה ב-[XslFoLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xslfoloadoptions). הקטע הבא מראה כיצד להשתמש במחלקה זו עם קבצים המתוארים לעיל.

```csharp
public static void Example_XSLFO_to_PDF()
    {
        var XmlContent = File.ReadAllText(_dataDir + "employees.xml");
        var XsltContent = File.ReadAllText(_dataDir + "employees.xslt");

        var options = new Aspose.Pdf.XslFoLoadOptions();

        //דוגמה לשימוש ב-XsltArgumentList
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
## מה חדש ב-Aspose.PDF 21.6

עם Aspose.PDF ל-.NET ניתן להסתיר תמונות באמצעות ImagePlacementAbsorber מהמסמך:

```csharp
public void PDFNET_49961()
{
   ImagePlacementAbsorber abs = new ImagePlacementAbsorber();
   Document doc = new Document("test.pdf");
   // הסתרת תמונה בעמוד הראשון
   doc.Pages[1].Accept(abs);

   foreach (ImagePlacement imagePlacement in abs.ImagePlacements)
   {
       imagePlacement.Hide();
   }

   doc.Save("test_out.pdf");
}
```

## מה חדש ב-Aspose.PDF 21.5

### איך לחלץ שם מלא של גופן מתיאורו/משאביו ב-PDF?

ניתן לקבל גופן מלא עם הקידומת עם התכונה BaseFont עבור מחלקת הגופן.

```csharp
Document pdf = new Document(dataDir + @"testfont.pdf");

Aspose.Pdf.Text.Font[] fonts = pdf.FontUtilities.GetAllFonts();
foreach (Aspose.Pdf.Text.Font font in fonts)
{
    Console.WriteLine($"font name : {font.FontName} BaseFont name : {font.BaseFont}");
}
pdf.Dispose();
```

## מה חדש ב-Aspose.PDF 21.4

### הוסף API למיזוג תמונות

Aspose.PDF 21.4 מאפשר לך לשלב תמונות.
Aspose.PDF 21.4 מאפשר לך לשלב תמונות.

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
גם תוכל לשלב את התמונות שלך בפורמט Tiff:

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

## מה חדש ב-Aspose.PDF 21.3

### חשיפה ציבורית של מאפיין לזיהוי הגנת מידע של Azure
### חשיפה ציבורית של נכס לזיהוי הגנת מידע של אז'ור

עם קטע הקוד הבא, תוכל לקבל גישה לתוכן המוצפן של קבצי PDF שלך, המוגנים באמצעות הגנת מידע של אז'ור:

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

## מה חדש ב-Aspose.PDF 21.1

### הוספת תמיכה באחזור צבע הרקע של קטע טקסט

בגרסה זו של Aspose.PDF, התפקיד הפך זמין לאחזר את צבע הרקע.
בגרסה זו של Aspose.PDF, התפקיד הפך לזמין לאחזר את צבע הרקע.

אנא שקול את הקוד הבא:

```csharp
Document pdfDocument = new Document(dataDir + "TextColor.pdf");
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber();

TextSearchOptions searchOptions = new TextSearchOptions(false);
searchOptions.SearchForTextRelatedGraphics = true;

textFragmentAbsorber.TextSearchOptions = searchOptions;

// קבל את ה-absorber לכל העמודים
pdfDocument.Pages.Accept(textFragmentAbsorber);

// קבל את קטעי הטקסט שנאספו
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// עבור על הקטעים
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine("Text: '{0}'", textFragment.Text);
    Console.WriteLine("BackgroundColor: '{0}'", textFragment.TextState.BackgroundColor);
    Console.WriteLine("ForegroundColor: '{0}'", textFragment.TextState.ForegroundColor);
    Console.WriteLine("Segment BackgroundColor: '{0}'", textFragment.Segments[1].TextState.BackgroundColor);
}
```
### לאחר המרה ל-HTML הגופן מוטמע במלואו בפלט

גם ב-Aspose.PDF 21.1, לאחר המרת PDF ל-HTML, נעשה זמין טמיעת גופנים במסמך HTML הפלט. זה אפשרי עם אפשרות השמירה הבוליאנית החדשה HtmlSaveParameter.SaveFullFont.

הנה קטע הקוד:

```csharp
HtmlSaveOptions saveOptions = new HtmlSaveOptions();
saveOptions.RasterImagesSavingMode = HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground;
saveOptions.PartsEmbeddingMode = HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml;
saveOptions.LettersPositioningMethod = HtmlSaveOptions.LettersPositioningMethods.UseEmUnitsAndCompensationOfRoundingErrorsInCss;
saveOptions.FontSavingMode = HtmlSaveOptions.FontSavingModes.AlwaysSaveAsTTF;
saveOptions.SaveTransparentTexts = true;
saveOptions.SaveFullFont = true;
```
