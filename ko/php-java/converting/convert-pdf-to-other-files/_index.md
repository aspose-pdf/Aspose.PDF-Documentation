---
title: PDF 파일을 다른 형식으로 변환하기
linktitle: PDF를 다른 형식으로 변환하기
type: docs
weight: 90
url: /ko/php-java/convert-pdf-to-other-files/
lastmod: "2024-05-20"
description: 이 주제는 Aspose.PDF가 PDF 파일을 다른 파일 형식으로 변환할 수 있는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## PDF를 EPUB로 변환하기

{{% alert color="success" %}}
**PDF를 EPUB로 온라인에서 변환해보세요**

Aspose.PDF for PHP는 ["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)라는 무료 온라인 애플리케이션을 제공합니다. 여기서 기능과 품질을 조사해볼 수 있습니다.

[![Aspose.PDF 변환 PDF to EPUB with Free App](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Electronic Publication">EPUB</abbr>** (전자 출판의 약자)은 국제 디지털 출판 포럼(IDPF)에서 제공하는 무료 오픈 전자책 표준입니다.
 파일은 .epub 확장자를 가집니다. EPUB은 콘텐츠를 특정 디스플레이 장치에 맞게 최적화할 수 있는 가변형 콘텐츠로 설계되었습니다. EPUB은 고정 레이아웃 콘텐츠도 지원합니다. 이 형식은 출판사와 변환 업체가 내부에서 사용할 수 있는 단일 형식으로 의도되었으며 배포 및 판매에 사용됩니다. 이는 Open eBook 표준을 대체합니다.

Aspose.PDF for PHP는 PDF 문서를 EPUB 형식으로 변환하는 기능을 지원합니다. Aspose.PDF for PHP에는 [Document.save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#save-java.lang.String-) 메서드의 두 번째 인수로 사용하여 EPUB 파일을 생성할 수 있는 [EpubSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubSaveOptions)라는 클래스가 있습니다. 이 요구 사항을 충족시키기 위해 다음 코드 스니펫을 사용해 보십시오.

```php
// Document 클래스의 새 인스턴스를 생성하고 입력 PDF 파일을 로드합니다.
$document = new Document($inputFile);

// EpubSaveOptions 클래스의 새 인스턴스를 생성합니다.
$saveOption = new EpubSaveOptions();

// 지정된 저장 옵션을 사용하여 문서를 EPUB 형식으로 저장합니다.
$document->save($outputFile, $saveOption);
```

## PDF를 LaTeX/TeX으로 변환

**Aspose.PDF for PHP**는 PDF를 LaTeX/TeX으로 변환하는 것을 지원합니다. LaTeX 파일 형식은 특별한 마크업이 있는 텍스트 파일 형식이며, 고품질 조판을 위한 TeX 기반 문서 준비 시스템에서 사용됩니다.

PDF 파일을 TeX로 변환하기 위해 Aspose.PDF는 변환 과정 중 임시 이미지를 저장하기 위한 `setOutDirectoryPath` 메서드를 제공하는 [LaTeXSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LaTeXSaveOptions) 클래스를 제공합니다.

다음 코드 스니펫은 Java로 PDF 파일을 TEX 형식으로 변환하는 과정을 보여줍니다.

```php
// 새로운 Document 객체를 생성하고 입력 PDF 파일을 로드합니다
$document = new Document($inputFile);

// 새로운 LaTeXSaveOptions 객체를 생성합니다
$saveOption = new LaTeXSaveOptions();
$saveOption->setOutDirectoryPath ($pathToOutputDirectory)

// 문서를 LaTeX로 저장합니다
$document->save($outputFile, $saveOption);
```

{{% alert color="success" %}}
**PDF를 LaTeX/TeX으로 온라인으로 변환해보세요**

Aspose.PDF for PHP는 ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)라는 온라인 무료 애플리케이션을 제공합니다. 여기서 기능과 품질을 조사해볼 수 있습니다.

[![Aspose.PDF Convertion PDF to LaTeX/TeX with Free App](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## PDF를 텍스트로 변환

**Aspose.PDF for PHP**는 전체 PDF 문서와 단일 페이지를 텍스트 파일로 변환하는 것을 지원합니다.

### 전체 PDF 문서를 텍스트 파일로 변환

[TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) 클래스의 Visit 메소드를 사용하여 PDF 문서를 TXT 파일로 변환할 수 있습니다.

다음 코드 스니펫은 모든 페이지에서 텍스트를 추출하는 방법을 설명합니다.

```php
// PDF 문서 로드
$document = new Document($inputFile);

// 문서에서 텍스트를 추출하기 위한 TextAbsorber 객체 생성
$textAbsorber = new TextAbsorber();

// 문서에서 텍스트 추출
$textAbsorber->visit($document);
$content = $textAbsorber->getText();

// 추출한 텍스트를 출력 파일에 저장
file_put_contents($outputFile, $content);

// 출력 파일의 파일 크기 가져오기
$fileSize = filesize($outputFile);
```

{{% alert color="success" %}}
 **PDF를 텍스트로 온라인 변환 시도**

Aspose.PDF for PHP는 ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt)라는 무료 온라인 응용 프로그램을 제공하여 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 변환 PDF를 무료 앱으로 텍스트로](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

### PDF 페이지를 텍스트 파일로 변환

Aspose.PDF for PHP를 사용하여 PDF 문서를 TXT 파일로 변환할 수 있습니다. 이 작업을 해결하려면 [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) 클래스의 Visit 메서드를 사용해야 합니다.

다음 코드 스니펫은 특정 페이지에서 텍스트를 추출하는 방법을 설명합니다.

```php
// PDF 문서 로드
$document = new Document($inputFile);

// 문서에서 텍스트를 추출하기 위한 TextAbsorber 객체 생성
$textAbsorber = new TextAbsorber();

$array = array(1, 3, 4);

foreach ($array as $page) {
    $textAbsorber->visit($document->getPages()->get_Item($page));
    $content = $textAbsorber->getText();
    
    $outputFile = $dataDir . DIRECTORY_SEPARATOR . 'result-pdf-to-text'. $page . '.txt';
    // 추출된 텍스트를 출력 파일에 저장
    file_put_contents($outputFile, $content);
}
```


## PDF를 XPS로 변환

**Aspose.PDF for PHP**는 PDF 파일을 <abbr title="XML Paper Specification">XPS</abbr> 형식으로 변환할 수 있는 기능을 제공합니다. Java를 사용하여 PDF 파일을 XPS 형식으로 변환하기 위해 제공된 코드 스니펫을 사용해 보겠습니다.

{{% alert color="success" %}}
**온라인에서 PDF를 XPS로 변환해보세요**

Aspose.PDF for PHP는 온라인 무료 애플리케이션 ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)를 제공합니다. 여기서 기능과 성능을 조사해볼 수 있습니다.

[![Aspose.PDF 변환 PDF를 XPS로 무료 앱으로](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

XPS 파일 형식은 주로 Microsoft Corporation의 XML Paper Specification과 관련이 있습니다. XML Paper Specification(XPS)은 이전에 Metro라는 코드명이었고 차세대 인쇄 경로(NGPP) 마케팅 개념을 포함하며, Windows 운영 체제에 문서 생성 및 보기 기능을 통합하려는 Microsoft의 이니셔티브입니다.

PDF 파일을 XPS로 변환하기 위해, Aspose.PDF는 [XpsSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsSaveOptions) 클래스를 제공합니다. 이 클래스는 XPS 파일을 생성하기 위해 Document.save(..) 생성자의 두 번째 인수로 사용됩니다.
 다음 코드 스니펫은 PDF 파일을 XPS 형식으로 변환하는 과정을 보여줍니다.

```php
// 새 Document 객체를 생성하고 입력 PDF 파일을 로드합니다
$document = new Document($inputFile);

// 새 XpsSaveOptions 객체를 생성합니다
$saveOption = new XpsSaveOptions();

// 지정된 저장 옵션을 사용하여 문서를 XPS로 저장합니다
$document->save($outputFile, $saveOption);
```