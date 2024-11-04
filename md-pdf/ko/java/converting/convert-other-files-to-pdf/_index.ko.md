---
title: 다양한 파일 형식을 PDF로 변환
linktitle: 다른 파일 형식을 PDF로 변환
type: docs
weight: 80
url: /java/convert-other-files-to-pdf/
lastmod: "2021-11-19"
description: 이 주제는 Aspose.PDF가 다른 파일 형식을 PDF 문서로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## EPUB을 PDF로 변환

**Aspose.PDF for Java**를 사용하면 간단히 EPUB 파일을 PDF 형식으로 변환할 수 있습니다.

<abbr title="electronic publication">EPUB</abbr> (전자 출판의 약자)은 국제 디지털 출판 포럼(IDPF)에서 제공하는 무료 및 오픈 전자책 표준입니다. 파일 확장자는 .epub입니다. EPUB은 가변 콘텐츠를 위해 설계되었으며, 이는 EPUB 리더가 특정 디스플레이 장치에 대한 텍스트를 최적화할 수 있음을 의미합니다.

EPUB 파일을 PDF 형식으로 변환하기 위해, Aspose.PDF for Java에는 [EpubLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubLoadOptions)라는 클래스가 있으며, 이는 원본 EPUB 파일을 로드하는 데 사용됩니다.
 그 후, 객체는 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) 객체 초기화의 인수로 전달되며, 이는 PDF 렌더링 엔진이 소스 문서의 입력 형식을 결정하는 데 도움이 됩니다.

다음 코드 스니펫은 EPUB 파일을 PDF 형식으로 변환하는 과정을 보여줍니다.

