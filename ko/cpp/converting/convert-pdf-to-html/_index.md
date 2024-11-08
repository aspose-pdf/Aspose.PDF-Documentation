---
title: PDF 파일을 HTML 형식으로 변환
linktitle: PDF 파일을 HTML 형식으로 변환
type: docs
weight: 50
url: /ko/cpp/convert-pdf-to-html/
lastmod: "2021-11-19"
description: 이 주제는 C++ 라이브러리를 사용하여 Aspose.PDF가 PDF 파일을 HTML 형식으로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for C++**는 다양한 파일 형식을 PDF 문서로 변환하고 PDF 파일을 다양한 출력 형식으로 변환하는 많은 기능을 제공합니다. 이 문서에서는 PDF 파일을 <abbr title="HyperText Markup Language">HTML</abbr>로 변환하는 방법에 대해 설명합니다. Aspose.PDF for C++는 InLineHtml 접근 방식을 사용하여 HTML 파일을 PDF 형식으로 변환하는 기능을 제공합니다. 우리는 PDF 파일을 HTML 형식으로 변환하는 기능에 대한 많은 요청을 받았으며 이 기능을 제공했습니다. 이 기능은 XHTML 1.0도 지원한다는 점에 유의하십시오.

**Aspose.PDF for C++**는 PDF 파일을 HTML로 변환하는 기능을 지원합니다. Aspose.PDF 라이브러리로 수행할 수 있는 주요 작업은 다음과 같습니다:

- PDF를 HTML로 변환;
- 출력물을 다중 페이지 HTML로 분할;
- SVG 파일 저장 폴더 지정;
- 변환 중 SVG 이미지 압축;
- 이미지 폴더 지정;
- 본문 내용만 있는 후속 파일 생성;
- 투명 텍스트 렌더링;
- PDF 문서 레이어 렌더링.

Aspose.PDF for C++는 소스 PDF 파일을 HTML로 변환하는 두 줄의 코드를 제공합니다. `SaveFormat 열거형`은 소스 파일을 HTML로 저장할 수 있는 Html 값을 포함합니다. 다음 코드 스니펫은 PDF 파일을 HTML로 변환하는 과정을 보여줍니다.

```cpp
void ConvertPDFtoHTML()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름에 대한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 파일 이름에 대한 문자열
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
    // HTML 형식으로 출력 저장
    document->Save(outfilename, SaveFormat::Html);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```
{{% alert color="success" %}}
**PDF를 HTML로 온라인 변환 시도하기**

