---
title: AcroForms 수정
linktitle: AcroForms 수정
type: docs
weight: 40
url: ko/java/modifing-form/
description: 이 섹션에서는 Aspose.PDF for PHP via Java를 사용하여 PDF 문서의 양식을 수정하는 방법을 설명합니다.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 사용자 정의 양식 필드 폰트 설정

Adobe PDF 파일의 양식 필드는 특정 기본 폰트를 사용하도록 구성할 수 있습니다. Aspose.PDF는 개발자가 14개의 기본 폰트 중 하나 또는 사용자 정의 폰트를 필드 기본 폰트로 적용할 수 있도록 합니다. 양식 필드에 사용되는 기본 폰트를 설정하고 업데이트하기 위해, Aspose.PDF는 DefaultAppearance (Font font, double size, Color color) 클래스를 제공합니다. 이 클래스는 com.aspose.pdf.DefaultAppearance를 사용하여 접근할 수 있습니다. 이 객체를 사용하기 위해서는 Field 클래스의 setDefaultAppearance(..) 메서드를 사용합니다.

다음 코드 스니펫은 PDF 양식 필드의 기본 폰트를 설정하는 방법을 보여줍니다.

```php

    // 문서 열기
    $document = new Document($inputFile);

    // 문서에서 특정 양식 필드 가져오기
    $field = $document->getForm()->get("textbox1");

    // 폰트 객체 생성
    $fontRepository = new FontRepository();
    $font = $fontRepository->findFont("ComicSansMS");

    $colors = new Color();
    $blackColor = $colors->getBlack();

    // 양식 필드에 대한 폰트 정보 설정
    $field->setDefaultAppearance(new DefaultAppearance($font, 10, $blackColor));

    // 업데이트된 문서 저장
    $document->save($outputFile);
    $document->close();        

    $document->close();
```


## Get/Set FieldLimit

이 코드는 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스를 사용하여 문서를 열고, 양식 필드를 검색하고, 최대 길이를 설정하고, 'setMaxLen' 및 'getMaxLen' 메서드를 사용하여 최대 길이를 검색하는 방법을 보여줍니다.

```php

    // 문서 열기
    $document = new Document($inputFile);

    // 문서에서 특정 양식 필드 가져오기
    $field = $document->getForm()->get("textbox1");
    
    $field->setMaxLen(10);

    // DOM을 사용하여 최대 필드 제한 가져오기
    $responseData = "Limit: " . $field->getMaxLen();          

    $document->close();
```

다음 코드 조각을 사용하여 Aspose.PDF.Facades 네임스페이스를 사용하여 동일한 값을 가져올 수도 있습니다.

```php

    // 문서 열기
    $document = new Document($inputFile);

    // 문서에서 특정 양식 필드 가져오기
    $field = $document->getForm()->get("textbox1");

    // DOM을 사용하여 최대 필드 제한 가져오기
    $responseData = "Limit: " . $field->getMaxLen();          

    $document->close();
```


유사하게, Aspose.PDF는 DOM 접근 방식을 사용하여 필드 제한을 가져오는 메서드를 가지고 있습니다. 다음 코드 스니펫은 그 단계를 보여줍니다.

```php

    // 문서 열기
    $document = new Document($inputFile);

    // 문서에서 특정 폼 필드 가져오기
    $field = $document->getForm()->get("textbox1");

    // 필드 삭제
    $field->delete();
    
    $document->close();
```
## PDF 문서에서 특정 폼 필드 삭제

모든 폼 필드는 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 Form 컬렉션에 포함되어 있습니다. 이 컬렉션은 삭제 메서드를 포함하여 폼 필드를 관리하는 다양한 메서드를 제공합니다. 특정 필드를 삭제하고 싶다면, 필드 이름을 매개변수로 전달하여 delete 메서드를 호출한 후 업데이트된 PDF 문서를 저장하십시오.

다음 코드 스니펫은 PDF 문서에서 이름이 지정된 필드를 삭제하는 방법을 보여줍니다.

```php

    // 문서 열기
    $document = new Document($inputFile);

    // 문서에서 특정 폼 필드 가져오기
    $field = $document->getForm()->get("textbox1");

    // 필드 삭제
    $field->delete();
    
    $document->close();
```


## PDF 문서에서 양식 필드 수정하기

[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 Form 컬렉션을 사용하여 PDF 문서의 양식 필드를 관리할 수 있습니다.

양식 필드를 수정하려면 Form 컬렉션에서 필드를 가져와 해당 속성을 설정합니다. 그런 다음 업데이트된 PDF 문서를 저장합니다.

다음 코드 스니펫은 PDF 문서에서 기존 양식 필드를 수정하는 방법을 보여줍니다.

```php

    // 문서 열기
    $document = new Document($inputFile);

    // 문서에서 특정 양식 필드 가져오기
    $field = $document->getForm()->get("textbox1");

    // 필드 값 수정
    $field->setValue("Updated Value");

    // 필드를 읽기 전용으로 설정
    $field->setReadOnly(true);

    // 업데이트된 문서 저장
    $document->save($outputFile);        
    $document->close();
```

### PDF 파일에서 양식 필드를 새 위치로 이동하기

양식 필드를 PDF 페이지의 새 위치로 이동하려면 먼저 필드 객체를 가져온 다음 setRect 메서드에 대한 새 값을 지정합니다.
 A [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) 객체가 새로운 좌표와 함께 setRect(..) 메서드에 할당됩니다. 그런 다음 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 save 메서드를 사용하여 업데이트된 PDF를 저장합니다.

다음 코드 스니펫은 양식 필드를 새 위치로 이동하는 방법을 보여줍니다.

```php

    // 문서 열기
    $document = new Document($inputFile);

    // 문서에서 특정 양식 필드 가져오기
    $field = $document->getForm()->get("textbox1");

    // 필드 위치 수정
    $field->setRect(new Rectangle(300, 400, 600, 500));

    // 업데이트된 문서 저장
    $document->save($outputFile);        
    $document->close();
```