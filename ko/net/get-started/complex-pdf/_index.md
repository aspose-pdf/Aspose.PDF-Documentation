---
title: 복잡한 PDF 생성
linktitle: 복잡한 PDF 생성
type: docs
weight: 60
url: ko/net/complex-pdf-example/
description: Aspose.PDF for NET를 사용하면 이미지, 텍스트 조각, 테이블이 포함된 더 복잡한 문서를 생성할 수 있습니다.
aliases:
    - /net/complex-pdf/
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

[Hello, World](/pdf/net/hello-world-example/) 예제에서는 C# 및 Aspose.PDF를 사용하여 PDF 문서를 생성하는 간단한 단계를 보여주었습니다. 이 글에서는 C# 및 Aspose.PDF for .NET을 사용하여 더 복잡한 문서를 생성하는 방법을 살펴보겠습니다. 예로, 여객 페리 서비스를 운영하는 가상의 회사에서 가져온 문서를 사용할 것입니다.
우리의 문서는 이미지, 두 개의 텍스트 조각(헤더와 단락), 그리고 테이블을 포함할 것입니다. 이러한 문서를 구축하기 위해, 우리는 DOM 기반 접근법을 사용할 것입니다. [DOM API 기초](/pdf/net/basics-of-dom-api/) 섹션에서 더 자세한 정보를 읽을 수 있습니다.

문서를 처음부터 생성할 때는 다음 단계를 따라야 합니다:

1.
1. 문서 객체에 [페이지](https://reference.aspose.com/pdf/net/aspose.pdf/page)를 추가합니다. 이제 우리 문서에는 페이지가 하나 있습니다.
1. 페이지에 [이미지](https://reference.aspose.com/pdf/net/aspose.pdf/image/methods/index)를 추가합니다.
1. 헤더용 [텍스트프래그먼트](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment)를 생성합니다. 헤더에는 Arial 글꼴, 글꼴 크기 24pt, 가운데 정렬을 사용합니다.
1. 페이지 [단락](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs)에 헤더를 추가합니다.
1. 설명용 [텍스트프래그먼트](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment)를 생성합니다. 설명에는 Arial 글꼴, 글꼴 크기 24pt, 가운데 정렬을 사용합니다.
1. 페이지 단락에 (설명)을 추가합니다.
1. 테이블을 생성하고 테이블 속성을 추가합니다.
1. 페이지 [단락](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs)에 (테이블)을 추가합니다.
1. 문서 "Complex.pdf"를 저장합니다.

다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.
다음 코드 스니펫도 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리에서 작동합니다.

```csharp
using Aspose.Pdf.Text;
using System;
using System.IO;

namespace Aspose.Pdf.Examples
{
    public static class ExampleGetStarted
    {
        private static readonly string _dataDir = "..\\..\\..\\Samples";
public static void MakeComplexDocument()
        {
            // 문서 객체 초기화
            Document document = new Document();
            // 페이지 추가
            Page page = document.Pages.Add();

            // -------------------------------------------------------------
            // 이미지 추가
            var imageFileName = System.IO.Path.Combine(_dataDir, "logo.png");
            page.AddImage(imageFileName, new Rectangle(20, 730, 120, 830));

            // -------------------------------------------------------------
            // 헤더 추가
            var header = new TextFragment("2020년 가을 새로운 페리 노선");
            header.TextState.Font = FontRepository.FindFont("Arial");
            header.TextState.FontSize = 24;
            header.HorizontalAlignment = HorizontalAlignment.Center;
            header.Position = new Position(130, 720);
            page.Paragraphs.Add(header);

            // 설명 추가
            var descriptionText = "방문객은 온라인으로 티켓을 구매해야 하며, 티켓은 하루 5,000장으로 제한됩니다. 페리 서비스는 절반 용량으로 운영되며 일정이 축소되었습니다. 줄을 서야 할 것으로 예상됩니다.";
            var description = new TextFragment(descriptionText);
            description.TextState.Font = FontRepository.FindFont("Times New Roman");
            description.TextState.FontSize = 14;
            description.HorizontalAlignment = HorizontalAlignment.Left;
            page.Paragraphs.Add(description);


            // 테이블 추가
            var table = new Table
            {
                ColumnWidths = "200",
                Border = new BorderInfo(BorderSide.Box, 1f, Color.DarkSlateGray),
                DefaultCellBorder = new BorderInfo(BorderSide.Box, 0.5f, Color.Black),
                DefaultCellPadding = new MarginInfo(4.5, 4.5, 4.5, 4.5),
                Margin =
                {
                    Bottom = 10
                },
                DefaultCellTextState =
                {
                    Font =  FontRepository.FindFont("Helvetica")
                }
            };

            var headerRow = table.Rows.Add();
            headerRow.Cells.Add("도시 출발");
            headerRow.Cells.Add("섬 출발");
            foreach (Cell headerRowCell in headerRow.Cells)
            {
                headerRowCell.BackgroundColor = Color.Gray;
                headerRowCell.DefaultCellTextState.ForegroundColor = Color.WhiteSmoke;
            }

            var time = new TimeSpan(6, 0, 0);
            var incTime = new TimeSpan(0, 30, 0);
            for (int i = 0; i < 10; i++)
            {
                var dataRow = table.Rows.Add();
                dataRow.Cells.Add(time.ToString(@"hh\:mm"));
                time=time.Add(incTime);
                dataRow.Cells.Add(time.ToString(@"hh\:mm"));
            }

            page.Paragraphs.Add(table);

            document.Save(System.IO.Path.Combine(_dataDir, "Complex.pdf"));

        }
    }
}
```

