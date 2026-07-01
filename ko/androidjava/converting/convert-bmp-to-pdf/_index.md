---
title: BMP를 PDF로 변환
linktitle: BMP를 PDF로 변환
type: docs
weight: 220
url: /ko/androidjava/convert-bmp-to-pdf/
lastmod: "2026-07-01"
description: Aspose.PDF for Android via Java를 사용하여 디스플레이 장치와 별도로 디지털 비트맵 이미지를 저장하는 PDF로 BMP 비트맵 파일을 쉽게 변환할 수 있습니다.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

BMP 이미지는 .BMP 확장자를 가진 파일로, 비트맵 디지털 이미지를 저장하는 데 사용되는 Bitmap Image 파일을 의미합니다. 이러한 이미지는 그래픽 어댑터와 무관하며 장치 독립 비트맵(DIB) 파일 형식이라고도 합니다.
Aspose.PDF for Java API를 사용하여 BMP를 PDF로 변환할 수 있습니다. 따라서 BMP 이미지를 변환하기 위해 다음 단계들을 따라 할 수 있습니다:

1. 새 문서를 초기화합니다
1. 샘플 BMP 이미지 파일을 로드합니다
1. 마지막으로, 출력 PDF 파일을 저장합니다

따라서 다음 코드 스니펫은 이러한 단계들을 따르고 Java를 사용하여 BMP를 PDF로 변환하는 방법을 보여줍니다:

```java
public void convertBMPtoPDF () {
        // Initialize document object
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

        // Load sample BMP image file
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "BMP-to-PDF.pdf");

        // Save output document
        try {
            document.save(pdfFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

