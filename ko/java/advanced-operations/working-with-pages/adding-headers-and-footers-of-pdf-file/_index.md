---
title: PDF 헤더 및 푸터 추가
linktitle: 헤더 및 푸터 추가
type: docs
weight: 70
url: ko/java/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for Java를 사용하여 PDF 파일에 TextStamp 클래스를 사용하여 헤더와 푸터를 추가할 수 있습니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF 스탬프는 종종 계약서, 보고서 및 제한된 자료에서 사용되며, 문서가 검토되고 "읽음", "자격 있음" 또는 "기밀" 등으로 표시되었음을 증명하기 위해 사용됩니다. 이 문서에서는 **Aspose.PDF for Java**를 사용하여 PDF 문서에 이미지 스탬프와 텍스트 스탬프를 추가하는 방법을 보여줍니다.

위의 코드 스니펫을 한 줄씩 읽어보면 문법과 코드 논리가 이해하기 쉽다는 것을 알 수 있습니다.

## PDF 파일의 헤더에 텍스트 추가하기

PDF 파일의 헤더에 텍스트를 추가하려면 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 클래스를 사용할 수 있습니다.
 TextStamp 클래스는 글꼴 크기, 글꼴 스타일, 글꼴 색상 등과 같은 텍스트 기반 스탬프를 생성하는 데 필요한 속성을 제공합니다. 머리글에 텍스트를 추가하려면 필요한 속성을 사용하여 Document 객체와 TextStamp 객체를 생성해야 합니다. 그 후, 페이지의 AddStamp 메서드를 호출하여 PDF의 머리글에 텍스트를 추가할 수 있습니다.

PDF의 머리글 영역에 텍스트가 조정되도록 TopMargin 속성을 설정해야 합니다. 또한 HorizontalAlignment를 Center로, VerticalAlignment를 Top으로 설정해야 합니다.

다음 코드 스니펫은 Java로 PDF 파일의 머리글에 텍스트를 추가하는 방법을 보여줍니다.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleAddPDFHeaderandFooter {
    // 문서 디렉토리의 경로입니다.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddingTextInHeaderOfPDFFile() {

        // 문서 열기
        Document pdfDocument = new Document(_dataDir + "TextinHeader.pdf");

        // 머리글 생성
        TextStamp textStamp = new TextStamp("Header Text");

        // 스탬프의 속성 설정
        textStamp.setTopMargin(10);
        textStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        textStamp.setVerticalAlignment(VerticalAlignment.Top);

        // 모든 페이지에 머리글 추가
        for (Page page : pdfDocument.getPages()) {
            page.addStamp(textStamp);
        }

        // 업데이트된 문서 저장
        pdfDocument.save(_dataDir + "TextinHeader_out.pdf");
    }
```

## PDF 파일의 바닥글에 텍스트 추가

PDF 파일의 바닥글에 텍스트를 추가하려면 TextStamp 클래스를 사용할 수 있습니다. TextStamp 클래스는 글꼴 크기, 글꼴 스타일, 글꼴 색상 등 텍스트 기반 스탬프를 생성하는 데 필요한 속성을 제공합니다. 바닥글에 텍스트를 추가하려면 Document 객체와 필요한 속성을 사용하여 TextStamp 객체를 생성해야 합니다. 그런 다음, AddStamp 메서드를 호출하여 PDF의 바닥글에 텍스트를 추가할 수 있습니다.

다음 코드 스니펫은 Java를 사용하여 PDF 파일의 바닥글에 텍스트를 추가하는 방법을 보여줍니다.

```java
    public static void AddingTextInFooterOfPDFFile() {
        // 문서 열기
        Document pdfDocument = new Document(_dataDir + "TextinFooter.pdf");
        // 바닥글 생성
        TextStamp textStamp = new TextStamp("바닥글 텍스트");
        // 스탬프의 속성 설정
        textStamp.setBottomMargin(10);
        textStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        textStamp.setVerticalAlignment(VerticalAlignment.Bottom);
        // 모든 페이지에 바닥글 추가
        for (Page page : pdfDocument.getPages()) {
            page.addStamp(textStamp);
        }
        _dataDir = _dataDir + "TextinFooter_out.pdf";
        // 업데이트된 PDF 파일 저장
        pdfDocument.save(_dataDir);
    }
