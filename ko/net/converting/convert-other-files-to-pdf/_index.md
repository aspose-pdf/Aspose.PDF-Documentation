---
title: 다른 파일 형식을 PDF로 변환하기 (.NET)
linktitle: 다른 파일 형식을 PDF로 변환하기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /ko/net/convert-other-files-to-pdf/
lastmod: "2021-11-01"
description: 이 주제에서는 Aspose.PDF를 사용하여 EPUB, MD, PCL, XPS, PS, XML 및 LaTeX와 같은 다른 파일 형식을 PDF 문서로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert other file formats to PDF in .NET",
    "alternativeHeadline": "Convert Multiple File Formats to PDF in C#",
    "abstract": "Aspose.PDF for .NET은 사용자가 EPUB, Markdown, PCL, XPS, PS, XML 및 LaTeX를 포함한 다양한 파일 형식을 고품질 PDF 문서로 원활하게 변환할 수 있는 다재다능한 기능을 소개합니다. 이 기능은 다양한 플랫폼에서 호환성과 접근성을 보장하면서 원본 콘텐츠의 무결성을 유지하여 문서 관리를 향상시킵니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "4039",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/convert-other-files-to-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-other-files-to-pdf/"
    },
    "dateModified": "2025-04-04",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

## 개요

이 문서에서는 **C#을 사용하여 다양한 다른 유형의 파일 형식을 PDF로 변환하는 방법**을 설명합니다. 다음 주제를 다룹니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

