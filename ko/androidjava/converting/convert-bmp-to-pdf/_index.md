---
title: BMP를 PDF로 변환
linktitle: BMP를 PDF로 변환
type: docs
weight: 220
url: /ko/androidjava/convert-bmp-to-pdf/
lastmod: "2021-06-05"
description: Aspose.PDF를 사용하여 BMP 비트맵 파일을 디스플레이 장치와 독립적으로 디지털 비트맵 이미지를 저장하는 데 사용되는 PDF로 쉽게 변환할 수 있습니다. for Android via Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

BMP 이미지는 .BMP 확장자를 가진 파일로, 비트맵 디지털 이미지를 저장하는 데 사용되는 비트맵 이미지 파일을 나타냅니다. 이러한 이미지는 그래픽 어댑터와 독립적이며 장치 독립 비트맵(DIB) 파일 형식이라고도 합니다.
BMP를 PDF로 변환하려면 Aspose.PDF for Java API를 사용할 수 있습니다. 따라서 BMP 이미지를 변환하기 위해 다음 단계를 따를 수 있습니다:

1. 새 문서 초기화
1. 샘플 BMP 이미지 파일 로드
1. 마지막으로 출력 PDF 파일 저장

다음 코드 스니펫은 이러한 단계를 따르며 Java를 사용하여 BMP를 PDF로 변환하는 방법을 보여줍니다:

```java
public void convertBMPtoPDF () {
        // 문서 객체 초기화
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.bmp");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // 샘플 BMP 이미지 파일 로드
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "BMP-to-PDF.pdf");

        // 출력 문서 저장
        try {
            document.save(pdfFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```