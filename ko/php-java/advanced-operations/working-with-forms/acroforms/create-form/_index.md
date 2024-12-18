---
title: 아크로폼 생성 - PHP에서 작성 가능한 PDF 생성
linktitle: 아크로폼 생성
type: docs
weight: 10
url: /ko/php-java/create-forms/
description: 이 섹션에서는 Aspose.PDF for PHP via Java를 사용하여 PDF 문서에서 아크로폼을 처음부터 생성하는 방법을 설명합니다.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 문서에 양식 필드 추가

[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스는 PDF 문서에서 양식 필드를 관리하는 데 도움이 되는 Form이라는 컬렉션을 제공합니다.

양식 필드를 추가하려면:

1. 추가하고자 하는 양식 필드를 생성합니다.
2. [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/Form) 컬렉션의 add 메서드를 호출합니다.

이 예제는 TextBoxField를 추가하는 방법을 보여줍니다. 동일한 접근 방식을 사용하여 모든 양식 필드를 추가할 수 있습니다:

1. 먼저 필드 객체를 생성하고 속성을 설정합니다.
2. 그런 다음 필드를 Form 컬렉션에 추가합니다.

### TextBoxField 추가

텍스트 필드는 수신자가 양식에 텍스트를 입력할 수 있게 하는 양식 요소입니다.
 사용자가 원하는 내용을 자유롭게 입력할 수 있도록 허용하고 싶을 때마다 사용할 수 있습니다.

다음 코드 스니펫은 PDF 문서에 TextBoxField를 추가하는 방법을 보여줍니다.

```php

    // 문서 열기
    $colors = new Color();
    $document = new Document($inputFile);
    $page = $document->getPages()->get_Item(1);

    // 필드 생성
    $textBoxField = new TextBoxField($page, new Rectangle(110, 300, 310, 320));
    $textBoxField->setPartialName("textbox1");
    $textBoxField->setValue("텍스트 상자에 있는 일부 값");

    $border = new Border($textBoxField);
    $border->setWidth(5);
    $border->setDash(new Dash(1, 1));
    $textBoxField->setBorder($border);
    $textBoxField->setColor($colors->getGreen());

    // 문서에 필드 추가
    $document->getForm()->add($textBoxField, 1);

    // 수정된 PDF 저장
    $document->save($outputFile);
    $document->close();
```

## RadioButtonField 추가하기

라디오 버튼은 일반적으로 다지선다형 질문에서 사용되며, 하나의 답변만 선택할 수 있는 경우에 사용됩니다.
다음 코드 스니펫은 PDF 문서에 [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField)를 추가하는 방법을 보여줍니다.

```php

    // 문서 열기            
    $document = new Document($inputFile);

    // PDF 파일에 페이지 추가
    $page = $document->getPages()->get_Item(1);

    // 페이지 번호를 인수로 사용하여 RadioButtonField 객체 인스턴스화
    $radio = new RadioButtonField($page);

    // 첫 번째 라디오 버튼 옵션 추가 및 그 기원을 지정
    // Rectangle 객체 사용

    $radio->addOption("Test1", new Rectangle(20, 720, 40, 740));

    // 두 번째 라디오 버튼 옵션 추가
    $radio->addOption("Test2", new Rectangle(120, 720, 140, 740));

    // Document 객체의 폼 객체에 라디오 버튼 추가
    $document->getForm()->add($radio);

    // PDF 파일 저장
    $document->save($outputFile);
    $document->close();
```

다음 코드 스니펫은 세 가지 옵션을 가진 [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField)를 추가하고 이를 테이블 셀 안에 배치하는 단계를 보여줍니다.

```php

    $colors = new Color();
    $document = new Document();
    $page = $document->getPages()->add();

    $table = new Table();
    $table->setColumnWidths("120 120 120");
    $page->getParagraphs()->add($table);
    $r1 = $table->getRows()->add();
    $c1 = $r1->getCells()->add();
    $c2 = $r1->getCells()->add();
    $c3 = $r1->getCells()->add();

    $rf = new RadioButtonField($page);
    $rf->setPartialName("radio1");
    $document->getForm()->add($rf, 1);

    $opt1 = new RadioButtonOptionField();
    $opt2 = new RadioButtonOptionField();
    $opt3 = new RadioButtonOptionField();

    $opt1->setOptionName("Item1");
    $opt2->setOptionName("Item2");
    $opt3->setOptionName("Item3");

    $opt1->setWidth(15.0);
    $opt1->setHeight(15.0);
    $opt2->setWidth(15.0);
    $opt2->setHeight(15.0);
    $opt3->setWidth(15.0);
    $opt3->setHeight(15.0);

    $rf->add($opt1);
    $rf->add($opt2);
    $rf->add($opt3);

    $border1 = new Border($opt1);
    $opt1->setBorder($border1);
    $opt1->getBorder()->setWidth(1.0);
    $opt1->getBorder()->setStyle(BorderStyle::$Solid);
    $opt1->getCharacteristics()->setBorder($colors->getBlack());
    $opt1->getDefaultAppearance()->setTextColor($colors->getRed()->toRgb());
    $opt1->setCaption(new TextFragment("항목1"));

    $border2 = new Border($opt2);
    $opt3->setBorder($border2);
    $opt3->getBorder()->setWidth(1.0);
    $opt3->getBorder()->setStyle(BorderStyle::$Solid);
    $opt2->getCharacteristics()->setBorder($colors->getBlack());
    $opt2->getDefaultAppearance()->setTextColor($colors->getRed()->toRgb());
    $opt2->setCaption(new TextFragment("항목2"));

    $border3 = new Border($opt3);
    $opt3->setBorder($border3);
    $opt3->getBorder()->setWidth(1.0);
    $opt3->getBorder()->setStyle(BorderStyle::$Solid);
    $opt3->getCharacteristics()->setBorder($colors->getBlack());
    $opt3->getDefaultAppearance()->setTextColor($colors->getRed()->toRgb());
    $opt3->setCaption(new TextFragment("항목3"));

    $c1->getParagraphs()->add($opt1);
    $c2->getParagraphs()->add($opt2);
    $c3->getParagraphs()->add($opt3);

    $document->save($outputFile);
    $document->close();
```


## 콤보박스 필드 추가

콤보박스는 문서에 드롭다운 메뉴를 추가하는 양식 필드입니다.

다음 코드 스니펫은 PDF 문서에 [ComboBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/ComboBoxField) 필드를 추가하는 방법을 보여줍니다.

```php

        $document = new Document($inputFile);

        // ComboBox 필드 객체 인스턴스화
        $page = $document->getPages()->get_Item(1);
        $combo = new ComboBoxField($page, new Rectangle(100, 600, 150, 616));

        // ComboBox에 옵션 추가
        $combo->addOption("Red");
        $combo->addOption("Yellow");
        $combo->addOption("Green");
        $combo->addOption("Blue");

        // 콤보박스 객체를 문서 객체의 폼 필드 컬렉션에 추가
        $document->getForm()->add($combo);

        // PDF 문서 저장
        $document->save($outputFile);
        $document->close();
```

## 폼에 툴팁 추가

Document 클래스는 PDF 문서에서 양식 필드를 관리하는 Form이라는 컬렉션을 제공합니다.
 양식 필드에 툴팁을 추가하려면 Field 클래스 AlternateName을 사용하세요. Adobe Acrobat은 ‘대체 이름’을 필드 툴팁으로 사용합니다.

다음의 코드 스니펫은 PHP로 양식 필드에 툴팁을 추가하는 방법을 보여줍니다.

```php

    $document = new Document($inputFile);
    $textBoxField = $document->getForm()->get("textbox1");

    // 텍스트 필드에 툴팁 설정
    $textBoxField->setAlternateName("텍스트 박스 툴팁");

    // PDF 문서 저장
    $document->save($outputFile);
    $document->close();
```