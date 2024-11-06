---
title: Что нового
linktitle: Что нового
type: docs
weight: 10
url: ru/net/whatsnew/
description: На этой странице представлены самые популярные новые функции в Aspose.PDF для .NET, которые были внедрены в последних выпусках.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2024-09-06"
---

## Что нового в Aspose.PDF 24.8

Конвертация документов PDF в формат PDF/A-4

Начиная с версии 24.8, стало возможным конвертировать документы PDF в PDF/A-4. Часть 4 стандарта, основанная на PDF 2.0, была опубликована в конце 2020 года.

Следующий фрагмент кода демонстрирует, как конвертировать документ в формат PDF/A-4, предполагая, что входной документ является PDF 2.x.

```cs

    string documentPath = "";
    string conversionLogPath = "";
    string resultPdfPath ="";

    using (var document = new Document(documentPath))
    {
        // Только документы PDF-2.x могут быть конвертированы в PDF/A-4
        document.Convert(conversionLogPath, PdfFormat.PDF_A_4, ConvertErrorAction.Delete);
        document.Save(resultPdfPath);
    }
```
Второй фрагмент кода демонстрирует, как конвертировать документ в формат PDF/A-4, когда входной документ является более ранней версией.

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

С 24.8 мы ввели метод для уплощения прозрачного содержимого в PDF документах:

```cs

    string documentPath = "";
    string resultPdfPath ="";

    using (var document = new Document(documentPath))
    {
        document.FlattenTransparency();
        document.Save(resultPdfPath);
    }
```


## Что нового в Aspose.PDF 24.7

Сравнение PDF документов с Aspose.PDF для .NET

С 24.7 стало возможно сравнивать содержимое PDF документов с пометками аннотаций и выводом бок о бок:

Первый фрагмент кода демонстрирует, как сравнить первые страницы двух PDF документов.
Первый фрагмент кода демонстрирует, как сравнить первые страницы двух PDF документов.

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

Второй фрагмент кода расширяет возможности сравнения на весь контент двух PDF документов.

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
Файлы прикреплены к задаче. Результат был получен в режиме:

AdditionalChangeMarks = true
ComparisonMode = ComparisonMode.ParseSpaces

## Что нового в Aspose.PDF 24.4

Этот релиз поддерживает применение маски обрезки к изображениям:

```cs
    Document doc = new Document("input.pdf");
    using (var fs1 = new FileStream("mask1.jpg", FileMode.Open))
    using (var fs2 = new FileStream("mask2.png", FileMode.Open))
    {
        doc.Pages[1].Resources.Images[1].AddStencilMask(fs1);
        doc.Pages[1].Resources.Images[2].AddStencilMask(fs2);
    }
```

Начиная с версии 24.4, вы можете выбрать источник бумаги по размеру страницы PDF в диалоговом окне печати с помощью API

Начиная с Aspose.PDF 24.4, эту настройку можно включать и выключать, используя свойство Document.PickTrayByPdfSize или фасад PdfContentEditor:

```cs
    using (Document document = new Document())
    {
        Page page = document.Pages.Add();
        page.Paragraphs.Add(new TextFragment("Привет, мир!"));

        // Установить флаг для выбора лотка для бумаги с использованием размера страницы PDF
        document.PickTrayByPdfSize = true;
        document.Save("result.pdf");
    }
```
```cs

    using (PdfContentEditor contentEditor = new PdfContentEditor())
    {
        contentEditor.BindPdf("input.pdf");

        // Установка флага для выбора лотка бумаги в зависимости от размера страницы PDF
        contentEditor.ChangeViewerPreference(ViewerPreference.PickTrayByPDFSize);
        contentEditor.Save("result.pdf");
    }
```

В этом релизе добавлен плагин Aspose.PDF Signature для .NET:

- Пример с созданием нового поля и опций:

```cs

    // создать подпись
    var plugin = new Signature();
    // создать объект SignOptions для установки инструкций
    var opt = new SignOptions(inputPfxPath, inputPfxPassword);
    // добавить путь к входному файлу
    opt.AddInput(new FileDataSource(inputPath));
    // установить путь к выходному файлу
    opt.AddOutput(new FileDataSource(outputPath));
    // установить дополнительные опции
    opt.Reason = "моя причина";
    opt.Contact = "мой контакт";
    opt.Location = "мое местоположение";
    // выполнить процесс
    plugin.Process(opt);
```

