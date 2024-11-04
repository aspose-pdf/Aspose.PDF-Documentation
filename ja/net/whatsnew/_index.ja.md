---
title: 新機能
linktitle: 新機能
type: docs
weight: 10
url: /net/whatsnew/
description: このページでは、最近のリリースで導入されたAspose.PDF for .NETの最も人気のある新機能を紹介します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2024-09-06"
---

## Aspose.PDF 24.8の新機能

PDF文書をPDF/A-4形式に変換

バージョン24.8以降、PDF文書をPDF/A-4に変換することが可能になりました。この規格の第4部は、PDF 2.0に基づいており、2020年末に公開されました。

以下のコードスニペットは、入力ドキュメントがPDF 2.xであることを前提に、ドキュメントをPDF/A-4形式に変換する方法を示しています。

```cs

    string documentPath = "";
    string conversionLogPath = "";
    string resultPdfPath ="";

    using (var document = new Document(documentPath))
    {
        // PDF-2.x文書のみをPDF/A-4に変換可能
        document.Convert(conversionLogPath, PdfFormat.PDF_A_4, ConvertErrorAction.Delete);
        document.Save(resultPdfPath);
    }
```
次のコードスニペットでは、入力ドキュメントが以前のバージョンの場合にドキュメントをPDF/A-4形式に変換する方法を示しています。

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

24.8以降、PDFドキュメントで透明コンテンツを平坦化する方法を導入しました：

```cs
    string documentPath = "";
    string resultPdfPath ="";

    using (var document = new Document(documentPath))
    {
        document.FlattenTransparency();
        document.Save(resultPdfPath);
    }
```

## Aspose.PDF 24.7の新機能

Aspose.PDF for .NETを使用してPDFドキュメントを比較する

24.7からは、PDFドキュメントの内容を注釈マークと並列出力で比較することが可能になりました：

最初のコードスニペットは、二つのPDFドキュメントの最初のページを比較する方法を示しています。
最初のコードスニペットは、2つのPDFドキュメントの最初のページを比較する方法を示しています。

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

2番目のコードスニペットは、2つのPDFドキュメントの全内容を比較する範囲を広げます。

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
## Aspose.PDF 24.4の新機能

このリリースでは、画像にクリッピングマスクを適用する機能がサポートされています：

```cs
    Document doc = new Document("input.pdf");
    using (var fs1 = new FileStream("mask1.jpg", FileMode.Open))
    using (var fs2 = new FileStream("mask2.png", FileMode.Open))
    {
        doc.Pages[1].Resources.Images[1].AddStencilMask(fs1);
        doc.Pages[1].Resources.Images[2].AddStencilMask(fs2);
    }
```

24.4からは、APIを使用して印刷ダイアログでPDFページサイズに基づいて用紙ソースを選択できます。

Aspose.PDF 24.4からは、この設定をDocument.PickTrayByPdfSizeプロパティまたはPdfContentEditorファサードを使用してオンまたはオフに切り替えることができます：

```cs
    using (Document document = new Document())
    {
        Page page = document.Pages.Add();
        page.Paragraphs.Add(new TextFragment("Hello world!"));

        // PDFページサイズを使用して用紙トレイを選択するフラグを設定
        document.PickTrayByPdfSize = true;
        document.Save("result.pdf");
    }
```
```cs

    using (PdfContentEditor contentEditor = new PdfContentEditor())
    {
        contentEditor.BindPdf("input.pdf");

        // PDFページサイズを使用して用紙トレイを選択するためのフラグを設定
        contentEditor.ChangeViewerPreference(ViewerPreference.PickTrayByPDFSize);
        contentEditor.Save("result.pdf");
    }
```

このリリースからAspose.PDF Signature for .NETプラグインが追加されました：

- 新しいフィールドとオプションを作成する例：

```cs

    // シグネチャを作成
    var plugin = new Signature();
    // 設定指示を設定するSignOptionsオブジェクトを作成
    var opt = new SignOptions(inputPfxPath, inputPfxPassword);
    // 入力ファイルパスを追加
    opt.AddInput(new FileDataSource(inputPath));
    // 出力ファイルパスを設定
    opt.AddOutput(new FileDataSource(outputPath));
    // 追加のオプションを設定
    opt.Reason = "私の理由";
    opt.Contact = "私の連絡先";
    opt.Location = "私の位置";
    // 処理を実行
    plugin.Process(opt);
```

