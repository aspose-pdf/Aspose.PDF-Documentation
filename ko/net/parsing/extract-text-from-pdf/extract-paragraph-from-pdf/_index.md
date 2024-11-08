---
title: PDF에서 단락 추출 C#
linktitle: PDF에서 단락 추출
type: docs
weight: 20
url: /ko/net/extract-paragraph-from-pdf/
description: 이 글은 Aspose.PDF의 ParagraphAbsorber - 특별 도구를 사용하여 PDF 문서에서 텍스트를 추출하는 방법에 대해 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 문서에서 단락 형태로 텍스트 추출

특정 텍스트를 검색하여(“일반 텍스트” 또는 “정규 표현식” 사용) 한 페이지 또는 전체 문서에서 텍스트를 가져오거나, 단일 페이지, 페이지 범위 또는 전체 문서의 전체 텍스트를 가져올 수 있습니다.
PDF 문서에서 텍스트를 가져오는 방법은 단일 페이지나 전체 문서에서 특정 텍스트를 검색(일반 텍스트나 정규 표현식 사용)하거나 단일 페이지, 페이지 범위 또는 전체 문서의 전체 텍스트를 가져오는 것입니다.

**1- PDF 페이지의 섹션과 문단 테두리 그리기:**

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하십시오.
private static void ExtractParagraph()
{
    // 문서 디렉토리 경로.
    string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    Document doc = new Document(dataDir + "input.pdf");
    Page page = doc.Pages[2];

    ParagraphAbsorber absorber = new ParagraphAbsorber();
    absorber.Visit(page);

    PageMarkup markup = absorber.PageMarkups[0];

    foreach (MarkupSection section in markup.Sections)
    {
        DrawRectangleOnPage(section.Rectangle, page);
        foreach (MarkupParagraph paragraph in section.Paragraphs)
        {
            DrawPolygonOnPage(paragraph.Points, page);
        }
    }

    doc.Save(dataDir + "output_out.pdf");
}

private static void DrawRectangleOnPage(Rectangle rectangle, Page page)
{
    page.Contents.Add(new Aspose.Pdf.Operators.GSave());
    page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 0, 0));
    page.Contents.Add(new Aspose.Pdf.Operators.SetRGBColorStroke(0, 1, 0));
    page.Contents.Add(new Aspose.Pdf.Operators.SetLineWidth(2));
    page.Contents.Add(
        new Aspose.Pdf.Operators.Re(rectangle.LLX,
            rectangle.LLY,
            rectangle.Width,
            rectangle.Height));
    page.Contents.Add(new Aspose.Pdf.Operators.ClosePathStroke());
    page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
}

private static void DrawPolygonOnPage(Point[] polygon, Page page)
{
    page.Contents.Add(new Aspose.Pdf.Operators.GSave());
    page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 0, 0));
    page.Contents.Add(new Aspose.Pdf.Operators.SetRGBColorStroke(0, 0, 1));
    page.Contents.Add(new Aspose.Pdf.Operators.SetLineWidth(1));
    page.Contents.Add(new Aspose.Pdf.Operators.MoveTo(polygon[0].X, polygon[0].Y));
    for (int i = 1; i < polygon.Length; i++)
    {
        page.Contents.Add(new Aspose.Pdf.Operators.LineTo(polygon[i].X, polygon[i].Y));
    }
    page.Contents.Add(new Aspose.Pdf.Operators.LineTo(polygon[0].X, polygon[0].Y));
    page.Contents.Add(new Aspose.Pdf.Operators.ClosePathStroke());
    page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
}
```
**2- 단락 컬렉션을 반복하여 텍스트를 가져옵니다:**

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리에서도 작동합니다.

```csharp
// 전체 예시와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해주세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 기존 PDF 파일을 엽니다
Document doc = new Document(dataDir + "input.pdf");
// ParagraphAbsorber 인스턴스를 생성합니다
ParagraphAbsorber absorber = new ParagraphAbsorber();
absorber.Visit(doc);

foreach (PageMarkup markup in absorber.PageMarkups)
{
    int i = 1;
    foreach (MarkupSection section in markup.Sections)
    {
        int j = 1;

        foreach (MarkupParagraph paragraph in section.Paragraphs)
        {
            StringBuilder paragraphText = new StringBuilder();

            foreach (List<TextFragment> line in paragraph.Lines)
            {
                foreach (TextFragment fragment in line)
                {
                    paragraphText.Append(fragment.Text);
                }
                paragraphText.Append("\r\n");
            }
            paragraphText.Append("\r\n");

            Console.WriteLine("페이지 {2}의 섹션 {1}의 단락 {0}:", j, i, markup.Number);
            Console.WriteLine(paragraphText.ToString());

            j++;
        }
        i++;
    }
}
```