- Пример с существующим пустым полем

```cs

    // создать подпись
    var plugin = new Signature();
    // создать объект SignOptions для установки инструкций
    var opt = new SignOptions(inputPfxPath, inputPfxPassword);
    // добавить путь к входному файлу с пустым полем подписи
    opt.AddInput(new FileDataSource(inputPath));
    // установить путь к выходному файлу
    opt.AddOutput(new FileDataSource(outputPath));
    // установить имя существующего поля подписи
    opt.Name = "Signature1";
    // выполнить процесс
    plugin.Process(opt);
```
## Что нового в Aspose.PDF 24.3

В этом релизе добавлен плагин PDF/A Converter для .NET:

```cs

    var options = new PdfAConvertOptions
    {
        PdfAVersion = PdfAStandardVersion.PDF_A_3B
    };

    // Добавить исходный файл
    options.AddInput(new FileDataSource("path_to_your_pdf_file.pdf")); // замените на ваш фактический путь к файлу

    // Добавить путь для сохранения преобразованного файла
    options.AddOutput(new FileDataSource("path_to_the_converted_file.pdf"));

    // Создать экземпляр плагина
    var plugin = new PdfAConverter();

    // Запустить преобразование
    plugin.Process(options);
```

- Реализовать поиск по списку фраз в TextFragmentAbsorber:

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
    // Получить результат
    var result = absorber.RegexResults
```
С 24.3 возможно добавить пустое поле для подписи на каждую страницу в файл PDF/A

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
            // Новый предложенный код, используя объект SignatureField (этот код работает хорошо)
            var doc = new Document(fs);
            var f = new SignatureField(doc.Pages[page], new Rectangle(10, 10, 100, 100));
            // Добавить стандартное представление для поля подписи
            f.DefaultAppearance = new DefaultAppearance("Helv", 12, System.Drawing.Color.Black);
            var newAddedField = doc.Form.Add(f, fieldName, page);

            // Как теперь сделать newAddedField видимым на всех страницах?
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
## Что нового в Aspose.PDF 24.2

С версии 24.2 стало возможно получать векторные данные из файла PDF

Был реализован GraphicsAbsorber для извлечения векторных данных из документов:

```cs
var doc = new Document(input);
var grAbsorber = new GraphicsAbsorber();
grAbsorber.Visit(doc.Pages[1]);
var elements = grAbsorber.Elements;
var operators = elements[1].Operators;
var rectangle = elements[1].Rectangle;
var position = elements[1].Position;
```

## Что нового в Aspose.PDF 24.1

С релиза 24.1 стало возможно импортировать аннотации в формате FDF в PDF:

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

Также поддерживается доступ к словарю страниц или каталогу документов.
Также поддерживает доступ к Словарю Страницы или Каталогу Документов.

Вот примеры кода для DictionaryEditor:

- Добавление новых значений

```cs
    // пример названий ключей
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

- Добавление и установка значений в словарь

```cs
    using (var doc = new Document())
    {
        var page = doc.Pages.Add();
        var dictionaryEditor = new DictionaryEditor(page);
        dictionaryEditor.Add(KEY_NAME, new CosPdfName("Old name"));
        // или 
        dictionaryEditor[KEY_NAME] = new CosPdfName("New name");
    }
```
- Получить значение из словаря

```cs
    using (var doc = new Document())
    {
        var page = doc.Pages.Add();
        var dictionaryEditor = new DictionaryEditor(page);
        dictionaryEditor[KEY_NAME] = new CosPdfName("name");
        var value = dictionaryEditor[KEY_NAME];
        // или 
        ICosPdfPrimitive primitive;
        dictionaryEditor.TryGetValue(KEY_NAME, out primitive);
    }
```

- Удалить значение из словаря

```cs
    using (var doc = new Document())
    {
        var page = doc.Pages.Add();
        var dictionaryEditor = new DictionaryEditor(page);
        dictionaryEditor.Add(KEY_NAME, new CosPdfName(EXPECTED_NAME));
        dictionaryEditor.Remove(KEY_NAME);
    }
```

## Что нового в Aspose.PDF 23.12

Форма может быть найдена, и текст может быть заменен с помощью следующего фрагмента кода:

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

Или форма может быть полностью удалена:

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

Другой вариант удаления формы:

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

