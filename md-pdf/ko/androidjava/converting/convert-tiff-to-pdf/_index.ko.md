---
title: TIFF를 PDF로 변환
linktitle: TIFF를 PDF로 변환
type: docs
weight: 210
url: /androidjava/convert-tiff-to-pdf/
lastmod: "2021-06-05"
description: Aspose.PDF for Android via Java는 여러 페이지 또는 여러 프레임의 TIFF 이미지를 PDF 애플리케이션으로 변환할 수 있습니다.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** 파일 형식은 단일 프레임이든 다중 프레임이든 <abbr title="Tag Image File Format">TIFF</abbr> 이미지를 지원합니다. 즉, Java 애플리케이션에서 TIFF 이미지를 PDF로 변환할 수 있습니다.

TIFF 또는 TIF, 태그 이미지 파일 형식은 이 파일 형식 표준을 준수하는 다양한 장치에서 사용하기 위한 래스터 이미지를 나타냅니다.
 TIFF 이미지는 서로 다른 이미지를 가진 여러 프레임을 포함할 수 있습니다. Aspose.PDF 파일 형식도 단일 프레임이든 다중 프레임 TIFF 이미지든 지원됩니다. 따라서 Java 애플리케이션에서 TIFF 이미지를 PDF로 변환할 수 있습니다. 따라서, 아래 단계에 따라 다중 페이지 TIFF 이미지를 다중 페이지 PDF 문서로 변환하는 예제를 살펴보겠습니다:

1. Document 클래스의 인스턴스를 생성합니다.
1. 입력 TIFF 이미지를 로드합니다.
1. 프레임의 FrameDimension을 가져옵니다.
1. 각 프레임에 대해 새 페이지를 추가합니다.
1. 마지막으로, 이미지를 PDF 페이지로 저장합니다.

또한, 다음 코드 스니펫은 다중 페이지 또는 다중 프레임 TIFF 이미지를 PDF로 변환하는 방법을 보여줍니다:

```java
 public void convertTIFFtoPDF () {
        // 문서 객체 초기화
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

        // 샘플 TIFF 이미지 파일 로드
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "TIFF-to-PDF.pdf");

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