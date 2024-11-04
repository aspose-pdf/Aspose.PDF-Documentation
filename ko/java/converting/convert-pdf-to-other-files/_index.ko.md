---
title: PDF 파일을 다른 형식으로 변환하기
linktitle: PDF를 다른 형식으로 변환하기
type: docs
weight: 90
url: /java/convert-pdf-to-other-files/
lastmod: "2021-11-19"
description: 이 주제는 Aspose.PDF가 PDF 파일을 다른 파일 형식으로 변환할 수 있도록 하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## PDF를 EPUB로 변환하기

{{% alert color="success" %}}
**PDF를 EPUB로 온라인으로 변환 시도하기**

Aspose.PDF for Java는 무료 온라인 애플리케이션 ["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)를 제공하여 기능과 품질을 직접 확인해 볼 수 있습니다.

[![Aspose.PDF Convertion PDF to EPUB with Free App](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Electronic Publication">EPUB</abbr>** (전자 출판의 약자)는 국제 디지털 출판 포럼(IDPF)의 무료 오픈 전자책 표준입니다.
 파일은 .epub 확장자를 가지고 있습니다. EPUB은 특정 디스플레이 장치에 맞게 텍스트를 최적화할 수 있는 리플로우 가능한 콘텐츠를 위해 설계되었습니다. EPUB은 고정 레이아웃 콘텐츠도 지원합니다. 이 형식은 출판사와 변환 업체가 내부적으로 사용할 수 있으며, 배포 및 판매를 위한 단일 형식으로 의도되었습니다. 이는 Open eBook 표준을 대체합니다.

Aspose.PDF for Java는 PDF 문서를 EPUB 형식으로 변환하는 기능을 지원합니다. Aspose.PDF for Java에는 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..) 메서드의 두 번째 인수로 사용할 수 있는 [EpubSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubSaveOptions)라는 클래스가 있어 EPUB 파일을 생성할 수 있습니다. 이 요구 사항을 충족하기 위해 다음 코드 스니펫을 사용해 보세요.

```java
// PDF 문서 로드
Document document = new Document(DATA_DIR + "PDFToEPUB.pdf");
// Epub 저장 옵션 인스턴스화
EpubSaveOptions options = new EpubSaveOptions();
// 콘텐츠에 대한 레이아웃 지정
options.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.Flow);
// ePUB 문서 저장
document.save(DATA_DIR + "PDFToEPUB_out.epub", options);
document.close();
```

## PDF를 LaTeX/TeX로 변환

**Aspose.PDF for Java**는 PDF를 LaTeX/TeX로 변환하는 것을 지원합니다. LaTeX 파일 형식은 전문적인 조판을 위한 TeX 기반 문서 준비 시스템에서 사용되는 특수 마크업이 있는 텍스트 파일 형식입니다.

PDF 파일을 TeX로 변환하기 위해, Aspose.PDF는 변환 과정 중 임시 이미지를 저장하기 위한 `setOutDirectoryPath` 메서드를 제공하는 [TeXSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TeXSaveOptions) 클래스를 갖고 있습니다.

다음 코드 스니펫은 Java로 PDF 파일을 TEX 형식으로 변환하는 과정을 보여줍니다.

```java
String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToTeX.pdf").toString();
String texDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToTeX_out.tex").toString();

// Document 객체 생성
Document document = new Document(documentFileName);

// LaTex 저장 옵션 인스턴스화
TeXSaveOptions saveOptions = new TeXSaveOptions();

// 출력 디렉토리 지정
String pathToOutputDirectory = DATA_DIR.toString();

// 저장 옵션 객체에 출력 디렉토리 경로 설정
saveOptions.setOutDirectoryPath(pathToOutputDirectory);

// PDF 파일을 LaTex 형식으로 저장
document.save(texDocumentFileName, saveOptions);
document.close();
```


{{% alert color="success" %}}
**PDF를 LaTeX/TeX로 온라인 변환 시도**

Aspose.PDF for Java는 온라인 무료 애플리케이션 ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)를 제공합니다. 여기서 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF Convertion PDF to LaTeX/TeX with Free App](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## PDF를 텍스트로 변환

**Aspose.PDF for Java**는 전체 PDF 문서와 단일 페이지를 텍스트 파일로 변환하는 것을 지원합니다.

### 전체 PDF 문서를 텍스트 파일로 변환

[TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) 클래스의 Visit 메소드를 사용하여 PDF 문서를 TXT 파일로 변환할 수 있습니다.

다음 코드 스니펫은 모든 페이지에서 텍스트를 추출하는 방법을 설명합니다.

```java
// 문서 열기
String pdfFileName = Paths.get(DATA_DIR.toString(), "demo.pdf").toString();
String txtFileName = Paths.get(DATA_DIR.toString(), "PDFToTXT_out.txt").toString();

// PDF 문서 로드
Document document = new Document(pdfFileName);
TextAbsorber ta = new TextAbsorber();
ta.visit(document);
// 추출된 텍스트를 텍스트 파일에 저장
BufferedWriter writer = new BufferedWriter(new FileWriter(txtFileName));
writer.write(ta.getText());
writer.close();
```


{{% alert color="success" %}}
**PDF를 텍스트로 온라인 변환 시도하기**

Aspose.PDF for Java는 온라인 무료 애플리케이션 ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt)을 제공하여 기능과 품질을 조사할 수 있습니다.