- 既存の空のフィールドを使用する例

```cs

    // シグネチャを作成
    var plugin = new Signature();
    // 設定指示を設定するSignOptionsオブジェクトを作成
    var opt = new SignOptions(inputPfxPath, inputPfxPassword);
    // 空の署名フィールドを含む入力ファイルパスを追加
    opt.AddInput(new FileDataSource(inputPath));
    // 出力ファイルパスを設定
    opt.AddOutput(new FileDataSource(outputPath));
    // 既存の署名フィールドの名前を設定
    opt.Name = "Signature1";
    // 処理を実行
    plugin.Process(opt);
```
## Aspose.PDF 24.3の新機能

このリリースから.NETプラグインのPDF/Aコンバーターが追加されました：

```cs
    var options = new PdfAConvertOptions
    {
        PdfAVersion = PdfAStandardVersion.PDF_A_3B
    };

    // ソースファイルを追加
    options.AddInput(new FileDataSource("path_to_your_pdf_file.pdf"));

    // 変換されたファイルを保存するパスを追加
    options.AddOutput(new FileDataSource("path_to_the_converted_file.pdf"));

    // プラグインインスタンスを作成
    var plugin = new PdfAConverter();

    // 変換を実行
    plugin.Process(options);
```

- TextFragmentAbsorberでフレーズリストを通じて検索を実装：

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
    // 結果を取得
    var result = absorber.RegexResults
```
24.3から、PDF/Aファイルのすべてのページに空の署名フィールドを追加することが可能になりました。

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
            // 新しい提案されたコード、SignatureFieldオブジェクトを使用（このコードは正常に動作します）
            var doc = new Document(fs);
            var f = new SignatureField(doc.Pages[page], new Rectangle(10, 10, 100, 100));
            // 署名フィールドのデフォルト外観を追加
            f.DefaultAppearance = new DefaultAppearance("Helv", 12, System.Drawing.Color.Black);
            var newAddedField = doc.Form.Add(f, fieldName, page);

            // どうすればnewAddedFieldをすべてのページで可視化することができますか？
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
## Aspose.PDF 24.2の新機能

24.2からPDFファイルからベクターデータを取得可能になりました。

ドキュメントからベクターデータを取得するためにGraphicsAbsorberが実装されました：

```cs
var doc = new Document(input);
var grAbsorber = new GraphicsAbsorber();
grAbsorber.Visit(doc.Pages[1]);
var elements = grAbsorber.Elements;
var operators = elements[1].Operators;
var rectangle = elements[1].Rectangle;
var position = elements[1].Position;
```

## Aspose.PDF 24.1の新機能

24.1リリースからPDFにFDF形式の注釈をインポート可能になりました：

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

また、ページ辞書またはドキュメントカタログへのアクセスもサポートしています。
ページディクショナリまたはドキュメントカタログへのアクセスをサポートします。

DictionaryEditorのコード例は以下の通りです：

- 新しい値を追加

```cs

    // キー名の例
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

- 辞書に値を追加して設定

```cs

    using (var doc = new Document())
    {
        var page = doc.Pages.Add();
        var dictionaryEditor = new DictionaryEditor(page);
        dictionaryEditor.Add(KEY_NAME, new CosPdfName("Old name"));
        // または
        dictionaryEditor[KEY_NAME] = new CosPdfName("New name");
    }
```
- 辞書から値を取得する

```cs
    using (var doc = new Document())
    {
        var page = doc.Pages.Add();
        var dictionaryEditor = new DictionaryEditor(page);
        dictionaryEditor[KEY_NAME] = new CosPdfName("name");
        var value = dictionaryEditor[KEY_NAME];
        // または
        ICosPdfPrimitive primitive;
        dictionaryEditor.TryGetValue(KEY_NAME, out primitive);
    }
```

- 辞書から値を削除する

```cs
    using (var doc = new Document())
    {
        var page = doc.Pages.Add();
        var dictionaryEditor = new DictionaryEditor(page);
        dictionaryEditor.Add(KEY_NAME, new CosPdfName(EXPECTED_NAME));
        dictionaryEditor.Remove(KEY_NAME);
    }
```

## Aspose.PDF 23.12の新機能

以下のコードスニペットを使用して、フォームを見つけてテキストを置換することができます:

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

または、フォームを完全に削除することができます:

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

フォームを削除する別の方法:

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

- 以下のコードスニペットを使用してすべてのフォームを削除できます:

