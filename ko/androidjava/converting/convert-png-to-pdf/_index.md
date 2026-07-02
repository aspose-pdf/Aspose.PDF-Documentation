---
title: PNG를 PDF로 변환
linktitle: PNG를 PDF로 변환
type: docs
weight: 200
url: /ko/androidjava/convert-png-to-pdf/
lastmod: "2026-07-01"
description: 이 문서는 Android에서 Java 애플리케이션을 통해 Aspose.PDF 라이브러리를 사용하여 PNG를 PDF로 변환하는 방법을 보여줍니다. 간단한 단계로 PNG 이미지를 PDF 형식으로 변환할 수 있습니다.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** 는 PNG 이미지를 PDF 형식으로 변환하는 기능을 지원합니다. 다음 코드 스니펫을 확인하여 작업을 구현하십시오.

<abbr title="Portable Network Graphics">PNG</abbr> 무손실 압축을 사용하고, 사용자들 사이에서 인기가 있는 래스터 이미지 파일 형식 유형을 의미합니다.

아래 단계에 따라 PNG를 PDF 이미지로 변환할 수 있습니다:

1. 입력 PNG 이미지를 로드합니다
1. 높이와 너비 값을 읽습니다
1. 새 문서를 생성하고 페이지를 추가합니다
1. 페이지 크기를 설정합니다
1. 출력 파일을 저장합니다

또한, 아래 코드 조각은 Java 애플리케이션에서 PNG를 PDF로 변환하는 방법을 보여줍니다:

```java
    public void convertPNGtoPDF () {
        // Initialize document object
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.png");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
```

