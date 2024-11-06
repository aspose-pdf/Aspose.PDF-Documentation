---
title: AcroForms 생성 - Java에서 작성 가능한 PDF 생성
linktitle: AcroForms 생성
type: docs
weight: 10
url: ko/java/create-forms/
description: 이 섹션에서는 Aspose.PDF for Java를 사용하여 PDF 문서에서 AcroForms를 처음부터 생성하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 문서에 양식 필드 추가

[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스는 PDF 문서에서 양식 필드를 관리하는 데 도움이 되는 Form이라는 컬렉션을 제공합니다.

양식 필드를 추가하려면:

1. 추가하려는 양식 필드를 생성합니다.
2. [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/Form) 컬렉션의 add 메서드를 호출합니다.

이 예제는 TextBoxField를 추가하는 방법을 보여줍니다. 동일한 방법으로 모든 양식 필드를 추가할 수 있습니다:

1. 먼저 필드 객체를 생성하고 속성을 설정합니다.
2. 그런 다음 필드를 Form 컬렉션에 추가합니다.

### TextBoxField 추가

텍스트 필드는 수신자가 양식에 텍스트를 입력할 수 있도록 하는 양식 요소입니다.
 이것은 사용자가 원하는 것을 입력할 자유를 허용하고자 할 때 언제든지 사용될 수 있습니다.

다음 코드 스니펫은 PDF 문서에 TextBoxField를 추가하는 방법을 보여줍니다.

```java
public class ExamplesCreateForm {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void AddingTextBoxField() {

        // 문서 열기
        Document pdfDocument = new Document(_dataDir + "TextField.pdf");
        Page page = pdfDocument.getPages().get_Item(1);
        // 필드 생성
        TextBoxField textBoxField = new TextBoxField(page, new Rectangle(100, 200, 300, 300));
        textBoxField.setPartialName("textbox1");
        textBoxField.setValue("Text Box");

        // TextBoxField.Border = new Border(
        Border border = new Border(textBoxField);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        textBoxField.setBorder(border);

        textBoxField.setColor(Color.getGreen());

        // 문서에 필드 추가
        pdfDocument.getForm().add(textBoxField, 1);

        // 수정된 PDF 저장
        pdfDocument.save(_dataDir + "TextBox_out.pdf");

    }
```

## RadioButtonField 추가

라디오 버튼은 일반적으로 다중 선택 질문에 사용되며, 하나의 답변만 선택할 수 있는 시나리오에서 사용됩니다.

다음 코드는 PDF 문서에 [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField)를 추가하는 방법을 보여줍니다.

```java
public static void AddingRadioButton() {
        Document pdfDocument = new Document();
        // PDF 파일에 페이지 추가
        pdfDocument.getPages().add();

        // 페이지 번호를 인수로 사용하여 RadioButtonField 객체 인스턴스화
        RadioButtonField radio = new RadioButtonField(pdfDocument.getPages().get_Item(1));

        // 첫 번째 라디오 버튼 옵션 추가 및 Rectangle 객체를 사용하여 기원 지정
        radio.addOption("Test", new Rectangle(20, 720, 40, 740));
        // 두 번째 라디오 버튼 옵션 추가
        radio.addOption("Test1", new Rectangle(120, 720, 140, 740));
        // Document 객체의 폼 객체에 라디오 버튼 추가
        pdfDocument.getForm().add(radio);
        // PDF 파일 저장
        pdfDocument.save("RadioButtonSample.pdf");

    }
```


다음 코드 스니펫은 세 가지 옵션을 가진 [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField)를 추가하고 이를 테이블 셀에 배치하는 단계를 보여줍니다.

```java
public static void AddingRadioButtonAdvanced() {
        Document doc = new Document();
        Page page = doc.getPages().add();
        Table table = new Table();
        table.setColumnWidths("120 120 120");
        page.getParagraphs().add(table);
        Row r1 = table.getRows().add();
        Cell c1 = r1.getCells().add();
        Cell c2 = r1.getCells().add();
        Cell c3 = r1.getCells().add();

        RadioButtonField rf = new RadioButtonField(page);
        rf.setPartialName("radio");
        doc.getForm().add(rf, 1);

        RadioButtonOptionField opt1 = new RadioButtonOptionField();
        RadioButtonOptionField opt2 = new RadioButtonOptionField();
        RadioButtonOptionField opt3 = new RadioButtonOptionField();

        opt1.setOptionName("Item1");
        opt2.setOptionName("Item2");
        opt3.setOptionName("Item3");

        opt1.setWidth(15);
        opt1.setHeight(15);
        opt2.setWidth(15);
        opt2.setHeight(15);
        opt3.setWidth(15);
        opt3.setHeight(15);

        rf.add(opt1);
        rf.add(opt2);
        rf.add(opt3);

        opt1.setBorder(new Border(opt1));
        opt1.getBorder().setWidth(1);
        opt1.getBorder().setStyle(BorderStyle.Solid);
        opt1.getCharacteristics().setBorder(Color.getBlack());
        opt1.getDefaultAppearance().setTextColor(java.awt.Color.RED);
        opt1.setCaption(new TextFragment("Item1"));
        opt2.setBorder(new Border(opt2));
        opt2.getBorder().setWidth(1);
        opt2.getBorder().setStyle(BorderStyle.Solid);
        opt2.getCharacteristics().setBorder(java.awt.Color.BLACK);
        opt2.getDefaultAppearance().setTextColor(java.awt.Color.RED);
        opt2.setCaption(new TextFragment("Item2"));
        opt3.setBorder(new Border(opt3));
        opt3.getBorder().setWidth(1);
        opt3.getBorder().setStyle(BorderStyle.Solid);
        opt3.getCharacteristics().setBorder(java.awt.Color.BLACK);
        opt3.getDefaultAppearance().setTextColor(java.awt.Color.RED);
        opt3.setCaption(new TextFragment("Item3"));
        c1.getParagraphs().add(opt1);
        c2.getParagraphs().add(opt2);
        c3.getParagraphs().add(opt3);

        doc.save("RadioButtonField.pdf");
    }
```


## RadioButtonField에 캡션 추가하기

다음 코드 스니펫은 [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField)와 연관된 캡션을 추가하는 방법을 보여줍니다:

```java
public static void AddingCaptionToRadioButtonField() {
        // 소스 PDF 폼 로드
        com.aspose.pdf.facades.Form form1 = new com.aspose.pdf.facades.Form(_dataDir + "RadioButtonField.pdf");
        Document document = new Document(_dataDir + "RadioButtonField.pdf");
        for (String item : form1.getFieldNames()) {
            System.out.println(item.toString());
            if (item.contains("radio1")) {
                RadioButtonField field0 = (RadioButtonField) document.getForm().get(item);
                RadioButtonOptionField fieldoption = new RadioButtonOptionField();
                fieldoption.setOptionName("Yes");
                fieldoption.setPartialName("Yesname");

                var updatedFragment = new TextFragment("test123");
                updatedFragment.getTextState().setFont(FontRepository.findFont("Arial"));
                updatedFragment.getTextState().setFontSize(10);
                updatedFragment.getTextState().setLineSpacing(6.32f);

                // TextParagraph 객체 생성
                TextParagraph par = new TextParagraph();

                // 단락 위치 설정
                par.setPosition(new Position(field0.getRect().getLLX(),
                        field0.getRect().getLLY() + updatedFragment.getTextState().getFontSize()));
                // 단어 줄바꿈 모드 지정
                par.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);

                // 새 TextFragment를 단락에 추가
                par.appendLine(updatedFragment);

                // TextBuilder를 사용하여 TextParagraph 추가
                TextBuilder textBuilder = new TextBuilder(document.getPages().get_Item(1));
                textBuilder.appendParagraph(par);

                field0.deleteOption("item1");
            }
        }
        document.save(_dataDir + "RadioButtonField_out.pdf");

    }
```


## 콤보박스 필드 추가하기

콤보박스는 문서에 드롭다운 메뉴를 추가하는 양식 필드입니다.

다음 코드 스니펫은 PDF 문서에 [ComboBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/ComboBoxField) 필드를 추가하는 방법을 보여줍니다.

```java
public static void AddingComboboxField() {
        // Document 객체 생성
        Document doc = new Document();
        // 문서 객체에 페이지 추가
        doc.getPages().add();
        // ComboBox Field 객체 인스턴스화
        ComboBoxField combo = new ComboBoxField(doc.getPages().get_Item(1), new Rectangle(100, 600, 150, 616));
        // 콤보박스에 옵션 추가
        combo.addOption("Red");
        combo.addOption("Yellow");
        combo.addOption("Green");
        combo.addOption("Blue");
        // 문서 객체의 폼 필드 컬렉션에 콤보박스 객체 추가
        doc.getForm().add(combo);
        // PDF 문서 저장
        doc.save("ComboBox_Added.pdf");
    }
```

## 양식에 툴팁 추가하기

Document 클래스는 PDF 문서의 양식 필드를 관리하는 Form이라는 컬렉션을 제공합니다.
 폼 필드에 툴팁을 추가하려면 Field 클래스 AlternateName을 사용하세요. Adobe Acrobat은 '대체 이름'을 필드 툴팁으로 사용합니다.

다음 코드 스니펫은 Java를 사용하여 폼 필드에 툴팁을 추가하는 방법을 보여줍니다.

```java
public static void AddTooltipToFormField() {
        // 소스 PDF 폼 로드
        Document doc = new Document(_dataDir + "AddTooltipToField.pdf");

        // 필드 가져오기
        TextBoxField textBoxField = (TextBoxField) doc.getForm().get("textbox1");

        // 텍스트 필드에 툴팁 설정
        textBoxField.setAlternateName("텍스트 상자 툴팁");

        // 수정된 문서 저장
        doc.save("output.pdf");
    }
```