```cs
    var document = new Document(input);
    var forms = document.Pages[1].Resources.Forms;

    forms.Clear();

    document.Save(output);
```
- PDFをMarkdownに変換する実装：

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

- OFDをPDFに変換する実装：

```cs
    var document = new Document("sample.ofd", new OfdLoadOptions());
    document.Save("sample.pdf");
```

このリリースからMergerプラグインが追加されました：

```cs
    // 出力されるマージされたPDFファイルへのパス。
    var outputPath = "TestMerge.pdf";

    // Mergerの新しいインスタンスを作成。
    var merger = new Merger();

    // MergeOptionsを作成。
    var opt = new MergeOptions();
    opt.AddInput(new FileDataSource(inputPath1));
    opt.AddInput(new FileDataSource(inputPath2));
    opt.AddOutput(new FileDataSource(outputPath));

    // PDFのマージ処理を実行。
    merger.Process(opt);
```

また、このリリースからChatGPTプラグインが追加されました：
このリリースから、ChatGPTプラグインが追加されました：

```cs
    using (var plugin = new PdfChatGpt())
    {
    var options = new PdfChatGptRequestOptions();
    options.AddOutput(new FileDataSource("PdfChatGPT_output.pdf")); // 出力ファイルパスを追加します。
    options.ApiKey = "Your API key."; // APIにアクセスするためのキーを提供する必要があります。
    options.MaxTokens = 1000; // チャット完了で生成する最大トークン数。

    // リクエストメッセージを追加します。
    options.Messages.Add(new Message
    {
        Content = "You are a helpful assistant.",
        Role = Role.System
    });
    options.Messages.Add(new Message
    {
        Content = "What is the biggest pizza diameter ever made?",
        Role = Role.User
    });

    // リクエストを処理します。
    var result = await plugin.ProcessAsync(options);

    var fileResultPath = result.ResultCollection[0].Data;
    var chatCompletionObject = result.ResultCollection[1].Data as ChatCompletion; // The ChatGPT API chat completion object.
    }
```

## Aspose.PDF 23.11の新機能
## Aspose.PDF 23.11の新機能

このリリースでは、PDFファイルから非表示テキストを削除することが可能になりました：

