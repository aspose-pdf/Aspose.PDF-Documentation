---
title: PNG를 PDF로 변환 
linktitle: PNG를 PDF로 변환
type: docs
weight: 200
url: ko/androidjava/convert-png-to-pdf/
lastmod: "2021-06-05"
description: 이 문서는 Aspose.PDF 라이브러리를 사용하여 Android의 Java 애플리케이션에서 PNG를 PDF로 변환하는 방법을 보여줍니다. 간단한 단계로 PNG 이미지를 PDF 형식으로 변환할 수 있습니다.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java**는 PNG 이미지를 PDF 형식으로 변환하는 기능을 지원합니다. 작업을 실현하기 위한 다음 코드 스니펫을 확인하십시오.

<abbr title="Portable Network Graphics">PNG</abbr>는 손실 없는 압축을 사용하는 래스터 이미지 파일 형식을 의미하며, 이는 사용자들 사이에서 인기를 끌고 있습니다.

다음 단계에 따라 PNG를 PDF 이미지로 변환할 수 있습니다:

1. 입력 PNG 이미지 로드
2. 높이와 너비 값 읽기
3. 새 문서 생성 및 페이지 추가
4. 페이지 크기 설정
5. 출력 파일 저장

또한, 아래 코드 스니펫은 Java 애플리케이션에서 PNG를 PDF로 변환하는 방법을 보여줍니다:

```java
    public void convertPNGtoPDF () {
        // 문서 객체 초기화
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