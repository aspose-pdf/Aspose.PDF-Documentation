---
title: PDF에서 테이블 데이터 추출하기
linktitle: 테이블 데이터 추출
type: docs
weight: 40
url: /net/extract-data-from-table-in-pdf/
description: Aspose.PDF for .NET을 사용하여 C#에서 PDF의 테이블 데이터를 추출하는 방법을 알아보세요
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 프로그래밍 방식으로 PDF에서 테이블 추출하기

PDF에서 테이블을 추출하는 것은 테이블이 다양한 방식으로 생성될 수 있기 때문에 간단한 작업이 아닙니다.

Aspose.PDF for .NET은 테이블을 쉽게 검색할 수 있는 도구를 제공합니다. 테이블 데이터를 추출하려면 다음과 같은 단계를 수행해야 합니다:

1. 문서 열기 - [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체를 인스턴스화합니다;
1. [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber) 객체를 생성합니다.
1.
1. `TableList`는 [AbsorbedTable](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable)의 목록입니다. 데이터를 얻으려면 `TableList`를 순회하면서 [RowList](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable/properties/rowlist)와 [CellList](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedrow/properties/celllist)를 처리하세요.
1. 각 [AbsorbedCell](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedcell)은 [TextFragments](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedcell/properties/textfragments) 컬렉션을 포함하고 있습니다. 이를 원하는 목적으로 처리할 수 있습니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

다음 예제는 모든 페이지에서 표 추출을 보여줍니다:

```csharp
public static void Extract_Table()
{
    // Load source PDF document
    var filePath="<... enter path to pdf file here ...>";
    Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(filePath);                       
    foreach (var page in pdfDocument.Pages)
    {
        Aspose.Pdf.Text.TableAbsorber absorber = new Aspose.Pdf.Text.TableAbsorber();
        absorber.Visit(page);
        foreach (AbsorbedTable table in absorber.TableList)
        {
            Console.WriteLine("Table");
            foreach (AbsorbedRow row in table.RowList)
            {
                foreach (AbsorbedCell cell in row.CellList)
                {                                 
                    foreach (TextFragment fragment in cell.TextFragments)
                    {
                        var sb = new StringBuilder();
                        foreach (TextSegment seg in fragment.Segments)
                            sb.Append(seg.Text);
                        Console.Write($"{sb.ToString()}|");
                    }                           
                }
                Console.WriteLine();
            }
        }
    }
}
```

## PDF 페이지 특정 영역의 테이블 추출

각 흡수된 테이블은 페이지상의 테이블 위치를 설명하는 [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable/properties/rectangle) 속성을 가지고 있습니다.

따라서 특정 지역에 위치한 테이블을 추출해야 할 경우, 특정 좌표와 함께 작업해야 합니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와도 함께 작동합니다.

다음 예제는 사각형 주석으로 표시된 테이블을 추출하는 방법을 보여줍니다:

```csharp
public static void Extract_Marked_Table()
{
    // 소스 PDF 문서 로드
    var filePath="<... 여기에 pdf 파일 경로 입력 ...>";
    Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(filePath);  
    var page = pdfDocument.Pages[1];
    var squareAnnotation =
        page.Annotations.FirstOrDefault(ann => ann.AnnotationType == Annotations.AnnotationType.Square)
        as Annotations.SquareAnnotation;


    Aspose.Pdf.Text.TableAbsorber absorber = new Aspose.Pdf.Text.TableAbsorber();
    absorber.Visit(page);

    foreach (AbsorbedTable table in absorber.TableList)
    {
        var isInRegion = (squareAnnotation.Rect.LLX < table.Rectangle.LLX) &&
        (squareAnnotation.Rect.LLY < table.Rectangle.LLY) &&
        (squareAnnotation.Rect.URX > table.Rectangle.URX) &&
        (squareAnnotation.Rect.URY > table.Rectangle.URY);

        if (isInRegion)
        {
            foreach (AbsorbedRow row in table.RowList)
            {
                foreach (AbsorbedCell cell in row.CellList)
                {

                    foreach (TextFragment fragment in cell.TextFragments)
                    {
                        var sb = new StringBuilder();
                        foreach (TextSegment seg in fragment.Segments)
                        {
                            sb.Append(seg.Text);
                        }
                        var text = sb.ToString();
                        Console.Write($"{text}|");
                    }
                }
                Console.WriteLine();
            }
        }
    }
}
```
## PDF에서 테이블 데이터 추출하고 CSV 파일에 저장하기

다음 예제는 테이블을 추출하여 CSV 파일로 저장하는 방법을 보여줍니다.
PDF를 엑셀 스프레드시트로 변환하는 방법은 [PDF를 엑셀로 변환하기](/pdf/net/convert-pdf-to-excel/) 문서를 참조하세요.

다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

```csharp
public static void Extract_Table_Save_CSV()
{
    // 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.

    // PDF 문서 로드
    Document pdfDocument = new Document(_dataDir + "input.pdf");

    // ExcelSave Option 객체 인스턴스화
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.CSV };

    // 출력을 XLS 형식으로 저장
    pdfDocument.Save("PDFToXLS_out.xlsx", excelSave);
}
```