```cs
    var document = new Document(inputFile);
    var textAbsorber = new TextFragmentAbsorber();

        // このオプションは、非表示テキストの置換後に他のテキストフラグメントが移動するのを防ぐために使用できます。
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

23.11からはスレッドの中断をサポート：

```cs

    public void InterruptExample()
    {
        string outputFile = testdata + "sample.pdf";
        // これは大量のテキストです。8350文字のLorem Ipsumを使用して中断を引き起こします
        string text = ExampleApp.LongText;
        using (InterruptMonitor monitor = new InterruptMonitor())
        {
            RowSpanWorker worker = new RowSpanWorker (outputFile, monitor);
            Thread thread = new Thread(new ThreadStart(worker.Work));
            thread.Start();

            // タイムアウトは、中断なしで完全なドキュメント保存に必要な時間より短くすべきです。
            Thread.Sleep(500);

            // プロセスを中断します
            monitor.Interrupt();

            // 中断を待ちます...
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

                    // 2行にわたってセルを追加し、長いテキストを含む
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
## Aspose.PDF 23.10 の新機能

最新のアップデートでは、タグ付きPDFからタグを削除する3つのバージョンを紹介します。

- ドキュメントのRootElement（ルートツリー要素）からノード要素を削除します：

```cs
    var document = new Document("some tagged pdf");
    var structure = document.LogicalStructure;
    var documentElement = structure.Children[0];
    var structElement = documentElement.Children.Count > 1 ? documentElement.Children[1] as StructElement : null;
    if (documentElement.Children.Remove(structElement))
    {
        // 要素が削除されました
        document.Save(outputPath);
    }

    // structElement 自体も削除できます
    //if (structElement != null)
    //{
    //    structElement.Remove();
    //    document.Save(outputPath);
    //}
```

- 文書からすべてのマーク付き要素のタグを削除しますが、構造要素は保持します：

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
- タグをすべて削除します:

```cs
    var document = new Document("some tagged pdf");
    var structure = document.LogicalStructure;
    var documentElement = structure.Children[0];
    documentElement.Remove();
    document.Save(outputPath);
```

10月23日より、文字の高さを測定する新機能が実装されました。以下のコードを使用して、文字の高さを測定してください。

```cs
    var doc = new Document(input);
    var absorber = new TextFragmentAbsorber();
    absorber.Visit(doc.Pages[1]);
    var height = absorber.TextFragments[1].TextState.MeasureHeight('A')
```

この測定は、ドキュメントに埋め込まれたフォントに基づいています。寸法情報が欠落している場合、この方法は0を返します。

また、このリリースでは、署名されたHASHを使用してPDFに署名する機能も提供されます:

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
新機能はプリントダイアログのプリセットページスケーリングです：

```cs
    Document document = new Document();
    document.Pages.Add();
    document.PrintScaling = PrintScaling.None;
    document.Save("output.pdf");
```

## Aspose.PDF 23.9の新機能

23.9から、記入可能フィールドから子アノテーションを削除するサポートが追加されました。

```cs

    doc = new Document("field-ref-add.pdf");
    field = (Field)doc.Form[fieldName];
    var annotation = field[1];
    doc.Pages[annotation .PageIndex].Annotations.Remove(annotation);
    doc.Save("field-ref-delete.pdf");
```

## Aspose.PDF 23.8の新機能

23.8から、インクリメンタルアップデートの検出をサポート。

PDFドキュメントでインクリメンタルアップデートを検出する機能が追加されました。この機能は、ドキュメントがインクリメンタルアップデートで保存された場合は'true'を返し、そうでない場合は'false'を返します。

```cs

    var path = "C:\test.pdf";
    var doc = new Document(path);
    Console.WriteLine(doc.HasIncrementalUpdate());
```

また、23.8はネストされたチェックボックスフィールドを扱う方法をサポートしています。
23.8はネストされたチェックボックスフィールドを扱う方法をサポートしています。

- 複数値チェックボックスフィールドを作成する：

```cs
    using (var document = new Document())
    {
    var page = document.Pages.Add();

    var checkbox = new CheckboxField(page, new Rectangle(50, 50, 70, 70));

    // 最初のチェックボックスグループオプション値を設定
    checkbox.ExportValue = "オプション 1";

    // 既存のオプションの直下に新しいオプションを追加
    checkbox.AddOption("オプション 2");

    // 指定された矩形で新しいオプションを追加
    checkbox.AddOption("オプション 3", new Rectangle(100, 100, 120, 120));

    document.Form.Add(checkbox);

    // 追加されたチェックボックスを選択
    checkbox.Value = "オプション 2";
    document.Save("checkbox_group.pdf");
    }
```

- 複数値チェックボックスの値を取得および設定する：

```cs
    using (Document doc = new Document("example.pdf"))
    {
    Form form = doc.Form;
    CheckboxField checkbox = form.Fields[0] as CheckboxField;

    // 許可された値はAllowedStatesコレクションから取得可能
    // Valueプロパティを使用してチェックボックスの値を設定
    checkbox.Value = checkbox.AllowedStates[0];
    checkboxValue = checkbox.Value; // 以前に設定された値，例：「オプション 1」

    // 値はAllowedStatesの任意の要素であるべき
    checkbox.Value = "オプション 2";
    checkboxValue = checkbox.Value; // オプション 2

    // チェックボックスの値を「オフ」に設定するか、Checkedをfalseに設定してチェックを外す
    checkbox.Value = "オフ";
    // あるいは、代替として：
    // checkbox.Checked = false;
    checkboxValue = checkbox.Value; // オフ
    }
```
## Aspose.PDF 23.7の新機能

Aspose.PDF 23.7では、形状抽出の追加をサポートしています：

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

テキスト追加時のオーバーフロー検出機能もサポートしています：

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
## Aspose.PDF 23.6の新機能

Aspose.PDF 23.6から次のプラグインを追加でサポート：

- Aspose PdfConverter HtmlからPDFへ
- Aspose PdfOrganizer リサイズAPI
- Aspose PdfOrganizer 圧縮API

Aspose.PdfFormを更新
- ドキュメントのフィールドからCSVファイルへの「値のエクスポート」機能を追加
- 個別のフィールドに対するプロパティを設定する機能を追加

また、HTML、Epubページのタイトルを設定する機能をサポート：

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
        Title = "Title for page"   // <-- これが追加されました
    };

    document.Save(Params.OutputPath + "53357-out.html", htmlSaveOptions);
```
## Aspose.PDF 23.5の新機能

23.5からRedactionAnnotationのFontSizeオプションを追加できるようになりました。次のコードスニペットを使用してこのタスクを解決します：

```cs
    Document doc = new Document(dataDir + "test_factuur.pdf");

    // 特定のページ領域のRedactionAnnotationインスタンスを作成
    RedactionAnnotation annot = new RedactionAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(367, 756.919982910156, 420, 823.919982910156));
    annot.FillColor = Aspose.Pdf.Color.Black;

    annot.BorderColor = Aspose.Pdf.Color.Yellow;
    annot.Color = Aspose.Pdf.Color.Blue;
    // レダクトアノテーションに印刷されるテキスト
    annot.OverlayText = "(Unknown)";
    annot.TextAlignment = Aspose.Pdf.HorizontalAlignment.Center;
    // レダクトアノテーション上でオーバーレイテキストを繰り返す
    annot.Repeat = false;
    // 新しいプロパティがここにあります！
    annot.FontSize = 20;
    // アノテーションを最初のページのアノテーションコレクションに追加
    doc.Pages[1].Annotations.Add(annot);
    // アノテーションをフラット化し、ページコンテンツをレダクトします（つまり、レダクトされたアノテーションの下のテキストと画像を削除します）
    annot.Redact();
    dataDir = dataDir + "47704_RedactPage_out_NETCORE.pdf";
    doc.Save(dataDir);
