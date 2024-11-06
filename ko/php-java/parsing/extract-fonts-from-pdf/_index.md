---
title: PDF에서 폰트 추출하기
linktitle: 폰트 추출
type: docs
weight: 30
url: ko/php-java/extract-fonts-from-pdf/
description: Aspose.PDF for PHP를 사용하여 PDF에서 폰트 추출하는 방법
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

PDF 문서에서 모든 폰트를 가져오고자 하는 경우, Document 클래스에서 제공하는 [Document.IDocumentFontUtilities.getAllFonts()](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getFontUtilities--) 메서드를 사용할 수 있습니다. 기존 PDF 문서에서 모든 폰트를 얻기 위한 다음 코드 스니펫을 확인하십시오:

```php

    // License 클래스의 새 인스턴스를 생성하고 라이선스 파일을 설정합니다.
    $licenceObject = new License();
    $licenceObject->setLicense($license);

    // PDF 문서가 포함된 디렉토리의 경로와 추출된 폰트의 출력 디렉토리를 설정합니다.
    $dataDir = getcwd() . DIRECTORY_SEPARATOR . "samples";
    $inputFile = $dataDir . DIRECTORY_SEPARATOR . "sample.pdf";

    // 응답 데이터 변수를 초기화합니다.
    $responseData = "";

    try {
        // PDF 문서를 로드합니다.
        $document = new Document($inputFile);

        // PDF 문서에서 사용된 모든 폰트를 가져옵니다.
        $fonts = java_values($document->getFontUtilities()->getAllFonts());

        // 각 폰트를 반복하여 TrueType 폰트 파일로 저장합니다.
        foreach ($fonts as $font) {
            // 폰트 파일의 출력 경로를 설정합니다.
            $outputFile = $dataDir . DIRECTORY_SEPARATOR . "results" . DIRECTORY_SEPARATOR . $font->getFontName() . ".ttf";

            // 폰트 파일을 쓰기 위한 FileOutputStream 객체를 생성합니다.
            $fontStream = new java("java.io.FileOutputStream", $outputFile);

            // 폰트를 TrueType 폰트 파일로 저장합니다.
            $font->save($fontStream);

            // 폰트 스트림을 닫습니다.
            $fontStream->close();

            // 응답 데이터에 폰트 이름을 추가합니다.
            $responseData = $responseData . $font->getFontName() . ", ";
        }

        // PDF 문서를 닫습니다.
        $document->close();
    }
```