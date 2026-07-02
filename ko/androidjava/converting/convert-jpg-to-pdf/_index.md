---
title: JPG를 PDF로 변환
linktitle: JPG를 PDF로 변환
type: docs
weight: 190
url: /ko/androidjava/convert-jpg-to-pdf/
lastmod: "2026-07-01"
description: JPG 이미지를 PDF 파일로 쉽게 변환하는 방법을 배워보세요. 또한, 페이지와 같은 높이와 너비를 가진 이미지로 PDF를 변환할 수 있습니다.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

JPG를 PDF로 변환하는 방법을 고민할 필요 없습니다. Apose.PDF for Android via Java 라이브러리가 최고의 해결책을 제공합니다.

다음 단계에 따라 Aspose.PDF for Android via Java를 사용하여 JPG 이미지를 PDF로 매우 쉽게 변환할 수 있습니다:

1. 객체를 초기화합니다 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스
1. JPG 이미지를 로드하고 단락에 추가
1. 출력 PDF 저장

아래 코드 조각은 JPG 이미지를 PDF로 변환하는 방법을 보여줍니다:

```java
public void convertJPEGtoPDF () {
        // Initialize document object
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.jpg");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Load sample JPEG image file
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "JPEG-to-PDF.pdf");

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