```
## Aspose.PDF 23.4の新機能

Aspose.PDFは.NET 7 SDKのリリースを発表しました。

## Aspose.PDF 23.3.1の新機能

Aspose.PDF 23.3から次のプラグインを追加するサポートが導入されました：

- Aspose.PdfForm
- Aspose.PdfConverter PDFからHTMLへ
- Aspose.PdfConverter PDFからXLSXへ
- Aspose.PdfOrganizer 回転
- Aspose.PdfExtrator 画像用

## Aspose.PDF 23.3の新機能

バージョン23.3では、画像に解像度を追加するサポートが導入されました。この問題を解決するために、次の二つの方法が使用できます：

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

そして、2番目のアプローチ：

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
画像はスケーリングされた解像度で配置されるか、FixedWidthまたはFixedHeightプロパティをIsApplyResolutionと組み合わせて設定することができます。

## Aspose.PDF 23.1.1の新機能

Aspose.PDF 23.1.1から次のプラグインを追加するサポートがあります：

- Aspose.PdfOrganizerプラグイン
- Aspose.PdfExtractorプラグイン

## Aspose.PDF 23.1の新機能

23.1バージョンからPrinterMarkアノテーションを作成するサポートがあります。

プリンターマークは、複数プレートの仕事の構成要素を識別するために生産担当者を支援し、生産中に一貫した出力を維持するためにページに追加されるグラフィックシンボルまたはテキストです。印刷業界で一般的に使用される例は以下の通りです：

- プレートの整列用の登録ターゲット
- 色とインク密度を測るためのグレーランプとカラーバー
- 出力媒体のトリミング箇所を示すカットマーク

色とインク密度を測るためのカラーバーを使用したオプションの例を示します。
色バーを使用して色とインク密度を測定するオプションの例を示します。

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
ベクター画像の抽出もサポートしてください。以下のコードを使用してベクターグラフィックスを検出して抽出してみてください：

```cs
    var doc = new Document(input);
    try{
        doc.Pages[1].TrySaveVectorGraphics(outputSvg);
    }
    catch(Exception){

    }
```

## Aspose.PDF 22.12の新機能

このリリースからPDFをDICOMイメージに変換するサポートが追加されました

```cs
    Document doc = new Document("source.pdf");
    DicomDevice dicom = new DicomDevice();
    FileStream outStream = new FileStream("out.dicom", FileMode.Create, FileAccess.ReadWrite);
    dicom.Process(doc.Pages[1], outStream);
