---
title: PDF를 PDF/A 형식으로 변환
linktitle: PDF를 PDF/A 형식으로 변환
type: docs
weight: 100
url: ko/net/convert-pdf-to-pdfa/
lastmod: "2021-11-01"
description: 이 주제에서는 Aspose.PDF를 사용하여 PDF 파일을 PDF/A 준수 PDF 파일로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for .NET**은 PDF 파일을 <abbr title="Portable Document Format / A">PDF/A</abbr> 준수 PDF 파일로 변환할 수 있습니다. 이 작업을 수행하기 전에 파일을 검증해야 합니다. 이 주제에서는 그 방법을 설명합니다.

{{% alert color="primary" %}}

PDF/A 준수를 검증하기 위해 Adobe Preflight를 따릅니다. 시장에 있는 모든 도구는 PDF/A 준수에 대한 자체적인 “표현”을 가지고 있습니다. 참고로 PDF/A 검증 도구에 관한 이 기사를 확인하세요. Aspose.PDF가 PDF 파일을 어떻게 생성하는지 검증하기 위해 Adobe 제품을 선택했습니다. Adobe는 PDF와 관련된 모든 것의 중심에 있기 때문입니다.

{{% /alert %}}

Document 클래스의 Convert 메소드를 사용하여 파일을 변환합니다.
{{% alert color="success" %}}
**온라인으로 PDF를 PDF/A로 변환해 보세요**

Aspose.PDF for .NET은 무료 온라인 애플리케이션 ["PDF를 PDF/A-1A로"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a) 제공합니다. 여기서 기능과 품질을 탐색해 볼 수 있습니다.

[![Aspose.PDF 변환 PDF를 PDF/A로 무료 앱으로](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 사용할 수 있습니다.

## PDF 파일을 PDF/A-1b로 변환

다음 코드 스니펫은 PDF 파일을 PDF/A-1b 준수 PDF로 변환하는 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리로의 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// 문서 열기
Document pdfDocument = new Document(dataDir + "PDFToPDFA.pdf");
           
// PDF/A 준수 문서로 변환
// 변환 과정 중 검증도 수행됩니다
pdfDocument.Convert(dataDir + "log.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

dataDir = dataDir + "PDFToPDFA_out.pdf";
// 출력 문서 저장
pdfDocument.Save(dataDir);
```
검증만 수행하려면 다음 코드 줄을 사용하세요:

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET에서 확인하세요.
// 문서 디렉터리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// 문서 열기
Document pdfDocument = new Document(dataDir + "ValidatePDFAStandard.pdf");

// PDF를 PDF/A-1a로 검증
pdfDocument.Validate(dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1B);
```

## PDF 파일을 PDF/A-3b로 변환

Aspose.PDF for .NET은 또한 PDF 파일을 PDF/A-3b 형식으로 변환하는 기능을 지원합니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET에서 확인하세요.
// 문서 디렉터리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// 문서 열기
Document pdfDocument = new Document(dataDir + "input.pdf");           

pdfDocument.Convert(new MemoryStream(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

dataDir = dataDir + "PDFToPDFA3b_out.pdf";
// 출력 문서 저장
pdfDocument.Save(dataDir);
```
## PDF 파일을 PDF/A-2u로 변환

Aspose.PDF for .NET은 PDF 파일을 PDF/A-2u 형식으로 변환하는 기능을 지원합니다.

```csharp
string inFile = "input.pdf";
string outFile = "output.pdf";
Aspose.PDF.Document doc = new Aspose.PDF.Document(inFile);
doc.Convert(new MemoryStream(), PdfFormat.PDF_A_2U, ConvertErrorAction.Delete);
doc.Save(outFile);
```

## PDF 파일을 PDF/A-3u로 변환

Aspose.PDF for .NET은 PDF 파일을 PDF/A-3u 형식으로 변환하는 기능을 지원합니다.

```csharp
string inFile = "input.pdf";
string outFile = "output.pdf";
Aspose.PDF.Document doc = new Aspose.PDF.Document(inFile);
doc.Convert(new MemoryStream(), PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);
doc.Save(outFile);
```

## PDF/A 파일에 첨부 파일 추가

PDF/A 준수 형식에 파일을 첨부할 필요가 있는 경우, Aspose.PDF.PdfFormat 열거형에서 PDF_A_3A 값을 사용하는 것이 좋습니다.
PDF/A_3a는 PDF/A 준수 파일에 모든 파일 형식을 첨부하는 기능을 제공하는 형식입니다.

```csharp

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하십시오.
// 문서 디렉토리로의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// 기존 파일을 로드하기 위해 Document 인스턴스를 인스턴스화합니다.
Aspose.Pdf.Document doc = new Document(dataDir + "input.pdf");
// 첨부파일로 추가할 새 파일을 설정합니다.
FileSpecification fileSpecification = new FileSpecification(dataDir + "aspose-logo.jpg", "대용량 이미지 파일");
// 문서의 첨부 파일 컬렉션에 첨부 파일을 추가합니다.
doc.EmbeddedFiles.Add(fileSpecification);
// 첨부 파일이 결과 파일에 포함되도록 PDF/A_3a로 변환을 수행합니다.
doc.Convert(dataDir + "log.txt", Aspose.Pdf.PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);
// 결과 파일을 저장합니다.
doc.Save(dataDir + "AddAttachmentToPDFA_out.pdf");
```

## 대체 글꼴로 누락된 글꼴 교체

PDFA 표준에 따르면, 글꼴은 PDFA 문서에 포함되어야 합니다.
PDFA 표준에 따르면, 폰트는 PDFA 문서에 포함되어야 합니다.

```csharp
// 완전한 예제와 데이터 파일을 보려면 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 로 이동하십시오.
// 문서 디렉토리로의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Aspose.Pdf.Text.Font originalFont = null;
try
{
    originalFont = FontRepository.FindFont("AgencyFB");
}
catch (Exception)
{
    // 목적지 기계에 폰트가 없습니다
    FontRepository.Substitutions.Add(new SimpleFontSubstitution("AgencyFB", "Arial"));
}
var fileNew = new FileInfo(dataDir + "newfile_out.pdf");
var pdf = new Document(dataDir + "input.pdf");
pdf.Convert( dataDir +  "log.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);
pdf.Save(fileNew.FullName);
```
