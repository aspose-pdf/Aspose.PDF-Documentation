---
title: PDF를 EPUB, LaTeX, 텍스트, XPS로 변환하기
linktitle: PDF를 다른 형식으로 변환
type: docs
weight: 90
url: /net/convert-pdf-to-other-files/
lastmod: "2021-11-01"
keywords: 변환, PDF, EPUB, LaTeX, 텍스트, XPS, C#
description: 이 주제에서는 C# 또는 .NET을 사용하여 PDF 파일을 EPUB, LaTeX, 텍스트, XPS 등의 다른 파일 형식으로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## PDF를 EPUB로 변환

{{% alert color="success" %}}
**PDF를 EPUB로 온라인 변환 시도하기**

Aspose.PDF for .NET은 무료 온라인 애플리케이션 ["PDF를 EPUB로"](https://products.aspose.app/pdf/conversion/pdf-to-epub)를 제공하여 기능과 품질을 탐색해 볼 수 있습니다.

[![Aspose.PDF 무료 앱으로 PDF를 EPUB로 변환](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="전자 출판">EPUB</abbr>**은 국제 디지털 출판 포럼(IDPF)에서 제공하는 자유롭고 개방된 전자책 표준입니다.
**<abbr title="전자 출판">EPUB</abbr>**는 국제 디지털 출판 포럼(IDPF)에서 제공하는 무료이자 개방형 전자책 표준입니다.
EPUB은 재배치 가능한 콘텐츠를 위해 설계되었으며, 이는 EPUB 리더기가 특정 디스플레이 장치에 최적화된 텍스트를 제공할 수 있음을 의미합니다. EPUB은 고정 레이아웃 콘텐츠도 지원합니다. 이 포맷은 출판사와 변환소가 내부적으로 사용할 수 있는 단일 포맷으로 의도되었으며, 유통 및 판매를 위해서도 사용됩니다. 이는 오픈 이북 표준을 대체합니다.

다음 코드 스니펫 또한 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

Aspose.PDF for .NET은 PDF 문서를 EPUB 포맷으로 변환하는 기능도 지원합니다. Aspose.PDF for .NET에는 `EpubSaveOptions`라는 클래스가 있으며, 이는 [`Document.Save(..)`](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) 메소드의 두 번째 인자로 사용할 수 있어 EPUB 파일을 생성할 수 있습니다.
다음 C# 코드 스니펫을 사용해 보세요.

```csharp
// 완전한 예제와 데이터 파일을 보려면 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 방문하세요.
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// PDF 문서를 로드합니다.
Document pdfDocument = new Document(dataDir + "PDFToEPUB.pdf");
// Epub 저장 옵션을 인스턴스화합니다.
EpubSaveOptions options = new EpubSaveOptions();
// 컨텐츠의 레이아웃을 지정합니다.
options.ContentRecognitionMode = EpubSaveOptions.RecognitionMode.Flow;
// ePUB 문서를 저장합니다.
pdfDocument.Save(dataDir + "PDFToEPUB_out.epub", options);
```
## PDF를 LaTeX/TeX로 변환

**Aspose.PDF for .NET**는 PDF를 LaTeX/TeX로 변환하는 기능을 지원합니다.
LaTeX 파일 형식은 특수 마크업이 있는 텍스트 파일 형식이며, 고품질 조판을 위한 TeX 기반 문서 준비 시스템에서 사용됩니다.

{{% alert color="success" %}}
**온라인에서 PDF를 LaTeX/TeX로 변환해 보세요**

Aspose.PDF for .NET은 무료 온라인 애플리케이션 ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)을 제공합니다. 여기서 기능과 작동 품질을 탐색해 볼 수 있습니다.

[![Aspose.PDF Convertion PDF to LaTeX/TeX with Free App](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

PDF 파일을 TeX로 변환하려면 Aspose.PDF는 변환 과정 중 임시 이미지를 저장하기 위한 속성 OutDirectoryPath를 제공하는 [LaTeXSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/latexsaveoptions) 클래스를 가지고 있습니다.

다음 코드 스니펫은 C#을 사용하여 PDF 파일을 TEX 형식으로 변환하는 과정을 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Document 객체 생성
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "PDFToTeX.pdf");

// LaTex 저장 옵션 인스턴스 생성          
LaTeXSaveOptions saveOptions = new LaTeXSaveOptions();

// 출력 디렉토리 지정
string pathToOutputDirectory = dataDir;

// 저장 옵션 객체에 출력 디렉토리 경로 설정
saveOptions.OutDirectoryPath = pathToOutputDirectory;

// PDF 파일을 LaTex 형식으로 저장           
doc.Save(dataDir + "PDFToTeX_out.tex", saveOptions);
```
## PDF를 텍스트로 변환

**Aspose.PDF for .NET**은 전체 PDF 문서와 단일 페이지를 텍스트 파일로 변환하는 기능을 지원합니다.

### 전체 PDF 문서를 텍스트 파일로 변환하기

[TextAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textabsorber) 클래스의 [Visit](https://reference.aspose.com/pdf/net/aspose.pdf.text/textabsorber/methods/visit/index) 메소드를 사용하여 PDF 문서를 TXT 파일로 변환할 수 있습니다.

다음 코드 조각은 모든 페이지의 텍스트를 추출하는 방법을 설명합니다.

```csharp
public static void ConvertPDFDocToTXT()
{
    // 문서 열기
    Document pdfDocument = new Document(_dataDir + "demo.pdf");
    TextAbsorber ta = new TextAbsorber();
    ta.Visit(pdfDocument);
    // 추출된 텍스트를 텍스트 파일에 저장
    File.WriteAllText(_dataDir + "input_Text_Extracted_out.txt",ta.Text);
}
```

{{% alert color="success" %}}
**온라인으로 PDF를 텍스트로 변환해 보세요**

Aspose.PDF for .NET은 무료 온라인 애플리케이션 ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt)를 제공합니다. 여기에서 기능과 작동 품질을 탐색해 볼 수 있습니다.

Aspose.PDF for .NET은 온라인 무료 애플리케이션 ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt)를 제공합니다. 여기서 기능과 품질을 탐색해 볼 수 있습니다.

[![Aspose.PDF Convertion PDF to Text with Free App](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)

### PDF 페이지를 텍스트 파일로 변환

Aspose.PDF for .NET을 사용하여 PDF 문서를 TXT 파일로 변환할 수 있습니다. 이 작업을 해결하기 위해 `TextAbsorber` 클래스의 `Visit` 메소드를 사용해야 합니다.

다음 코드 조각은 특정 페이지에서 텍스트를 추출하는 방법을 설명합니다.

```csharp
public static void ConvertPDFPagestoTXT()
{
    Document pdfDocument = new Document(System.IO.Path.Combine(_dataDir, "demo.pdf"));
    TextAbsorber ta = new TextAbsorber();
    var pages = new [] {1, 3, 4};
    foreach (var page in pages)
    {
        ta.Visit(pdfDocument.Pages[page]);
    }
   
    // 추출된 텍스트를 텍스트 파일에 저장
    File.WriteAllText(System.IO.Path.Combine(_dataDir, "input_Text_Extracted_out.txt"), ta.Text);
}
```

## PDF를 XPS로 변환

**Aspose.PDF for .NET**은 PDF 파일을 <abbr title="XML Paper Specification">XPS</abbr> 형식으로 변환할 수 있는 기능을 제공합니다. C#을 사용하여 PDF 파일을 XPS 형식으로 변환하는 제시된 코드 스니펫을 사용해 보겠습니다.

{{% alert color="success" %}}
**온라인에서 PDF를 XPS로 변환해 보세요**

Aspose.PDF for .NET은 무료 온라인 애플리케이션 ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)를 제공합니다. 여기에서 기능성과 작동 품질을 직접 확인해 볼 수 있습니다.

[![Aspose.PDF Convertion PDF to XPS with Free App](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

XPS 파일 유형은 주로 마이크로소프트 코퍼레이션의 XML Paper Specification과 관련이 있습니다. XML Paper Specification (XPS), 이전 코드명은 Metro이며, Next Generation Print Path (NGPP) 마케팅 개념을 포함하는 것은, 문서 생성과 보기를 Windows 운영 체제에 통합하는 마이크로소프트의 이니셔티브입니다.

PDF 파일을 XPS로 변환하기 위해, Aspose.PDF는 XPS 파일을 생성하기 위해 [Document.Save(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) 메소드의 두 번째 인수로 사용되는 [XpsSaveOptions](https://reference.aspose.com/net/pdf/aspose.pdf/xpssaveoptions) 클래스를 가지고 있습니다.
PDF 파일을 XPS로 변환하기 위해, Aspose.PDF는 [XpsSaveOptions](https://reference.aspose.com/net/pdf/aspose.pdf/xpssaveoptions) 클래스를 사용하며, 이는 [Document.Save(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) 메소드의 두 번째 인자로 사용되어 XPS 파일을 생성합니다.

다음 코드 스니펫은 PDF 파일을 XPS 형식으로 변환하는 과정을 보여줍니다.

```csharp
// 완성된 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인할 수 있습니다.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// PDF 문서를 로드합니다.
Document pdfDocument = new Document(dataDir + "input.pdf");

// XPS 저장 옵션을 인스턴스화합니다.
Aspose.Pdf.XpsSaveOptions saveOptions = new Aspose.Pdf.XpsSaveOptions();
// XPS 문서를 저장합니다.
pdfDocument.Save("PDFToXPS_out.xps", saveOptions)
```
