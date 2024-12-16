---
title: What's new
linktitle: What's new
type: docs
weight: 10
url: /ko/net/whatsnew/
description: 이 페이지에서는 최근 릴리스에서 도입된 Aspose.PDF for .NET의 가장 인기 있는 새로운 기능을 소개합니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2024-09-06"
---

## Aspose.PDF 24.8의 새로운 기능

PDF 문서를 PDF/A-4 형식으로 변환

버전 24.8부터 PDF 문서를 PDF/A-4로 변환할 수 있게 되었습니다. 이 표준의 제4부는 2020년 말에 PDF 2.0을 기반으로 발행되었습니다.

다음 코드 스니펫은 입력 문서가 PDF 2.x인 경우 문서를 PDF/A-4 형식으로 변환하는 방법을 보여줍니다.

```cs

    string documentPath = "";
    string conversionLogPath = "";
    string resultPdfPath ="";

    using (var document = new Document(documentPath))
    {
        // PDF-2.x 문서만 PDF/A-4로 변환할 수 있습니다
        document.Convert(conversionLogPath, PdfFormat.PDF_A_4, ConvertErrorAction.Delete);
        document.Save(resultPdfPath);
    }
```
두 번째 코드 스니펫은 입력 문서가 이전 버전일 때 문서를 PDF/A-4 형식으로 변환하는 방법을 보여줍니다.

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

24.8부터 PDF 문서에서 투명한 콘텐츠를 평탄화하는 방법을 도입했습니다:

```cs
    string documentPath = "";
    string resultPdfPath ="";

    using (var document = new Document(documentPath))
    {
        document.FlattenTransparency();
        document.Save(resultPdfPath);
    }
```

## Aspose.PDF 24.7의 새로운 기능

Aspose.PDF for .NET을 사용한 PDF 문서 비교

24.7부터 PDF 문서의 내용을 주석 표시와 나란히 출력으로 비교할 수 있습니다:

첫 번째 코드 스니펫은 두 PDF 문서의 첫 페이지를 비교하는 방법을 보여줍니다.
첫 번째 코드 스니펫은 두 PDF 문서의 첫 페이지를 비교하는 방법을 보여줍니다.

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

두 번째 코드 스니펫은 두 PDF 문서의 전체 내용을 비교하는 범위를 확장합니다.

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
## Aspose.PDF 24.4의 새로운 기능

이 릴리즈는 이미지에 클리핑 마스크를 적용하는 것을 지원합니다:

```cs
    Document doc = new Document("input.pdf");
    using (var fs1 = new FileStream("mask1.jpg", FileMode.Open))
    using (var fs2 = new FileStream("mask2.png", FileMode.Open))
    {
        doc.Pages[1].Resources.Images[1].AddStencilMask(fs1);
        doc.Pages[1].Resources.Images[2].AddStencilMask(fs2);
    }
```

24.4부터 API를 사용하여 인쇄 대화 상자에서 PDF 페이지 크기에 따라 용지 공급원을 선택할 수 있습니다.

Aspose.PDF 24.4부터 이 선호도는 Document.PickTrayByPdfSize 속성 또는 PdfContentEditor 파사드를 사용하여 켜고 끌 수 있습니다:

```cs
    using (Document document = new Document())
    {
        Page page = document.Pages.Add();
        page.Paragraphs.Add(new TextFragment("Hello world!"));

        // PDF 페이지 크기를 사용하여 용지 트레이를 선택하도록 플래그 설정
        document.PickTrayByPdfSize = true;
        document.Save("result.pdf");
    }
```
```cs

    using (PdfContentEditor contentEditor = new PdfContentEditor())
    {
        contentEditor.BindPdf("input.pdf");

        // PDF 페이지 크기를 사용하여 용지함 선택 플래그 설정
        contentEditor.ChangeViewerPreference(ViewerPreference.PickTrayByPDFSize);
        contentEditor.Save("result.pdf");
    }
```

이 릴리스에서 Aspose.PDF Signature for .NET 플러그인이 추가되었습니다:

- 새 필드 및 옵션 생성 예:

