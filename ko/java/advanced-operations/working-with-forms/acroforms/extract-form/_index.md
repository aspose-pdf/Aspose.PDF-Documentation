---
title: Extract Data AcroForms
linktitle: Extract Data AcroForms
type: docs
weight: 30
url: ko/java/extract-form/
description: 이 섹션에서는 Aspose.PDF for Java를 사용하여 PDF 문서에서 양식을 추출하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 문서의 개별 필드에서 값 가져오기

양식 필드의 [getValue() 메서드](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--)를 사용하면 특정 필드의 값을 가져올 수 있습니다.

값을 얻으려면 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 Form 컬렉션에서 양식 필드를 가져옵니다.

이 예제는 [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField)를 선택하고 [getValue() 메서드](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--)를 사용하여 그 값을 검색합니다.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Document;
import com.aspose.pdf.Field;
import com.aspose.pdf.TextBoxField;

public class ExamplesExtractFormData {
    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void GetValueFromIndividualFieldPDFDocument() {
        // 문서 열기
        Document pdfDocument = new Document(_dataDir+"GetValueFromField.pdf");

        // 필드 가져오기
        TextBoxField textBoxField = (TextBoxField) pdfDocument.getForm().get("textbox1");

        // 필드 이름 가져오기
        System.out.printf("PartialName :-" + textBoxField.getPartialName());

        // 필드 값 가져오기
        System.out.printf("Value :-" + textBoxField.getValue());
    }
```


## PDF 문서의 모든 필드에서 값 가져오기

PDF 문서의 모든 필드에서 값을 가져오기 위해서는 모든 폼 필드를 탐색한 후 [getValue() 메서드](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--)를 사용하여 값을 가져와야 합니다. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 [getForm() 메서드](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--)를 사용하여 Form 컬렉션에서 각 필드를 가져오고, getFields()를 사용하여 폼 필드 목록을 Field 배열에 가져온 다음 배열을 순회하여 필드의 값을 가져옵니다.

다음 코드 스니펫은 PDF 문서의 모든 필드에서 값을 가져오는 방법을 보여줍니다.

```java
    public static void GetValuesFromAllFieldsPDFDocument() {
        // 문서 열기
        Document document = new Document(_dataDir + "GetValuesFromAllFields.pdf");

        Field[] fields = document.getForm().getFields();
        for (int i = 0; i < fields.length; i++) {

            System.out.println("폼 필드: " + fields[i].getFullName());
            System.out.println("폼 필드 값: " + fields[i].getValue());
        }

    }
}
```


## PDF 파일의 특정 영역에서 양식 필드 가져오기

일부 경우에는 전체 양식이 아닌, 예를 들어 인쇄된 시트의 왼쪽 위 사분면에서만 데이터를 얻어야 할 때가 있습니다. Aspose.PDF for Java를 사용하면, 이는 문제가 되지 않습니다. PDF 파일의 주어진 영역 외부에 있는 필드를 걸러내기 위해 영역을 지정할 수 있습니다. PDF 파일의 특정 영역에서 양식 필드를 가져오려면:

1. Document 객체를 사용하여 PDF 파일을 엽니다.
1. 문서의 Forms 컬렉션에서 양식을 가져옵니다.
1. 직사각형 영역을 지정하고 이를 Form 객체의 [getFieldsInRect](https://reference.aspose.com/pdf/java/com.aspose.pdf/Form#getFieldsInRect-com.aspose.pdf.Rectangle-) 메서드에 전달합니다. [Fields](https://reference.aspose.com/pdf/java/com.aspose.pdf/Field) 컬렉션이 반환됩니다.
1. 이를 사용하여 필드를 조작합니다.

다음 코드 스니펫은 PDF 파일의 특정 직사각형 영역에서 양식 필드를 가져오는 방법을 보여줍니다.

```java
public static void GetValuesFromSpecificRegion() {
    // PDF 파일 열기
    Document doc = new Document(_dataDir + "GetFieldsFromRegion.pdf");

    // 해당 영역에서 필드를 가져오기 위해 직사각형 객체 생성
    Rectangle rectangle = new Rectangle(35, 30, 500, 500);

    // PDF 양식 가져오기
    com.aspose.pdf.Form form = doc.getForm();

    // 직사각형 영역에서 필드 가져오기
    Field[] fields = form.getFieldsInRect(rectangle);

    // 필드 이름과 값 표시
    for (Field field : fields)
    {
        // 모든 위치에 대한 이미지 배치 속성 표시
        System.out.println("Field Name: " + field.getFullName() + "-" + "Field Value: " + field.getValue());
    }
}
```