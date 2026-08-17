---
title: AcroForm 만들기 - Java로 채울 수 있는 PDF 만들기
linktitle: AcroForm 생성
type: docs
weight: 10
url: /java/create-form/
description: Java용 Aspose.PDF를 사용하여 PDF 문서에서 처음부터 AcroForm 필드를 만듭니다.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 파일에 대화형 AcroForm 필드 만들기
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 AcroForm 필드를 생성하는 방법을 설명합니다. 대화형 PDF 양식의 텍스트 상자, 다중 위젯 텍스트 필드, 라디오 버튼, 콤보 상자, 체크박스, 목록 상자, 서명 필드 및 바코드 필드를 다룹니다.
---

Aspose.PDF for Java를 사용하면 처음부터 광범위한 AcroForm 필드 유형을 만들 수 있습니다.


## 
텍스트 상자 필드 만들기



새 PDF 양식에 한 줄 텍스트 입력 필드를 추가해야 할 때 이 예를 사용하십시오.


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만들고 페이지를 추가하세요.

1. 
대상 직사각형이 있는 [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/)를 만들고 모양을 구성합니다.

1. 
양식에 필드를 추가하고 문서를 저장합니다.


```java
public static void addTextBoxField(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Rectangle rectangle = new Rectangle(10, 600, 110, 620, true);
        TextBoxField textBoxField = new TextBoxField(page, rectangle);
        textBoxField.setPartialName("textbox1");
        textBoxField.setValue("Text Box");
        textBoxField.setDefaultAppearance(new DefaultAppearance("Arial", 10, Color.getDarkBlue().toRgb()));

        Border border = new Border(textBoxField);
        border.setWidth(1);
        border.setStyle(BorderStyle.Dashed);
        border.setDash(new Dash(3, 3));
        textBoxField.setBorder(border);

        textBoxField.getCharacteristics().setBorder(Color.getRed());
        textBoxField.getCharacteristics().setBackground(Color.getYellow().toRgb());

        document.getForm().add(textBoxField, 1);
        document.save(outputFile.toString());
    }
}
```

## 
여러 위젯이 포함된 텍스트 상자 필드 만들기



동일한 텍스트 필드 값이 페이지의 여러 위치에 표시되어야 하는 경우 이 예를 사용하십시오.


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만들고 페이지를 추가하세요.

1. 
필드 위젯에 대한 여러 직사각형과 모양을 정의합니다.

1. 
[TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/)를 생성하고 각 위젯을 구성한 후 문서를 저장합니다.


```java
public static void addTextBoxFieldNt(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Rectangle[] rects = {
                new Rectangle(10, 600, 110, 620, true),
                new Rectangle(10, 630, 110, 650, true),
                new Rectangle(10, 660, 110, 680, true)
        };

        DefaultAppearance[] defaultAppearances = {
                new DefaultAppearance("Arial", 10, Color.getDarkBlue().toRgb()),
                new DefaultAppearance("Helvetica", 12, Color.getDarkGreen().toRgb()),
                new DefaultAppearance(FontRepository.findFont("Calibri"), 14, Color.getDarkMagenta().toRgb())
        };

        TextBoxField textBoxField = new TextBoxField(page, rects);
        textBoxField.setPartialName("textbox1");
        textBoxField.setValue("Some text");

        int index = 0;
        for (WidgetAnnotation widget : textBoxField) {
            widget.setDefaultAppearance(defaultAppearances[index]);
            index++;
        }

        Border border = new Border(textBoxField);
        border.setWidth(1);
        border.setStyle(BorderStyle.Dashed);
        border.setDash(new Dash(3, 3));
        textBoxField.setBorder(border);

        textBoxField.getCharacteristics().setBorder(Color.getRed());
        textBoxField.getCharacteristics().setBackground(Color.getYellow().toRgb());

        document.getForm().add(textBoxField);
        document.save(outputFile.toString());
    }
}
```

## 
라디오 버튼 필드 생성



양식에서 사용자가 사전 정의된 세트에서 하나의 옵션을 선택할 수 있도록 해야 하는 경우 이 예를 사용하십시오.


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만들고 페이지를 추가하세요.

1. 
[RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/radiobuttonfield/)를 만들고 필요한 옵션을 추가하세요.

1. 
양식에 필드를 추가하고 PDF를 저장합니다.


