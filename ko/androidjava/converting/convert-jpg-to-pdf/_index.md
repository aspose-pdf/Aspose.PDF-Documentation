---
title: JPG를 PDF로 변환
linktitle: JPG를 PDF로 변환
type: docs
weight: 190
url: ko/androidjava/convert-jpg-to-pdf/
lastmod: "2021-06-05"
description: JPG 이미지를 PDF 파일로 쉽게 변환하는 방법을 배웁니다. 또한, 페이지의 동일한 높이와 너비로 이미지를 PDF로 변환할 수 있습니다.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

JPG를 PDF로 변환하는 방법을 궁금해할 필요가 없습니다. Apose.PDF for Android via Java 라이브러리가 최고의 솔루션을 제공합니다.

아래의 단계를 따르면, Aspose.PDF for Android via Java로 JPG 이미지를 매우 쉽게 PDF로 변환할 수 있습니다:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스의 객체 초기화
2. JPG 이미지를 로드하고 단락에 추가
3. 출력 PDF 저장

아래의 코드 스니펫은 JPG 이미지를 PDF로 변환하는 방법을 보여줍니다:

```java
public void convertJPEGtoPDF () {
        // 문서 객체 초기화
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

        // 샘플 JPEG 이미지 파일 로드
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "JPEG-to-PDF.pdf");

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