```

## Aspose.PDF 22.09の新機能

22.09からは署名に主題区分の順序を変更するプロパティを追加するサポートがあります（E=, CN=, O=, OU=, ）。

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
## Aspose.PDF 22.6の新機能

22.5以降、PDFからSubScriptおよびSuperScriptテキストを抽出するサポートが追加されました。

PDFドキュメントにH2OのようなSubScriptおよびSuperScriptテキストが含まれている場合、PDFからテキストを抽出する際には、その書式情報も抽出される必要があります（抽出されたプレーンテキストで）。
PDFにイタリック体のテキストが含まれている場合、それも抽出内容に含める必要があります。

```cs
Document doc = new Document(input);
TextFragmentAbsorber absorber = new TextFragmentAbsorber("TM");
absorber.Visit(doc.Pages[1]);
```

## Aspose.PDF 22.4の新機能

このリリースには、Aspose.PDF for .NETの情報が含まれています：

- PDF to ODS: 下付きテキストと上付きテキストを認識する;

**例**

```cs
Document pdfDocument = new Document("Superscript-Subscript.pdf");
ExcelSaveOptions options = new ExcelSaveOptions();
options.Format = ExcelSaveOptions.ExcelFormat.ODS;
pdfDocument.Save("output.ods"), options);
```

- PDF to XMLSpreadSheet2003: 下付きテキストと上付きテキストを認識する;

- PDF to Excel: 下付きテキストと上付きテキストを認識する;
- PDFからExcelへ：下付き文字と上付き文字のテキストを認識する;

- ドキュメントを保存する際にUR署名を削除する;

- ドキュメントを保存する際にMarkInfoのSuspectsフラグを削除する;

- ドキュメントを保存する際に情報を削除する

## Aspose.PDF 22.3の新機能

このリリースには以下のアップデートが含まれています:

- AFRelationshipのサポート;

- PDFヘッダーの検証;

- ドキュメントを保存する際にadbe.x509.rsa_sha1サブフィルタを削除する;

- フィールドを数値および日付形式でフォーマットする;

- FDF 2.0でRC4暗号化の使用を禁止する.

## Aspose.PDF 22.2の新機能

22.2バージョンから、PdfFileSignatureを使用してLTVでドキュメントに署名し、ハッシングをSHA1からSHA256に変更することが可能です。

```csharp
使用例:
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
## Aspose.PDF 22.1の新機能

現在、Aspose.PDF for .NETは、最も人気のあるドキュメントフォーマットの一つであるポータブルドキュメントフォーマット(PDF)バージョン2.0からのドキュメントの読み込みをサポートしています。

## Aspose.PDF 21.11の新機能

### パスワードに非ラテン文字を許可

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

## Aspose.PDF 21.10の新機能

### 隠されたテキストを検出する方法は？

TextState.Invisibleを使用して、レンダリングモード設定の外でテキストの不可視性に関する情報を取得してください。

以下のコードをテストに使用しました：

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
### PDFドキュメントのレイヤー数についての情報を取得する方法は？

```csharp
コードスニペットを使用してください：
var inFile = "1234.pdf";
Document doc = new Document(inFile);
List layers = doc.Pages[1].Layers;
```

## Aspose.PDF 21.9の新機能

Aspose.PDF for .NETを使用して、署名エリアの背景色とラベルのフォント色をカスタマイズします。

```csharp
using (PdfFileSignature pdfSign = new PdfFileSignature())
{
    pdfSign.BindPdf(inFile);
    var rect = new System.Drawing.Rectangle(310, 45, 200, 50);
    var pkcs = new PKCS7(inPfxFile, "");
    pkcs.CustomAppearance = new SignatureCustomAppearance()
    {//色を設定
        ForegroundColor = Color.DarkGreen,
        BackgroundColor = Color.LightSeaGreen,
    };
    pdfSign.Sign(1, true, rect, pkcs);
    pdfSign.Save(outFile);
}
```

## Aspose.PDF 21.8の新機能

### デジタル署名のテキスト色を変更する方法は？

21.8バージョンのForegroundColorプロパティにより、デジタル署名のテキスト色を変更できます。