- Все формы могут быть удалены с помощью следующего фрагмента кода:

```cs
    var document = new Document(input);
    var forms = document.Pages[1].Resources.Forms;

    forms.Clear();

    document.Save(output);
```
- Реализуйте конвертацию PDF в Markdown:

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

- Реализуйте конвертацию OFD в PDF:

```cs
    var document = new Document("sample.ofd", new OfdLoadOptions());
    document.Save("sample.pdf");
```

В этом релизе добавлен плагин Merger:

```cs
    // Путь к выходному файлу объединенного PDF.
    var outputPath = "TestMerge.pdf";

    // Создайте новый экземпляр Merger.
    var merger = new Merger();

    // Создайте MergeOptions.
    var opt = new MergeOptions();
    opt.AddInput(new FileDataSource(inputPath1));
    opt.AddInput(new FileDataSource(inputPath2));
    opt.AddOutput(new FileDataSource(outputPath));

    // Обработайте объединение PDF.
    merger.Process(opt);
```

Также в этом релизе добавлен плагин ChatGPT:
Также, начиная с этого релиза, добавлен плагин ChatGPT:

```cs
    using (var plugin = new PdfChatGpt())
    {
    var options = new PdfChatGptRequestOptions();
    options.AddOutput(new FileDataSource("PdfChatGPT_output.pdf")); // Добавьте путь к выходному файлу.
    options.ApiKey = "Ваш API ключ."; // Вам необходимо предоставить ключ для доступа к API.
    options.MaxTokens = 1000; // Максимальное количество токенов для генерации в завершении чата.

    // Добавьте сообщения запроса.
    options.Messages.Add(new Message
    {
        Content = "Вы полезный помощник.",
        Role = Role.System
    });
    options.Messages.Add(new Message
    {
        Content = "Какой максимальный диаметр пиццы когда-либо делали?",
        Role = Role.User
    });

    // Обработайте запрос.
    var result = await plugin.ProcessAsync(options);

    var fileResultPath = result.ResultCollection[0].Data;
    var chatCompletionObject = result.ResultCollection[1].Data as ChatCompletion; // Объект завершения чата API ChatGPT.
    }
```

## Что нового в Aspose.PDF 23.11
## Что нового в Aspose.PDF 23.11

С этой версии можно удалять скрытый текст из файла PDF:

