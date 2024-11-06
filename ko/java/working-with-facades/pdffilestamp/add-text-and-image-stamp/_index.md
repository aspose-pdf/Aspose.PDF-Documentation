---
title: 텍스트 및 이미지 스탬프 추가
type: docs
weight: 20
url: ko/java/add-text-and-image-stamp/
description: 이 섹션에서는 com.aspose.pdf.facades를 사용하여 PdfFileStamp 클래스로 텍스트 및 이미지 스탬프를 추가하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## PDF 파일의 모든 페이지에 텍스트 스탬프 추가

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스는 PDF 파일의 모든 페이지에 텍스트 스탬프를 추가할 수 있도록 합니다.
 In order to add text stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) and [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) classes.

텍스트 스탬프를 추가하려면 먼저 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스와 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 클래스의 객체를 생성해야 합니다. 당신은 또한 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 클래스의 BindLogo 메소드를 사용하여 텍스트 스탬프를 생성해야 합니다. [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 객체를 사용하여 원점, 회전, 배경 등과 같은 다른 속성도 설정할 수 있습니다. 그런 다음 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스의 [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades.PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) 메소드를 사용하여 PDF 파일에 스탬프를 추가할 수 있습니다. 마지막으로 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스의 [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) 메소드를 사용하여 출력 PDF 파일을 저장합니다. 다음의 코드 스니펫은 PDF 파일의 모든 페이지에 텍스트 스탬프를 추가하는 방법을 보여줍니다.

```java
 public static void AddTextStampOnAllPagesInPdfFile() {
        // PdfFileStamp 객체 생성
        PdfFileStamp fileStamp = new PdfFileStamp();

        // 문서 열기
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // 스탬프 생성
        Stamp stamp = new Stamp();
        stamp.bindLogo(new FormattedText("Hello World!", java.awt.Color.BLUE, java.awt.Color.GRAY, FontStyle.Helvetica,
                EncodingType.Winansi, true, 14));
        stamp.setOrigin(10, 400);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // PDF 파일에 스탬프 추가
        fileStamp.addStamp(stamp);

        // 업데이트된 PDF 파일 저장
        fileStamp.save(_dataDir + "AddTextStamp-All_out.pdf");

        // fileStamp 닫기
        fileStamp.close();
    }
```

## PDF 파일의 특정 페이지에 텍스트 스탬프 추가

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스는 PDF 파일의 특정 페이지에 텍스트 스탬프를 추가할 수 있게 해줍니다.
 In order to add text stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp)and [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) classes.  
