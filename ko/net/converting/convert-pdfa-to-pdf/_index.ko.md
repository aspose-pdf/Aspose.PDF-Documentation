---
title: PDF/A를 PDF 형식으로 변환
linktitle: PDF/A를 PDF 형식으로 변환
type: docs
weight: 110
url: /net/convert-pdfa-to-pdf/
lastmod: "2021-11-01"
description: 이 주제에서는 Aspose.PDF를 사용하여 .NET 라이브러리로 PDF/A 파일을 PDF 문서로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리에서도 작동합니다.

## PDF/A 문서를 PDF로 변환

PDF/A 문서를 PDF로 변환한다는 것은 원본 문서에서 <abbr title="Portable Document Format Archive">PDF/A</abbr> 제한을 제거하는 것을 의미합니다.
[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스는 입력/원본 파일에서 PDF 준수 정보를 제거하는 [RemovePdfaCompliance(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/removepdfacompliance) 메소드를 가지고 있습니다.

```csharp
public static void ConvertPDFAtoPDF()
{
    // 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인할 수 있습니다.
    Document pdfDocument = new Document(_dataDir + "PDFAToPDF.pdf");
    // PDF/A 준수 정보 제거
    pdfDocument.RemovePdfaCompliance();
    // 업데이트된 문서 저장
    pdfDocument.Save(_dataDir + "PDFAToPDF_out.pdf");
}
```
이 정보는 문서에 변경이 발생할 때 제거됩니다(예: 페이지 추가). 다음 예에서는 페이지를 추가한 후 출력 문서가 PDF/A 준수를 잃어버립니다.

```csharp
public static void ConvertPDFAtoPDFAdvanced()
{
    // 완전한 예제와 데이터 파일을 보려면 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 을 방문하세요.
    Document pdfDocument = new Document(_dataDir + "PDFAToPDF.pdf");
    // 새로운 (빈) 페이지를 추가하면 PDF/A 준수 정보가 제거됩니다.
    pdfDocument.Pages.Add();
    // 업데이트된 문서를 저장합니다
    pdfDocument.Save(_dataDir + "PDFAToPDF_out.pdf");
}
```