```cs
    var document = new Document(inputFile);
    var textAbsorber = new TextFragmentAbsorber();

        // Эта опция может быть использована для предотвращения перемещения других текстовых фрагментов после замены скрытого текста.
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

С 23.11 поддерживается прерывание потока:

```cs

    public void InterruptExample()
    {
        string outputFile = testdata + "sample.pdf";
        // это большой текст, используется Lorem Ipsum на 8350 символов для вызова приостановки
        string text = ExampleApp.LongText;
        using (InterruptMonitor monitor = new InterruptMonitor())
        {
            RowSpanWorker worker = new RowSpanWorker (outputFile, monitor);
            Thread thread = new Thread(new ThreadStart(worker.Work));
            thread.Start();

            // Тайм-аут должен быть меньше времени, необходимого для полного сохранения документа (без прерывания).
            Thread.Sleep(500);

            // Прервать процесс
            monitor.Interrupt();

            // Ожидание прерывания...
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

                    // добавить ячейку, которая занимает два ряда и содержит очень длинный текст
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
## Что нового в Aspose.PDF 23.10

Текущее обновление представляет три варианта удаления тегов из тегированных PDF.

- Удалить некоторые элементы узла из documentElement (корневой элемент дерева):

```cs
    var document = new Document("some tagged pdf");
    var structure = document.LogicalStructure;
    var documentElement = structure.Children[0];
    var structElement = documentElement.Children.Count > 1 ? documentElement.Children[1] as StructElement : null;
    if (documentElement.Children.Remove(structElement))
    {
        // элемент удален
        document.Save(outputPath);
    }

    // Вы также можете удалить сам structElement
    //if (structElement != null)
    //{
    //    structElement.Remove();
    //    document.Save(outputPath);
    //}
```

- Удалить все помеченные тегами элементы из документа, но сохранить структурные элементы:

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
- Удалите все теги:

```cs
    var document = new Document("some tagged pdf");
    var structure = document.LogicalStructure;
    var documentElement = structure.Children[0];
    documentElement.Remove();
    document.Save(outputPath);
```

С 23.10 была реализована новая функция для измерения высоты символов. Используйте следующий код для измерения высоты символа.

```cs
    var doc = new Document(input);
    var absorber = new TextFragmentAbsorber();
    absorber.Visit(doc.Pages[1]);
    var height = absorber.TextFragments[1].TextState.MeasureHeight('A')
```

Обратите внимание, что измерение основано на шрифте, встроенном в документ. Если какая-либо информация о размере отсутствует, этот метод возвращает 0.

Также в этом релизе представлена функция Подписать PDF с использованием подписанного HASH:

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
Ещё одна новая функция - Масштабирование страницы в диалоговом окне предустановок печати:

```cs
    Document document = new Document();
    document.Pages.Add();
    document.PrintScaling = PrintScaling.None;
    document.Save("output.pdf");
```

## Что нового в Aspose.PDF 23.9

С версии 23.9 появилась поддержка удаления дочерней аннотации из заполняемого поля.

```cs

    doc = new Document("field-ref-add.pdf");
    field = (Field)doc.Form[fieldName];
    var annotation = field[1];
    doc.Pages[annotation .PageIndex].Annotations.Remove(annotation);
    doc.Save("field-ref-delete.pdf");
```

## Что нового в Aspose.PDF 23.8

С версии 23.8 появилась поддержка обнаружения инкрементных обновлений.

Функция для обнаружения инкрементных обновлений в PDF-документе была добавлена. Эта функция возвращает 'true', если документ был сохранён с инкрементными обновлениями; в противном случае, она возвращает 'false'.

```cs

    var path = "C:\test.pdf";
    var doc = new Document(path);
    Console.WriteLine(doc.HasIncrementalUpdate());
```

Также, 23.8 поддерживает способы работы с вложенными полями флажков.
Также, версия 23.8 поддерживает способы работы с вложенными полями флажков.

- Создание поля флажка с множественным выбором:

```cs
    using (var document = new Document())
    {
    var page = document.Pages.Add();

    var checkbox = new CheckboxField(page, new Rectangle(50, 50, 70, 70));

    // Установите значение первой группы флажков
    checkbox.ExportValue = "option 1";

    // Добавьте новый вариант прямо под существующими
    checkbox.AddOption("option 2");

    // Добавьте новый вариант в заданном прямоугольнике
    checkbox.AddOption("option 3", new Rectangle(100, 100, 120, 120));

    document.Form.Add(checkbox);

    // Выберите добавленный флажок
    checkbox.Value = "option 2";
    document.Save("checkbox_group.pdf");
    }
```

- Получение и установка значения многоступенчатого флажка:

```cs
    using (Document doc = new Document("example.pdf"))
    {
    Form form = doc.Form;
    CheckboxField checkbox = form.Fields[0] as CheckboxField;

    // Допустимые значения можно получить из коллекции AllowedStates
    // Установите значение флажка, используя свойство Value
    checkbox.Value = checkbox.AllowedStates[0];
    checkboxValue = checkbox.Value; // ранее установленное значение, например "option 1"

    // Значение должно быть любым элементом из AllowedStates
    checkbox.Value = "option 2";
    checkboxValue = checkbox.Value; // option 2

    // Снимите отметку, установив значение «Off» или установив Checked в false
    checkbox.Value = "Off";
    // или, по выбору:
    // checkbox.Checked = false;
    checkboxValue = checkbox.Value; // Off
    }
```
## Что нового в Aspose.PDF 23.7

С версии Aspose.PDF 23.7 появилась поддержка добавления извлечения фигур:

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

Также поддерживается возможность обнаружения переполнения при добавлении текста:

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

## Что нового в Aspose.PDF 23.6

В Aspose.PDF 23.6 появилась поддержка добавления следующих плагинов:

- Aspose PdfConverter Html в PDF
- Aspose PdfOrganizer Resize API
- Aspose PdfOrganizer Compress API

Обновление Aspose.PdfForm 
- добавлена функция 'Экспорт "Значений из полей в документе в файл CSV"'
- добавлена возможность устанавливать свойства для отдельных полей

Также поддерживается возможность установки заголовка для страниц HTML, Epub:

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
        Title = "Заголовок страницы"   // <-- добавлено
    };

    document.Save(Params.OutputPath + "53357-out.html", htmlSaveOptions);
```
## Что нового в Aspose.PDF 23.5

С версии 23.5 появилась поддержка добавления опции FontSize для RedactionAnnotation. Используйте следующий фрагмент кода для решения этой задачи:

```cs
    Document doc = new Document(dataDir + "test_factuur.pdf");

    // Создайте экземпляр RedactionAnnotation для конкретной области страницы
    RedactionAnnotation annot = new RedactionAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(367, 756.919982910156, 420, 823.919982910156));
    annot.FillColor = Aspose.Pdf.Color.Black;

    annot.BorderColor = Aspose.Pdf.Color.Yellow;
    annot.Color = Aspose.Pdf.Color.Blue;
    // Текст, который будет напечатан на аннотации к редакции
    annot.OverlayText = "(Unknown)";
    annot.TextAlignment = Aspose.Pdf.HorizontalAlignment.Center;
    // Повторение текста поверх аннотации редакции
    annot.Repeat = false;
    // Новое свойство здесь!
    annot.FontSize = 20;
    // Добавить аннотацию в коллекцию аннотаций первой страницы
    doc.Pages[1].Annotations.Add(annot);
    // Сглаживает аннотацию и редактирует содержимое страницы (т.е. удаляет текст и изображение
    // Под редактируемой аннотацией)
    annot.Redact();
    dataDir = dataDir + "47704_RedactPage_out_NETCORE.pdf";
    doc.Save(dataDir);