```


## PDF 파일의 헤더에 이미지 추가

PDF 파일의 헤더에 이미지를 추가하려면 [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp) 클래스를 사용할 수 있습니다. Image Stamp 클래스는 글꼴 크기, 글꼴 스타일, 글꼴 색상 등 이미지 기반 스탬프를 생성하는 데 필요한 속성을 제공합니다. 헤더에 이미지를 추가하려면 Document 객체와 필요한 속성을 사용하여 Image Stamp 객체를 생성해야 합니다. 그런 다음, PDF의 헤더에 이미지를 추가하기 위해 페이지의 [AddStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) 메서드를 호출할 수 있습니다.

```java
public static void AddingImageInHeaderOfPDFFile() {

// 문서 열기
Document pdfDocument = new Document(_dataDir + "ImageInHeader.pdf");

// 헤더 생성
ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.jpg");

// 스탬프의 속성 설정
imageStamp.setTopMargin(10);
imageStamp.setHorizontalAlignment(HorizontalAlignment.Center);
imageStamp.setVerticalAlignment(VerticalAlignment.Top);
// 모든 페이지에 헤더 추가
for (Page page : pdfDocument.getPages()) {
page.addStamp(imageStamp);
}

_dataDir = _dataDir + "ImageInHeader_out.pdf";

// 업데이트된 PDF 파일 저장
pdfDocument.save(_dataDir);
}
```


다음 코드 스니펫은 Java로 PDF 파일의 헤더에 이미지를 추가하는 방법을 보여줍니다.

## PDF 파일의 바닥글에 이미지 추가

Image Stamp 클래스를 사용하여 PDF 파일의 바닥글에 이미지를 추가할 수 있습니다. Image Stamp 클래스는 폰트 크기, 폰트 스타일, 폰트 색상 등 이미지 기반 스탬프를 생성하는 데 필요한 속성을 제공합니다. 바닥글에 이미지를 추가하려면 Document 객체와 필요한 속성을 사용하여 Image Stamp 객체를 생성해야 합니다. 그 후, AddStamp 메서드를 호출하여 PDF의 바닥글에 이미지를 추가할 수 있습니다.

{{% alert color="primary" %}}

PDF의 바닥글 영역에 이미지를 조정할 수 있도록 BottomMargin 속성을 설정해야 합니다. 또한 [HorizontalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/HorizontalAlignment)를 `Center`로 설정하고 [VerticalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/VerticalAlignment)를 `Bottom`으로 설정해야 합니다.

{{% /alert %}}

다음 코드 스니펫은 Java로 PDF 파일의 바닥글에 이미지를 추가하는 방법을 보여줍니다.

```java
    public static void AddingImageInFooterOfPDFFile() {

        // 문서 열기
        Document pdfDocument = new Document(_dataDir + "ImageInFooter.pdf");

        // 바닥글 만들기
        ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.jpg");

        // 스탬프 속성 설정
        imageStamp.setBottomMargin(10);
        imageStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        imageStamp.setVerticalAlignment(VerticalAlignment.Bottom);
        // 모든 페이지에 바닥글 추가
        for (Page page : pdfDocument.getPages()) {
            page.addStamp(imageStamp);
        }

        _dataDir = _dataDir + "ImageInFooter_out.pdf";

        // 업데이트된 PDF 파일 저장
        pdfDocument.save(_dataDir);
    }
