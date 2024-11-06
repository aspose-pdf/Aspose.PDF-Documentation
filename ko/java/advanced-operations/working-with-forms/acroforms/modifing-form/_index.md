---
title: AcroForms 수정
linktitle: AcroForms 수정
type: docs
weight: 40
url: ko/java/modifing-form/
description: 이 섹션에서는 Aspose.PDF for Java를 사용하여 PDF 문서의 양식을 수정하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 사용자 지정 양식 필드 폰트 설정

Adobe PDF 파일의 양식 필드는 특정 기본 폰트를 사용하도록 구성할 수 있습니다. Aspose.PDF는 개발자가 14개 핵심 폰트 중 하나 또는 사용자 지정 폰트를 필드 기본 폰트로 적용할 수 있도록 합니다. 양식 필드에 사용되는 기본 폰트를 설정하고 업데이트하려면 Aspose.PDF에는 DefaultAppearance (Font font, double size, Color color) 클래스가 있습니다. 이 클래스는 com.aspose.pdf.DefaultAppearance를 사용하여 액세스할 수 있습니다. 이 객체를 사용하려면 Field 클래스의 setDefaultAppearance(..) 메서드를 사용하십시오.

다음 코드 조각은 PDF 양식 필드의 기본 폰트를 설정하는 방법을 보여줍니다.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.DefaultAppearance;
import com.aspose.pdf.Document;
import com.aspose.pdf.Field;
import com.aspose.pdf.Font;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.Rectangle;
import com.aspose.pdf.TextBoxField;

public class ExamplesModifying {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void SetFormFieldFontOtherThan14CorePDFFonts() {
        // 문서 열기
        Document pdfDocument = new Document(_dataDir + "FormFieldFont14.pdf");
        // 문서에서 특정 양식 필드 가져오기
        Field field = (Field) pdfDocument.getForm().get("textbox1");

        // 폰트 객체 생성
        Font font = FontRepository.findFont("ComicSansMS");

        // 양식 필드에 대한 폰트 정보 설정
        field.setDefaultAppearance (new DefaultAppearance(font, 10, java.awt.Color.BLACK));
        
        // 업데이트된 문서 저장
        pdfDocument.save(_dataDir + "FormFieldFont14_out.pdf");
    }
```


## Get/Set FieldLimit

FormEditor 클래스의 SetFieldLimit 메서드는 필드 제한, 즉 필드에 입력할 수 있는 최대 문자 수를 설정할 수 있게 해줍니다.

```java
    public static void GettingMaximumFieldLimit()
    {
        // DOM을 사용하여 최대 필드 제한 가져오기
        Document doc = new Document(_dataDir + "FieldLimit.pdf");
        TextBoxField field = (TextBoxField)doc.getForm().get("textbox1");
        System.out.println("Limit: " +field.getMaxLen());
    }
```

다음 코드 스니펫을 사용하여 Aspose.PDF.Facades 네임스페이스를 사용하여 동일한 값을 얻을 수도 있습니다.

```java
    public static void GettingMaximumFieldLimitFacades()
    {
        // Facades를 사용하여 최대 필드 제한 가져오기
        com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form();
        form.bindPdf(_dataDir + "FieldLimit.pdf");
        System.out.println("Limit: " + form.getFieldLimit("textbox1"));
    }
```

마찬가지로 Aspose.PDF는 DOM 접근 방식을 사용하여 필드 제한을 가져오는 메서드를 가지고 있습니다.
 다음 코드 스니펫은 단계를 보여줍니다.

```java
    public static void SettingMaximumFieldLimit()
    {
        // DOM을 사용하여 최대 필드 제한 설정
        Document doc = new Document(_dataDir + "FieldLimit.pdf");
        TextBoxField field = (TextBoxField)doc.getForm().get("textbox1");
        field.setMaxLen(10);
        System.out.println("Limit: " +field.getMaxLen());       
    }
```

## PDF 문서에서 특정 양식 필드 삭제

모든 양식 필드는 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 Form 컬렉션에 포함되어 있습니다. 이 컬렉션은 양식 필드를 관리하는 다양한 메서드를 제공하며, delete 메서드도 포함되어 있습니다. 특정 필드를 삭제하려면 필드 이름을 delete 메서드의 매개변수로 전달한 다음 업데이트된 PDF 문서를 저장하십시오.

다음 코드 스니펫은 PDF 문서에서 이름이 지정된 필드를 삭제하는 방법을 보여줍니다.

```java
    public static void DeleteParticularFormField()
    {    
        // 문서 열기
        Document pdfDocument = new Document("input.pdf");

        // 이름으로 지정된 필드 삭제
        pdfDocument.getForm().delete("textbox1");

        // 수정된 PDF 저장
        pdfDocument.save("output.pdf");
    }
```

## PDF 문서에서 폼 필드 수정

[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 Form 컬렉션은 PDF 문서에서 폼 필드를 관리할 수 있게 해줍니다.

폼 필드를 수정하려면 Form 컬렉션에서 필드를 가져와 해당 속성을 설정합니다. 그런 다음 업데이트된 PDF 문서를 저장합니다.

다음 코드 스니펫은 PDF 문서에서 기존 폼 필드를 수정하는 방법을 보여줍니다.

```java
    public static void ModifyFormField()
    {
        Document pdfDocument = new Document("input.pdf");
        // 필드 가져오기
        TextBoxField textBoxField = (TextBoxField) pdfDocument.getForm().get("textbox1");

        // 필드 값 수정
        textBoxField.setValue("Updated Value");

        // 필드를 읽기 전용으로 설정
        textBoxField.setReadOnly(true);

        // 업데이트된 문서 저장
        pdfDocument.save("output.pdf");
    }
```

### PDF 파일에서 폼 필드를 새 위치로 이동

폼 필드를 PDF 페이지의 새 위치로 이동하려면 먼저 필드 객체를 가져온 다음 setRect 메서드에 대해 새 값을 지정합니다.
 A [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) 객체가 새로운 좌표로 setRect(..) 메서드에 할당됩니다. 그런 다음 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 save 메서드를 사용하여 업데이트된 PDF를 저장합니다.

다음 코드 스니펫은 양식 필드를 새 위치로 이동하는 방법을 보여줍니다.

```java
    public static void ModifyMoveFormFieldNewLocation()
    {    
        // 문서 열기
        Document pdfDocument = new Document(_dataDir+"input.pdf");
        // 필드 가져오기
        TextBoxField textBoxField = (TextBoxField) pdfDocument.getForm().get("textbox1");

        // 필드 위치 수정
        textBoxField.setRect(new Rectangle(300, 400, 600, 500));

        // 수정된 문서 저장
        pdfDocument.save("output.pdf");
    }
}
```