[![Aspose.PDF 변환 PDF를 텍스트로 무료 앱으로](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

### PDF 페이지를 텍스트 파일로 변환하기

Aspose.PDF for Java를 사용하여 PDF 문서를 TXT 파일로 변환할 수 있습니다. 이 작업을 해결하려면 [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) 클래스의 Visit 메서드를 사용해야 합니다.

다음 코드 스니펫은 특정 페이지에서 텍스트를 추출하는 방법을 설명합니다.

```java
String pdfFileName = Paths.get(DATA_DIR.toString(), "demo.pdf").toString();
String txtFileName = Paths.get(DATA_DIR.toString(), "PDFToTXT_out.txt").toString();

// PDF 문서 로드
Document document = new Document(pdfFileName);

TextAbsorber ta = new TextAbsorber();
int[] pages = new int[] { 1, 3, 4 };

for (int page : pages) {
    ta.visit(document.getPages().get_Item(page));
}

// 추출한 텍스트를 텍스트 파일에 저장
BufferedWriter writer = new BufferedWriter(new FileWriter(txtFileName));
writer.write(ta.getText());
writer.close();
document.close();
```


## PDF를 XPS로 변환하기

**Aspose.PDF for Java**는 PDF 파일을 <abbr title="XML Paper Specification">XPS</abbr> 형식으로 변환할 수 있는 기능을 제공합니다. Java로 PDF 파일을 XPS 형식으로 변환하기 위해 제공된 코드 스니펫을 사용해 봅시다.

{{% alert color="success" %}}
**PDF를 XPS로 온라인 변환 시도하기**

Aspose.PDF for Java는 ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)라는 무료 온라인 응용 프로그램을 제공합니다. 여기서 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 변환 PDF를 XPS로 무료 앱으로](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

XPS 파일 형식은 주로 Microsoft Corporation의 XML Paper Specification과 연관되어 있습니다. XML Paper Specification (XPS)은 이전에 Metro라는 코드명이 붙여졌으며, 차세대 인쇄 경로(NGPP) 마케팅 개념을 포함하는 Microsoft의 Windows 운영 체제에 문서 생성 및 보기 통합을 위한 이니셔티브입니다.

PDF 파일을 XPS로 변환하려면 Aspose.PDF는 XPS 파일을 생성하기 위해 Document.save(..) 생성자의 두 번째 인수로 사용되는 [XpsSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsSaveOptions) 클래스를 제공합니다.
 다음 코드 스니펫은 PDF 파일을 XPS 형식으로 변환하는 과정을 보여줍니다.

```java
String documentFileName = Paths.get(DATA_DIR.toString(), "sample.pdf").toString();
String xpsDocumentFileName = Paths.get(DATA_DIR.toString(), "sample-res-xps.xps").toString();

// Document 객체 생성
Document document = new Document(documentFileName);

// XPS 저장 옵션 인스턴스화
XpsSaveOptions saveOptions = new XpsSaveOptions();

// XML 형식으로 출력 저장
document.save(xpsDocumentFileName, saveOptions);
document.close();
```