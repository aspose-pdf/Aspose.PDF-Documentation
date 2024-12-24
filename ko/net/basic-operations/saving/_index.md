---
title: PDF 문서 프로그래밍 방식으로 저장
linktitle: PDF 저장
type: docs
weight: 30
url: /ko/net/save-pdf-document/
description: C# Aspose.PDF for .NET PDF 라이브러리를 사용하여 PDF 파일을 저장하는 방법을 알아보세요. 파일 시스템, 스트림 및 웹 애플리케이션에 PDF 문서 저장하기.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

다음 코드 스니펫은 새로운 그래픽 [Aspose.Drawing](/pdf/ko/net/drawing/) 인터페이스에서도 작동합니다.

## 파일 시스템에 PDF 문서 저장

`Document` 클래스의 `Save` 메서드를 사용하여 생성하거나 조작한 PDF 문서를 파일 시스템에 저장할 수 있습니다.
형식 유형(옵션)을 제공하지 않으면 문서는 Aspose.PDF v.1.7 (*.pdf) 형식으로 저장됩니다.

```csharp
public static void SaveDocument()
{
    var originalFileName = Path.Combine(_dataDir, "SimpleResume.pdf");
    var modifiedFileName = Path.Combine(_dataDir, "SimpleResumeModified.pdf");

    var pdfDocument = new Aspose.Pdf.Document(originalFileName);
    // 일부 조작을 수행하다, 예를 들어 새로운 빈 페이지 추가
    pdfDocument.Pages.Add();
    pdfDocument.Save(modifiedFileName);
}
```
## 스트림에 PDF 문서 저장하기

생성하거나 조작한 PDF 문서를 스트림으로 저장할 수도 있습니다. 이는 `Save` 메서드의 오버로드를 사용하여 수행할 수 있습니다.

```csharp
public static void SaveDocumentStream()
{
    var originalFileName = Path.Combine(_dataDir, "SimpleResume.pdf");
    var modifiedFileName = Path.Combine(_dataDir, "SimpleResumeModified.pdf");

    var pdfDocument = new Aspose.Pdf.Document(originalFileName);
    // 일부 조작을 수행합니다, 예를 들어 새 빈 페이지 추가
    pdfDocument.Pages.Add();
    pdfDocument.Save(System.IO.File.OpenWrite(modifiedFileName));
}
```

## 웹 애플리케이션에서 PDF 문서 저장하기

웹 애플리케이션에서 문서를 저장하기 위해 위에서 제안한 방법들을 사용할 수 있습니다. 또한, `Document` 클래스는 [HttpResponse](https://docs.microsoft.com/en-us/dotnet/api/system.web.httpresponse?view=netframework-4.8) 클래스와 함께 사용하기 위해 `Save` 메서드를 오버로드합니다.

```csharp
var originalFileName = Path.Combine(_dataDir, "SimpleResume.pdf");
var pdfDocument = new Aspose.Pdf.Document(originalFileName);
// 일부 조작을 수행합니다, 예를 들어 새 빈 페이지 추가
pdfDocument.Pages.Add();
pdfDocument.Save(Response, originalFileName, ContentDisposition.Attachment, new PdfSaveOptions());
```
자세한 설명은 [Showcase](/pdf/ko/net/showcases/) 섹션을 참조하십시오.

## PDF/A 또는 PDF/X 형식 저장

PDF/A는 전자 문서의 보관 및 장기 보존을 위해 사용되는 휴대용 문서 형식(PDF)의 ISO 표준화 버전입니다.
PDF/A는 장기 보관에 적합하지 않은 기능을 금지하는 점에서 PDF와 다릅니다. 예를 들어, 글꼴 연결(글꼴 삽입과 대조적으로) 및 암호화가 그러합니다. PDF/A 뷰어에 대한 ISO 요구 사항에는 색상 관리 지침, 내장 글꼴 지원 및 내장 주석을 읽기 위한 사용자 인터페이스가 포함됩니다.

PDF/X는 PDF ISO 표준의 하위 집합입니다. PDF/X의 목적은 그래픽 교환을 용이하게 하는 것이며, 따라서 표준 PDF 파일에는 적용되지 않는 일련의 인쇄 관련 요구 사항이 있습니다.

두 경우 모두 `Save` 메소드를 사용하여 문서를 저장하며, 문서는 `Convert` 메소드를 사용하여 준비해야 합니다.

```csharp
public static void SaveDocumentAsPDFx()
{
    var pdfDocument = new Aspose.Pdf.Document("..\\..\\..\\Samples\\SimpleResume.pdf");
    pdfDocument.Pages.Add();
    pdfDocument.Convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
    pdfDocument.Save("..\\..\\..\\Samples\\SimpleResume_X3.pdf");
}
```