```java
public static void addRadioButton(Path outputFile) {
    try (Document document = new Document()) {
        document.getPages().add();

        RadioButtonField radio = new RadioButtonField(document.getPages().get_Item(1));
        radio.addOption("Option 1", new Rectangle(100, 640, 120, 680, true));
        radio.addOption("Option 2", new Rectangle(140, 640, 160, 680, true));

        document.getForm().add(radio);
        document.save(outputFile.toString());
    }
}
```

## 
콤보 상자 필드 만들기



사용자가 드롭다운 목록에서 하나의 값을 선택해야 하는 경우 이 예를 사용합니다.


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만들고 페이지를 추가하세요.

1. 
[ComboBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/comboboxfield/)를 만들고 선택 가능한 옵션을 추가합니다.

1. 
기본 선택을 설정하고 문서를 저장합니다.


```java
public static void addComboBox(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        ComboBoxField combo = new ComboBoxField(page, new Rectangle(100, 640, 150, 656, true));
        combo.addOption("Red");
        combo.addOption("Yellow");
        combo.addOption("Green");
        combo.addOption("Blue");
        combo.setSelected(3);

        document.getForm().add(combo);
        document.save(outputFile.toString());
    }
}
```

## 
체크박스 필드 생성



양식에 동의 또는 기능 선택과 같은 참 또는 거짓 옵션이 필요한 경우 이 예를 사용하십시오.


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만들고 페이지를 추가하세요.

1. 
[CheckboxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/checkboxfield/)를 생성하고 모양을 구성합니다.

1. 
양식에 확인란을 추가하고 출력 파일을 저장합니다.


```java
public static void addCheckboxFieldToPdf(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        CheckboxField checkbox = new CheckboxField(page, new Rectangle(50, 620, 100, 650, true));
        checkbox.getCharacteristics().setBackground(Color.getAqua().toRgb());
        checkbox.setStyle(BoxStyle.Circle);

        document.getForm().add(checkbox);
        document.save(outputFile.toString());
    }
}
```

## 
목록 상자 필드 만들기



양식이 표시 목록에 사용 가능한 여러 선택 항목을 표시해야 하는 경우 이 예를 사용하십시오.


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만들고 페이지를 추가하세요.

1. 
[ListBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/listboxfield/)를 만들고 사용 가능한 옵션을 추가합니다.

1. 
양식에 필드를 추가하고 문서를 저장합니다.


```java
public static void addListBoxFieldToPdf(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        ListBoxField listBox = new ListBoxField(page, new Rectangle(50, 650, 100, 700, true));
        listBox.setPartialName("list");
        listBox.addOption("Red");
        listBox.addOption("Green");
        listBox.addOption("Blue");

        document.getForm().add(listBox);
        document.save(outputFile.toString());
    }
}
```

## 
서명 필드 만들기



문서에서 디지털 서명을 위해 표시 영역을 예약해야 하는 경우 이 예를 사용하십시오.


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만들고 페이지를 추가하세요.

1. 
필요한 직사각형에 [서명 필드](https://reference.aspose.com/pdf/java/com.aspose.pdf/signaturefield/)를 만듭니다.

1. 
양식에 필드를 추가하고 출력 PDF를 저장합니다.


```java
public static void addSignatureField(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        SignatureField signatureField = new SignatureField(page, new Rectangle(100, 700, 200, 800, true));
        signatureField.setPartialName("Signature1");
        document.getForm().add(signatureField);
        document.save(outputFile.toString());
    }
}
```

## 
바코드 필드 생성



양식이 바코드 필드 내부에 기계 판독 가능 데이터를 표시해야 하는 경우 이 예를 사용하십시오.


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만들고 페이지를 추가하세요.

1. 
[BarcodeField](https://reference.aspose.com/pdf/java/com.aspose.pdf/barcodefield/)를 생성하고 바코드 값을 추가합니다.

1. 
양식에 필드를 추가하고 문서를 저장합니다.

```java
public static void addBarcodeField(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        BarcodeField barcode = new BarcodeField(page, new Rectangle(100, 700, 200, 740, true));
        barcode.setPartialName("Barcode1");
        barcode.addBarcode("1234567890");
        document.getForm().add(barcode);
        document.save(outputFile.toString());
    }
}
```