```cs

    // 서명 생성
    var plugin = new Signature();
    // 지침 설정을 위한 SignOptions 객체 생성
    var opt = new SignOptions(inputPfxPath, inputPfxPassword);
    // 입력 파일 경로 추가
    opt.AddInput(new FileDataSource(inputPath));
    // 출력 파일 경로 설정
    opt.AddOutput(new FileDataSource(outputPath));
    // 추가 옵션 설정
    opt.Reason = "내 이유";
    opt.Contact = "내 연락처";
    opt.Location = "내 위치";
    // 처리 수행
    plugin.Process(opt);
```

- 기존 빈 필드 사용 예:

```cs

    // 서명 생성
    var plugin = new Signature();
    // 지침 설정을 위한 SignOptions 객체 생성
    var opt = new SignOptions(inputPfxPath, inputPfxPassword);
    // 빈 서명 필드가 있는 입력 파일 경로 추가
    opt.AddInput(new FileDataSource(inputPath));
    // 출력 파일 경로 설정
    opt.AddOutput(new FileDataSource(outputPath));
    // 기존 서명 필드의 이름 설정
    opt.Name = "Signature1";
    // 처리 수행
    plugin.Process(opt);
```
## Aspose.PDF 24.3의 새로운 기능

이 릴리스에서 .NET 플러그인인 PDF/A 변환기가 추가되었습니다:

```cs
    var options = new PdfAConvertOptions
    {
        PdfAVersion = PdfAStandardVersion.PDF_A_3B
    };

    // 원본 파일 추가
    options.AddInput(new FileDataSource("path_to_your_pdf_file.pdf")); // 실제 파일 경로로 교체

    // 변환된 파일을 저장할 경로 추가
    options.AddOutput(new FileDataSource("path_to_the_converted_file.pdf"));

    // 플러그인 인스턴스 생성
    var plugin = new PdfAConverter();

    // 변환 실행
    plugin.Process(options);
```

- TextFragmentAbsorber를 사용하여 구문 리스트에서 검색 구현:

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
    // 결과 가져오기
    var result = absorber.RegexResults
```
24.3 버전부터 PDF/A 파일의 모든 페이지에 빈 서명 필드를 추가할 수 있습니다.

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
            // 새로 제안된 코드, SignatureField 객체 사용 (이 코드는 잘 작동합니다)
            var doc = new Document(fs);
            var f = new SignatureField(doc.Pages[page], new Rectangle(10, 10, 100, 100));
            // 서명 필드의 기본 모양 추가
            f.DefaultAppearance = new DefaultAppearance("Helv", 12, System.Drawing.Color.Black);
            var newAddedField = doc.Form.Add(f, fieldName, page);

            // 이제 newAddedField를 모든 페이지에서 보이게 할 수 있을까요?
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
## Aspose.PDF 24.2의 새로운 기능

24.2부터 PDF 파일에서 벡터 데이터를 가져올 수 있게 되었습니다.

문서에서 벡터 데이터를 얻기 위해 GraphicsAbsorber가 구현되었습니다:

```cs
var doc = new Document(input);
var grAbsorber = new GraphicsAbsorber();
grAbsorber.Visit(doc.Pages[1]);
var elements = grAbsorber.Elements;
var operators = elements[1].Operators;
var rectangle = elements[1].Rectangle;
var position = elements[1].Position;
```

## Aspose.PDF 24.1의 새로운 기능

24.1 릴리스부터 PDF에 FDF 형식의 주석을 가져올 수 있습니다:

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

또한, 페이지 사전 또는 문서 카탈로그에 접근을 지원합니다.
페이지 사전이나 문서 카탈로그에 접근할 수 있는 지원도 제공됩니다.

다음은 DictionaryEditor에 대한 코드 예제입니다:

- 새로운 값 추가

```cs
    // 키 이름의 예
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

- 사전에 값 추가 및 설정

```cs
    using (var doc = new Document())
    {
        var page = doc.Pages.Add();
        var dictionaryEditor = new DictionaryEditor(page);
        dictionaryEditor.Add(KEY_NAME, new CosPdfName("Old name"));
        // 또는 
        dictionaryEditor[KEY_NAME] = new CosPdfName("New name");
    }
```
- 사전에서 값 가져오기