1. EPUB [`LoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/loadoptions)를 생성합니다.
2. [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) 객체를 초기화합니다.
3. 출력 PDF 문서를 저장합니다.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertEPUBtoPDF {

    private ConvertEPUBtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // EPUB LoadOptions를 생성합니다.
        EpubLoadOptions options = new EpubLoadOptions();

        // 문서 객체를 초기화합니다.
        String epubFileName = Paths.get(_dataDir.toString(), "aliceDynamic.epub").toString();
        Document document = new Document(epubFileName, options);

        // 출력 PDF 문서를 저장합니다.
        document.save(Paths.get(_dataDir.toString(),"EPUBtoPDF.pdf").toString());
    }
}
```

{{% alert color="success" %}}
**EPUB을 PDF로 온라인에서 변환해보세요**

Aspose.PDF for Java는 온라인 무료 애플리케이션 ["EPUB to PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf)를 제공하여, 기능과 품질을 조사해볼 수 있습니다.

[![Aspose.PDF Convertion EPUB to PDF with Free App](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

## Markdown을 PDF로 변환

**이 기능은 버전 19.6 이상에서 지원됩니다.**

{{% alert color="success" %}}
**Markdown을 PDF로 온라인에서 변환해보세요**

Aspose.PDF for Java는 온라인 무료 애플리케이션 ["Markdown to PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf)를 제공하여, 기능과 품질을 조사해볼 수 있습니다.

[![Aspose.PDF Convertion Markdown to PDF with Free App](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Markdown은 웹 저자를 위한 텍스트를 HTML로 변환하는 도구입니다.
 Markdown은 읽고 쓰기 쉬운 일반 텍스트 형식으로 작성한 후 구조적으로 유효한 XHTML(또는 HTML)로 변환할 수 있게 해줍니다.

다음 코드 스니펫은 Aspose.PDF for Java를 사용하여 이 기능을 사용하는 방법을 보여줍니다:

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertMDtoPDF {

    private ConvertMDtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Latex Load 옵션 객체를 인스턴스화
        MdLoadOptions options = new MdLoadOptions();
        
        // Document 객체 생성
        String markdownFileName = Paths.get(_dataDir.toString(), "samplefile.md").toString();
        Document document = new Document(markdownFileName, options);

        // 출력 PDF 문서 저장
        document.save(Paths.get(_dataDir.toString(),"MarkdownToPDF.pdf").toString());
    }
}
```

## PCL을 PDF로 변환하기

<abbr title="Printer Command Language">PCL</abbr> (프린터 명령어 언어)는 표준 프린터 기능에 접근하기 위해 개발된 Hewlett-Packard의 프린터 언어입니다. PCL 레벨 1에서 5e/5c까지는 수신된 순서대로 처리되고 해석되는 제어 시퀀스를 사용하는 명령 기반 언어입니다. 소비자 수준에서 PCL 데이터 스트림은 프린터 드라이버에 의해 생성됩니다. PCL 출력은 사용자 정의 애플리케이션에 의해 쉽게 생성될 수도 있습니다.

{{% alert color="success" %}}
**온라인에서 PCL을 PDF로 변환해보세요**

Aspose.PDF for Java는 무료 온라인 애플리케이션 ["PCL to PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf)를 제공하여 기능과 품질을 시험해볼 수 있습니다.

[![Aspose.PDF Convertion PCL to PDF with Free App](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

**현재, PCL5 및 이전 버전만 지원됩니다.**

|**명령어 세트**|**지원**|**예외**|**설명**|

| :- | :- | :- | :- |
|작업 제어 명령어|+|양면 인쇄 모드|인쇄 프로세스를 제어: 복사본 수, 출력함, 단면/양면 인쇄, 왼쪽 및 위쪽 오프셋 등|
|페이지 제어 명령어|+|천공 건너뛰기 명령어|페이지 크기, 여백, 페이지 방향, 줄 간격, 문자 간 거리 등을 지정|
|커서 위치 지정 명령어|+| |커서 위치 및, 따라서 텍스트, 래스터 또는 벡터 이미지의 기원과 세부사항을 지정|

|Font selection commands|+|<p>1. 투명 인쇄 데이터 명령.</p><p>2. 내장된 소프트 폰트. 현재 버전에서는 소프트 폰트를 생성하는 대신, 라이브러리가 대상 기기에 설치된 기존 "하드" TrueType 폰트에서 적절한 폰트를 선택합니다. <br>   적절성은 너비/높이 비율에 의해 정의됩니다. <br>   이 기능은 비트맵 및 TrueType 폰트에만 작동하며, 소프트 폰트로 인쇄된 텍스트가 원본 파일의 텍스트와 일치함을 보장하지 않습니다. <br>   왜냐하면 소프트 폰트의 문자 코드가 기본 코드와 일치하지 않을 수 있기 때문입니다.</p><p>3. 사용자 정의 기호 세트.</p>|PCL 파일에서 소프트(내장) 폰트를 로드하고 메모리에서 관리할 수 있습니다.|
|Raster graphics commands|+|흑백 전용|PCL 파일에서 래스터 이미지를 메모리에 로드하고, 너비, 높이, 압축 유형, 해상도 등의 래스터 매개변수를 지정할 수 있습니다.|
|Color commands|+| |모든 인쇄 가능한 객체에 색상을 적용할 수 있습니다.|
|Print Model commands|+| |래스터로 미리 정의된 및 사용자 정의 패턴으로 텍스트, 래스터 이미지 및 직사각형 영역을 채우고, 패턴 및 소스 래스터 이미지에 대한 투명도 모드를 지정할 수 있습니다.|
 <br>미리 정의된 패턴은 해칭, 교차 해칭 및 음영 패턴입니다.|
|사각형 영역 채우기 명령어|+| |패턴을 사용하여 사각형 영역을 생성하고 채울 수 있습니다.|
|HP-GL/2 벡터 그래픽 명령어|+|스크린 벡터 명령어(SV), 투명 모드 명령어(TR), 투명 데이터 명령어(TD), RO(좌표계 회전), 스케일러블 또는 비트맵 폰트 명령어(SB), 문자 기울기 명령어(SL) 및 추가 공간(ES)은 구현되지 않았으며 DV(가변 텍스트 경로 정의) 명령어는 베타 버전으로 구현되었습니다.|<p>- PCL 파일에서 HP-GL/2 벡터 이미지를 메모리에 로드할 수 있습니다. 벡터 이미지는 인쇄 가능한 영역의 좌하단 모서리를 원점으로 하며, 크기 조정, 변환, 회전 및 잘라내기가 가능합니다.</p><p>- 벡터 이미지는 텍스트(레이블)와 직사각형, 원, 타원, 선, 호, 베지어 곡선 및 단순한 도형들로 구성된 복잡한 도형 같은 기하학적 도형을 포함할 수 있습니다.</p><p>- 레이블의 문자들을 포함한 닫힌 도형은 단색 채우기 또는 벡터 패턴으로 채울 수 있습니다.</p><p>- 패턴은 해칭, 교차 해칭, 음영 처리, 사용자가 정의한 래스터, PCL 해칭 또는 교차 해칭, PCL 사용자가 정의한 것으로 될 수 있습니다. PCL 패턴은 래스터입니다. 레이블은 개별적으로 회전, 크기 조정, 그리고 네 가지 방향(위, 아래, 왼쪽, 오른쪽)으로 방향을 지정할 수 있습니다. 왼쪽과 오른쪽 방향은 연속적인 문자 배열을 포함합니다. 위와 아래 방향은 한 문자 아래에 다른 문자가 오는 배열을 포함합니다.</p>|
|Macross|―| |PCL 명령어의 시퀀스를 메모리에 로드하고 이 시퀀스를 여러 번 사용할 수 있도록 허용하여 예를 들어 페이지 헤더를 인쇄하거나 여러 페이지에 하나의 형식을 설정할 수 있습니다.|
|Unicode text|―| |비 ASCII 문자를 인쇄할 수 있도록 허용합니다. 구현되지 않음 샘플 파일 부족으로 <br>유니코드 텍스트|
|PCL6 (PCL-XL)| |테스트 파일 부족으로 베타 버전에서만 구현되었습니다. 임베디드 폰트도 지원되지 않습니다. JetReady 확장은 JetReady 사양을 가질 수 없기 때문에 지원되지 않습니다.|바이너리 파일 형식.|

### PCL 파일을 PDF 형식으로 변환하기

PCL에서 PDF로의 변환을 허용하기 위해, [Aspose.PDF for Java](https://products.aspose.com/pdf/java)에는 [PclLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PclLoadOptions) 클래스가 있으며, 이는 [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions) 객체를 초기화하는 데 사용됩니다. 이 객체는 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) 객체 초기화 중에 인수로 전달되며 PDF 렌더링 엔진이 원본 문서의 입력 형식을 결정하는 데 도움이 됩니다.

다음 코드 스니펫은 PCL 파일을 PDF 형식으로 변환하는 과정을 보여줍니다.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPCLtoPDF {

    private ConvertPCLtoPDF() {
        
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {        
        ConvertPCLtoPDF_Simple();
        ConvertPCLtoPDF_Advanced();
    }

    public static void ConvertPCLtoPDF_Simple() {
        PclLoadOptions options = new PclLoadOptions();
        Document pdfDocument= new Document(_dataDir + "demo.pcl", options);
        pdfDocument.save(_dataDir + "epub_test.pdf");        
    }

    public static void ConvertPCLtoPDF_Advanced() {
        PclLoadOptions options = new PclLoadOptions();
        options.SupressErrors=true;
        Document pdfDocument= new Document(_dataDir + "demo.pcl", options);
        if (options.Exceptions!=null)
            for (Exception ex : options.Exceptions)
            {
                System.out.println(ex.getMessage());
            }
        pdfDocument.save(_dataDir + "pcl_test.pdf");        
    }
}
```

### 알려진 문제

1. 텍스트 문자열과 이미지의 원본이 소스 PCL 파일의 것과 약간 다를 수 있습니다. 인쇄 방향이 0º이 아닌 경우 벡터 이미지도 마찬가지입니다. 벡터 플롯의 좌표 시스템이 회전된 경우(RO 명령이 선행된 경우) 벡터 이미지의 레이블 원본도 다를 수 있습니다.
2. 레이블 원본(LO), 변수 텍스트 경로 정의(DV), 절대 방향(DI) 또는 상대 방향(DR) 명령의 시퀀스에 의해 레이블이 영향을 받는 경우 벡터 이미지의 레이블 원본이 소스 PCL 파일의 것과 다를 수 있습니다.
3. 텍스트가 비트맵 또는 TrueType 소프트(내장) 글꼴로 렌더링되어야 하는 경우 텍스트가 잘못 읽힐 수 있습니다. 현재 이러한 글꼴은 부분적으로만 지원되기 때문입니다(지원되는 기능 테이블의 예외 참조). 이 경우 소프트 글꼴의 문자 코드가 기본 문자 코드와 일치하는 경우에만 텍스트가 올바르게 읽힐 수 있습니다. 또한 읽은 텍스트의 스타일이 소스 PCL 파일의 것과 다를 수 있습니다. 소프트 글꼴 헤더에 스타일을 설정할 필요가 없기 때문입니다.

1. 구문 분석된 PCL 파일에 Intellifont 또는 Universal 소프트 폰트가 포함되어 있으면 Intellifont 및 Universal 폰트가 전혀 지원되지 않기 때문에 예외가 발생합니다.
1. 구문 분석된 PCL 파일에 매크로 명령이 포함되어 있으면 매크로 명령이 지원되지 않기 때문에 구문 분석 결과가 원본 파일과 크게 다를 것입니다.

## 텍스트를 PDF로 변환

**Aspose.PDF for Java**는 텍스트 파일을 PDF 형식으로 변환할 수 있는 기능을 제공합니다. 이 문서에서는 Aspose.PDF를 사용하여 텍스트 파일을 PDF로 얼마나 쉽게 효율적으로 변환할 수 있는지 보여줍니다.

텍스트 파일을 PDF로 변환해야 할 때, 처음에는 어떤 리더에서 원본 텍스트 파일을 읽어야 합니다. 우리는 StringBuilder를 사용하여 텍스트 파일 내용을 읽었습니다. Document 객체를 인스턴스화하고 Pages 컬렉션에 새 페이지를 추가합니다. TextFragment의 새 객체를 생성하고 StringBuilder 객체를 생성자에 전달합니다. TextFragment 객체를 사용하여 Paragraphs 컬렉션에 새 단락을 추가하고 Document 클래스의 Save 메서드를 사용하여 결과 PDF 파일을 저장합니다.
**텍스트를 PDF로 온라인에서 변환해보세요**
{{% alert color="success" %}}

Aspose.PDF for Java는 온라인 무료 애플리케이션 ["텍스트를 PDF로"](https://products.aspose.app/pdf/conversion/txt-to-pdf)를 제공하여, 기능 및 품질을 조사해볼 수 있습니다.

[![Aspose.PDF 변환 텍스트를 PDF로 무료 앱으로](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

### 일반 텍스트 파일을 PDF로 변환

```java
package com.aspose.pdf.examples;
/**
 * TXT를 PDF로 변환
 */

import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertTextToPDF {

    private ConvertTextToPDF() {
    }

    final static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");
    final static Charset ENCODING = StandardCharsets.UTF_8;

    public static void main(String[] args) throws IOException {
        ConvertTXT_to_PDF_Simple();
    }

    public static void ConvertTXT_to_PDF_Simple() throws IOException {
        // 문서 객체 초기화

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();
        Path txtDocumentFileName = Paths.get(_dataDir.toString(), "rfc822.txt");

        // 빈 생성자를 호출하여 Document 객체를 인스턴스화
        Document pdfDocument = new Document();

        // Document의 Pages 컬렉션에 새 페이지 추가
        Page page = pdfDocument.getPages().add();

        // TextFragment의 인스턴스를 생성하고 reader 객체에서 전달된 텍스트를
        // 생성자의 인수로 전달
        TextFragment text = new TextFragment(Files.readString(txtDocumentFileName, ENCODING));

        // 단락 컬렉션에 새 텍스트 단락을 추가하고 TextFragment 객체를 전달
        page.getParagraphs().add(text);

        // 결과 PDF 파일 저장
        pdfDocument.save(pdfDocumentFileName);
    }
```


### 사전 형식이 지정된 텍스트 파일을 PDF로 변환

```java
    public static void ConvertPreFormattedTextToPdf() throws IOException {

        Path txtDocumentFileName = Paths.get(_dataDir.toString(), "rfc822.txt");
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();

        // 텍스트 파일을 문자열 배열로 읽습니다
        java.util.List<String> lines = Files.readAllLines(txtDocumentFileName, ENCODING);

        // 빈 생성자를 호출하여 Document 객체를 인스턴스화합니다
        Document pdfDocument = new Document();

        // Document의 Pages 컬렉션에 새 페이지를 추가합니다
        Page page = pdfDocument.getPages().add();

        // 더 나은 표현을 위해 왼쪽 및 오른쪽 여백을 설정합니다
        page.getPageInfo().getMargin().setLeft(20);
        page.getPageInfo().getMargin().setRight(10);
        page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
        page.getPageInfo().getDefaultTextState().setFontSize(12);

        for (String line : lines) {
            // 줄에 "용지 넘김" 문자가 포함되어 있는지 확인합니다
            // https://en.wikipedia.org/wiki/Page_break 참조
            if (line.startsWith("\f")) {
                page = pdfDocument.getPages().add();
                page.getPageInfo().getMargin().setLeft(20);
                page.getPageInfo().getMargin().setRight(10);
                page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
                page.getPageInfo().getDefaultTextState().setFontSize(12);
            } else {
                // TextFragment의 인스턴스를 생성하고
                // 줄을 인수로
                // 생성자에 전달합니다
                TextFragment text = new TextFragment(line);

                // 문단 컬렉션에 새 텍스트 단락을 추가하고 TextFragment
                // 객체를 전달합니다
                page.getParagraphs().add(text);
            }

            pdfDocument.save(pdfDocumentFileName);
        }
    }
}
```


## XPS를 PDF로 변환하기

**Aspose.PDF for Java**는 <abbr title="XML Paper Specification">XPS</abbr> 파일을 PDF 형식으로 변환하는 기능을 지원합니다. 이 기사를 통해 작업을 해결하십시오.

XPS, XML Paper Specification은 문서 생성 및 보기 기능을 Windows에 통합하기 위해 사용되는 Microsoft 파일 형식입니다. Aspose.PDF for Java를 사용하면 Adobe의 휴대용 파일 형식인 PDF로 XPS 파일을 변환할 수 있습니다.

파일 형식은 기본적으로 배포 및 저장을 위해 주로 사용되는 압축된 XML 파일입니다. 수정하기 매우 어렵고 주로 Microsoft에 의해 구현됩니다.

[Aspose.PDF for Java](https://products.aspose.com/pdf/java)를 사용하여 XPS 파일을 PDF로 변환하려면 [XpsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsLoadOptions) 클래스를 사용하십시오.
 이것은 [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions) 객체를 초기화하는 데 사용됩니다. 이후 이 객체는 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) 객체 초기화 시 인수로 전달되어 PDF 렌더링 엔진이 소스 문서의 입력 형식을 결정하는 데 도움을 줍니다.

XP와 Windows 7 모두 제어판에서 프린터를 확인하면 XPS 프린터가 사전 설치되어 있는 것을 찾을 수 있습니다. XPS 파일을 생성하려면 출력 장치로 해당 프린터를 사용할 수 있습니다. Windows 7에서는 파일을 더블 클릭하여 XPS 뷰어에서 열 수 있습니다. Microsoft의 웹사이트에서 [XPS 뷰어](http://windows.microsoft.com/en-US/windows-vista/what-is-the-xps-viewer)를 다운로드할 수도 있습니다.

다음 코드 스니펫은 XPS 파일을 PDF 형식으로 변환하는 과정을 보여줍니다.

```java
public final class ConvertXPStoPDF {

    private ConvertXPStoPDF() {
    }

    final static Path _dataDir = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {
        Convert_XSLFO_to_PDF();
    }

    public static void Convert_XSLFO_to_PDF() throws IOException {
        // 문서 객체 초기화

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();
        String xpsDocumentFileName = Paths.get(_dataDir.toString(), "demo.xml").toString();

        // XPS 로드 옵션을 사용하여 LoadOption 객체 인스턴스화
        LoadOptions options = new XpsLoadOptions();

        // 빈 생성자를 호출하여 Document 객체 인스턴스화
        Document pdfDocument = new Document(xpsDocumentFileName, options);

        // 결과 PDF 파일 저장
        pdfDocument.save(pdfDocumentFileName);
    }
}
```

{{% alert color="success" %}}
**XPS 형식을 PDF로 온라인 변환 시도**

Aspose.PDF for Java는 ["XPS to PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/)라는 무료 온라인 애플리케이션을 제공합니다. 이곳에서 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 변환 XPS to PDF 무료 앱](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## PostScript를 PDF로 변환

**Aspose.PDF for Java**는 PostScript 파일을 PDF 형식으로 변환하는 기능을 지원합니다. Aspose.PDF의 기능 중 하나는 변환 중에 사용할 글꼴 폴더를 설정할 수 있다는 것입니다.

PostScript 파일을 PDF 형식으로 변환하기 위해 Aspose.PDF for Java는 [PsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PsLoadOptions) 클래스를 제공하며, 이는 LoadOptions 객체를 초기화하는 데 사용됩니다. 나중에 이 객체는 Document 객체 생성자에 인수로 전달할 수 있으며, 이는 PDF 렌더링 엔진이 원본 문서의 형식을 결정하는 데 도움이 됩니다.


다음 코드 스니펫은 PostScript 파일을 PDF 형식으로 변환하는 데 사용할 수 있습니다:

```java
public static void ConvertPostScriptToPDF_Simple(){
        // 문서 객체 초기화

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo.pdf").toString();
        String psDocumentFileName = Paths.get(_dataDir.toString(), "demo.ps").toString();
        PsLoadOptions options = new PsLoadOptions();

        // 문서 객체 생성
        Document document = new Document(psDocumentFileName, options);

        // 출력 PDF 문서 저장
        document.save(pdfDocumentFileName);
    }
```

또한, 변환 중에 사용할 글꼴 폴더 집합을 설정할 수 있습니다:

```java
public static void ConvertPostscriptToPDFAvdanced() {
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo.pdf").toString();
        String psDocumentFileName = Paths.get(_dataDir.toString(), "demo.ps").toString();
        PsLoadOptions options = new PsLoadOptions();
        
        options.setFontsFolders(new String[] { "c:\tmp\fonts1", "c:\tmp\fonts2" });

        // 문서 객체 생성
        Document document = new Document(psDocumentFileName, options);

        // 출력 PDF 문서 저장
        document.save(pdfDocumentFileName);
    }
```


## XML을 PDF로 변환

XML 형식은 구조화된 데이터를 저장하는 데 사용됩니다. Aspose.PDF에서 <abbr title="Extensible Markup Language">XML</abbr>을 PDF로 변환하는 몇 가지 방법이 있습니다.

{{% alert color="success" %}}
**온라인에서 XML을 PDF로 변환 시도**

Aspose.PDF for Java는 ["XML to PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf)라는 무료 온라인 애플리케이션을 제공하여 기능과 작동 품질을 조사할 수 있습니다.

[![Aspose.PDF Convertion XML to PDF with Free App](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}

XSL-FO 표준을 기반으로 하는 XML 문서를 사용하는 옵션을 고려하십시오.

### XSL-FO를 PDF로 변환

XSL-FO 파일을 PDF로 변환하는 것은 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) 객체와 [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions)을 사용하여 구현할 수 있습니다.

```java
package com.aspose.pdf.examples;
/**
 * XML을 PDF로 변환
 */

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertXMLtoPDF {

    private ConvertXMLtoPDF() {
    }

    final static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");
    public static void main(String[] args) throws IOException {
        Convert_XSLFO_to_PDF();
        Convert_XSLFO_to_PDF_Adv();
    }

    public static void Convert_XSLFO_to_PDF() throws IOException {
        // 문서 객체 초기화

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();
        String xmlDocumentFileName = Paths.get(_dataDir.toString(), "demo.xml").toString();
        String xsltDocumentFileName = Paths.get(_dataDir.toString(), "employees.xslt").toString();

        XslFoLoadOptions options = new XslFoLoadOptions(xsltDocumentFileName);

        // 빈 생성자를 호출하여 Document 객체 인스턴스화
        Document pdfDocument = new Document(xmlDocumentFileName,options);

        // 결과 PDF 파일 저장
        pdfDocument.save(pdfDocumentFileName);
    }
}
```


### XSL-FO를 PDF로 변환하고 오류 처리 전략 설정

```java
// 문서 객체 초기화

String documentFileName = Paths.get(DATA_DIR.toString(), "demo_txt.pdf").toString();
String xmlDocumentFileName = Paths.get(DATA_DIR.toString(), "demo.xml").toString();
String xsltDocumentFileName = Paths.get(DATA_DIR.toString(), "employees.xslt").toString();

XslFoLoadOptions options = new XslFoLoadOptions(xsltDocumentFileName);

// 오류 처리 전략 설정
options.setParsingErrorsHandlingType(XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately);

// 빈 생성자를 호출하여 Document 객체 인스턴스화
Document document = new Document(xmlDocumentFileName, options);

// 결과 PDF 파일 저장
document.save(documentFileName);
document.close();
```

## LaTeX/TeX를 PDF로 변환

LaTeX 파일 형식은 TeX 언어군의 LaTeX 파생형으로 마크업이 포함된 텍스트 파일 형식이며, LaTeX는 TeX 시스템의 파생 형식입니다.
 LaTeX (ˈleɪtɛk/ lay-tek 또는 lah-tek)는 문서 준비 시스템이자 문서 마크업 언어입니다. 수학, 물리학, 컴퓨터 과학을 포함한 많은 분야에서 과학 문서의 커뮤니케이션 및 출판을 위해 널리 사용됩니다. 또한 산스크리트어 및 아랍어와 같은 복잡한 다국어 자료를 포함한 서적 및 기사의 준비 및 출판에 중요한 역할을 합니다. LaTeX는 출력 형식을 지정하기 위해 TeX 조판 프로그램을 사용하며 자체적으로 TeX 매크로 언어로 작성되었습니다.

**Aspose.PDF for Java**는 TeX 파일을 PDF 형식으로 변환하는 기능을 지원하며, 이 요구 사항을 충족하기 위해 com.aspose.pdf 패키지에는 LaTex 파일을 로드하고 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) 클래스를 사용하여 PDF 형식으로 출력물을 렌더링하는 기능을 제공하는 [LatexLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LatexLoadOptions)라는 클래스가 있습니다. 다음 코드 스니펫은 LaTex 파일을 PDF 형식으로 변환하는 과정을 보여줍니다.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertLATEXtoPDF {

    private ConvertLATEXtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // LaTex 로드 옵션 객체를 인스턴스화합니다.
        TeXLoadOptions options = new TeXLoadOptions();
        
        // 문서 객체를 생성합니다.
        String latexFileName = Paths.get(_dataDir.toString(), "samplefile.tex").toString();
        Document document = new Document(latexFileName, options);

        // 출력 PDF 문서를 저장합니다.
        document.save(Paths.get(_dataDir.toString(),"TEXtoPDF.pdf").toString());
    }
}
```

{{% alert color="success" %}}
**온라인에서 LaTeX/TeX를 PDF로 변환해보세요**

Aspose.PDF for Java는 ["LaTex to PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf)라는 무료 온라인 애플리케이션을 제공합니다. 여기에서 기능과 품질을 조사해 볼 수 있습니다.
[![Aspose.PDF 변환 LaTeX/TeX를 PDF로 무료 앱과 함께](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}