```

## 하나의 PDF 파일에 다른 헤더 추가하기

우리는 TopMargin 또는 Bottom Margin 속성을 사용하여 문서의 Header/Footer 섹션에 TextStamp를 추가할 수 있다는 것을 알고 있지만, 때때로 하나의 PDF 문서에 여러 헤더/바닥글을 추가해야 할 필요가 있을 수 있습니다.
 **Aspose.PDF for Java**는 이를 수행하는 방법을 설명합니다.

이 요구 사항을 충족하기 위해, 우리는 개별 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 객체를 생성하고(필요한 헤더/푸터의 수에 따라 객체 수가 결정됨) PDF 문서에 추가할 것입니다. 우리는 또한 각 스탬프 객체에 대해 다른 서식 정보를 지정할 수 있습니다. 다음 예제에서는 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체와 세 개의 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 객체를 생성한 후, PDF의 헤더 섹션에 텍스트를 추가하기 위해 페이지의 [AddStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) 메서드를 사용했습니다. 다음 코드 스니펫은 Aspose.PDF for Java를 사용하여 PDF 파일의 푸터에 이미지를 추가하는 방법을 보여줍니다.

```java
public static void AddingDifferentHeadersInOnePDFFile() {

        // 소스 문서 열기
        Document pdfDocument = new Document(_dataDir + "AddingDifferentHeaders.pdf");

        // 세 개의 스탬프 생성
        TextStamp stamp1 = new TextStamp("Header 1");
        TextStamp stamp2 = new TextStamp("Header 2");
        TextStamp stamp3 = new TextStamp("Header 3");

        // 스탬프 정렬 설정 (페이지 상단에 수평 중앙으로 스탬프 배치)
        stamp1.setVerticalAlignment(VerticalAlignment.Top);
        stamp1.setHorizontalAlignment(HorizontalAlignment.Center);
        // 글꼴 스타일을 굵게 지정
        stamp1.getTextState().setFontStyle(FontStyles.Bold);
        // 텍스트 전경색 정보를 빨강으로 설정
        stamp1.getTextState().setForegroundColor(Color.getRed());
        // 글꼴 크기를 14로 지정
        stamp1.getTextState().setFontSize(14);

        // 이제 두 번째 스탬프 객체의 수직 정렬을 상단으로 설정해야 합니다
        stamp2.setVerticalAlignment(VerticalAlignment.Top);
        // 스탬프의 수평 정렬 정보를 중앙 정렬로 설정
        stamp2.setHorizontalAlignment(HorizontalAlignment.Center);
        // 스탬프 객체의 확대 비율 설정
        stamp2.setZoom(10);

        // 세 번째 스탬프 객체의 서식 설정
        // 스탬프 객체의 수직 정렬 정보를 상단으로 지정
        stamp3.setVerticalAlignment(VerticalAlignment.Top);
        // 스탬프 객체의 수평 정렬 정보를 중앙 정렬로 설정
        stamp3.setHorizontalAlignment(HorizontalAlignment.Center);
        // 스탬프 객체의 회전 각도 설정
        stamp3.setRotateAngle(35);
        // 스탬프의 배경색을 분홍색으로 설정
        stamp3.getTextState().setBackgroundColor(Color.getPink());

        // 스탬프의 글꼴 얼굴 정보를 Verdana로 변경
        stamp3.getTextState().setFont(FontRepository.findFont("Verdana"));
        // 첫 번째 스탬프는 첫 페이지에 추가됩니다;
        pdfDocument.getPages().get_Item(1).addStamp(stamp1);
        // 두 번째 스탬프는 두 번째 페이지에 추가됩니다;
        pdfDocument.getPages().get_Item(2).addStamp(stamp2);
        // 세 번째 스탬프는 세 번째 페이지에 추가됩니다.
        pdfDocument.getPages().get_Item(3).addStamp(stamp3);

        _dataDir = _dataDir + "multiheader_out.pdf";

        // 업데이트된 PDF 파일 저장
        pdfDocument.save(_dataDir);
    }

}
```