Aspose.PDF for C++는 ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html)라는 무료 온라인 애플리케이션을 제공합니다. 여기서 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF Convertion PDF to HTML with Free App](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

## 출력 분할을 여러 페이지 HTML로

여러 페이지가 있는 큰 PDF 파일을 HTML 형식으로 변환할 때 출력은 단일 HTML 페이지로 나타납니다. 이는 매우 길어질 수 있습니다. 페이지 크기를 제어하려면 PDF를 HTML로 변환하는 동안 출력을 여러 페이지로 분할할 수 있습니다. 다음 코드 스니펫을 사용해 보세요.

```cpp
void ConvertPDFtoHTML_SplittingOutputToMultiPageHTML()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 파일 이름을 위한 문자열
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    // HTML 저장 옵션 객체 인스턴스화
    auto htmlOptions = MakeObject<HtmlSaveOptions>();
    // 출력을 여러 페이지로 분할하도록 지정
    htmlOptions->set_SplitIntoPages(true);

    try {
    // 출력을 HTML 형식으로 저장
    document->Save(_dataDir + outfilename, htmlOptions);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## SVG 파일 저장 폴더 지정

PDF를 HTML로 변환하는 동안 SVG 이미지를 저장할 폴더를 지정할 수 있습니다. [`HtmlSaveOption class`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options) [`SpecialFolderForSvgImages property`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options#ac1bb3905c599118fb3db67fd67a5a06f)을 사용하여 특별한 SVG 이미지 디렉토리를 지정합니다. 이 속성은 변환 중에 발견된 SVG 이미지를 저장해야 하는 디렉토리의 경로를 가져오거나 설정합니다. 매개변수가 비어 있거나 null인 경우, 모든 SVG 파일은 다른 이미지 파일과 함께 저장됩니다.

```cpp
void ConvertPDFtoHTML_SpecifyFolderForStoringSVGfiles()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름에 대한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 파일 이름에 대한 문자열
    String infilename("sample.pdf");
    String outfilename("SaveSVGFiles_out.html");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    // HTML 저장 옵션 객체 인스턴스화
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // PDF를 HTML로 변환하는 동안 SVG 이미지가 저장될 폴더 지정
    htmlOptions->SpecialFolderForSvgImages = (_dataDir + String("\\svg\\"));

    // HTML 형식으로 출력 저장
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## PDF를 HTML로 변환하는 동안 SVG 이미지 압축

PDF를 HTML로 변환하는 동안 SVG 이미지를 압축하려면 다음 코드를 사용해 보십시오:

```cpp
void ConvertPDFtoHTML_CompressingSVGimages()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 파일 이름을 위한 문자열
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    // HTML 저장 옵션 객체 인스턴스화
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // PDF를 HTML로 변환하는 동안 SVG 이미지가 저장되는 폴더 지정
    htmlOptions->SpecialFolderForSvgImages = (_dataDir + String("\\svg\\"));

    // HTML 형식으로 출력 저장
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## 이미지 폴더 지정

PDF를 HTML로 변환하는 동안 이미지가 저장될 폴더를 지정할 수도 있습니다:

```cpp
void ConvertPDFtoHTML_SpecifyFolderForStoringAllImages()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for file name
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instantiate HTML Save Option object
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // Specify the folder where All images are saved during PDF to HTML conversion
    htmlOptions->SpecialFolderForAllImages = (_dataDir + String("\\images\\"));

    // Save the output in HTML format
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## 본문 내용만 포함하는 후속 파일 만들기

최근에 PDF 파일을 HTML로 변환하고 사용자가 각 페이지의 `<body>` 태그 내용만 가져올 수 있는 기능을 도입해 달라는 요청을 받았습니다. 이 코드 조각은 CSS, `<html>`, `<head>` 세부 사항이 포함된 하나의 파일과 다른 파일들에는 `<body>` 내용만 포함된 페이지를 생성합니다.

이 요구사항을 충족하기 위해 [HtmlSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options) 클래스에 새로운 속성인 HtmlMarkupGenerationMode가 도입되었습니다.

다음의 간단한 코드 조각을 사용하여 출력 HTML을 페이지로 분할할 수 있습니다. 출력 페이지에서는 모든 HTML 객체가 현재 위치에 정확히 가야 합니다 (폰트 처리 및 출력, CSS 생성 및 출력, 이미지 생성 및 출력), 단 출력 HTML은 현재 태그 내부에 배치된 내용을 포함하게 됩니다 (이제 “body” 태그는 생략됩니다). 그러나 이 접근 방식을 사용할 때 CSS에 대한 링크는 코드의 책임입니다, 왜냐하면 같은 것들은 제거될 것이기 때문입니다. 이를 위해, File.ReadAllText()를 통해 CSS를 읽고 AJAX를 통해 웹 페이지로 전송하여 jQuery에 의해 적용되도록 할 수 있습니다.

```cpp
void ConvertPDFtoHTML_CreateSubsequentFilesWithBodyContentsOnly()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 파일 이름을 위한 문자열
    String infilename("sample.pdf");
    String outfilename("CreateSubsequentFiles_out.html");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    // HTML 저장 옵션 객체 인스턴스화
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    htmlOptions->HtmlMarkupGenerationMode = HtmlSaveOptions::HtmlMarkupGenerationModes::WriteOnlyBodyContent;
    htmlOptions->set_SplitIntoPages(true);

    // 출력물을 HTML 형식으로 저장
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
## 투명 텍스트 렌더링

소스/입력 PDF 파일에 전경 이미지로 가려진 투명 텍스트가 포함된 경우, 텍스트 렌더링 문제가 발생할 수 있습니다. 이러한 시나리오를 처리하기 위해 [SaveShadowedTextsAsTransparentTexts](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options#a6269cf414eb8c252f0ba64a0baf2f9ef) 및 SaveTransparentTexts 속성을 사용할 수 있습니다.

```cpp
void ConvertPDFtoHTML_TransparentTextRendering()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 파일 이름을 위한 문자열
    String infilename("sample.pdf");
    String outfilename("TransparentTextRendering_out.html");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    // HTML 저장 옵션 객체 인스턴스화
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    htmlOptions->HtmlMarkupGenerationMode = HtmlSaveOptions::HtmlMarkupGenerationModes::WriteOnlyBodyContent;
    htmlOptions->SaveShadowedTextsAsTransparentTexts = true;
    htmlOptions->SaveTransparentTexts = true;

    // HTML 형식으로 출력 저장
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## PDF 문서 레이어 렌더링

우리는 PDF를 HTML로 변환하는 동안 별도의 레이어 타입 요소로 PDF 문서 레이어를 렌더링할 수 있습니다:

```cpp
void ConvertPDFtoHTML_DocumentLayersRendering()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 파일 이름을 위한 문자열
    String infilename("sample.pdf");
    String outfilename("LayersRendering_out.html");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    // HTML 저장 옵션 객체 생성
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // 출력 HTML에서 PDF 문서 레이어를 별도로 렌더링하도록 지정
    htmlOptions->set_ConvertMarkedContentToLayers(true);

    // HTML 형식으로 출력 저장
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```