```cs
    using (var doc = new Document())
    {
        var page = doc.Pages.Add();
        var dictionaryEditor = new DictionaryEditor(page);
        dictionaryEditor[KEY_NAME] = new CosPdfName("name");
        var value = dictionaryEditor[KEY_NAME];
        // 또는
        ICosPdfPrimitive primitive;
        dictionaryEditor.TryGetValue(KEY_NAME, out primitive);
    }
```

- 사전에서 값 제거하기

```cs
    using (var doc = new Document())
    {
        var page = doc.Pages.Add();
        var dictionaryEditor = new DictionaryEditor(page);
        dictionaryEditor.Add(KEY_NAME, new CosPdfName(EXPECTED_NAME));
        dictionaryEditor.Remove(KEY_NAME);
    }
```

## Aspose.PDF 23.12의 새로운 기능

다음 코드 조각을 사용하여 양식을 찾고 텍스트를 교체할 수 있습니다:

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

또는, 양식을 완전히 제거할 수 있습니다:

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

양식을 제거하는 또 다른 변형:

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

- 다음 코드 조각을 사용하여 모든 양식을 삭제할 수 있습니다:

```cs
    var document = new Document(input);
    var forms = document.Pages[1].Resources.Forms;

    forms.Clear();

    document.Save(output);
```
- PDF를 마크다운으로 변환 구현:

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

- OFD를 PDF로 변환 구현:

```cs
    var document = new Document("sample.ofd", new OfdLoadOptions());
    document.Save("sample.pdf");
```

이번 릴리스에서 Merger 플러그인 추가:

```cs
    // 출력 병합 PDF 파일 경로.
    var outputPath = "TestMerge.pdf";

    // Merger의 새 인스턴스 생성.
    var merger = new Merger();

    // MergeOptions 생성.
    var opt = new MergeOptions();
    opt.AddInput(new FileDataSource(inputPath1));
    opt.AddInput(new FileDataSource(inputPath2));
    opt.AddOutput(new FileDataSource(outputPath));

    // PDF 병합 처리.
    merger.Process(opt);
```

또한, 이번 릴리스에서 ChatGPT 플러그인 추가:
## Aspose.PDF 23.11의 새로운 기능

이번 릴리스에서 ChatGPT 플러그인이 추가되었습니다:

```cs
    using (var plugin = new PdfChatGpt())
    {
    var options = new PdfChatChatGptRequestOptions();
    options.AddOutput(new FileDataSource("PdfChatGPT_output.pdf")); // 출력 파일 경로 추가.
    options.ApiKey = "Your API key."; // API 접근을 위한 키를 제공해야 합니다.
    options.MaxTokens = 1000; // 채팅 완성에서 생성할 최대 토큰 수.

    // 요청 메시지 추가.
    options.Messages.Add(new Message
    {
        Content = "도움이 되는 조수입니다.",
        Role = Role.System
    });
    options.Messages.Add(new Message
    {
        Content = "지금까지 만들어진 가장 큰 피자 지름은 얼마인가요?",
        Role = Role.User
    });

    // 요청 처리.
    var result = await plugin.ProcessAsync(options);

    var fileResultPath = result.ResultCollection[0].Data;
    var chatCompletionObject = result.ResultCollection[1].Data as ChatCompletion; // ChatGPT API 채팅 완성 객체.
    }
```
## Aspose.PDF 23.11의 새로운 기능

이번 릴리스에서 PDF 파일에서 숨겨진 텍스트를 제거할 수 있습니다:

