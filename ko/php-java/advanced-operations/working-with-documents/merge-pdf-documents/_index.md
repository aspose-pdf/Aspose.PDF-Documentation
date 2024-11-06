---
title: PDF 병합을 프로그래밍 방식으로 수행하기
linktitle: PDF 파일 병합
type: docs
weight: 50
url: ko/php-java/merge-pdf-documents/
description: 이 페이지는 PHP를 사용하여 PDF 문서를 단일 PDF 파일로 병합하는 방법을 설명합니다.
lastmod: "2024-06-05"
---

이제 PDF 파일 병합은 가장 요구되는 작업 중 하나입니다.
이 문서는 Aspose.PDF for PHP via Java를 사용하여 여러 PDF 파일을 단일 PDF 문서로 병합하는 방법을 보여줍니다. 예제는 Java로 작성되었지만, API는 다른 프로그래밍 언어에서도 사용할 수 있습니다. PDF 파일은 첫 번째 파일이 다른 문서의 끝에 결합되도록 병합됩니다.

## PHP를 사용하여 PDF 파일 병합

{{% alert color="primary" %}}

Aspose.PDF를 사용하여 PDF 파일을 병합하고 이 링크에서 온라인으로 결과를 얻을 수 있습니다: [Merger](https://products.aspose.app/pdf/merger)

{{% /alert %}}

두 개의 PDF 파일을 연결하려면:

1. 각 입력 PDF 파일을 포함하는 두 개의 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document) 객체를 만듭니다.

1. 그런 다음 [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection) 컬렉션의 Add 메서드를 호출하여 다른 PDF 파일을 추가하려는 Document 객체에 추가합니다.
1. 두 번째 Document 객체의 PageCollection 컬렉션을 첫 번째 PageCollection 컬렉션의 Add 메서드에 전달합니다.
1. 마지막으로 Save 메서드를 사용하여 출력 PDF 파일을 저장합니다.

다음 코드 스니펫은 PHP를 사용하여 PDF 파일을 연결하는 방법을 보여줍니다.

```php
    // 첫 번째 문서 열기
    $document1 = new Document($inputFile1);
    
    // 두 번째 문서 열기
    $document2 = new Document($inputFile2);

    // 두 번째 문서의 페이지를 첫 번째 문서에 추가
    $document1->getPages()->add($document2->getPages());

    // 연결된 출력 파일 저장
    $document1->save($outputFile);
    $document1->close();
    $document2->close();
```