---
title: PDF에 이미지 스탬프 추가 프로그래밍적으로
linktitle: PDF 파일의 이미지 스탬프
type: docs
weight: 10
url: /ko/java/image-stamps-in-pdf-page/
description: Aspose.PDF for Java 라이브러리의 ImageStamp 클래스를 사용하여 PDF 문서에 이미지 스탬프를 추가합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 파일에 이미지 스탬프 추가

[ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) 클래스를 사용하여 PDF 문서에 이미지를 스탬프로 추가할 수 있습니다. [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) 클래스는 높이, 너비 및 불투명도 등을 지정하는 방법을 제공합니다.

이미지 스탬프를 추가하려면:

1. 필요한 속성을 사용하여 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체와 ImageStamp 객체를 생성합니다.

1. [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 클래스의 [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) 메서드를 호출하여 PDF에 스탬프를 추가합니다.

다음 코드 스니펫은 PDF 파일에 이미지 스탬프를 추가하는 방법을 보여줍니다.

```java
public static void AddImageStampInPDFFile() {
        // 문서 열기
        Document pdfDocument = new Document(_dataDir + "AddImageStamp.pdf");

        // 이미지 스탬프 생성
        ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.png");
        imageStamp.setBackground(true);
        imageStamp.setXIndent(100);
        imageStamp.setYIndent(100);
        imageStamp.setHeight(48);
        imageStamp.setWidth(225);
        imageStamp.setRotate(Rotation.on270);
        imageStamp.setOpacity(0.5);

        // 특정 페이지에 스탬프 추가
        pdfDocument.getPages().get_Item(1).addStamp(imageStamp);

        // 출력 문서 저장
        pdfDocument.save(_dataDir + "AddImageStamp_out.pdf");

    }
```


## 스탬프 추가 시 이미지 품질 제어

[ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) 클래스는 이미지 스탬프를 PDF 문서에 추가할 수 있게 해줍니다. 또한 PDF 파일에 워터마크로 이미지를 추가할 때 이미지 품질을 제어할 수 있습니다. 이를 가능하게 하기 위해 [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) 클래스에 setQuality(...)라는 메소드가 추가되었습니다. 유사한 메소드는 com.aspose.pdf.facades 패키지의 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/Stamp) 클래스에서도 찾을 수 있습니다.

다음 코드 스니펫은 PDF 파일에 스탬프로 추가할 때 이미지 품질을 제어하는 방법을 보여줍니다.

```java
 public static void ControlImageQualityWhenAddingStamp() {
        // 문서 열기
        Document pdfDocument = new Document(_dataDir + "AddImageStamp.pdf");

        // 이미지 스탬프 생성
        ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.png");
        imageStamp.setQuality(10);
        pdfDocument.getPages().get_Item(1).addStamp(imageStamp);

        pdfDocument.save(_dataDir + "ControlImageQuality_out.pdf");
    }
```


## 부동 박스에서 이미지 스탬프를 배경으로 사용

Aspose.PDF API를 사용하면 부동 박스에 이미지 스탬프를 배경으로 추가할 수 있습니다. FloatingBox 클래스의 BackgroundImage 속성을 사용하여 부동 박스에 대한 배경 이미지 스탬프를 설정할 수 있으며, 다음 코드 샘플에 나와 있습니다.

```java
public static void ImageStampAsBackgroundInFloatingBox() {
        // Document 객체를 인스턴스화
        Document doc = new Document();
        // PDF 문서에 페이지 추가
        Page page = doc.getPages().add();

        // FloatingBox 객체 생성
        FloatingBox aBox = new FloatingBox(200, 100);

        // FloatingBox의 왼쪽 위치 설정
        aBox.setLeft(40);
        // FloatingBox의 위쪽 위치 설정
        aBox.setTop(80);
        // FloatingBox의 수평 정렬 설정
        aBox.setHorizontalAlignment(HorizontalAlignment.Center);
        // FloatingBox의 단락 컬렉션에 텍스트 조각 추가
        aBox.getParagraphs().add(new TextFragment("main text"));
        // FloatingBox의 테두리 설정
        aBox.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));

        // 배경 이미지 추가
        Image img = new Image();
        img.setFile(_dataDir + "aspose-logo.png");
        aBox.setBackgroundImage(img);

        // FloatingBox의 배경색 설정
        aBox.setBackgroundColor(Color.getYellow());

        // 페이지 객체의 단락 컬렉션에 FloatingBox 추가
        page.getParagraphs().add(aBox);
        // PDF 문서 저장
        doc.save(_dataDir + "AddImageStampAsBackgroundInFloatingBox_out.pdf");
    }
}
```