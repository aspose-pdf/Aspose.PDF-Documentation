---
title: TIFF를 PDF로 변환
linktitle: TIFF를 PDF로 변환
type: docs
weight: 210
url: /ko/androidjava/convert-tiff-to-pdf/
lastmod: "2026-07-01"
description: Aspose.PDF for Android via Java은 다중 페이지 또는 다중 프레임 TIFF 이미지를 PDF 애플리케이션으로 변환할 수 있도록 합니다.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** 파일 형식이 지원됩니다, 단일 프레임이든 다중 프레임이든 <abbr title="Tag Image File Format">TIFF</abbr> 이미지. 이는 Java 애플리케이션에서 TIFF 이미지를 PDF로 변환할 수 있다는 의미입니다.

TIFF 또는 TIF(Tagged Image File Format)는 이 파일 형식 표준을 준수하는 다양한 장치에서 사용하도록 설계된 래스터 이미지를 나타냅니다. TIFF 이미지에는 서로 다른 이미지를 갖는 여러 프레임이 포함될 수 있습니다. Aspose.PDF 파일 형식도 지원되며, 단일 프레임이든 다중 프레임 TIFF 이미지든 상관 없습니다. 따라서 Java 애플리케이션에서 TIFF 이미지를 PDF로 변환할 수 있습니다. 아래 단계에 따라 다중 페이지 TIFF 이미지를 다중 페이지 PDF 문서로 변환하는 예제를 살펴보겠습니다:

1. Document 클래스의 인스턴스를 생성합니다
1. 입력 TIFF 이미지를 로드합니다
1. 프레임의 FrameDimension을 가져옵니다
1. 각 프레임마다 새 페이지를 추가합니다
1. 마지막으로 이미지를 PDF 페이지에 저장합니다

또한, 다음 코드 스니펫은 다중 페이지 또는 다중 프레임 TIFF 이미지를 PDF로 변환하는 방법을 보여줍니다:

```java
 public void convertTIFFtoPDF () {
        // Initialize document object
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.tiff");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Load sample TIFF image file
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "TIFF-to-PDF.pdf");

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