```
## Что нового в Aspose.PDF 23.4

Aspose.PDF объявил о выпуске SDK для .NET 7.

## Что нового в Aspose.PDF 23.3.1

С версии Aspose.PDF 23.3 добавлена поддержка следующих плагинов:

- Aspose.PdfForm
- Aspose.PdfConverter PDF в HTML
- Aspose.PdfConverter PDF в XLSX
- Aspose.PdfOrganizer Rotate
- Aspose.PdfExtrator для изображений

## Что нового в Aspose.PDF 23.3

Версия 23.3 ввела поддержку добавления разрешения к изображению. Для решения этой задачи можно использовать два метода:

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

И второй подход:

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
Изображение будет размещено с масштабируемым разрешением, или вы можете установить свойства FixedWidth или FixedHeight в сочетании с IsApplyResolution

## Что нового в Aspose.PDF 23.1.1

С версии Aspose.PDF 23.1.1 поддерживается добавление следующих плагинов:

- Плагин Aspose.PdfOrganizer
- Плагин Aspose.PdfExtractor

## Что нового в Aspose.PDF 23.1

Начиная с версии 23.1 поддерживается создание аннотации PrinterMark.

Знаки печати - это графические символы или текст, добавленные на страницу для помощи производственному персоналу в идентификации компонентов многопластинной работы и поддержании постоянного качества вывода во время производства. Примеры, обычно используемые в печатной промышленности, включают:

- Метки регистрации для выравнивания пластин
- Серые рампы и цветные полосы для измерения цветов и плотности чернил
- Метки обрезки, показывающие, где должен быть обрезан носитель вывода

Мы покажем пример опции с цветными полосами для измерения цветов и плотности чернил.
Мы покажем пример опции с цветными полосами для измерения цветов и плотности чернил.

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
Также поддерживает извлечение векторных изображений. Попробуйте использовать следующий код для обнаружения и извлечения векторной графики:

```cs
    var doc = new Document(input);
    try{
        doc.Pages[1].TrySaveVectorGraphics(outputSvg);
    }
    catch(Exception){

    }
```

## Что нового в Aspose.PDF 22.12

С этого релиза поддерживается конвертация PDF в DICOM изображение

```cs
    Document doc = new Document("source.pdf");
    DicomDevice dicom = new DicomDevice();
    FileStream outStream = new FileStream("out.dicom", FileMode.Create, FileAccess.ReadWrite);
    dicom.Process(doc.Pages[1], outStream);
```    

## Что нового в Aspose.PDF 22.09

С 22.09 поддерживается добавление свойства для изменения порядка рубрик темы (E=, CN=, O=, OU=, ) в подпись.

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
            //или
            //DigitalSubjectFormat = new SubjectNameElements[] { SubjectNameElements.OU, SubjectNameElements.S, SubjectNameElements.C }
        };
        fileSign.Sign(1, true, rect, signature);
        fileSign.Save(outputPdf);
    }
```
## Что нового в Aspose.PDF 22.6

