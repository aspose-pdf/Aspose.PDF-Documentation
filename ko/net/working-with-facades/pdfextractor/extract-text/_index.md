---
title: PDF 파일에서 텍스트 추출
type: docs
weight: 30
url: ko/net/extract-text/
description: 이 섹션은 PdfExtractor 클래스를 사용하여 PDF에서 텍스트를 추출하는 방법을 설명합니다.
lastmod: "2021-06-05"
---

이 문서에서는 PDF 파일에서 텍스트를 추출하는 방법의 세부 사항을 살펴보겠습니다. 이러한 모든 추출 기능은 [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) 클래스에 한 곳에서 제공됩니다. 코드에서 이러한 기능을 사용하는 방법을 알아보겠습니다.

[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) 클래스는 세 가지 유형의 추출 기능을 제공합니다. 이 세 가지 범주는 텍스트, 이미지 및 첨부 파일입니다. 이러한 세 가지 범주 각각에서 추출을 수행하기 위해 PdfExtractor는 여러 메서드를 제공하며, 이들은 함께 작동하여 최종 출력을 제공합니다.

예를 들어, 텍스트를 추출하기 위해 세 가지 메서드를 사용할 수 있습니다. [ExtractText, GetText, HasNextPageText 및 GetNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/index). 이제 텍스트를 추출하기 시작하려면, 먼저 [ExtractText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extracttext/index) 메서드를 호출해야 합니다; 이는 PDF 파일에서 텍스트를 추출하고 메모리에 저장합니다. 그 후, [GetText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/gettext/index) 메서드는 이 추출된 텍스트를 디스크의 지정된 위치에 파일로 저장합니다. [HasNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextpagetext) 는 각 페이지를 반복하며 다음 페이지에 텍스트가 있는지 확인하는 데 도움을 줍니다. 텍스트가 포함되어 있으면 [GetNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getnextpagetext/index) 는 개별 페이지의 텍스트를 파일에 저장하는 데 도움을 줍니다.
문자 추출 모드를 추출하려면 다음 코드를 사용하십시오:

```csharp
public static void ExtractTextExtractonMode()
{
    bool WholeText = true;
    // PdfExtractor 클래스의 객체 생성
    PdfExtractor pdfExtractor = new PdfExtractor();

    // 입력 PDF 바인드
    pdfExtractor.BindPdf(_dataDir + "sample.pdf");

    // 텍스트 추출
    // pdfExtractor.ExtractTextMode = 0; //순수 모드
    pdfExtractor.ExtractTextMode = 1; //원시 모드
    pdfExtractor.ExtractText();


    if (!WholeText)
    {
        pdfExtractor.GetText(_dataDir + "sample.txt");
    }
    else
    {
        // 텍스트를 별도의 파일로 추출
        int pageNumber = 1;
        while (pdfExtractor.HasNextPageText())
        {
            pdfExtractor.GetNextPageText($"{_dataDir}\\sample{pageNumber:D3}.txt");
            pageNumber++;
        }
    }
}
```