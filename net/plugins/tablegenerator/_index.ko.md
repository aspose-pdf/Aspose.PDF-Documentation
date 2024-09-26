---
title: 테이블 생성기
type: docs
weight: 130
url: /net/plugins/tablegenerator/
description: 지정된 PDF 문서 페이지 번호에 테이블을 추가/삽입할 수 있습니다.
lastmod: "2024-01-24"
draft: false
---

.NET을 사용하여 PDF 문서에서 동적이고 시각적으로 매력적인 테이블을 만들 필요가 있으신가요? Aspose.PDF for .NET은 이 과정을 단순화하는 강력한 TableGenerator 클래스를 제공합니다. 이 장에서는 Aspose.PDF Table Generator를 사용하여 PDF 문서에 테이블을 생성하는 단계를 [Aspose.PDF Table Generator](https://products.aspose.org/pdf/net/table-generator/)를 통해 데모 문서를 생성하고 TableGenerator 클래스로 테이블을 생성하는 것까지 걸쳐 설명하겠습니다.
테이블 생성 방법을 단계별로 알아봅시다.

## 사전 요구 사항

다음이 필요합니다:

* Visual Studio 2019 이상
* Aspose.PDF for .NET 24.3 이상
* 샘플 PDF 파일

## 데모 문서 생성

테이블을 생성하기 전에, 테이블이 삽입될 빈 페이지가 있는 데모 문서를 만들어 보겠습니다.
테이블 생성을 시작하기 전에, 테이블이 삽입될 데모 문서를 빈 페이지와 함께 생성해 봅시다.

* 새 PDF 문서를 생성합니다.
* 문서에 빈 페이지를 추가합니다.
* 지정된 파일에 문서를 저장합니다.

```cs
// <summary>
// 빈 페이지가 있는 데모 문서를 생성합니다.
//
// 매개 변수:
// - fileName: 출력 파일의 경로와 이름입니다.
// </summary>
internal static void CreateDemoDocument(string fileName)
{
    // 새 PDF 문서를 생성합니다.
    var document = new Aspose.Pdf.Document();

    // 문서에 네 개의 빈 페이지를 추가합니다.
    for (int i = 0; i < 2; i++)
    {
        document.Pages.Add();
    }

    // 지정된 파일에 문서를 저장합니다.
    document.Save(fileName);
}
```

## 테이블 생성

데모 문서가 준비되면, `TableGenerator` 클래스를 사용하여 테이블을 생성할 수 있습니다. 다양한 콘텐츠 유형과 형식 옵션을 사용하여 테이블을 생성하는 방법을 보여주는 다음 스니펫입니다. 테이블을 생성하는 방법은 다음과 같습니다:

* `TableGenerator` 클래스의 새 인스턴스를 생성합니다.
* `TableGenerator` 클래스의 새 인스턴스를 생성합니다.
* 테이블 옵션을 생성하고 입력 및 출력 파일 데이터 소스를 지정합니다.
* 옵션에 테이블과 행, 셀을 추가하면서 내용과 포맷을 지정합니다.
* `Process` 메소드를 사용하여 테이블 생성을 처리하고 결과 컨테이너를 얻습니다.

### 테이블 생성하기

Aspose.PDF를 사용하여 테이블을 생성하는 방법은 다음과 같습니다:

```cs
// TableGenerator 클래스의 새 인스턴스를 생성합니다.
var generator = new TableGenerator();

// 테이블 옵션을 생성하고 데모 테이블을 추가합니다.
var options = new TableOptions();

// 옵션에 입력 및 출력 파일 데이터 소스를 추가합니다.
options.AddInput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));
options.AddOutput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));

// 첫 번째 테이블을 옵션에 추가합니다.
options
    .InsertPageAfter(1)
    .AddTable()
```

위 코드에서는 `TableOptions` 인스턴스를 생성하고 PDF 문서의 입력 및 출력 파일 데이터 소스를 지정합니다.
위 코드에서는 `TableOptions`의 인스턴스를 생성하고 PDF 문서에 대한 입력 및 출력 파일 데이터 소스를 지정합니다.

### 테이블에 콘텐츠 추가하기

테이블이 생성되면, 텍스트, HTML, 이미지 등 다양한 유형의 콘텐츠를 포함하는 행과 셀로 채울 수 있습니다. 다음은 테이블에 콘텐츠를 추가하는 방법입니다:

```csharp
options
    .AddTable()
        .AddRow()
            .AddCell()
                .AddParagraph(new HtmlFragment("<h1>Header 1</h1>")) // 셀에 HTML 콘텐츠 추가하기.
            .AddCell()
                .AddParagraph(new HtmlFragment("<h2>Header 2</h2>"))
            .AddCell()
                .AddParagraph(new HtmlFragment("<h3>Header 3</h3>"));
```

이 예에서는 테이블에 행을 추가하고 헤더를 나타내는 HTML 조각이 포함된 셀로 채웁니다.

유용한 메소드:

* **InsertPageAfter**: 지정된 페이지 번호 뒤에 페이지를 삽입합니다.
* **InsertPageBefore**: 지정된 페이지 번호 앞에 페이지를 삽입합니다.
* **AddTable**: 문서에 테이블을 추가합니다.
* **AddTable**: 문서에 테이블 추가
* **AddRow**: 테이블에 행 추가
* **AddCell**: 행에 셀 추가
* **AddParagraph**: 셀에 내용 추가

다음 유형의 내용을 단락으로 추가할 수 있습니다:

* **HtmlFragment** - HTML 마크업을 기반으로 한 내용
* **TeXFragment** - TeX/LaTeX 마크업을 기반으로 한 내용
* **TextFragment** - 간단한 텍스트 내용
* **Image** - 그래픽

## 테이블 생성 수행

내용을 추가한 후 테이블 생성을 시작할 수 있습니다.

```cs
// 테이블 생성을 처리하고 결과 컨테이너를 가져옵니다.
var resultContainer = generator.Process(options);

// 결과 컬렉션의 결과 수를 출력합니다.
Console.WriteLine(resultContainer.ResultCollection.Count);
```

`Process` 메소드는 테이블 생성을 수행합니다. 이 메소드는 또한 오류를 처리하기 위해 try-catch로 감쌀 수 있습니다.

아래에서 전체 코드 예제를 볼 수 있습니다:

```cs
using Aspose.Pdf;
using Aspose.Pdf.Plugins;
using Aspose.Pdf.Text;

namespace AsposePluginsNet8.Documentation
{
    // 테이블 생성 사용법을 보여주는 클래스를 나타냅니다.
    internal static class TableDemo
    {
        // 테이블 생성 데모를 실행합니다.
        internal static void Run()
        {
            // 데모 문서를 생성하고 테이블을 생성합니다.
            CreateDemoDocument(@"C:\Samples\Results\table-generator-demo.pdf");
            CreateDemoTable();
        }

        // 네 개의 빈 페이지가 있는 데모 문서를 생성합니다.
        //
        // 매개변수:
        // - fileName: 출력 파일의 경로와 이름입니다.
        internal static void CreateDemoDocument(string fileName)
        {
            // 새로운 PDF 문서를 생성합니다.
            var document = new Aspose.Pdf.Document();

            // 문서에 네 개의 빈 페이지를 추가합니다.
            for (int i = 0; i < 2; i++)
            {
                document.Pages.Add();
            }

            // 지정된 파일에 문서를 저장합니다.
            document.Save(fileName);
        }

        // TableGenerator 클래스를 사용하여 테이블을 생성합니다.
        internal static void CreateDemoTable()
        {
            // TableGenerator 클래스의 새 인스턴스를 생성합니다.
            var generator = new TableGenerator();

            // 테이블 옵션을 생성하고 데모 테이블을 추가합니다.
            var options = new TableOptions();

            // 옵션에 입력 및 출력 파일 데이터 소스를 추가합니다.
            options.AddInput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));
            options.AddOutput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));

            // 옵션에 첫 번째 테이블을 추가합니다.
            options
                .InsertPageAfter(1)
                .AddTable()
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new HtmlFragment("<h1>Header 1</h1>"))
                        .AddCell()
                            .AddParagraph(new HtmlFragment("<h2>Header 2</h2>"))
                        .AddCell()
                            .AddParagraph(new HtmlFragment("<h3>Header 3</h3>"))
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new TeXFragment("{\\small The equation $E=mc^2$, discovered in 1905 by Albert Einstein.}", true))
                        .AddCell()
                            .AddParagraph(new TextFragment("Cell 2 2"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Cell 2 3"))
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new TextFragment("Cell 3 1a"))
                            .AddParagraph(new TextFragment("Cell 3 1b"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Cell 3 2"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Cell 3 3"));

            // 옵션에 두 번째 테이블을 추가합니다.
            options
                .InsertPageBefore(2)
                .AddTable()
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new TextFragment("Header 1 1"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Header 1 2"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Header 1 3"))
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new Image()
                            {
                                File = @"C:\Samples\logo.png",
                                FixWidth = 75,
                                FixHeight = 75,
                            })
                        .AddCell()
                            .AddParagraph(new Image()
                            {
                                File = @"C:\Samples\sample.svg",
                                FileType = ImageFileType.Svg,
                                FixWidth = 75,
                                FixHeight = 75
                            })
                        .AddCell()
                            .AddParagraph(new Image()
                            {
                                ImageStream = File.OpenRead(@"C:\Samples\Conversion\Demo.dcm"),
                                FileType = ImageFileType.Dicom,
                                FixWidth = 75,
                                FixHeight = 75
                            });

            // 테이블 생성을 처리하고 결과 컨테이너를 가져옵니다.
            var resultContainer = generator.Process(options);

            // 결과 컬렉션의 결과 수를 출력합니다.
            Console.WriteLine(resultContainer.ResultCollection.Count);
        }
    }
}
```