С версии 22.5 поддержка извлечения текста с нижним и верхним индексом из PDF.

Если документ PDF содержит текст с нижним и верхним индексом, например H2O, то при извлечении текста из PDF должна также извлекаться информация о форматировании (в извлеченном обычном тексте).
Если PDF содержит текст курсивом, он также должен быть включен в извлеченное содержимое.

```cs
Document doc = new Document(input);
TextFragmentAbsorber absorber = new TextFragmentAbsorber("TM");
absorber.Visit(doc.Pages[1]);
```

## Что нового в Aspose.PDF 22.4

Этот релиз включает информацию для Aspose.PDF для .NET:

- PDF в ODS: Распознавание текста с нижним и верхним индексом;

**пример**

```cs
Document pdfDocument = new Document("Superscript-Subscript.pdf");
ExcelSaveOptions options = new ExcelSaveOptions();
options.Format = ExcelSaveOptions.ExcelFormat.ODS;
pdfDocument.Save("output.ods"), options);
```

- PDF в XMLSpreadSheet2003: Распознавание текста с нижним и верхним индексом;

- PDF в Excel: Распознавание текста с нижним и верхним индексом;
- PDF в Excel: Распознавание текста в нижнем и верхнем индексах;

- Удаление подписей UR при сохранении документа;

- Удаление флага Suspects в MarkInfo при сохранении документа;

- Удаление информации при сохранении документа

## Что нового в Aspose.PDF 22.3

Этот релиз включает следующие обновления:

- Поддержка AFRelationship;

- Проверка заголовка PDF;

- Удаление подфильтра adbe.x509.rsa_sha1 при сохранении документа;

- Формат поля как число и формат даты;

- Запрет использования шифрования RC4 в FDF 2.0.

## Что нового в Aspose.PDF 22.2

Начиная с версии 22.2, стало возможно подписывать документ с использованием PdfFileSignature с LTV, а также изменять хэширование с SHA1 на SHA256.