```csharp
```csharp
using (PdfFileSignature pdfSign = new PdfFileSignature())
{
    pdfSign.BindPdf(inFile);
    //署名の場所を指定するための矩形を作成
    System.Drawing.Rectangle rect = new System.Drawing.Rectangle(310, 45, 200, 50);
    PKCS7 pkcs = new PKCS7(inPfxFile, "");
    pkcs.CustomAppearance = new SignatureCustomAppearance()
    {//テキストの色を設定
        ForegroundColor = Color.Green
    };
    // PDFファイルに署名
    pdfSign.Sign(1, true, rect, pkcs);
    //出力PDFファイルを保存
    pdfSign.Save(outFile);
}
```

## Aspose.PDF 21.7の新機能

### XMLおよびXLSを基にしたPDFの作成

XSLパラメータを追加するには、独自の[XsltArgumentList](https://docs.microsoft.com/en-us/dotnet/api/system.xml.xsl.xsltargumentlist?view=net-5.0)を作成し、[XslFoLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xslfoloadoptions)のプロパティとして設定します。以下のスニペットは、上記のファイルを使用する方法を示しています。

```csharp
public static void Example_XSLFO_to_PDF()
    {
        var XmlContent = File.ReadAllText(_dataDir + "employees.xml");
        var XsltContent = File.ReadAllText(_dataDir + "employees.xslt");

        var options = new Aspose.Pdf.XslFoLoadOptions();

        //XsltArgumentListの使用例
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
## Aspose.PDF 21.6の新機能

Aspose.PDF for .NETでは、ドキュメントからImagePlacementAbsorberを使用して画像を非表示にできます：

```csharp
public void PDFNET_49961()
{
   ImagePlacementAbsorber abs = new ImagePlacementAbsorber();
   Document doc = new Document("test.pdf");
   // 1ページ目の画像を非表示
   doc.Pages[1].Accept(abs);

   foreach (ImagePlacement imagePlacement in abs.ImagePlacements)
   {
       imagePlacement.Hide();
   }

   doc.Save("test_out.pdf");
}
```

## Aspose.PDF 21.5の新機能

### PDFの説明/リソースからフォントの完全な名前を抽出する方法は？

BaseFontプロパティを使用して、フォントクラスのプレフィックス付きの完全なフォントを取得できます。

```csharp
Document pdf = new Document(dataDir + @"testfont.pdf");

Aspose.Pdf.Text.Font[] fonts = pdf.FontUtilities.GetAllFonts();
foreach (Aspose.Pdf.Text.Font font in fonts)
{
    Console.WriteLine($"font name : {font.FontName} BaseFont name : {font.BaseFont}");
}
pdf.Dispose();
```

## Aspose.PDF 21.4の新機能

### 画像を結合するためのAPIを追加

Aspose.PDF 21.4では、画像を結合することができます。
Aspose.PDF 21.4では、画像を結合することができます。

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

## Aspose.PDF 21.3の新機能

### Azure Information Protectionの検出を公開するためのプロパティ
### Azure Information Protectionを使用してプロパティを公開する

次のコードスニペットを使用すると、Azure Information Protectionで保護されたPDFファイルの暗号化されたペイロードにアクセスできるようになります：

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

## Aspose.PDF 21.1の新機能

### TextFragmentの背景色の取得をサポート

このバージョンのAspose.PDFでは、TextFragmentの背景色を取得する機能が利用可能になりました。
このバージョンのAspose.PDFでは、背景色を取得する機能が利用可能になりました。

以下のコードを参照してください：

```csharp
Document pdfDocument = new Document(dataDir + "TextColor.pdf");
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber();

TextSearchOptions searchOptions = new TextSearchOptions(false);
searchOptions.SearchForTextRelatedGraphics = true;

textFragmentAbsorber.TextSearchOptions = searchOptions;

// すべてのページに対して吸収器を適用
pdfDocument.Pages.Accept(textFragmentAbsorber);

// 抽出されたテキストフラグメントを取得
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// フラグメントをループ処理
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine("Text: '{0}'", textFragment.Text);
    Console.WriteLine("BackgroundColor: '{0}'", textFragment.TextState.BackgroundColor);
    Console.WriteLine("ForegroundColor: '{0}'", textFragment.TextState.ForegroundColor);
    Console.WriteLine("Segment BackgroundColor: '{0}'", textFragment.Segments[1].TextState.BackgroundColor);
}
```
### HTMLへの変換後、フォントは出力内に完全に埋め込まれます

Aspose.PDF 21.1では、PDFをHTMLに変換した後、出力HTMLドキュメント内に埋め込まれたフォントが利用可能になりました。これは、新しいブール型の保存オプションHtmlSaveParameter.SaveFullFontを使用することで可能です。

こちらがコードスニペットです：

```csharp
HtmlSaveOptions saveOptions = new HtmlSaveOptions();
saveOptions.RasterImagesSavingMode = HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground;
saveOptions.PartsEmbeddingMode = HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml;
saveOptions.LettersPositioningMethod = HtmlSaveOptions.LettersPositioningMethods.UseEmUnitsAndCompensationOfRoundingErrorsInCss;
saveOptions.FontSavingMode = HtmlSaveOptions.FontSavingModes.AlwaysSaveAsTTF;
saveOptions.SaveTransparentTexts = true;
saveOptions.SaveFullFont = true;
```