텍스트 스탬프를 추가하려면 먼저 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 및 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 클래스의 객체를 생성해야 합니다. You also need to create the text stamp using [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) method of [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) class.  
당신은 또한 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 클래스의 [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) 메서드를 사용하여 텍스트 스탬프를 생성해야 합니다. You can set other attributes like origin, rotation, background etc.
다른 속성들, 예를 들어 원점, 회전, 배경 등을 설정할 수 있습니다. using [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 객체도 사용합니다. 특정 페이지에 텍스트 스탬프를 추가하려면 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 클래스의 [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#setPages-int:A-) 속성을 설정해야 합니다. 이 속성은 스탬프를 추가하려는 페이지의 번호가 포함된 정수 배열을 필요로 합니다. 그런 다음 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스의 [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) 메서드를 사용하여 PDF 파일에 스탬프를 추가할 수 있습니다. 마지막으로 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스의 [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) 메서드를 사용하여 출력 PDF 파일을 저장합니다. 다음 코드 스니핏은 PDF 파일의 특정 페이지에 텍스트 스탬프를 추가하는 방법을 보여줍니다.

```java
 public static void AddTextStampOnParticularPagesInPdfFile() {
        // PdfFileStamp 객체 생성
        PdfFileStamp fileStamp = new PdfFileStamp();

        // 문서 열기
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // 스탬프 생성
        Stamp stamp = new Stamp();
        stamp.bindLogo(new FormattedText("Hello World!", java.awt.Color.BLUE, java.awt.Color.GRAY, FontStyle.Helvetica,
                EncodingType.Winansi, true, 14));
        stamp.setOrigin(10, 400);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // 특정 페이지 설정
        stamp.setPages(new int[] { 2 });

        // 스탬프를 PDF 파일에 추가
        fileStamp.addStamp(stamp);

        // 업데이트된 PDF 파일 저장
        fileStamp.save(_dataDir + "AddTextStamp-Page_out.pdf");

        // fileStamp 닫기
        fileStamp.close();
    }
```

## PDF 파일의 모든 페이지에 이미지 스탬프 추가

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스는 PDF 파일의 모든 페이지에 이미지 스탬프를 추가할 수 있도록 합니다.
 In order to add image stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) and [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) classes.

이미지 스탬프를 추가하려면 먼저 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 및 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 클래스의 객체를 생성해야 합니다. 당신은 또한 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 클래스의 [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) 메서드를 사용하여 이미지 스탬프를 만들어야 합니다. [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 객체를 사용하여 원점, 회전, 배경 등과 같은 다른 속성을 설정할 수 있습니다. 그런 다음 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스의 [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades.PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) 메서드를 사용하여 PDF 파일에 스탬프를 추가할 수 있습니다. 마지막으로 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스의 [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) 메서드를 사용하여 출력 PDF 파일을 저장합니다. 다음 코드 조각은 PDF 파일의 모든 페이지에 이미지 스탬프를 추가하는 방법을 보여줍니다.

```java
public static void AddImageStampOnParticularPagesInPdfFile() {
        // PdfFileStamp 객체 생성
        PdfFileStamp fileStamp = new PdfFileStamp();

        // 문서 열기
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // 스탬프 생성
        Stamp stamp = new Stamp();
        stamp.bindImage(_dataDir + "aspose-logo.png");
        stamp.setOrigin(10, 200);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // PDF 파일에 스탬프 추가
        fileStamp.addStamp(stamp);

        // 업데이트된 PDF 파일 저장
        fileStamp.save(_dataDir + "AddImageStamp-All_out.pdf");

        // fileStamp 닫기
        fileStamp.close();
    }
```

### 스탬프로 이미지 품질 제어

이미지를 스탬프 객체로 추가할 때, 이미지의 품질을 제어할 수도 있습니다. 이 요구 사항을 충족시키기 위해, [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 클래스에 Quality 속성이 추가되었습니다. 이는 퍼센트로 표시된 이미지의 품질을 나타냅니다 (유효 값은 0..100입니다).

## PDF 파일의 특정 페이지에 이미지 스탬프 추가

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스는 PDF 파일의 특정 페이지에 이미지 스탬프를 추가할 수 있게 해줍니다.
 In order to add image stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) and [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) classes.  

이미지 스탬프를 추가하려면 먼저 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 및 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 클래스의 객체를 생성해야 합니다. 당신은 또한 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 클래스의 [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) 메소드를 사용하여 이미지 스탬프를 생성해야 합니다. You can set other attributes like origin, rotation, background etc.  
다른 속성들을 설정할 수 있습니다. 예를 들어, 원점, 회전, 배경 등. using [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 객체도 사용합니다. 특정 페이지에 이미지 스탬프를 추가하려면, [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 클래스의 [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#setPages-int:A-) 속성을 설정해야 합니다. 이 속성은 스탬프를 추가하려는 페이지의 번호가 포함된 정수 배열을 필요로 합니다. 그런 다음, [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스의 [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) 메소드를 사용하여 PDF 파일에 스탬프를 추가할 수 있습니다. 마지막으로, [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스의 [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) 메소드를 사용하여 출력 PDF 파일을 저장합니다. 다음 코드 스니펫은 PDF 파일의 특정 페이지에 이미지 스탬프를 추가하는 방법을 보여줍니다.

```java
  public static void AddImageStampOnAllPagesInPdfFile() {
        // PdfFileStamp 객체 생성
        PdfFileStamp fileStamp = new PdfFileStamp();

        // 문서 열기
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // 스탬프 생성
        Stamp stamp = new Stamp();
        stamp.bindImage(_dataDir + "aspose-logo.png");
        stamp.setOrigin(10, 200);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // 특정 페이지 설정
        stamp.setPages(new int[] { 2 });

        // PDF 파일에 스탬프 추가
        fileStamp.addStamp(stamp);

        // 업데이트된 PDF 파일 저장
        fileStamp.save(_dataDir + "AddImageStamp-Page_out.pdf");

        // fileStamp 닫기
        fileStamp.close();
    }
```