```csharp
Пример использования:
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
## Что нового в Aspose.PDF 22.1

Теперь Aspose.PDF для .NET поддерживает загрузку документов из одного из самых популярных форматов документов, Portable Document Format (PDF) версии 2.0.

## Что нового в Aspose.PDF 21.11

### Разрешить нелатинские символы в пароле

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

## Что нового в Aspose.PDF 21.10

### Как обнаружить скрытый текст?

Пожалуйста, используйте TextState.Invisible для получения информации о невидимости текста за пределами настройки режима отображения.

Мы использовали следующий код для тестирования:

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
### Как получить информацию о количестве слоёв в PDF документе?

```csharp
Please use code snippet:
var inFile = "1234.pdf";
Document doc = new Document(inFile);
List layers = doc.Pages[1].Layers;
```

## Что нового в Aspose.PDF 21.9

Настройте цвет фона для внешнего вида подписи и цвет шрифта меток в области подписи с Aspose.PDF для .NET.

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

## Что нового в Aspose.PDF 21.8

### Как изменить цвет текста в цифровой подписи?

В версии 21.8 свойство ForegroundColor позволяет изменять цвет текста в цифровой подписи.

```csharp
```
```csharp
using (PdfFileSignature pdfSign = new PdfFileSignature())
{
    pdfSign.BindPdf(inFile);
    //создаем прямоугольник для размещения подписи
    System.Drawing.Rectangle rect = new System.Drawing.Rectangle(310, 45, 200, 50);
    PKCS7 pkcs = new PKCS7(inPfxFile, "");
    pkcs.CustomAppearance = new SignatureCustomAppearance()
    {//устанавливаем цвет текста
        ForegroundColor = Color.Green
    };
    // подписываем PDF файл
    pdfSign.Sign(1, true, rect, pkcs);
    //сохраняем выходной PDF файл
    pdfSign.Save(outFile);
}
```

## Что нового в Aspose.PDF 21.7

### Создание PDF на основе XML и XLS с параметрами

Для добавления параметров XSL нам нужно создать собственный [XsltArgumentList](https://docs.microsoft.com/en-us/dotnet/api/system.xml.xsl.xsltargumentlist?view=net-5.0) и установить его как свойство в [XslFoLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xslfoloadoptions). Следующий фрагмент показывает, как использовать этот класс с описанными выше примерами файлов.

```csharp
public static void Example_XSLFO_to_PDF()
    {
        var XmlContent = File.ReadAllText(_dataDir + "employees.xml");
        var XsltContent = File.ReadAllText(_dataDir + "employees.xslt");

        var options = new Aspose.Pdf.XslFoLoadOptions();

        //Пример использования XsltArgumentList
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
## Что нового в Aspose.PDF 21.6

С Aspose.PDF для .NET вы можете скрыть изображения с помощью ImagePlacementAbsorber из документа:

```csharp
public void PDFNET_49961()
{
   ImagePlacementAbsorber abs = new ImagePlacementAbsorber();
   Document doc = new Document("test.pdf");
   // Скрыть изображение на первой странице
   doc.Pages[1].Accept(abs);

   foreach (ImagePlacement imagePlacement in abs.ImagePlacements)
   {
       imagePlacement.Hide();
   }

   doc.Save("test_out.pdf");
}
```

## Что нового в Aspose.PDF 21.5

### Как извлечь полное имя шрифта из его описания/ресурса в PDF?

Вы можете получить полное имя шрифта с префиксом с свойством BaseFont для класса Font.

```csharp
Document pdf = new Document(dataDir + @"testfont.pdf");

Aspose.Pdf.Text.Font[] fonts = pdf.FontUtilities.GetAllFonts();
foreach (Aspose.Pdf.Text.Font font in fonts)
{
    Console.WriteLine($"font name : {font.FontName} BaseFont name : {font.BaseFont}");
}
pdf.Dispose();
```

## Что нового в Aspose.PDF 21.4

### Добавлен API для объединения изображений

Aspose.PDF 21.4 позволяет объединять изображения.
Aspose.PDF 21.4 позволяет объединять изображения.

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
Также вы можете объединить свои изображения в формате Tiff:

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

## Что нового в Aspose.PDF 21.3

### Открытое публичное свойство для обнаружения защиты информации Azure
### Публичное раскрытие свойства для обнаружения защиты Azure Information Protection

Следующий фрагмент кода позволит вам получить доступ к зашифрованным данным ваших PDF-файлов, защищенных с помощью Azure Information Protection:

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

## Что нового в Aspose.PDF 21.1

### Добавлена поддержка получения цвета фона TextFragment

В этой версии Aspose.PDF появилась функция получения цвета фона.
В этой версии Aspose.PDF стала доступна функция получения цвета фона.

Пожалуйста, рассмотрите следующий код:

```csharp
Document pdfDocument = new Document(dataDir + "TextColor.pdf");
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber();

TextSearchOptions searchOptions = new TextSearchOptions(false);
searchOptions.SearchForTextRelatedGraphics = true;

textFragmentAbsorber.TextSearchOptions = searchOptions;

// Принять абсорбер для всех страниц
pdfDocument.Pages.Accept(textFragmentAbsorber);

// Получить извлеченные фрагменты текста
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Пройтись по фрагментам
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine("Текст: '{0}'", textFragment.Text);
    Console.WriteLine("Цвет фона: '{0}'", textFragment.TextState.BackgroundColor);
    Console.WriteLine("Цвет переднего плана: '{0}'", textFragment.TextState.ForegroundColor);
    Console.WriteLine("Цвет фона сегмента: '{0}'", textFragment.Segments[1].TextState.BackgroundColor);
}
```
### После конвертации в HTML шрифт полностью встроен в результат

Также, в Aspose.PDF 21.1, после конвертации PDF в HTML, стало доступно встраивание шрифтов в выходной HTML-документ. Это возможно с новой булевой опцией сохранения HtmlSaveParameter.SaveFullFont.

Вот фрагмент кода:

```csharp
HtmlSaveOptions saveOptions = new HtmlSaveOptions();
saveOptions.RasterImagesSavingMode = HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground;
saveOptions.PartsEmbeddingMode = HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml;
saveOptions.LettersPositioningMethod = HtmlSaveOptions.LettersPositioningMethods.UseEmUnitsAndCompensationOfRoundingErrorsInCss;
saveOptions.FontSavingMode = HtmlSaveOptions.FontSavingModes.AlwaysSaveAsTTF;
saveOptions.SaveTransparentTexts = true;
saveOptions.SaveFullFont = true;
```
