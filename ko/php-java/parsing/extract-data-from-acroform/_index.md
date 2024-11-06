---
title: AcroForm에서 데이터 추출
linktitle: AcroForm에서 데이터 추출
type: docs
weight: 50
url: ko/php-java/extract-data-from-acroform/
description: 많은 PDF 문서에 AcroForms가 존재합니다. 이 기사는 PHP와 Aspose.PDF를 사용하여 AcroForms에서 데이터를 추출하는 방법을 이해하는 데 도움을 주기 위해 작성되었습니다.
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF 문서에서 양식 필드 추출

Aspose.PDF for PHP는 양식 필드를 생성하고 채우는 것뿐만 아니라 PDF 파일에서 양식 필드 데이터나 양식 필드 정보를 쉽게 추출할 수 있게 합니다.

양식 필드의 이름을 미리 알지 못한다고 가정해 보겠습니다. 그러면 PDF의 각 페이지를 반복하여 PDF의 모든 AcroForms 및 양식 필드의 값을 추출해야 합니다. 양식에 접근하려면 [getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) 메소드를 사용해야 합니다.

```php

    // License 클래스의 새 인스턴스를 만들고 라이선스 파일을 설정합니다.
    $licenceObject = new License();
    $licenceObject->setLicense($license);

    // PDF 문서를 포함하는 디렉터리의 경로를 설정합니다.
    $dataDir = getcwd() . DIRECTORY_SEPARATOR . "samples";

    // 입력 PDF 파일의 경로를 설정합니다.
    $inputFile = $dataDir . DIRECTORY_SEPARATOR . "StudentInfoFormElectronic.pdf";

    // 응답이 JSON 형식임을 나타내도록 응답 헤더를 설정합니다.
    header('Content-Type: application/json; charset=utf-8');

    // 응답 데이터 변수를 초기화합니다.
    $responseData = "";

    try {
        // Document 클래스의 새 인스턴스를 만들고 입력 PDF 파일을 로드합니다.
        $document = new Document($inputFile);

        // 문서에서 양식 필드를 가져와 PHP 값으로 변환합니다.
        $fields = java_values($document->getForm()->getFields());

        // 각 양식 필드를 반복하여 필드 이름과 값을 추출합니다.
        foreach ($fields as $formField) {
            // 필드 이름과 값을 응답 데이터에 연결합니다.
            $responseData = $responseData . "(필드 이름: " . $formField->getPartialName() . " |";
            $responseData = $responseData . " 값: " . $formField->getValue() . "),";
        }

        // 문서를 닫습니다.
        $document->close();
    }
```


만약 값을 추출하고자 하는 양식 필드의 이름을 알고 있다면 Documents.Form 컬렉션의 인덱서를 사용하여 이 데이터를 빠르게 검색할 수 있습니다.

## PDF 파일에서 XML로 데이터 추출

Form 클래스는 ExportXml 메소드를 사용하여 PDF 파일에서 XML 파일로 데이터를 내보낼 수 있도록 합니다. XML로 데이터를 내보내기 위해서는 Form 클래스의 객체를 생성한 다음 FileStream 객체를 사용하여 ExportXml 메소드를 호출해야 합니다. 마지막으로 FileStream 객체를 닫고 Form 객체를 폐기할 수 있습니다. 다음 코드 스니펫은 XML 파일로 데이터를 내보내는 방법을 보여줍니다.

```php

    // 문서 열기
    $form = new facades_Form();
    $form->bindPdf($inputFile);

    // 폰트 파일을 쓰기 위한 FileOutputStream 객체 생성
    $xmlOutputStream = new java("java.io.FileOutputStream", "output.xml");

    // 데이터 내보내기
    $form->exportXml($xmlOutputStream);

    // 파일 스트림 닫기
    $xmlOutputStream->close();

    // 문서 닫기
    $form->close();
```

## PDF 파일에서 FDF로 데이터 내보내기

PDF 양식 데이터를 XFDF 파일로 내보내기 위해, 우리는 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) 클래스의 [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) 메소드를 사용할 수 있습니다.

해당 클래스는 `com.aspose.pdf.facades`에서 가져온 것입니다. 유사한 이름에도 불구하고, 이 클래스는 약간 다른 목적을 가지고 있습니다.

FDF로 데이터를 내보내기 위해서는 `Form` 클래스의 객체를 생성한 후 `OutputStream` 객체를 사용하여 `exportXfdf` 메서드를 호출해야 합니다. 다음 코드 스니펫은 데이터를 XFDF 파일로 내보내는 방법을 보여줍니다.

```php

    // 문서 열기
    $form = new facades_Form();
    $form->bindPdf($inputFile);

    // 폰트 파일을 쓰기 위한 FileOutputStream 객체 생성
    $xmlOutputStream = new java("java.io.FileOutputStream", "output.fdf");

    // 데이터 내보내기
    $form->exportFdf($xmlOutputStream);

    // 파일 스트림 닫기
    $xmlOutputStream->close();

    // 문서 닫기
    $form->close();
```

## PDF 파일에서 XFDF로 데이터 내보내기

PDF 양식 데이터를 XFDF 파일로 내보내기 위해서는 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) 클래스의 [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) 메서드를 사용할 수 있습니다.

데이터를 XFDF로 내보내려면 `Form` 클래스의 객체를 생성한 다음 `OutputStream` 객체를 사용하여 `exportXfdf` 메서드를 호출해야 합니다. 
다음 코드 스니펫은 데이터 XFDF 파일로 내보내는 방법을 보여줍니다.

```php

    // 문서 열기
    $form = new facades_Form();
    $form->bindPdf($inputFile);

    // 폰트 파일을 쓰기 위한 FileOutputStream 객체 생성
    $xmlOutputStream = new java("java.io.FileOutputStream", "output.xfdf");

    // 데이터 내보내기
    $form->exportXfdf($xmlOutputStream);

    // 파일 스트림 닫기
    $xmlOutputStream->close();

    // 문서 닫기
    $form->close();
```