- [EPUB을 PDF로 변환하기](#csharp-convert-epub-to-pdf)
- [Markdown을 PDF로 변환하기](#csharp-convert-markdown-to-pdf)
- [PCL을 PDF로 변환하기](#csharp-convert-pcl-to-pdf)
- [텍스트를 PDF로 변환하기](#csharp-convert-text-to-pdf)
- [사전 형식화된 텍스트를 PDF로 변환하기](#csharp-convert-pre-formatted-text-to-pdf)
- [XPS를 PDF로 변환하기](#csharp-convert-xps-to-pdf)
- [PostScript를 PDF로 변환하기](#csharp-convert-ps-to-pdf)
- [XML을 PDF로 변환하기](#csharp-convert-xml-to-pdf)
- [XLS-FO를 PDF로 변환하기](#csharp-convert-xlsfo-to-pdf)
- [LaTeX/TeX를 PDF로 변환하기](#csharp-convert-latex-to-pdf)
- [OFD를 PDF로 변환하기](#csharp-convert-ofd-to-pdf)

## EPUB을 PDF로 변환하기

**Aspose.PDF for .NET**은 EPUB 파일을 PDF 형식으로 간단하게 변환할 수 있도록 합니다.

<abbr title="전자 출판">EPUB</abbr> (전자 출판의 약자)은 국제 디지털 출판 포럼(IDPF)에서 제공하는 무료 및 개방형 전자책 표준입니다. 파일 확장자는 .epub입니다. EPUB는 재흐름 가능한 콘텐츠를 위해 설계되었으며, 이는 EPUB 리더가 특정 디스플레이 장치에 맞게 텍스트를 최적화할 수 있음을 의미합니다.

EPUB는 고정 레이아웃 콘텐츠도 지원합니다. 이 형식은 출판사와 변환 회사가 내부적으로 사용할 수 있는 단일 형식으로 설계되었으며, 배포 및 판매에도 사용됩니다. 이는 Open eBook 표준을 대체합니다. EPUB 3 버전은 표준화된 모범 사례, 연구, 정보 및 이벤트를 위한 주요 서적 무역 협회인 서적 산업 연구 그룹(BISG)에서 승인되었습니다.

{{% alert color="success" %}}
**EPUB을 PDF로 온라인 변환해 보세요**

Aspose.PDF for .NET은 온라인 무료 애플리케이션 ["EPUB to PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf)를 제공하여 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF EPUB을 PDF로 변환하는 무료 앱](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

<a name="csharp-convert-epub-to-pdf" id="csharp-convert-epub-to-pdf"><strong>EPUB을 PDF로 변환하기</strong></a>

1. [EpubLoadOptions](https://reference.aspose.com/pdf/ko/net/aspose.pdf/epubloadoptions) 클래스의 인스턴스를 생성합니다.
2. 소스 파일 이름과 옵션을 언급하여 [Document](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document) 클래스의 인스턴스를 생성합니다.
3. 원하는 파일 이름으로 문서를 저장합니다.

다음 코드 스니펫은 C#을 사용하여 EPUB 파일을 PDF 형식으로 변환하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertEPUBtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options
    var options = new Aspose.Pdf.EpubLoadOptions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "EPUBToPDF.epub", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertEPUBtoPDF_out.pdf");
    }
}
```

변환을 위해 페이지 크기를 설정할 수도 있습니다. 새 페이지 크기를 정의하려면 `SizeF` 객체를 사용하고 이를 [EpubLoadOptions](https://reference.aspose.com/pdf/ko/net/aspose.pdf/epubloadoptions/constructors/main) 생성자에 전달합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertEPUBtoPDFAdv()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options
    var options = new Aspose.Pdf.EpubLoadOptions(new SizeF(1190, 1684));

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "EPUBToPDF.epub", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertEPUBtoPDFAdv_out.pdf");
    }
}
```

## Markdown을 PDF로 변환하기

**이 기능은 버전 19.6 이상에서 지원됩니다.**

{{% alert color="success" %}}
**Markdown을 PDF로 온라인 변환해 보세요**

Aspose.PDF for .NET은 온라인 무료 애플리케이션 ["Markdown to PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf)를 제공하여 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF Markdown을 PDF로 변환하는 무료 앱](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Aspose.PDF for .NET은 입력 [Markdown](https://daringfireball.net/projects/markdown/syntax) 데이터 파일을 기반으로 PDF 문서를 생성하는 기능을 제공합니다. Markdown을 PDF로 변환하려면 [MdLoadOptions](https://reference.aspose.com/pdf/ko/net/aspose.pdf/mdloadoptions)를 사용하여 [Document](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document)를 초기화해야 합니다.

다음 코드 스니펫은 Aspose.PDF 라이브러리와 함께 이 기능을 사용하는 방법을 보여줍니다:

<a name="csharp-convert-markdown-to-pdf" id="csharp-convert-markdown-to-pdf"><strong>Markdown을 PDF로 변환하기</strong></a>

1. [MdLoadOptions](https://reference.aspose.com/pdf/ko/net/aspose.pdf/mdloadoptions/) 클래스의 인스턴스를 생성합니다.
2. 소스 파일 이름과 옵션을 언급하여 [Document](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document) 클래스의 인스턴스를 생성합니다.
3. 원하는 파일 이름으로 문서를 저장합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertMarkdownToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options
    var options = new Aspose.Pdf.MdLoadOptions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.md", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertMarkdownToPDF_out.pdf");
    }
}
```

## PCL을 PDF로 변환하기

<abbr title="프린터 명령어 언어">PCL</abbr> (Printer Command Language)은 표준 프린터 기능에 접근하기 위해 개발된 Hewlett-Packard 프린터 언어입니다. PCL 레벨 1부터 5e/5c까지는 제어 시퀀스를 사용하는 명령 기반 언어로, 수신된 순서대로 처리되고 해석됩니다. 소비자 수준에서 PCL 데이터 스트림은 인쇄 드라이버에 의해 생성됩니다. PCL 출력은 사용자 정의 애플리케이션에 의해 쉽게 생성될 수 있습니다.

{{% alert color="success" %}}
**PCL을 PDF로 온라인 변환해 보세요**

Aspose.PDF for .NET은 온라인 무료 애플리케이션 ["PCL to PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf)를 제공하여 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF PCL을 PDF로 변환하는 무료 앱](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

**현재 PCL5 및 이전 버전만 지원됩니다.**

<table>
    <thead>
        <tr>
            <th>
                명령 세트
            </th>
            <th>
                지원
            </th>
            <th>
                예외
            </th>
            <th>
                설명
            </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                작업 제어 명령
            </td>
            <td>
                +
            </td>
            <td>
                양면 인쇄 모드
            </td>
            <td>
                인쇄 프로세스 제어: 복사 수, 출력 빈, 단면/양면 인쇄, 왼쪽 및 위쪽 오프셋 등.
            </td>
        </tr>
        <tr>
            <td>
                페이지 제어 명령
            </td>
            <td>
                +
            </td>
            <td>
                천공 건너뛰기 명령
            </td>
            <td>
                페이지 크기, 여백, 페이지 방향, 줄 간격, 문자 간격 등을 지정합니다.
            </td>
        </tr>
        <tr>
            <td>
                커서 위치 지정 명령
            </td>
            <td>
                +
            </td>
            <td>
                &nbsp;
            </td>
            <td>
                커서 위치 및 텍스트, 래스터 또는 벡터 이미지의 원점을 지정합니다.
            </td>
        </tr>
        <tr>
            <td>
                글꼴 선택 명령
            </td>
            <td>
                +
            </td>
            <td>
                <ol>
                    <li>투명 인쇄 데이터 명령.</li>
                    <li>내장 소프트 글꼴. 현재 버전에서는 소프트 글꼴을 생성하는 대신, 라이브러리는 대상 머신에 설치된 기존 "하드" TrueType 글꼴 중 적합한 글꼴을 선택합니다. <br/>
                        적합성은 너비/높이 비율로 정의됩니다.<br/>
                        이 기능은 비트맵 및 TrueType 글꼴에만 작동하며, 소프트 글꼴로 인쇄된 텍스트가 소스 파일의 텍스트와 일치할 것이라는 보장은 없습니다.<br/>
                        소프트 글꼴의 문자 코드가 기본 코드와 일치하지 않을 수 있습니다.
                    </li>
                    <li>사용자 정의 기호 세트.</li>
                </ol>
            </td>
            <td>
                PCL 파일에서 소프트(내장) 글꼴을 로드하고 메모리에서 관리할 수 있습니다.
            </td>
        </tr>
        <tr>
            <td>
                래스터 그래픽 명령
            </td>
            <td>
                +
            </td>
            <td>
                흑백만 지원
            </td>
            <td>
                PCL 파일에서 래스터 이미지를 메모리로 로드하고 래스터 매개변수를 지정할 수 있습니다. <br
                    > 예: 너비, 높이, 압축 유형, 해상도 등.
            </td>
        </tr>
        <tr>
            <td>
                색상 명령
            </td>
            <td>
                +
            </td>
            <td>
                &nbsp;
            </td>
            <td>
                모든 인쇄 가능한 객체에 색상을 지정할 수 있습니다.
            </td>
        </tr>
        <tr>
            <td>
                인쇄 모델 명령
            </td>
            <td>
                +
            </td>
            <td>
                &nbsp;
            </td>
            <td>
                텍스트, 래스터 이미지 및 사각형 영역을 래스터 미리 정의된 패턴 및 <br>
                사용자 정의 패턴으로 채울 수 있으며 패턴 및 소스 래스터 이미지의 투명도 모드를 지정할 수 있습니다. <br> 미리 정의된 패턴은 해칭, 교차 해칭 및 음영입니다.
            </td>
        </tr>
        <tr>
            <td>
                사각형 영역 채우기 명령
            </td>
            <td>
                +
            </td>
            <td>
                &nbsp;
            </td>
            <td>
                패턴으로 사각형 영역을 생성하고 채울 수 있습니다.
            </td>
        </tr>
        <tr>
            <td>
                HP-GL/2 벡터 그래픽 명령
            </td>
            <td>
                +
            </td>
            <td>
                스크린 벡터 명령(SV), 투명도 모드 명령(TR), 투명 데이터 명령(TD), RO
                (좌표계 회전), 확장 가능 또는 비트맵 글꼴 명령(SB), 문자 기울기 명령(SL) 및
                여유 공간(ES)은 구현되지 않았으며 DV(변수 텍스트 경로 정의) 명령은 베타 버전에서 구현되었습니다.
            </td>
            <td>
                PCL 파일에서 HP-GL/2 벡터 이미지를 메모리로 로드할 수 있습니다. 벡터 이미지는 인쇄 가능한 영역의 왼쪽 하단 모서리에 원점이 있으며, 크기를 조정하고, 변환하고, 회전하고, 클리핑할 수 있습니다. <br>
                벡터 이미지는 텍스트(레이블) 및 사각형, 원, 타원, 선, 호, 베지어 곡선 및 단순 도형으로 구성된 복잡한 도형과 같은 기하학적 도형을 포함할 수 있습니다. <br> 레이블의 닫힌 도형은 단색 채우기 또는 벡터 패턴으로 채울 수 있습니다. <br> 패턴은 해칭, 교차 해칭, 음영, 사용자 정의된 래스터, PCL 해칭 또는 교차 해칭 및 PCL 사용자 정의로 사용할 수 있습니다. PCL 패턴은 래스터입니다. 레이블은 개별적으로 회전, 크기 조정 및 네 방향(위, 아래, 왼쪽 및 오른쪽)으로 방향을 지정할 수 있습니다. 왼쪽 및 오른쪽 방향은 글자를 차례로 배열합니다. 위쪽 및 아래쪽 방향은 글자를 위아래로 배열합니다.
            </td>
        </tr>
        <tr>
            <td>
                매크로
            </td>
            <td>
                ―
            </td>
            <td>
                &nbsp;
            </td>
            <td>
                PCL 명령의 시퀀스를 메모리로 로드하고 이 시퀀스를 여러 번 사용할 수 있습니다. 예를 들어 페이지 헤더를 인쇄하거나 여러 페이지에 대해 하나의 형식을 설정하는 데 사용할 수 있습니다.
            </td>
        </tr>
        <tr>
            <td>
                유니코드 텍스트
            </td>
            <td>
                ―
            </td>
            <td>
                &nbsp;
            </td>
            <td>
                비 ASCII 문자를 인쇄할 수 있습니다. 유니코드 텍스트가 포함된 샘플 파일이 부족하여 구현되지 않았습니다.
            </td>
        </tr>
        <tr>
            <td>
                PCL6 (PCL-XL)
            </td>
            <td>
                &nbsp;
            </td>
            <td>
                테스트 파일 부족으로 인해 베타 버전에서만 구현되었습니다. 내장 글꼴도 지원되지 않습니다.<br> JetReady 확장은 JetReady 사양이 없기 때문에 지원되지 않습니다.
            </td>
            <td>
                이진 파일 형식입니다.
            </td>
        </tr>
    </tbody>
</table>

### PCL 파일을 PDF 형식으로 변환하기

PCL에서 PDF로의 변환을 허용하기 위해 Aspose.PDF는 [`PclLoadOptions`](https://reference.aspose.com/pdf/ko/net/aspose.pdf/pclloadoptions) 클래스를 제공하여 LoadOptions 객체를 초기화하는 데 사용됩니다. 이후 이 객체는 Document 객체 초기화 시 인수로 전달되어 PDF 렌더링 엔진이 소스 문서의 입력 형식을 결정하는 데 도움을 줍니다.

다음 코드 스니펫은 PCL 파일을 PDF 형식으로 변환하는 과정을 보여줍니다.

<a name="csharp-convert-pcl-to-pdf" id="csharp-convert-pcl-to-pdf"><strong>PCL을 PDF로 변환하기</strong></a>

1. [PclLoadOptions](https://reference.aspose.com/pdf/ko/net/aspose.pdf/pclloadoptions/) 클래스의 인스턴스를 생성합니다.
2. 소스 파일 이름과 옵션을 언급하여 [Document](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document/) 클래스의 인스턴스를 생성합니다.
3. 원하는 파일 이름으로 문서를 저장합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPCLtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options
    var options = new Aspose.Pdf.PclLoadOptions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ConvertPCLtoPDF.pcl", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertPCLtoPDF_out.pdf");
    }
}
```

변환 과정에서 오류 감지를 모니터링할 수도 있습니다. 이를 위해 PclLoadOptions 객체를 구성해야 합니다: SupressErrors를 설정하거나 해제합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPCLtoPDFAdvanced()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options
    var options = new Aspose.Pdf.PclLoadOptions { SupressErrors = true };

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ConvertPCLtoPDFAdvanced.pcl", options))
    {
        if (options.Exceptions != null)
        {
            foreach (var ex in options.Exceptions)
            {
                Console.WriteLine(ex.Message);
            }
        }
        // Save PDF document
        document.Save(dataDir + "ConvertPCLtoPDFAdvanced_out.pdf");
    }
}
```

### 알려진 문제

1. 텍스트 문자열 및 이미지의 원점이 소스 PCL 파일의 원점과 약간 다를 수 있습니다. 인쇄 방향이 0°가 아닐 경우 동일하게 적용됩니다. 벡터 이미지의 경우 벡터 플롯의 좌표계가 회전된 경우(RO 명령이 선행됨)에도 동일합니다.
2. 벡터 이미지의 레이블 원점이 소스 PCL 파일의 원점과 다를 수 있습니다. 레이블이 명령 시퀀스의 영향을 받을 경우: 레이블 원점(LO), 변수 텍스트 경로 정의(DV), 절대 방향(DI) 또는 상대 방향(DR).
3. 텍스트는 비트맵 또는 TrueType 소프트(내장) 글꼴로 렌더링해야 할 경우 잘못 읽힐 수 있습니다. 현재 이러한 글꼴은 부분적으로만 지원됩니다(지원되는 기능 표의 예외 참조). 이 경우 소프트 글꼴의 문자 코드가 기본 코드와 일치하는 경우에만 텍스트가 올바르게 읽힐 수 있습니다. 읽은 텍스트의 스타일도 소스 PCL 파일의 스타일과 다를 수 있습니다. 소프트 글꼴 헤더에서 스타일을 설정할 필요가 없습니다.
4. 구문 분석된 PCL 파일에 Intellifont 또는 Universal 소프트 글꼴이 포함되어 있는 경우 예외가 발생합니다. Intellifont 및 Universal 글꼴은 전혀 지원되지 않습니다.
5. 구문 분석된 PCL 파일에 매크로 명령이 포함되어 있는 경우 구문 분석 결과가 소스 파일과 크게 다를 수 있습니다. 매크로 명령은 지원되지 않습니다.

## 텍스트를 PDF로 변환하기

**Aspose.PDF for .NET**은 일반 텍스트 및 사전 형식화된 텍스트 파일을 PDF 형식으로 변환하는 기능을 지원합니다.

텍스트를 PDF로 변환하는 것은 PDF 페이지에 텍스트 조각을 추가하는 것을 의미합니다. 텍스트 파일의 경우, 우리는 두 가지 유형의 텍스트를 다루고 있습니다: 사전 형식화된 텍스트(예: 25줄에 80자)와 비형식 텍스트(일반 텍스트). 우리의 필요에 따라 이 추가를 스스로 제어하거나 라이브러리의 알고리즘에 맡길 수 있습니다.

{{% alert color="success" %}}
**TEXT를 PDF로 온라인 변환해 보세요**

Aspose.PDF for .NET은 온라인 무료 애플리케이션 ["Text to PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf)를 제공하여 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF TEXT를 PDF로 변환하는 무료 앱](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

### 일반 텍스트 파일을 PDF로 변환하기

일반 텍스트 파일의 경우, 다음 기술을 사용할 수 있습니다:

<a name="csharp-convert-text-to-pdf" id="csharp-convert-text-to-pdf"><strong>텍스트를 PDF로 변환하기</strong></a>

1. _TextReader_를 사용하여 전체 텍스트를 읽습니다.
2. [Document](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document/) 객체를 인스턴스화하고 페이지 컬렉션에 새 페이지를 추가합니다.
3. [TextFragment](https://reference.aspose.com/pdf/ko/net/aspose.pdf.text/textfragment/)의 새 객체를 생성하고 _TextReader_ 객체를 생성자에 전달합니다.
4. _TextFragment_ 객체를 _Paragraphs_ 컬렉션의 단락으로 추가합니다. 텍스트 양이 페이지를 초과하면 라이브러리 알고리즘이 자동으로 추가 페이지를 추가합니다.
5. [Document](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document/) 클래스의 **Save** 메서드를 사용합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPlainTextFileToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Read the source text file
    using (var streamReader = new StreamReader(dataDir + "TextToPDFInput.txt"))
    {
        // // Create PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            var page = document.Pages.Add();
            // Create an instance of TextFragment and pass the text from reader object to its constructor as argument
            var text = new Aspose.Pdf.Text.TextFragment(streamReader.ReadToEnd());
            // Add a new text paragraph in paragraphs collection and pass the TextFragment object
            page.Paragraphs.Add(text);
            // Save PDF document
            document.Save(dataDir + "TextToPDF_out.pdf");
        }
    }
}
```

### 사전 형식화된 텍스트 파일을 PDF로 변환하기

사전 형식화된 텍스트를 변환하는 것은 일반 텍스트와 비슷하지만 여백, 글꼴 유형 및 크기와 같은 추가 작업을 수행해야 합니다. 글꼴은 모노스페이스여야 합니다(예: Courier New).

C#을 사용하여 사전 형식화된 텍스트를 PDF로 변환하려면 다음 단계를 따르십시오:

<a name="csharp-convert-pre-formatted-text-to-pdf" id="csharp-convert-pre-formatted-text-to-pdf"><strong>사전 형식화된 TXT를 PDF로 변환하기</strong></a>

1. 전체 텍스트를 문자열 배열로 읽습니다.
2. [Document](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document/) 객체를 인스턴스화하고 [Pages](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document/pages/) 컬렉션에 새 페이지를 추가합니다.
3. 문자열 배열을 반복하여 각 문자열을 [Paragraphs](https://reference.aspose.com/pdf/ko/net/aspose.pdf/paragraphs/) 컬렉션의 단락으로 추가합니다.

이 경우 라이브러리의 알고리즘도 추가 페이지를 추가하지만, 우리는 이 과정을 스스로 제어할 수 있습니다. 다음 예제는 사전 형식화된 텍스트 파일을 A4 페이지 크기로 PDF 문서로 변환하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPreFormattedTextToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Read the text file as array of string
    var lines = File.ReadAllLines(dataDir + "ConvertPreFormattedTextToPdf.txt");

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Set left and right margins for better presentation
        page.PageInfo.Margin.Left = 20;
        page.PageInfo.Margin.Right = 10;
        page.PageInfo.DefaultTextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Courier New");
        page.PageInfo.DefaultTextState.FontSize = 12;

        foreach (var line in lines)
        {
            // check if line contains "form feed" character
            // see https://en.wikipedia.org/wiki/Page_break
            if (line.StartsWith("\x0c"))
            {
                page = document.Pages.Add();
                page.PageInfo.Margin.Left = 20;
                page.PageInfo.Margin.Right = 10;
                page.PageInfo.DefaultTextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Courier New");
                page.PageInfo.DefaultTextState.FontSize = 12;
            }
            else
            {
                // Create an instance of TextFragment and pass the line to its constructor as argument
                var text = new Aspose.Pdf.Text.TextFragment(line);
                // Add a new text paragraph in paragraphs collection and pass the TextFragment object
                page.Paragraphs.Add(text);
            }
        }
        // Save PDF document
        document.Save(dataDir + "PreFormattedTextToPDF_out.pdf");
    }
}
```

## XPS를 PDF로 변환하기

**Aspose.PDF for .NET**은 <abbr title="XML Paper Specification">XPS</abbr> 파일을 PDF 형식으로 변환하는 기능을 지원합니다. 이 기사를 확인하여 작업을 해결하십시오.

XPS 파일 형식은 주로 Microsoft Corporation의 XML Paper Specification과 관련이 있습니다. XML Paper Specification(XPS)은 이전에 Metro라는 코드명을 가지고 있었으며, 차세대 인쇄 경로(NGPP) 마케팅 개념을 포함하고 있으며, Microsoft의 문서 생성 및 보기 통합을 위한 이니셔티브입니다.

{{% alert color="primary" %}}

파일 형식은 기본적으로 배포 및 저장을 위해 사용되는 압축된 XML 파일입니다. 편집하기 매우 어렵고 주로 Microsoft에서 구현됩니다.

{{% /alert %}}

XPS를 PDF로 변환하기 위해 Aspose.PDF for .NET은 [XpsLoadOption](https://reference.aspose.com/pdf/ko/net/aspose.pdf/xpsloadoptions)이라는 클래스를 도입하여 [LoadOptions](https://reference.aspose.com/pdf/ko/net/aspose.pdf/loadoptions) 객체를 초기화하는 데 사용됩니다. 이후 이 객체는 Document 객체 초기화 시 인수로 전달되어 PDF 렌더링 엔진이 소스 문서의 입력 형식을 결정하는 데 도움을 줍니다.

{{% alert color="primary" %}}

XP 및 Windows 7에서는 제어판에서 프린터를 찾아보면 미리 설치된 XPS 프린터를 찾을 수 있습니다. 이러한 파일을 생성하려면 해당 프린터를 출력 장치로 사용할 수 있습니다. Windows 7에서는 파일을 두 번 클릭하여 XPS 뷰어에서 열 수 있습니다. Microsoft 웹사이트에서 XPS 뷰어를 다운로드할 수도 있습니다.

{{% /alert %}}

다음 코드 스니펫은 C#을 사용하여 XPS 파일을 PDF 형식으로 변환하는 과정을 보여줍니다.

<a name="csharp-convert-xps-to-pdf" id="csharp-convert-xps-to-pdf"><strong>XPS를 PDF로 변환하기</strong></a>

1. [XpsLoadOptions](https://reference.aspose.com/pdf/ko/net/aspose.pdf/xpsloadoptions/) 클래스의 인스턴스를 생성합니다.
2. 소스 파일 이름과 옵션을 언급하여 [Document](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document/) 클래스의 인스턴스를 생성합니다.
3. 원하는 파일 이름으로 PDF 형식으로 문서를 저장합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertXPSToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Instantiate Options object
    var options = new Aspose.Pdf.XpsLoadOptions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "XPSToPDF.xps", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertXPSToPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**XPS 형식을 PDF로 온라인 변환해 보세요**

Aspose.PDF for .NET은 온라인 무료 애플리케이션 ["XPS to PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/)를 제공하여 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF XPS를 PDF로 변환하는 무료 앱](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## PostScript를 PDF로 변환하기

<a name="csharp-convert-ps-to-pdf" id="csharp-convert-ps-to-pdf"><strong>PostScript를 PDF로 변환하기</strong></a>

**Aspose.PDF for .NET**은 PostScript 파일을 PDF 형식으로 변환하는 기능을 지원합니다. Aspose.PDF의 기능 중 하나는 변환 중에 사용할 글꼴 폴더 세트를 설정할 수 있다는 것입니다.

PostScript 파일을 PDF 형식으로 변환하기 위해 Aspose.PDF for .NET은 LoadOptions 객체를 초기화하는 데 사용되는 [PsLoadOptions](https://reference.aspose.com/pdf/ko/net/aspose.pdf/psloadoptions) 클래스를 제공합니다. 이후 이 객체는 Document 객체 생성자에 인수로 전달되어 PDF 렌더링 엔진이 소스 문서의 형식을 결정하는 데 도움을 줍니다.

다음 코드 스니펫은 Aspose.PDF for .NET을 사용하여 PostScript 파일을 PDF 형식으로 변환하는 데 사용할 수 있습니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPostScriptToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options
    var options = new PsLoadOptions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ConvertPostscriptInput.ps", options))
    {
        // Save PDF document
        document.Save(dataDir + "PSToPDF_out.pdf");
    }
}
```

또한 변환 중에 사용할 글꼴 폴더 세트를 설정할 수 있습니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPostscriptToPDFAdvanced()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options with custom font folders
    var options = new Aspose.Pdf.PsLoadOptions
    {
        FontsFolders = new[] { dataDir + @"\fonts1", dataDir + @"\fonts2" }
    };

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ConvertPostscriptInput.ps", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertPostscriptToPDFAdvanced_out.pdf");
    }
}
```

## XML을 PDF로 변환하기

<a name="csharp-convert-xml-to-pdf" id="csharp-convert-xml-to-pdf"><strong>XML을 PDF로 변환하기</strong></a>

XML 형식은 구조화된 데이터를 저장하는 데 사용됩니다. Aspose.PDF에서 <abbr title="Extensible Markup Language">XML</abbr>을 PDF로 변환하는 방법은 여러 가지가 있습니다:

1. XSLT를 사용하여 모든 XML 데이터를 HTML로 변환하고 아래에 설명된 대로 HTML을 PDF로 변환합니다.
2. Aspose.PDF XSD 스키마를 사용하여 XML 문서를 생성합니다.
3. XSL-FO 표준을 기반으로 하는 XML 문서를 사용합니다.

{{% alert color="success" %}}
**XML을 PDF로 온라인 변환해 보세요**

Aspose.PDF for .NET은 온라인 무료 애플리케이션 ["XML to PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf)를 제공하여 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF XML을 PDF로 변환하는 무료 앱](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}

## XSL-FO를 PDF로 변환하기

<a name="csharp-convert-xslfo-to-pdf" id="csharp-convert-xslfo-to-pdf"><strong>XSL-FO를 PDF로 변환하기</strong></a>

XSL-FO 파일을 PDF로 변환하는 것은 전통적인 Aspose.PDF 기술을 사용하여 [Document](https://reference.aspose.com/page/net/aspose.page/document) 객체를 [XslFoLoadOptions](https://reference.aspose.com/pdf/ko/net/aspose.pdf/xslfoloadoptions)와 함께 인스턴스화하여 구현할 수 있습니다. 그러나 때때로 잘못된 파일 구조를 만날 수 있습니다. 이 경우 XSL-FO 변환기는 오류 처리 전략을 설정할 수 있습니다. `ThrowExceptionImmediately`, `TryIgnore` 또는 `InvokeCustomHandler`를 선택할 수 있습니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Convert_XSLFO_to_PDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options
    var options = new Aspose.Pdf.XslFoLoadOptions(dataDir + "XSLFOToPdfInput.xslt");
    // Set error handling strategy
    options.ParsingErrorsHandlingType = Aspose.Pdf.XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately;

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "XSLFOToPdfInput.xml", options))
    {
        // Save PDF document
        document.Save(dataDir + "XSLFOToPdf_out.pdf");
    }
}
```

## LaTeX/TeX를 PDF로 변환하기

<a name="csharp-convert-latex-to-pdf" id="csharp-convert-latext-to-pdf"><strong>LaTeX/TeX를 PDF로 변환하기</strong></a>

LaTeX 파일 형식은 TeX 언어 계열의 LaTeX 파생 마크업이 포함된 텍스트 파일 형식입니다. LaTeX는 TeX 시스템의 파생 형식입니다. LaTeX(ˈleɪtɛk/lay-tek 또는 lah-tek)는 문서 준비 시스템 및 문서 마크업 언어입니다. 수학, 물리학 및 컴퓨터 과학을 포함한 여러 분야에서 과학 문서의 커뮤니케이션 및 출판에 널리 사용됩니다. 또한 산스크리트어 및 아랍어와 같은 복잡한 다국어 자료가 포함된 책 및 기사의 준비 및 출판에서 중요한 역할을 합니다. LaTeX는 출력 형식을 지정하기 위해 TeX 조판 프로그램을 사용하며, 자체적으로 TeX 매크로 언어로 작성됩니다.

{{% alert color="success" %}}
**LaTeX/TeX를 PDF로 온라인 변환해 보세요**

Aspose.PDF for .NET은 온라인 무료 애플리케이션 ["LaTex to PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf)를 제공하여 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF LaTeX/TeX를 PDF로 변환하는 무료 앱](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}

Aspose.PDF for .NET은 TeX 파일을 PDF 형식으로 변환하는 기능을 지원하며, 이 요구 사항을 충족하기 위해 Aspose.Pdf 네임스페이스에는 LaTeX 파일을 로드하고 [Document class](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document)를 사용하여 PDF 형식으로 출력을 렌더링하는 기능을 제공하는 [LatexLoadOptions](https://reference.aspose.com/pdf/ko/net/aspose.pdf/latexloadoptions) 클래스가 있습니다. 다음 코드 스니펫은 C#을 사용하여 LaTeX 파일을 PDF 형식으로 변환하는 과정을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertTeXtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options
    var options = new Aspose.Pdf.TeXLoadOptions();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "samplefile.tex", options))
    {
        // Save PDF document
        document.Save(dataDir + "TeXToPDF_out.pdf");
    }
}
```

## OFD를 PDF로 변환하기

<a name="csharp-convert-ofd-to-pdf" id="csharp-convert-ofd-to-pdf"><strong>OFD를 PDF로 변환하기</strong></a>

OFD 형식은 "Open Fixed-layout Document"를 의미하며, 전자 파일 저장을 위한 중국의 국가 표준으로 설정되어 있으며, 인기 있는 PDF 형식의 대안으로 사용됩니다. 고정 레이아웃 문서를 지원하여 다양한 플랫폼에서 일관된 표시를 보장합니다. OFD 파일은 디지털 문서 및 비즈니스 애플리케이션을 포함한 다양한 용도로 사용됩니다.

Aspose.PDF for .NET은 OFD 파일을 PDF 형식으로 변환하는 기능을 지원하며, 이 요구 사항을 충족하기 위해 Aspose.Pdf 네임스페이스에는 OFD 파일을 로드하고 [Document class](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document)를 사용하여 PDF 형식으로 출력을 렌더링하는 기능을 제공하는 [OfdLoadOptions](https://reference.aspose.com/pdf/ko/net/aspose.pdf/ofdloadoptions/) 클래스가 있습니다.

다음 코드 스니펫은 C#을 사용하여 OFD 파일을 PDF 형식으로 변환하는 과정을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertOFDToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options
    var options = new Aspose.Pdf.OfdLoadOptions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ConvertOFDToPDF.ofd", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertOFDToPDF_out.pdf");
    }
}
```