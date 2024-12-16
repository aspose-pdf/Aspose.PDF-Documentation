---
title: 다른 파일 형식을 PDF로 변환하기 in .NET
linktitle: 다른 파일 형식을 PDF로 변환하기
type: docs
weight: 80
url: /ko/net/convert-other-files-to-pdf/
lastmod: "2021-11-01"
description: 이 주제에서는 Aspose.PDF를 사용하여 EPUB, MD, PCL, XPS, PS, XML 및 LaTeX와 같은 다른 파일 형식을 PDF 문서로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## 개요

이 문서에서는 **C#을 사용하여 다양한 다른 유형의 파일 형식을 PDF로 변환하는 방법**에 대해 설명합니다. 다음 주제를 다룹니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 사용할 수도 있습니다.

_형식_: **EPUB**
- [C# EPUB을 PDF로 변환](#csharp-convert-epub-to-pdf)
- [C# EPUB을 PDF로 변환하기](#csharp-convert-epub-to-pdf)
- [C# EPUB 파일을 PDF로 변환하는 방법](#csharp-convert-epub-to-pdf)

_형식_: **Markdown**
- [C# Markdown을 PDF로 변환](#csharp-convert-markdown-to-pdf)
- [C# Markdown을 PDF로 변환하기](#csharp-convert-markdown-to-pdf)
- [C# Markdown 파일을 PDF로 변환하는 방법](#csharp-convert-markdown-to-pdf)
- [C# Markdown 파일을 PDF로 변환하는 방법](#csharp-convert-markdown-to-pdf)

_형식_: **MD**
- [C# MD를 PDF로 변환](#csharp-convert-md-to-pdf)
- [C# MD를 PDF로 변환](#csharp-convert-md-to-pdf)
- [C# MD 파일을 PDF로 변환하는 방법](#csharp-convert-md-to-pdf)

_형식_: **PCL**
- [C# PCL을 PDF로 변환](#csharp-convert-pcl-to-pdf)
- [C# PCL을 PDF로 변환](#csharp-convert-pcl-to-pdf)
- [C# PCL 파일을 PDF로 변환하는 방법](#csharp-convert-pcl-to-pdf)

_형식_: **Text**
- [C# 텍스트를 PDF로 변환](#csharp-convert-text-to-pdf)
- [C# 텍스트를 PDF로 변환](#csharp-convert-text-to-pdf)
- [C# 텍스트 파일을 PDF로 변환하는 방법](#csharp-convert-text-to-pdf)

_형식_: **TXT**
- [C# TXT를 PDF로 변환](#csharp-convert-txt-to-pdf)
- [C# TXT를 PDF로 변환](#csharp-convert-txt-to-pdf)
- [C# TXT 파일을 PDF로 변환하는 방법](#csharp-convert-txt-to-pdf)

_형식_: **Plain Text**
- [C# 일반 텍스트를 PDF로 변환](#csharp-convert-plain-text-to-pdf)
- [C# 일반 텍스트를 PDF로 변환](#csharp-convert-plain-text-to-pdf)
- [C# 일반 텍스트 파일을 PDF로 변환하는 방법](#csharp-convert-plain-text-to-pdf)
- [C# 일반 텍스트 파일을 PDF로 변환하는 방법](#csharp-convert-plain-text-to-pdf)

_포맷_: **Preformatted TXT**
- [C# 사전에 형식이 지정된 텍스트를 PDF로 변환](#csharp-convert-pre-formatted-txt-to-pdf)
- [C# 사전에 형식이 지정된 텍스트를 PDF로 변환](#csharp-convert-pre-formatted-txt-to-pdf)
- [C# 사전에 형식이 지정된 텍스트 파일을 PDF로 변환하는 방법](#csharp-convert-pre-formatted-txt-to-pdf)

_포맷_: **Pre Text**
- [C# Pre Text를 PDF로 변환](#csharp-convert-pre-text-to-pdf)
- [C# Pre Text를 PDF로 변환](#csharp-convert-pre-text-to-pdf)
- [C# Pre Text 파일을 PDF로 변환하는 방법](#csharp-convert-pre-text-to-pdf)

_포맷_: **XPS**
- [C# XPS를 PDF로 변환](#csharp-convert-xps-to-pdf)
- [C# XPS를 PDF로 변환](#csharp-convert-xps-to-pdf)
- [C# XPS 파일을 PDF로 변환하는 방법](#csharp-convert-xps-to-pdf)

## EPUB을 PDF로 변환

**Aspose.PDF for .NET**을 사용하면 EPUB 파일을 PDF 형식으로 쉽게 변환할 수 있습니다.

<abbr title="electronic publication">EPUB</abbr>은 국제 디지털 출판 포럼(IDPF)에서 제공하는 무료이자 개방된 전자책 표준입니다.
<abbr title="전자 출판">EPUB</abbr>(전자 출판을 위한 약어)는 국제 디지털 출판 포럼(IDPF)에서 제공하는 무료이자 개방된 전자책 표준입니다.

EPUB는 고정 레이아웃 콘텐츠도 지원합니다. 이 포맷은 출판사와 변환 업체가 내부적으로 사용할 수 있는 단일 포맷으로 의도되었으며, 배포 및 판매를 위해서도 사용됩니다. 이는 오픈 이북 표준을 대체합니다. EPUB 3 버전은 콘텐츠의 패키징을 위한 표준화된 최선의 관행, 연구, 정보 및 이벤트를 위한 주요 도서 업계 협회인 Book Industry Study Group(BISG)에 의해서도 지지받고 있습니다.

{{% alert color="success" %}}
**온라인으로 EPUB를 PDF로 변환해 보세요**

Aspose.PDF for .NET은 무료 온라인 애플리케이션 ["EPUB to PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf)를 제공합니다. 여기에서 기능과 작동 품질을 탐색해 볼 수 있습니다.

[![Aspose.PDF Convertion EPUB to PDF with Free App](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

<a name="csharp-convert-epub-to-pdf" id="csharp-convert-epub-to-pdf"><strong><em>단계:</em> C#에서 EPUB를 PDF로 변환</strong></a>
<a name="csharp-convert-epub-to-pdf" id="csharp-convert-epub-to-pdf"><strong><em>단계:</em> C#에서 EPUB를 PDF로 변환하기</strong></a>

1. [EpubLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/epubloadoptions) 클래스의 인스턴스를 생성합니다.
2. 출처 파일명과 옵션을 명시하여 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스의 인스턴스를 생성합니다.
3. 원하는 파일 이름으로 문서를 저장합니다.

다음 코드 스니펫은 C#을 사용하여 EPUB 파일을 PDF 형식으로 변환하는 방법을 보여줍니다.

```csharp
public static void ConvertEPUBtoPDF()
{
    EpubLoadOptions option = new EpubLoadOptions();
    Document pdfDocument = new Document(_dataDir + "WebAssembly.epub", option);
    pdfDocument.Save(_dataDir + "epub_test.pdf");
}
```

또한 변환 시 페이지 크기를 설정할 수 있습니다. 새 페이지 크기를 정의하려면 `SizeF` 객체를 생성하고 [EpubLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/epubloadoptions/constructors/main) 생성자에 전달합니다.

```csharp
public static void ConvertEPUBtoPDFAdv()
{
    EpubLoadOptions option = new EpubLoadOptions(new SizeF(1190, 1684));
    Document pdfDocument = new Document(_dataDir + "WebAssembly.epub", option);
    pdfDocument.Save(_dataDir + "epub_test.pdf");
}
```
## Markdown을 PDF로 변환

**이 기능은 버전 19.6 이상에서 지원됩니다.**

{{% alert color="success" %}}
**Markdown을 PDF로 온라인으로 변환해 보세요**

Aspose.PDF for .NET은 ["Markdown to PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf)라는 무료 온라인 애플리케이션을 제공합니다. 여기에서 기능성과 작동 품질을 탐색해 볼 수 있습니다.

[![Aspose.PDF 무료 앱으로 Markdown을 PDF로 변환](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Aspose.PDF for .NET은 입력 [Markdown](https://daringfireball.net/projects/markdown/syntax) 데이터 파일을 기반으로 PDF 문서를 생성하는 기능을 제공합니다. Markdown을 PDF로 변환하기 위해 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)를 [MdLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/mdloadoptions)을 사용하여 초기화해야 합니다.

다음 코드 스니펫은 Aspose.PDF 라이브러리를 사용하여 이 기능을 사용하는 방법을 보여줍니다:

<a name="csharp-convert-markdown-to-pdf" id="csharp-convert-markdown-to-pdf"><strong><em>단계:</em> C#에서 Markdown을 PDF로 변환</strong></a> |
<a name="csharp-convert-markdown-to-pdf" id="csharp-convert-markdown-to-pdf"><strong><em>단계:</em> C#에서 마크다운을 PDF로 변환</strong></a> |
<a name="csharp-convert-md-to-pdf" id="csharp-convert-md-to-pdf"><strong><em>단계:</em> C#에서 MD를 PDF로 변환</strong></a>

1. [MdLoadOptions ](https://reference.aspose.com/pdf/net/aspose.pdf/mdloadoptions/) 클래스의 인스턴스를 생성합니다.
2. 원본 파일명과 옵션을 명시하여 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스의 인스턴스를 생성합니다.
3. 원하는 파일 이름으로 문서를 저장합니다.

```csharp
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// 마크다운 문서 열기
Document pdfDocument= new Document(dataDir + "sample.md", new MdLoadOptions());
// PDF 형식으로 문서 저장
pdfDocument.Save(dataDir + "MarkdownToPDF.pdf");
```

## PCL을 PDF로 변환

<abbr title="Printer Command Language">PCL</abbr> (Printer Command Language)은 표준 프린터 기능에 접근하기 위해 개발된 Hewlett-Packard 프린터 언어입니다.
<abbr title="Printer Command Language">PCL</abbr> (Printer Command Language)은 표준 프린터 기능에 접근하기 위해 개발된 Hewlett-Packard 프린터 언어입니다.

{{% alert color="success" %}}
**온라인에서 PCL을 PDF로 변환해 보세요**

Aspose.PDF for .NET은 ["PCL to PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf)라는 무료 온라인 애플리케이션을 제공합니다. 여기에서 기능성과 품질을 탐구해 볼 수 있습니다.

[![Aspose.PDF 변환 PCL에서 PDF로 무료 앱](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

**현재는 PCL5 및 이전 버전만 지원됩니다**

<table>
    <thead>
        <tr>
            <th>
                명령어 세트
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
                작업 제어 명령어

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
        인쇄 프로세스 제어: 복사본 수, 출력함, 단면/양면 인쇄, 왼쪽 및 상단 오프셋 등
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
        퍼포레이션 스킵 명령
    </td>
    <td>
        페이지 크기, 여백, 페이지 방향, 줄 간격, 글자 간격 등을 지정.
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
        커서 위치를 지정하고, 따라서 텍스트, 래스터 또는 벡터 이미지 및 세부 정보의 원점을 지정.
    </td>
</tr>
```

<tr>
    <td>
        커서 위치를 지정하고 따라서 텍스트, 래스터 또는 벡터 이미지 및 세부 정보의 기원을 설정합니다.
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
            <li>임베디드 소프트 글꼴. 현재 버전에서는 소프트 글꼴을 생성하는 대신 우리 라이브러리는
                대상 기기에 설치된 기존 "하드" 트루타입 글꼴 중 적합한 글꼴을 선택합니다. <br/>
                적합성은 너비/높이 비율에 의해 정의됩니다.<br/>
                이 기능은 비트맵 및 트루타입 글꼴에만 작동하며
                소프트 글꼴로 인쇄된 텍스트가 원본 파일의 해당 텍스트와 관련이 있음을 보장하지 않습니다.<br/>
                왜냐하면 소프트 글꼴의 문자 코드가 기본 코드와 일치하지 않을 수 있기 때문입니다.
            </li>
            <li>사용자 정의 심볼 세트.</li>
        </ol>
    </td>
</tr>
```

<li>사용자 정의 심볼 세트.</li>
</ol>
</td>
<td>
PCL 파일에서 소프트(내장된) 폰트를 로드하고 메모리에서 관리할 수 있습니다.
</td>
</tr>
<tr>
<td>
래스터 그래픽 명령어
</td>
<td>
+
</td>
<td>
흑백만 가능
</td>
<td>
PCL 파일에서 래스터 이미지를 메모리로 로드하고, 너비, 높이, 압축 유형, 해상도 등의 래스터 매개변수를 지정할 수 있습니다. <br>
</td>
</tr>
<tr>
<td>
색상 명령어
</td>
<td>
+
</td>
<td>
&nbsp;
</td>
<td>
모든 인쇄 가능한 객체에 대한 색상 지정이 가능합니다.
</td>
</tr>
<tr>
<td>
프린트 모델 명령어
```

### 모델 명령 인쇄
- 텍스트, 래스터 이미지 및 사각형 영역을 래스터 사전 정의 및 사용자 정의 패턴으로 채울 수 있습니다. 패턴과 소스 래스터 이미지에 대한 투명도 모드를 지정합니다. 사전 정의된 패턴은 해칭, 크로스 해치 및 음영입니다.

### 사각형 영역 채우기 명령
- 패턴으로 사각형 영역을 생성하고 채울 수 있습니다.

### HP-GL/2 벡터 그래픽 명령
- 스크린 벡터 명령 (SV), 투명도 모드 명령 (TR), 투명 데이터 명령 (TD), RO
```
SV(스크린 벡터 명령), TR(투명 모드 명령), TD(투명 데이터 명령), RO(좌표 시스템 회전), SB(확장 또는 비트맵 폰트 명령), SL(문자 기울기 명령) 및 ES(추가 공간)는 구현되지 않았으며 DV(가변 텍스트 경로 정의) 명령은 베타 버전에서 실현되었습니다.

HP-GL/2 벡터 이미지를 PCL 파일에서 메모리로 로드를 허용합니다. 벡터 이미지는 인쇄 가능 영역의 왼쪽 하단에 원점을 가지며, 크기 조정, 이동, 회전 및 클리핑이 가능합니다. 벡터 이미지는 레이블로서의 텍스트와 직사각형, 원, 타원, 선, 호, 베지어 곡선 및 간단한 도형으로 구성된 복잡한 도형을 포함할 수 있습니다. 레이블의 글자를 포함한 닫힌 도형은 솔리드 채우기 또는 벡터 패턴으로 채워질 수 있습니다. 패턴은 해칭, 크로스 해치, 음영, 사용자 정의 래스터, PCL 해칭 또는 크로스 해치 및 PCL

해칭, 크로스 해칭, 음영, 사용자 정의 래스터, PCL 해칭 또는 크로스 해칭 및 PCL 사용자 정의입니다. PCL 패턴은 래스터입니다. 라벨은 개별적으로 회전, 확대/축소 및 네 방향(위, 아래, 왼쪽, 오른쪽)으로 지시할 수 있습니다. 왼쪽과 오른쪽 방향은 연속된 글자 배치를 포함합니다. 위쪽과 아래쪽 방향은 글자를 세로로 배치합니다.

매크로

메모리에 PCL 명령 시퀀스를 로드하고 이 시퀀스를 여러 번 사용할 수 있습니다. 예를 들어, 페이지 헤더를 인쇄하거나 일련의 페이지에 동일한 형식을 설정하는 데 사용됩니다.

유니코드 텍스트
```

            </td>
            <td>
                &nbsp;
            </td>
            <td>
                ASCII가 아닌 문자 인쇄 허용. 유니코드 텍스트가 포함된 샘플 파일이 없어 구현되지 않음
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
                테스트 파일 부족으로 베타 버전에서만 구현됨. 임베디드 폰트도 지원되지 않음.<br> JetReady 확장은 JetReady 사양을 가질 수 없기 때문에 지원되지 않음.
            </td>
            <td>
                이진 파일 형식.
            </td>
        </tr>
    </tbody>
</table>

### PCL 파일을 PDF 형식으로 변환

PCL에서 PDF로 변환을 허용하기 위해, Aspose.PDF는 LoadOptions 객체를 초기화하는 데 사용되는 [`PclLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions) 클래스를 가지고 있습니다.
```
PCL을 PDF로 변환하려면 Aspose.PDF에는 LoadOptions 객체를 초기화하는 데 사용되는 [`PclLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions) 클래스가 있습니다.

다음 코드 스니펫은 PCL 파일을 PDF 형식으로 변환하는 과정을 보여줍니다.

<a name="csharp-convert-pcl-to-pdf" id="csharp-convert-pcl-to-pdf"><strong><em>단계:</em> C#에서 PCL을 PDF로 변환</strong></a>

1. [PclLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions/) 클래스의 인스턴스를 생성합니다.
2. 원본 파일 이름과 옵션을 명시하여 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) 클래스의 인스턴스를 생성합니다.
3. 원하는 파일 이름으로 문서를 저장합니다.

```csharp
public static void ConvertPCLtoPDF()
{
    PclLoadOptions options = new PclLoadOptions();
    Document pdfDocument= new Document(_dataDir + "demo.pcl", options);
    pdfDocument.Save(_dataDir + "pcl_test.pdf");
}
```

변환 과정 중 오류 탐지를 모니터링할 수도 있습니다.
변환 과정 중에 오류 감지를 모니터링할 수도 있습니다.

```csharp
public static void ConvertPCLtoPDFAvdanced()
{
    PclLoadOptions options = new PclLoadOptions { SupressErrors = true };
    Document pdfDocument= new Document(_dataDir + "demo.pcl", options);
    if (options.Exceptions!=null)
        foreach (var ex in options.Exceptions)
        {
            Console.WriteLine(ex.Message);
        }
    pdfDocument.Save(_dataDir + "pcl_test.pdf");
}
```

### 알려진 문제점

1. 인쇄 방향이 0°이 아닌 경우 원본 PCL 파일의 텍스트 문자열과 이미지의 원점이 약간 달라질 수 있습니다. 벡터 플롯의 좌표 시스템이 회전된 경우(RO 명령어가 앞선 경우) 벡터 이미지에도 동일하게 적용됩니다.
1. 벡터 이미지의 라벨 원점이 원본 PCL 파일의 라벨 원점과 다를 수 있습니다. 이는 라벨 원점(LO), 가변 텍스트 경로 정의(DV), 절대 방향(DI), 상대 방향(DR)의 명령어 시퀀스의 영향을 받을 경우입니다.
1.
1. PCL 파일이 Intellifont 또는 Universal 소프트 폰트를 포함하고 있는 경우, Intellifont 및 Universal 폰트는 전혀 지원되지 않기 때문에 예외가 발생합니다.
1. PCL 파일이 매크로 명령을 포함하고 있는 경우, 매크로 명령이 지원되지 않기 때문에 파싱 결과는 원본 파일과 크게 다를 것입니다.

## 텍스트를 PDF로 변환

**Aspose.PDF for .NET**는 일반 텍스트 및 서식 있는 텍스트 파일을 PDF 형식으로 변환하는 기능을 지원합니다.

텍스트를 PDF로 변환한다는 것은 PDF 페이지에 텍스트 조각을 추가하는 것을 의미합니다. 텍스트 파일의 경우, 우리는 2가지 유형의 텍스트를 다룹니다: 서식 있는 텍스트(예: 한 줄에 80개의 문자가 있는 25줄)와 서식이 없는 텍스트(일반 텍스트). 우리의 필요에 따라 이 추가를 직접 제어하거나 라이브러리의 알고리즘에 맡길 수 있습니다.

{{% alert color="success" %}}
**온라인에서 TEXT를 PDF로 변환해 보세요**

Aspose.PDF for .NET은 무료 온라인 애플리케이션 ["Text to PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf)를 제공합니다. 여기서 기능성과 작동 품질을 직접 확인해 볼 수 있습니다.
Aspose.PDF for .NET은 온라인 무료 애플리케이션 ["텍스트를 PDF로"](https://products.aspose.app/pdf/conversion/txt-to-pdf) 소개합니다. 여기서 기능과 작동 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 텍스트를 PDF로 변환하는 무료 앱](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)

### 평문 파일을 PDF로 변환

평문 파일의 경우 다음 기술을 사용할 수 있습니다:

<a name="csharp-convert-text-to-pdf" id="csharp-convert-text-to-pdf"><strong><em>단계:</em> C#에서 텍스트를 PDF로 변환</strong></a> |
<a name="csharp-convert-txt-to-pdf" id="csharp-convert-txt-to-pdf"><strong><em>단계:</em> C#에서 TXT를 PDF로 변환</strong></a> |
<a name="csharp-convert-plain-text-to-pdf" id="csharp-convert-plain-text-to-pdf"><strong><em>단계:</em> C#에서 평문을 PDF로 변환</strong></a>

1. _TextReader_를 사용하여 전체 텍스트를 읽습니다;
2.
2.
3. [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment/)의 새 객체를 생성하고 생성자에 _TextReader_ 객체를 전달하세요;
4. _TextFragment_ 객체를 _Paragraphs_ 컬렉션에 단락으로 추가하세요. 페이지보다 텍스트 양이 많을 경우, 라이브러리 알고리즘이 자동으로 추가 페이지를 추가합니다;
5. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) 클래스의 **Save** 메소드를 사용하세요;

```csharp
// 완전한 예제와 데이터 파일을 보려면 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 을 방문하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// 원본 텍스트 파일을 읽습니다.
TextReader tr = new StreamReader(dataDir + "log.txt");

// 빈 생성자를 호출하여 Document 객체의 인스턴스를 만듭니다.
Document pdfDocument= new Document();

// Document의 Pages 컬렉션에 새 페이지를 추가합니다.
Page page = pdfDocument.Pages.Add();

// TextFragment 인스턴스를 생성하고 reader 객체에서 읽은 텍스트를 생성자 인수로 전달합니다.
TextFragment text = new TextFragment(tr.ReadToEnd());

// paragraphs 컬렉션에 새 텍스트 단락을 추가하고 TextFragment 객체를 전달합니다.
page.Paragraphs.Add(text);

// 결과 PDF 파일을 저장합니다.
pdfDocument.Save(dataDir + "TexttoPDF_out.pdf");
```
### 사전 포맷된 텍스트 파일을 PDF로 변환

사전 포맷된 텍스트를 변환하는 것은 일반 텍스트와 비슷하지만 여백, 글꼴 유형 및 크기 설정과 같은 추가 작업이 필요합니다. 당연히 글꼴은 고정폭이어야 합니다(예: Courier New).

C#에서 사전 포맷된 텍스트를 PDF로 변환하는 단계는 다음과 같습니다:

<a name="csharp-convert-pre-text-to-pdf" id="csharp-convert-pre-text-to-pdf"><strong><em>단계:</em> C#에서 사전 텍스트를 PDF로 변환</strong></a> |
<a name="csharp-convert-pre-formatted-txt-to-pdf" id="csharp-convert-pre-formatted-txt-to-pdf"><strong><em>단계:</em> C#에서 사전 포맷된 TXT를 PDF로 변환</strong></a>

1. 전체 텍스트를 문자열 배열로 읽습니다;
2. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) 객체를 인스턴스화하고 [Pages](https://reference.aspose.com/pdf/net/aspose.pdf/document/pages/) 컬렉션에 새 페이지를 추가합니다;
3.
이 경우, 라이브러리의 알고리즘은 추가 페이지를 추가하지만 우리는 이 과정을 스스로 제어할 수 있습니다.
다음 예는 서식 있는 텍스트 파일(80x25)을 A4 페이지 크기의 PDF 문서로 변환하는 방법을 보여줍니다.

```csharp
public static void ConvertPreFormattedTextToPdf()
{
    // 문자열 배열로 텍스트 파일을 읽습니다
    var lines = System.IO.File.ReadAllLines(_dataDir + "rfc822.txt");

    // 빈 생성자를 호출하여 Document 객체를 인스턴스화합니다
    Document pdfDocument= new Document();

    // Document의 Pages 컬렉션에 새 페이지를 추가합니다
    Page page = pdfDocument.Pages.Add();

    // 보다 나은 프레젠테이션을 위해 왼쪽 및 오른쪽 여백을 설정합니다
    page.PageInfo.Margin.Left = 20;
    page.PageInfo.Margin.Right = 10;
    page.PageInfo.DefaultTextState.Font = FontRepository.FindFont("Courier New");
    page.PageInfo.DefaultTextState.FontSize = 12;

    foreach (var line in lines)
    {
        // 줄이 "form feed" 문자를 포함하는지 확인합니다
        // https://en.wikipedia.org/wiki/Page_break 참조
        if (line.StartsWith("\x0c"))
        {
            page = pdfDocument.Pages.Add();
            page.PageInfo.Margin.Left = 20;
            page.PageInfo.Margin.Right = 10;
            page.PageInfo.DefaultTextState.Font = FontRepository.FindFont("Courier New");
            page.PageInfo.DefaultTextState.FontSize = 12;
        }
        else
        {
            // TextFragment의 인스턴스를 생성하고
            // 줄을
            // 생성자의 인수로 전달합니다
            TextFragment text = new TextFragment(line);

            // paragraphs 컬렉션에 새 텍스트 단락을 추가하고 TextFragment 객체를 전달합니다
            page.Paragraphs.Add(text);
        }
    }

    // 결과 PDF 파일을 저장합니다
    pdfDocument.Save(_dataDir + "TexttoPDF_out.pdf");
}
```
## XPS를 PDF로 변환

**Aspose.PDF for .NET**은 <abbr title="XML Paper Specification">XPS</abbr> 파일을 PDF 형식으로 변환하는 기능을 지원합니다. 이 기사를 확인하여 과제를 해결하세요.

XPS 파일 유형은 주로 Microsoft Corporation의 XML Paper Specification과 관련이 있습니다. XML Paper Specification(XPS)은 이전에 Metro로 코드명이 지어졌으며 Next Generation Print Path(NGPP) 마케팅 개념을 포괄하는 것으로, 문서 생성 및 보기를 Windows 운영 체제에 통합하려는 Microsoft의 계획입니다.

{{% alert color="primary" %}}

파일 형식은 기본적으로 배포 및 저장에 주로 사용되는 압축된 XML 파일입니다. 편집하기 매우 어렵고 주로 Microsoft에서 구현됩니다.

{{% /alert %}}

Aspose.PDF for .NET을 사용하여 XPS를 PDF로 변환하려면 [XpsLoadOption](https://reference.aspose.com/pdf/net/aspose.pdf/xpsloadoptions)이라는 클래스를 도입하여 [LoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/loadoptions) 객체를 초기화하는 데 사용됩니다.
Aspose.PDF for .NET을 사용하여 XPS를 PDF로 변환하기 위해 [XpsLoadOption](https://reference.aspose.com/pdf/net/aspose.pdf/xpsloadoptions) 이라는 클래스를 소개했습니다. 이 클래스는 [LoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/loadoptions) 객체를 초기화하는 데 사용됩니다.

{{% alert color="primary" %}}

XP와 Windows 7 모두에서 제어판, 그리고 프린터를 확인하면 XPS 프린터가 사전 설치되어 있어야 합니다. 이 프린터를 출력 장치로 사용하여 파일을 생성할 수 있습니다. Windows 7에서는 파일을 더블 클릭해서 XPS 뷰어에서 바로 열 수 있어야 합니다. Microsoft의 웹사이트에서 XPS 뷰어를 다운로드할 수도 있습니다.

{{% /alert %}}

다음 코드 스니펫은 C#을 사용하여 XPS 파일을 PDF 형식으로 변환하는 과정을 보여줍니다.

<a name="csharp-convert-xps-to-pdf" id="csharp-convert-xps-to-pdf"><strong><em>단계:</em> C#에서 XPS를 PDF로 변환</strong></a>

1. [XpsLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xpsloadoptions/) 클래스의 인스턴스를 생성합니다.
2.
2.
3. 원하는 파일 이름으로 문서를 PDF 형식으로 저장하세요.

```csharp
// 전체 예제와 데이터 파일을 보려면 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 을 방문하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// XPS 로드 옵션을 사용하여 LoadOption 객체를 인스턴스화합니다.
Aspose.Pdf.LoadOptions options = new XpsLoadOptions();

// 문서 객체를 생성합니다.
Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "XPSToPDF.xps", options);

// 결과 PDF 문서를 저장합니다.
document.Save(dataDir + "XPSToPDF_out.pdf");
```

{{% alert color="success" %}}
**XPS 형식을 PDF로 변환해 보세요**

Aspose.PDF for .NET은 무료 온라인 애플리케이션 ["XPS to PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/)를 제공합니다. 여기에서 기능성과 품질을 탐색해 볼 수 있습니다.

[![Aspose.PDF Convertion XPS to PDF with Free App](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}
{{% /alert %}}

## PostScript를 PDF로 변환

**Aspose.PDF for .NET**은 PostScript 파일을 PDF 포맷으로 변환하는 기능을 지원합니다. Aspose.PDF의 한 기능은 변환하는 동안 사용될 폰트 폴더 세트를 설정할 수 있다는 것입니다.

PostScript 파일을 PDF 포맷으로 변환하기 위해, Aspose.PDF for .NET은 [PsLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/psloadoptions) 클래스를 제공합니다. 이 클래스는 LoadOptions 객체를 초기화하는 데 사용됩니다. 이후 이 객체는 Document 객체 생성자에 인수로 전달될 수 있으며, 이는 PDF 렌더링 엔진이 소스 문서의 포맷을 판단하는 데 도움을 줍니다.

다음 코드 스니펫은 Aspose.PDF for .NET을 사용하여 PostScript 파일을 PDF 포맷으로 변환하는 데 사용할 수 있습니다:

```csharp
// 완전한 예제와 데이터 파일을 보려면 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 방문하세요.
// 문서 디렉토리의 경로입니다.
string _dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// PsLoadOptions의 새 인스턴스를 생성합니다
PsLoadOptions options = new PsLoadOptions();
// 생성된 로드 옵션으로 .ps 문서를 엽니다
Document pdfDocument = new Document(_dataDir + "input.ps", options);
// 문서를 저장합니다
pdfDocument.Save(dataDir + "PSToPDF.pdf");
```
추가로, 변환 중에 사용될 폰트 폴더 세트를 설정할 수 있습니다:

```csharp
public static void ConvertPostscriptToPDFAvdanced()
{
    PsLoadOptions options = new PsLoadOptions
    {
        FontsFolders = new [] { @"c:\tmp\fonts1", @"c:\tmp\fonts2"}
    };
    Document pdfDocument = new Document(_dataDir + "input.ps", options);
    pdfDocument.Save(_dataDir + "ps_test.pdf");
}
```

## XML을 PDF로 변환

XML 형식은 구조화된 데이터를 저장하는 데 사용됩니다. Aspose.PDF에서 XML을 PDF로 변환하는 몇 가지 방법은 다음과 같습니다:

1. XSLT를 사용하여 어떤 XML 데이터도 HTML로 변환하고 아래에 설명된 대로 HTML을 PDF로 변환
1. Aspose.PDF XSD 스키마를 사용하여 XML 문서 생성
1. XSL-FO 표준을 기반으로 한 XML 문서 사용

{{% alert color="success" %}}
**온라인으로 XML을 PDF로 변환해 보세요**

Aspose.PDF for .NET은 기능과 품질을 조사해 볼 수 있는 무료 온라인 애플리케이션 ["XML to PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf)를 제공합니다.
Aspose.PDF for .NET은 ["XML to PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf)라는 무료 온라인 애플리케이션을 제공합니다. 여기에서 기능과 품질을 테스트해볼 수 있습니다.
{{% /alert %}}

[![Aspose.PDF Convertion XML to PDF with Free App](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)

## XSL-FO를 PDF로 변환하기

XSL-FO 파일을 PDF로 변환하는 것은 전통적인 Aspose.PDF 기술을 사용하여 [Document](https://reference.aspose.com/page/net/aspose.page/document) 객체를 [XslFoLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xslfoloadoptions)와 함께 인스턴스화하는 것을 통해 구현할 수 있습니다. 하지만 가끔 파일 구조가 올바르지 않은 경우를 만날 수 있습니다. 이 경우, XSL-FO 컨버터는 오류 처리 전략을 설정할 수 있습니다. `ThrowExceptionImmediately`, `TryIgnore` 또는 `InvokeCustomHandler`를 선택할 수 있습니다.

```csharp
public static void Convert_XSLFO_to_PDF()
{
    // XslFoLoadOption 객체 인스턴스화
    var options = new XslFoLoadOptions(".\\samples\\employees.xslt");
    // 오류 처리 전략 설정
    options.ParsingErrorsHandlingType = XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately;
    // Document 객체 생성
    var pdfDocument = new Aspose.Pdf.Document(".\\samples\\employees.xml", options);
    pdfDocument.Save(_dataDir + "data_xml.pdf");
}
```
## LaTeX/TeX를 PDF로 변환

LaTeX 파일 형식은 LaTeX의 파생 TeX 언어 계열에서 마크업이 있는 텍스트 파일 형식이며, LaTeX는 TeX 시스템의 파생 형식입니다. LaTeX(ˈleɪtɛk/lay-tek 또는 lah-tek)는 문서 준비 시스템이자 문서 마크업 언어입니다. 수학, 물리학, 컴퓨터 과학을 포함한 많은 분야에서 과학 문서의 소통과 출판에 널리 사용됩니다. 또한 산스크리트와 아랍어 같은 복잡한 다국어 자료가 포함된 책과 기사의 준비 및 출판에서도 중요한 역할을 합니다. LaTeX는 TeX 조판 프로그램을 사용하여 출력물을 포맷하며, 자체적으로 TeX 매크로 언어로 작성됩니다.

{{% alert color="success" %}}
**LaTeX/TeX를 PDF로 온라인 변환해 보세요**

Aspose.PDF for .NET은 무료 온라인 애플리케이션 ["LaTex to PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf)를 제공합니다. 여기서 기능과 작동 품질을 탐구해 볼 수 있습니다.

[![Aspose.PDF Convertion LaTeX/TeX to PDF with Free App](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
[![Aspose.PDF Convertion LaTeX/TeX to PDF with Free App](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}

Aspose.PDF for .NET은 TeX 파일을 PDF 형식으로 변환하는 기능을 지원하며, 이를 위해 Aspose.Pdf 네임스페이스는 LaTex 파일을 로드하고 [Document class](https://reference.aspose.com/pdf/net/aspose.pdf/document)를 사용하여 출력을 PDF 형식으로 렌더링할 수 있는 기능을 제공하는 [LatexLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/latexloadoptions)라는 클래스를 가지고 있습니다. 
다음 코드 스니펫은 C#을 사용하여 LaTex 파일을 PDF 형식으로 변환하는 과정을 보여줍니다.

```csharp
public static void ConvertTeXtoPDF()
{
    // Latex Load 옵션 객체를 생성합니다
    TeXLoadOptions options = new TeXLoadOptions();
    // Document 객체를 생성합니다
    Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(_dataDir + "samplefile.tex", options);
    // 출력을 PDF 파일에 저장합니다
    pdfDocument.Save(_dataDir + "TeXToPDF_out.pdf");
}
```