```cs
    var document = new Document(inputFile);
    var textAbsorber = new TextFragmentAbsorber();

        // 이 옵션은 숨겨진 텍스트를 대체한 후 다른 텍스트 조각이 이동하는 것을 방지하는 데 사용할 수 있습니다.
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

23.11부터 스레드 중단 지원:

```cs

    public void InterruptExample()
    {
        string outputFile = testdata + "sample.pdf";
        //이것은 일시 중단을 유발하기 위해 8350자의 Lorem Ipsum을 사용한 큰 텍스트입니다.
        string text = ExampleApp.LongText;
        using (InterruptMonitor monitor = new InterruptMonitor())
        {
            RowSpanWorker worker = new RowSpanWorker (outputFile, monitor);
            Thread thread = new Thread(new ThreadStart(worker.Work));
            thread.Start();

            // 타임아웃은 전체 문서 저장 시간(중단 없이)보다 짧아야 합니다.
            Thread.Sleep(500);

            // 프로세스 중단
            monitor.Interrupt();

            // 중단을 기다림...
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

                    // 두 행에 걸쳐 있는 세포에 긴 텍스트를 추가
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
## Aspose.PDF 23.10의 새로운 기능

현재 업데이트에서 태그가 지정된 PDF에서 태그를 제거하는 세 가지 버전을 소개합니다.

- 문서 요소(documentElement, 루트 트리 요소)에서 일부 노드 요소 제거:

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

    // structElement 자체를 삭제할 수도 있습니다
    //if (structElement != null)
    //{
    //    structElement.Remove();
    //    document.Save(outputPath);
    //}
```

- 문서에서 모든 표시된 요소 태그를 제거하지만 구조 요소는 유지:

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
- 모든 태그 제거:

```cs
    var document = new Document("some tagged pdf");
    var structure = document.LogicalStructure;
    var documentElement = structure.Children[0];
    documentElement.Remove();
    document.Save(outputPath);
```

23.10부터 문자 높이를 측정하는 새 기능이 도입되었습니다. 다음 코드를 사용하여 문자의 높이를 측정하세요.

```cs
    var doc = new Document(input);
    var absorber = new TextFragmentAbsorber();
    absorber.Visit(doc.Pages[1]);
    var height = absorber.TextFragments[1].TextState.MeasureHeight('A')
```

측정은 문서에 포함된 폰트를 기반으로 합니다. 차원 정보가 누락된 경우 이 메소드는 0을 반환합니다.

또한 이번 릴리스에서는 서명된 HASH를 사용하여 PDF에 서명하는 기능을 제공합니다:

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
새로운 기능인 인쇄 대화 상자 프리셋 페이지 스케일링:

```cs
    Document document = new Document();
    document.Pages.Add();
    document.PrintScaling = PrintScaling.None;
    document.Save("output.pdf");
```

## Aspose.PDF 23.9의 새로운 기능

23.9부터 채울 수 있는 필드에서 자식 주석을 제거하는 기능을 지원합니다.

```cs

    doc = new Document("field-ref-add.pdf");
    field = (Field)doc.Form[fieldName];
    var annotation = field[1];
    doc.Pages[annotation .PageIndex].Annotations.Remove(annotation);
    doc.Save("field-ref-delete.pdf");
```

## Aspose.PDF 23.8의 새로운 기능

23.8부터 증분 업데이트 감지 기능을 추가 지원합니다.

PDF 문서에서 증분 업데이트를 감지하는 기능이 추가되었습니다. 이 기능은 문서가 증분 업데이트로 저장되었는지 여부를 반환합니다; 그렇지 않으면 'false'를 반환합니다.

```cs

    var path = "C:\\test.pdf";
    var doc = new Document(path);
    Console.WriteLine(doc.HasIncrementalUpdate());
```

또한, 23.8은 중첩된 체크박스 필드를 다루는 방법을 지원합니다.
23.8은 중첩된 체크박스 필드를 사용하는 방법을 지원합니다.

- 다중 값 체크박스 필드 생성:

```cs
    using (var document = new Document())
    {
    var page = document.Pages.Add();

    var checkbox = new CheckboxField(page, new Rectangle(50, 50, 70, 70));

    // 첫 번째 체크박스 그룹 옵션 값을 설정
    checkbox.ExportValue = "option 1";

    // 기존 옵션 바로 아래에 새 옵션 추가
    checkbox.AddOption("option 2");

    // 주어진 직사각형에 새 옵션 추가
    checkbox.AddOption("option 3", new Rectangle(100, 100, 120, 120));

    document.Form.Add(checkbox);

    // 추가된 체크박스 선택
    checkbox.Value = "option 2";
    document.Save("checkbox_group.pdf");
    }
```

- 다중 값 체크박스의 값을 가져오고 설정:

```cs
    using (Document doc = new Document("example.pdf"))
    {
    Form form = doc.Form;
    CheckboxField checkbox = form.Fields[0] as CheckboxField;

    // 허용된 값은 AllowedStates 컬렉션에서 검색할 수 있음
    // Value 속성을 사용하여 체크박스 값 설정
    checkbox.Value = checkbox.AllowedStates[0];
    checkboxValue = checkbox.Value; // 이전에 설정된 값, 예: "option 1"

    // 값은 AllowedStates의 어떤 요소이어야 함
    checkbox.Value = "option 2";
    checkboxValue = checkbox.Value; // option 2

    // Value를 "Off"로 설정하거나 Checked를 false로 설정하여 체크박스 선택 해제
    checkbox.Value = "Off";
    // 또는, 선택적으로:
    // checkbox.Checked = false;
    checkboxValue = checkbox.Value; // Off
    }
```
## Aspose.PDF 23.7의 새로운 기능

Aspose.PDF 23.7에서는 도형 추출 기능을 추가할 수 있습니다:

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

텍스트 추가 시 Overflow 감지 기능도 지원합니다:

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
## Aspose.PDF 23.6의 새로운 기능

Aspose.PDF 23.6부터 다음 플러그인 추가 지원:

- Aspose PdfConverter Html to PDF
- Aspose PdfOrganizer 크기 조정 API
- Aspose PdfOrganizer 압축 API

Aspose.PdfForm 업데이트
- 문서의 필드에서 값 추출하여 CSV 파일로 내보내기 기능 추가
- 개별 필드의 속성 설정 기능 추가

또한 HTML, Epub 페이지의 제목 설정 기능 추가 지원:

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
        Title = "Title for page"   // <-- 이 추가됨
    };

    document.Save(Params.OutputPath + "53357-out.html", htmlSaveOptions);
```
## Aspose.PDF 23.5의 새로운 기능

23.5 버전부터 RedactionAnnotation에 FontSize 옵션을 추가할 수 있게 되었습니다. 다음 코드 스니펫을 사용하여 이 작업을 해결하세요:

```cs
    Document doc = new Document(dataDir + "test_factuur.pdf");

    // 특정 페이지 영역에 대한 RedactionAnnotation 인스턴스 생성
    RedactionAnnotation annot = new RedactionAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(367, 756.919982910156, 420, 823.919982910156));
    annot.FillColor = Aspose.Pdf.Color.Black;

    annot.BorderColor = Aspose.Pdf.Color.Yellow;
    annot.Color = Aspose.Pdf.Color.Blue;
    // 레다트 주석에 인쇄될 텍스트
    annot.OverlayText = "(Unknown)";
    annot.TextAlignment = Aspose.Pdf.HorizontalAlignment.Center;
    // 레다트 주석에 오버레이 텍스트 반복
    annot.Repeat = false;
    // 새로운 속성!
    annot.FontSize = 20;
    // 첫 페이지의 주석 컬렉션에 주석 추가
    doc.Pages[1].Annotations.Add(annot);
    // 주석을 평탄화하고 페이지 내용을 레다트 (즉, 레다트된 주석 아래의 텍스트 및 이미지 제거)
    annot.Redact();
    dataDir = dataDir + "47704_RedactPage_out_NETCORE.pdf";
    doc.Save(dataDir);
```
## Aspose.PDF 23.4의 새로운 기능

Aspose.PDF에서 .NET 7 SDK 출시를 발표했습니다.

## Aspose.PDF 23.3.1의 새로운 기능

Aspose.PDF 23.3부터 다음 플러그인 추가 지원:

- Aspose.PdfForm
- Aspose.PdfConverter PDF to HTML
- Aspose.PdfConverter PDF to XLSX
- Aspose.PdfOrganizer Rotate
- Aspose.PdfExtrator for Images

## Aspose.PDF 23.3의 새로운 기능

버전 23.3에서 이미지에 해상도를 추가하는 기능을 도입했습니다. 이 문제를 해결할 수 있는 두 가지 방법은 다음과 같습니다:

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

그리고 두 번째 접근 방식:

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
이미지는 스케일된 해상도로 배치되거나 FixedWidth 또는 FixedHeight 속성을 IsApplyResolution과 결합하여 설정할 수 있습니다.

## Aspose.PDF 23.1.1의 새로운 기능

Aspose.PDF 23.1.1부터 다음 플러그인 추가 지원:

- Aspose.PdfOrganizer 플러그인
- Aspose.PdfExtractor 플러그인

## Aspose.PDF 23.1의 새로운 기능

23.1 버전부터 PrinterMark 주석 생성을 지원합니다.

프린터의 표시는 인쇄 공정에서 여러 판의 구성 요소를 식별하고 생산 중에 일관된 출력을 유지하는 데 도움이 되는 그래픽 기호 또는 텍스트입니다. 인쇄 산업에서 일반적으로 사용되는 예는 다음과 같습니다:

- 판을 맞추기 위한 등록 목표
- 색상과 잉크 밀도를 측정하기 위한 회색 경사 및 색상 바
- 출력 매체를 자를 위치를 보여주는 절단 표시

색상 바를 사용한 색상 및 잉크 밀도 측정 옵션의 예를 보여 드리겠습니다.
색상 막대를 사용하여 색상과 잉크 밀도를 측정하는 옵션의 예를 보여 드리겠습니다.

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
벡터 이미지 추출도 지원합니다. 다음 코드를 사용하여 벡터 그래픽을 감지하고 추출해 보세요:

```cs
    var doc = new Document(input);
    try{
        doc.Pages[1].TrySaveVectorGraphics(outputSvg);
    }
    catch(Exception){

    }
```

## Aspose.PDF 22.12의 새로운 기능

이번 릴리스에서는 PDF를 DICOM 이미지로 변환하는 기능을 지원합니다.

```cs
    Document doc = new Document("source.pdf");
    DicomDevice dicom = new DicomDevice();
    FileStream outStream = new FileStream("out.dicom", FileMode.Create, FileAccess.ReadWrite);
    dicom.Process(doc.Pages[1], outStream);
```    

## Aspose.PDF 22.09의 새로운 기능

22.09부터 서명에 주제 루브릭의 순서를 수정하는 속성을 추가하는 기능을 지원합니다.(E=, CN=, O=, OU=, )

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
## Aspose.PDF 22.6의 새로운 기능

22.5부터 PDF에서 첨자와 윗첨자 텍스트를 추출하는 기능을 지원합니다.

PDF 문서에 H2O와 같은 첨자 및 윗첨자 텍스트가 포함되어 있는 경우, PDF에서 텍스트를 추출할 때 해당 형식 정보도 추출되어야 합니다(추출된 일반 텍스트에서).
PDF에 이탤릭체 텍스트가 포함되어 있다면, 추출된 내용에도 포함되어야 합니다.

```cs
Document doc = new Document(input);
TextFragmentAbsorber absorber = new TextFragmentAbsorber("TM");
absorber.Visit(doc.Pages[1]);
```

## Aspose.PDF 22.4의 새로운 기능

이 릴리스는 Aspose.PDF for .NET에 대한 정보를 포함합니다:

- PDF에서 ODS로: 첨자 및 윗첨자에서 텍스트 인식;

**예시**

```cs
Document pdfDocument = new Document("Superscript-Subscript.pdf");
ExcelSaveOptions options = new ExcelSaveOptions();
options.Format = ExcelSaveOptions.ExcelFormat.ODS;
pdfDocument.Save("output.ods"), options);
```

- PDF에서 XMLSpreadSheet2003로: 첨자 및 윗첨자에서 텍스트 인식;

- PDF에서 Excel로: 첨자 및 윗첨자에서 텍스트 인식;
- PDF에서 Excel로: 아래첨자 및 윗첨자의 텍스트 인식;

- 문서 저장 시 UR 서명 제거;

- 문서 저장 시 MarkInfo에서 Suspects 플래그 제거;

- 문서 저장 시 정보 제거

## Aspose.PDF 22.3의 새로운 기능

이 릴리스는 다음 업데이트를 포함합니다:

- AFRelationship 지원;

- PDF 헤더 검증;

- 문서 저장 시 adbe.x509.rsa_sha1 서브필터 제거;

- 숫자 및 날짜 형식으로 필드 형식 지정;

- FDF 2.0에서 RC4 암호화 사용 금지

## Aspose.PDF 22.2의 새로운 기능

22.2 버전부터는 LTV를 사용하여 PdfFileSignature로 문서에 서명할 수 있으며, SHA1에서 SHA256으로 해싱을 변경할 수 있습니다.

```csharp
예제 사용:
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
## Aspose.PDF 22.1의 새로운 기능

이제 Aspose.PDF for .NET은 가장 인기 있는 문서 형식 중 하나인 Portable Document Format (PDF) 버전 2.0에서 문서를 로드하는 것을 지원합니다.

## Aspose.PDF 21.11의 새로운 기능

### 비 라틴 문자 비밀번호 허용

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

## Aspose.PDF 21.10의 새로운 기능

### 숨겨진 텍스트 감지 방법?

TextState.Invisible을 사용하여 렌더링 모드 설정 외부에서 텍스트의 불투명 정보를 얻으십시오.

테스트에 다음 코드를 사용했습니다:

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
### PDF 문서의 레이어 수에 대한 정보를 얻는 방법은 무엇입니까?

```csharp
코드 스니펫을 사용하세요:
var inFile = "1234.pdf";
Document doc = new Document(inFile);
List layers = doc.Pages[1].Layers;
```

## Aspose.PDF 21.9의 새로운 기능

Aspose.PDF for .NET을 사용하여 서명 영역의 배경색과 레이블의 글꼴 색상을 사용자 정의합니다.

```csharp
using (PdfFileSignature pdfSign = new PdfFileSignature())
{
    pdfSign.BindPdf(inFile);
    var rect = new System.Drawing.Rectangle(310, 45, 200, 50);
    var pkcs = new PKCS7(inPfxFile, "");
    pkcs.CustomAppearance = new SignatureCustomAppearance()
    {//색상 설정
        ForegroundColor = Color.DarkGreen,
        BackgroundColor = Color.LightSeaGreen,
    };
    pdfSign.Sign(1, true, rect, pkcs);
    pdfSign.Save(outFile);
}
```

## Aspose.PDF 21.8의 새로운 기능

### 디지털 서명에서 텍스트 색상을 변경하는 방법은?

21.8 버전의 ForegroundColor 속성을 사용하면 디지털 서명에서 텍스트 색상을 변경할 수 있습니다.

```csharp
```
```csharp
using (PdfFileSignature pdfSign = new PdfFileSignature())
{
    pdfSign.BindPdf(inFile);
    //서명 위치를 위한 사각형 생성
    System.Drawing.Rectangle rect = new System.Drawing.Rectangle(310, 45, 200, 50);
    PKCS7 pkcs = new PKCS7(inPfxFile, "");
    pkcs.CustomAppearance = new SignatureCustomAppearance()
    {//텍스트 색상 설정
        ForegroundColor = Color.Green
    };
    // PDF 파일에 서명
    pdfSign.Sign(1, true, rect, pkcs);
    //결과 PDF 파일 저장
    pdfSign.Save(outFile);
}
```

## Aspose.PDF 21.7의 새로운 기능

### XML 및 XLS를 기반으로 한 PDF 생성

XSL 매개변수를 추가하려면 [XsltArgumentList](https://docs.microsoft.com/en-us/dotnet/api/system.xml.xsl.xsltargumentlist?view=net-5.0)를 생성하고 [XslFoLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xslfoloadoptions)의 속성으로 설정해야 합니다. 다음 코드 조각은 위에 설명된 샘플 파일을 사용하여 이 클래스를 사용하는 방법을 보여줍니다.

```csharp
public static void Example_XSLFO_to_PDF()
    {
        var XmlContent = File.ReadAllText(_dataDir + "employees.xml");
        var XsltContent = File.ReadAllText(_dataDir + "employees.xslt");

        var options = new Aspose.Pdf.XslFoLoadOptions();

        //XsltArgumentList 사용 예
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
## Aspose.PDF 21.6의 새로운 기능

Aspose.PDF for .NET을 사용하면 문서에서 ImagePlacementAbsorber를 사용하여 이미지를 숨길 수 있습니다:

```csharp
public void PDFNET_49961()
{
   ImagePlacementAbsorber abs = new ImagePlacementAbsorber();
   Document doc = new Document("test.pdf");
   // 첫 페이지의 이미지 숨기기
   doc.Pages[1].Accept(abs);

   foreach (ImagePlacement imagePlacement in abs.ImagePlacements)
   {
       imagePlacement.Hide();
   }

   doc.Save("test_out.pdf");
}
```

## Aspose.PDF 21.5의 새로운 기능

### PDF의 설명/자원에서 글꼴 전체 이름을 추출하는 방법은?

Font 클래스의 BaseFont 속성으로 접두사가 있는 전체 글꼴을 얻을 수 있습니다.

```csharp
Document pdf = new Document(dataDir + @"testfont.pdf");

Aspose.Pdf.Text.Font[] fonts = pdf.FontUtilities.GetAllFonts();
foreach (Aspose.Pdf.Text.Font font in fonts)
{
    Console.WriteLine($"font name : {font.FontName} BaseFont name : {font.BaseFont}");
}
pdf.Dispose();
```

## Aspose.PDF 21.4의 새로운 기능

### 이미지 병합 API 추가

Aspose.PDF 21.4는 이미지를 결합할 수 있습니다.
Aspose.PDF 21.4는 이미지를 결합할 수 있습니다.

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
## Aspose.PDF 21.3의 새로운 기능

### Azure Information Protection 감지를 위한 속성의 공개 노출

또한 TIFF 형식으로 이미지를 병합할 수 있습니다:

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
### Azure Information Protection을 통해 속성을 공개하는 방법

다음 코드 스니펫을 사용하면 Azure Information Protection으로 보호된 PDF 파일의 암호화된 페이로드에 접근할 수 있습니다:

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

## Aspose.PDF 21.1의 새로운 기능

### TextFragment의 배경색 검색 지원 추가

이 버전의 Aspose.PDF에서는 배경색을 검색하는 기능이 제공됩니다.
이 Aspose.PDF 버전에서는 배경색을 검색할 수 있는 기능이 제공되었습니다.

다음 코드를 고려해 주세요:

```csharp
Document pdfDocument = new Document(dataDir + "TextColor.pdf");
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber();

TextSearchOptions searchOptions = new TextSearchOptions(false);
searchOptions.SearchForTextRelatedGraphics = true;

textFragmentAbsorber.TextSearchOptions = searchOptions;

// 모든 페이지에 대해 absorber를 적용
pdfDocument.Pages.Accept(textFragmentAbsorber);

// 추출된 텍스트 조각을 가져옵니다
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// 조각을 반복 처리
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine("Text: '{0}'", textFragment.Text);
    Console.WriteLine("BackgroundColor: '{0}'", textFragment.TextState.BackgroundColor);
    Console.WriteLine("ForegroundColor: '{0}'", textFragment.TextState.ForegroundColor);
    Console.WriteLine("Segment BackgroundColor: '{0}'", textFragment.Segments[1].TextState.BackgroundColor);
}
```
### HTML로 변환 후 글꼴이 출력물에 완전히 포함됩니다

또한, Aspose.PDF 21.1에서 PDF를 HTML로 변환한 후, 출력 HTML 문서에 포함된 글꼴이 사용 가능해졌습니다. 이는 새로운 불리언 저장 옵션 HtmlSaveParameter.SaveFullFont을 통해 가능합니다.

다음은 코드 스니펫입니다:

```csharp
HtmlSaveOptions saveOptions = new HtmlSaveOptions();
saveOptions.RasterImagesSavingMode = HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground;
saveOptions.PartsEmbeddingMode = HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml;
saveOptions.LettersPositioningMethod = HtmlSaveOptions.LettersPositioningMethods.UseEmUnitsAndCompensationOfRoundingErrorsInCss;
saveOptions.FontSavingMode = HtmlSaveOptions.FontSavingModes.AlwaysSaveAsTTF;
saveOptions.SaveTransparentTexts = true;
saveOptions.SaveFullFont = true;
```
