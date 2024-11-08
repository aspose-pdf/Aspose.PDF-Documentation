---
title: PDF에 텍스트 스탬프 추가 프로그래밍 방식으로
linktitle: PDF 파일에 텍스트 스탬프
type: docs
weight: 20
url: /ko/java/text-stamps-in-the-pdf-file/
description: Java를 사용하여 TextStamp 클래스를 통해 PDF 파일에 텍스트 스탬프를 추가합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Java로 텍스트 스탬프 추가

Aspose.PDF for Java는 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 클래스를 제공하여 PDF 파일에 텍스트 스탬프를 추가합니다.
 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 클래스는 스탬프 객체에 대한 글꼴 크기, 글꼴 스타일, 글꼴 색상 등을 지정하기 위한 필수 메서드를 제공합니다. 텍스트 스탬프를 추가하기 위해서는 먼저 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체와 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 객체를 필수 메서드를 사용하여 생성해야 합니다. 그 후, [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 클래스의 [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) 메서드를 호출하여 PDF 문서에 스탬프를 추가할 수 있습니다.

다음 코드 스니펫은 PDF 파일에 텍스트 스탬프를 추가하는 방법을 보여줍니다.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.*;
import com.aspose.pdf.facades.Stamp;

public class ExampleStampingImage {
    // 문서 디렉토리 경로
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddTextStamp() {
        // 문서 열기
        Document pdfDocument = new Document("input.pdf");
        // 텍스트 스탬프 생성
        TextStamp textStamp = new TextStamp("Sample Stamp");
        // 스탬프가 배경인지 설정
        textStamp.setBackground(true);
        // 원점 설정
        textStamp.setXIndent(100);
        textStamp.setYIndent(100);
        // 스탬프 회전
        textStamp.setRotate(Rotation.on90);
        // 텍스트 속성 설정
        textStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        textStamp.getTextState().setFontSize(14.0F);
        textStamp.getTextState().setFontStyle(FontStyles.Bold);
        textStamp.getTextState().setFontStyle(FontStyles.Italic);
        textStamp.getTextState().setForegroundColor(Color.getGreen());
        // 특정 페이지에 스탬프 추가
        pdfDocument.getPages().get_Item(1).addStamp(textStamp);
        // 출력 문서 저장
        pdfDocument.save("TextStamp_output.pdf");
    }
```

## TextStamp 객체의 정렬 정의

PDF 문서에 워터마크를 추가하는 것은 자주 요구되는 기능 중 하나이며, Aspose.PDF for Java는 이미지뿐만 아니라 텍스트 워터마크를 추가할 수 있는 기능을 완벽히 제공합니다. [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 클래스는 PDF 파일에 텍스트 스탬프를 추가하는 기능을 제공합니다. 최근에는 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 객체를 사용할 때 텍스트의 정렬을 지정할 수 있는 기능이 필요하다는 요구가 있었습니다. 이 요구를 충족하기 위해, [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 클래스에 setTextAlignment(..) 메서드를 도입했습니다. 이 메서드를 사용하여 수평 텍스트 정렬을 지정할 수 있습니다.

다음 코드 스니펫은 기존의 PDF 문서를 로드하고 그 위에 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp)를 추가하는 예제를 보여줍니다.

```java
    public static void DefineAlignmentTextStamp() {
        // 입력 파일로 Document 객체를 인스턴스화
        Document pdfDocument = new Document("input.pdf");
        // 샘플 문자열로 FormattedText 객체를 인스턴스화
        FormattedText text = new FormattedText("This");
        
        // FormattedText에 새로운 텍스트 줄 추가
        text.addNewLineText("is sample");
        text.addNewLineText("Center Aligned");
        text.addNewLineText("TextStamp");
        text.addNewLineText("Object");
        // FormattedText를 사용하여 TextStamp 객체 생성
        TextStamp stamp = new TextStamp(text);
        // 텍스트 스탬프의 수평 정렬을 중앙 정렬로 지정
        stamp.setHorizontalAlignment(HorizontalAlignment.Center);
        // 텍스트 스탬프의 수직 정렬을 중앙 정렬로 지정
        stamp.setVerticalAlignment(VerticalAlignment.Center);
        // TextStamp의 텍스트 수평 정렬을 중앙 정렬로 지정
        stamp.setTextAlignment(HorizontalAlignment.Center);
        // 스탬프 객체의 상단 여백 설정
        stamp.setTopMargin(20);
        // PDF 파일의 모든 페이지에 스탬프 추가
        pdfDocument.getPages().get_Item(1).addStamp(stamp);
        
        // 출력 문서 저장
        pdfDocument.save("TextStamp_output.pdf");
    }
```


## PDF 파일에 스탬프로 채우기 및 윤곽선 텍스트

텍스트 추가 및 편집 시나리오에 대한 렌더링 모드 설정을 구현하였습니다. 윤곽선 텍스트를 렌더링하려면 [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState) 객체를 생성하고 RenderingMode를 TextRenderingMode.StrokeText로 설정한 후 StrokingColor 속성에 대한 색상을 선택하십시오. 이후, BindTextState() 메서드를 사용하여 스탬프에 TextState를 바인딩합니다.

다음 코드 스니펫은 채우기 및 윤곽선 텍스트 추가를 보여줍니다:

```java
   public static void FillStrokeTextAsStampInPDFFile(){
        // 고급 속성을 전송하기 위한 TextState 객체 생성
        TextState ts = new TextState();
        
        // 윤곽선 색상 설정
        ts.setStrokingColor(Color.getGray());
        
        // 텍스트 렌더링 모드 설정
        ts.setRenderingMode (TextRenderingMode.StrokeText);
        
        // 입력 PDF 문서 로드
        PdfFileStamp fileStamp = new PdfFileStamp(new Document(_dataDir + "input.pdf"));

        Stamp stamp = new Stamp();
        stamp.bindLogo(new FormattedText("PAID IN FULL", java.awt.Color.GRAY, "Arial", EncodingType.Winansi, true, 78));

        // TextState 바인딩
        stamp.bindTextState(ts);
        // X,Y 원점 설정
        stamp.setOrigin(100, 100);
        stamp.setOpacity (5);
        stamp.setBlendingSpace (BlendingColorSpace.DeviceRGB);
        stamp.setRotation (45.0F);
        stamp.setBackground(false);
        // 스탬프 추가
        fileStamp.addStamp(stamp);
        fileStamp.save(_dataDir + "ouput_out.pdf");
        fileStamp.close();
    }
```