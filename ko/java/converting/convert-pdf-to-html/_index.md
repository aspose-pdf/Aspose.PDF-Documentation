---
title: PDF 파일을 HTML 형식으로 변환 
linktitle: PDF 파일을 HTML 형식으로 변환
type: docs
weight: 50
url: /ko/java/convert-pdf-to-html/
lastmod: "2021-11-19"
description: 이 주제는 Aspose.PDF가 Java 라이브러리를 사용하여 PDF 파일을 HTML 형식으로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

Aspose.PDF for Java는 다양한 파일 형식을 PDF 문서로 변환하고 PDF 파일을 다양한 출력 형식으로 변환하기 위한 많은 기능을 제공합니다. 이 기사에서는 PDF 파일을 HTML 형식으로 변환하고 PDF 파일의 이미지를 특정 폴더에 저장하는 방법을 설명합니다.

{{% alert color="success" %}}
**PDF를 HTML로 온라인으로 변환해보세요**

Aspose.PDF for Java는 ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html)이라는 온라인 무료 애플리케이션을 제공합니다. 여기서 기능과 품질을 조사해볼 수 있습니다.

[![Aspose.PDF 변환 PDF to HTML 무료 앱](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)

{{% /alert %}}

큰 PDF 파일을 여러 페이지로 HTML 형식으로 변환할 때, 출력은 단일 HTML 페이지로 나타납니다. 이는 매우 길어질 수 있습니다. 페이지 크기를 제어하기 위해, PDF를 HTML로 변환하는 동안 출력을 여러 페이지로 분할할 수 있습니다.

## PDF 페이지를 HTML로 변환

Aspose.PDF for Java는 다양한 파일 형식을 PDF 문서로 변환하고 PDF 파일을 다양한 출력 형식으로 변환하는 많은 기능을 제공합니다. 이 문서에서는 PDF 파일을 HTML 형식으로 변환하고 PDF 파일의 이미지를 특정 폴더에 저장하는 방법을 설명합니다.

다음 코드 스니펫은 PDF를 HTML로 변환할 때 사용할 수 있는 모든 가능한 옵션을 보여줍니다.

```java
// 소스 PDF 문서를 엽니다
Document pdfDocument = new Document(_dataDir + "PDFToHTML.pdf");

// 파일을 MS 문서 형식으로 저장합니다
pdfDocument.save(_dataDir + "output_out.html", SaveFormat.Html);
```

## PDF를 HTML로 변환 - 출력 분할하여 다중 페이지 HTML로

Aspose.PDF for Java는 PDF 문서를 HTML을 포함한 다양한 출력 형식으로 변환하는 기능을 지원합니다.
 그러나 대용량 PDF 파일(여러 페이지로 구성된 경우)을 변환할 때 개별 PDF 페이지를 별도의 HTML 파일로 저장해야 할 수도 있습니다.

여러 페이지로 구성된 대용량 PDF 파일을 HTML 형식으로 변환할 때 출력이 단일 HTML 페이지로 나타납니다. 이는 매우 길어질 수 있습니다. 페이지 크기를 제어하기 위해 PDF를 HTML로 변환하는 동안 출력을 여러 페이지로 나누는 것이 가능합니다. 다음 코드 스니펫을 사용해 보세요.

```java
// 소스 PDF 문서 열기
Document document = new Document(_dataDir + "PDFToHTML.pdf");

// HTML SaveOptions 객체 인스턴스화
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();

// 출력을 여러 페이지로 나누도록 지정
htmlOptions.setSplitIntoPages(true);

// 문서 저장
document.save(_dataDir + "MultiPageHTML_out.html", htmlOptions);    
```

## PDF를 HTML로 변환 - 이미지를 SVG 형식으로 저장하지 않기

PDF를 HTML로 변환할 때 이미지 저장의 기본 출력 형식은 SVG입니다. PDF 변환 중 일부 이미지는 SVG 벡터 이미지로 변환됩니다. 이 과정은 느릴 수 있습니다. 대신 이미지를 PNG로 변환할 수 있습니다. 이를 허용하기 위해 Aspose.PDF는 벡터에 SVG를 사용하거나 PNG를 생성하는 옵션을 제공합니다.

PDF 파일을 HTML 형식으로 변환할 때 이미지의 SVG 형식 렌더링을 완전히 제거하려면 다음 코드 스니펫을 사용해 보십시오.

```java
 // PDF 파일 로드
Document document = new Document(DATA_DIR + "PDFToHTML.pdf")

// HTML 저장 옵션 객체 인스턴스화
HtmlSaveOptions saveOptions = new HtmlSaveOptions();

// PDF를 HTML로 변환하는 동안 SVG 이미지가 저장되는 폴더 지정
saveOptions.setSpecialFolderForSvgImages(DATA_DIR.toString());

// 출력 파일 저장
document.save(DATA_DIR + "SaveSVGFiles_out.html", saveOptions);
```

## 변환 중 SVG 이미지 압축

PDF를 HTML로 변환하는 동안 SVG 이미지를 압축하려면 다음 코드를 사용해 보십시오.

```java
// PDF 파일 로드
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");

// 테스트된 기능으로 HtmlSaveOption 생성
HtmlSaveOptions saveOptions = new HtmlSaveOptions();

// SVG 이미지를 압축합니다(있는 경우)
saveOptions.setCompressSvgGraphicsIfAny(true);
document.save(DATA_DIR + "SaveSVGFiles_out.html", saveOptions);
document.close();
```

## PDF를 HTML로 변환 - 이미지 폴더 지정

기본적으로 PDF 파일을 HTML로 변환할 때, PDF의 이미지는 출력 HTML이 생성되는 동일한 디렉토리에 생성된 별도의 폴더에 저장됩니다. 그러나 때때로 HTML 파일을 생성할 때 이미지를 저장할 다른 폴더를 지정해야 할 필요가 있습니다. 이를 위해 [SaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SaveOptions)를 도입했습니다. [SpecialFolderForAllImages 메서드](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/#setSpecialFolderForAllImages-java.lang.String-)는 이미지를 저장할 대상 폴더를 지정하는 데 사용됩니다.

```java
// PDF 파일을 로드합니다
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");
HtmlSaveOptions saveOptions = new HtmlSaveOptions();

// 이미지를 저장할 별도의 폴더를 지정합니다
saveOptions.setSpecialFolderForAllImages(DATA_DIR.toString());
document.save(DATA_DIR + "SaveSVGFiles_out.html", saveOptions);
document.close();
```

## 본문 내용만 포함된 후속 파일 생성

다음의 간단한 코드 스니펫을 사용하여 출력 HTML을 페이지로 분할할 수 있습니다. 출력 페이지에서는 모든 HTML 객체가 현재 위치에 정확히 위치해야 합니다 (폰트 처리 및 출력, CSS 생성 및 출력, 이미지 생성 및 출력), 다만 출력 HTML은 현재 태그 내부에 배치된 콘텐츠를 포함할 것입니다 (이제 “body” 태그는 생략됩니다).

```java
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");

HtmlSaveOptions saveOptions = new HtmlSaveOptions();

saveOptions.setHtmlMarkupGenerationMode(HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent);
saveOptions.setSplitIntoPages(true);

document.save(DATA_DIR + "CreateSubsequentFiles_out.html", saveOptions);
document.close();
```

## 투명 텍스트 렌더링

소스/입력 PDF 파일에 전경 이미지에 의해 가려진 투명 텍스트가 포함된 경우, 텍스트 렌더링 문제 발생 가능성이 있습니다. 이러한 시나리오를 처리하기 위해 `setSaveShadowedTextsAsTransparentTexts` 및 `setSaveTransparentTexts` 메서드를 사용할 수 있습니다.

```java
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");

// HTML SaveOptions 객체를 인스턴스화
HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();
htmlsaveOptions.setSaveShadowedTextsAsTransparentTexts(true);
htmlsaveOptions.setSaveTransparentTexts(true);

// 문서 저장
document.save(DATA_DIR + "TransparentTextRendering_out.html", htmlsaveOptions);
document.close();
```


## PDF 문서 레이어 렌더링

PDF를 HTML로 변환하는 동안 PDF 문서 레이어를 별도의 레이어 타입 요소로 렌더링할 수 있습니다:

```java
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");
// HTML 저장 옵션 객체를 인스턴스화합니다.

HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();

// 출력 HTML에서 PDF 문서 레이어를 별도로 렌더링하도록 지정합니다.
htmlsaveOptions.setConvertMarkedContentToLayers(true);

// 문서를 저장합니다.
document.save(DATA_DIR + "LayersRendering_out.html", htmlsaveOptions);
document.close();
```

PDF를 HTML로 변환하는 것은 Aspose.PDF의 가장 인기 있는 기능 중 하나입니다. 이는 PDF 문서 뷰어를 사용하지 않고도 다양한 플랫폼에서 PDF 파일의 내용을 볼 수 있게 해주기 때문입니다. 출력 HTML은 WWW 표준에 부합하며 모든 웹 브라우저에서 쉽게 표시될 수 있습니다. 이 기능을 사용하여 PDF 파일을 손에 들고 있는 기기에서 볼 수 있습니다. PDF 보기 응용 프로그램을 설치할 필요가 없고 간단한 웹 브라우저를 사용할 수 있기 때문입니다.

## PDF to HTML - 폰트 리소스 제외

PDF를 HTML로 변환할 때 모든 또는 일부 폰트 리소스를 제외하려는 경우, Aspose.PDF for Java API를 사용하여 HtmlSaveOptions 클래스를 통해 이를 달성할 수 있습니다. 이 목적을 위해 API는 두 가지 옵션을 제공합니다.

- `htmlOptions.FontSavingMode = HTmlSaveOptions.FontSavingModes.DontSave` - 모든 폰트의 내보내기를 방지하기 위해
- `htmlOptions.ExcludeFontNameList = (new String[] { "ArialMT", "SymbolMT" });` - 특정 폰트의 내보내기를 방지하기 위해 (폰트 이름은 해시 없이 지정되어야 함)

폰트 리소스를 제외하고 PDF를 HTML로 변환하려면 다음 단계를 사용하십시오:

1. HtmlSaveOptions 클래스의 새 객체를 정의합니다
1. HtmlSaveOptions.ExcludeFontNameList에서 내보내기를 방지할 폰트 이름을 정의하고 설정합니다
1. save 메서드를 사용하여 PDF를 HTML로 변환합니다

```java
HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();
htmlsaveOptions.setExplicitListOfSavedPages(
        new int[]{
                1
        }
);
htmlsaveOptions.setFixedLayout(true);
htmlsaveOptions.setCompressSvgGraphicsIfAny(false);
htmlsaveOptions.setSaveTransparentTexts(true);
htmlsaveOptions.setSaveShadowedTextsAsTransparentTexts(true);
htmlsaveOptions.setExcludeFontNameList(new String[]{"ArialMT", "SymbolMT"});
htmlsaveOptions.setFontSavingMode(HtmlSaveOptions.FontSavingModes.DontSave);
htmlsaveOptions.setDefaultFontName("Comic Sans MS");
htmlsaveOptions.setUseZOrder(true);
htmlsaveOptions
        .setLettersPositioningMethod(LettersPositioningMethods.UseEmUnitsAndCompensationOfRoundingErrorsInCss);
htmlsaveOptions
        .setPartsEmbeddingMode(HtmlSaveOptions.PartsEmbeddingModes.NoEmbedding);
htmlsaveOptions
        .setRasterImagesSavingMode(HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground);
htmlsaveOptions.setSplitIntoPages(false);

Document document = new Document(DATA_DIR + "sample.pdf");
document.save(DATA_DIR + "output_out.html", htmlsaveOptions);
document.close();
```