---
title: 툴팁 사용 
linktitle: PDF 툴팁
type: docs
weight: 20
url: /ko/java/pdf-tooltip/
description: Java와 Aspose.PDF를 사용하여 PDF의 텍스트 조각에 툴팁을 추가하는 방법을 배웁니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 보이지 않는 버튼을 추가하여 검색된 텍스트에 툴팁 추가

PDF 문서에서 특정 구문이나 단어에 대한 세부 정보를 툴팁으로 추가하여 사용자가 텍스트에 마우스 커서를 올려놓을 때 팝업되도록 하는 경우가 자주 있습니다. Aspose.PDF for Java는 검색된 텍스트 위에 보이지 않는 버튼을 추가하여 툴팁을 생성하는 기능을 제공합니다. 다음 코드 스니펫은 이 기능을 구현하는 방법을 보여줍니다:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.ButtonField;
import com.aspose.pdf.Document;
import com.aspose.pdf.TextFragment;
import com.aspose.pdf.TextFragmentAbsorber;
import com.aspose.pdf.TextFragmentCollection;

public class ExampleToolTip {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddToolTip() {
        String outputFile = _dataDir + "Tooltip_out.pdf";

        // 텍스트가 있는 샘플 문서 생성
        Document doc = new Document();
        doc.getPages().add().getParagraphs().add(new TextFragment("여기에 마우스 커서를 이동하면 툴팁이 표시됩니다"));
        doc.getPages().get_Item(1).getParagraphs().add(new TextFragment("여기에 마우스 커서를 이동하면 매우 긴 툴팁이 표시됩니다"));
        doc.save(outputFile);

        // 텍스트가 있는 문서 열기
        Document document = new Document(outputFile);
        // 정규식과 일치하는 모든 구문을 찾기 위한 TextAbsorber 객체 생성
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("여기에 마우스 커서를 이동하면 툴팁이 표시됩니다");
        // 문서 페이지에 대해 흡수기 수락
        document.getPages().accept(absorber);
        // 추출된 텍스트 조각 가져오기
        TextFragmentCollection textFragments = absorber.getTextFragments();

        // 조각 반복
        for(TextFragment fragment : textFragments)
        {
            // 텍스트 조각 위치에 보이지 않는 버튼 생성
            ButtonField field = new ButtonField(fragment.getPage(), fragment.getRectangle());
            // AlternateName 값은 뷰어 애플리케이션에 의해 툴팁으로 표시됩니다
            field.setAlternateName ("텍스트에 대한 툴팁.");
            // 문서에 버튼 필드 추가
            document.getForm().add(field);
        }

        // 다음은 매우 긴 툴팁의 샘플입니다
        absorber = new TextFragmentAbsorber("여기에 마우스 커서를 이동하면 매우 긴 툴팁이 표시됩니다");
        document.getPages().accept(absorber);
        textFragments = absorber.getTextFragments();

        for(TextFragment fragment : textFragments)
        {
            ButtonField field = new ButtonField(fragment.getPage(), fragment.getRectangle());
            // 매우 긴 텍스트 설정
            field.setAlternateName ("Lorem ipsum dolor sit amet, consectetur adipiscing elit," +
                                    " sed do eiusmod tempor incididunt ut labore et dolore magna" +
                                    " aliqua. Ut enim ad minim veniam, quis nostrud exercitation" +
                                    " ullamco laboris nisi ut aliquip ex ea commodo consequat." +
                                    " Duis aute irure dolor in reprehenderit in voluptate velit" +
                                    " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint" +
                                    " occaecat cupidatat non proident, sunt in culpa qui officia" +
                                    " deserunt mollit anim id est laborum.");
            document.getForm().add(field);
        }

        // 문서 저장
        document.save(outputFile);
    }
}
```


{{% alert color="primary" %}}

툴팁의 길이에 관해서, 툴팁 텍스트는 PDF 문서에 PDF 문자열 유형으로 포함되어 있으며, 콘텐츠 스트림 외부에 있습니다. PDF 파일에는 이러한 문자열에 대한 효과적인 제한이 없습니다(참고: PDF 참조 부록 C). 그러나 특정 프로세서에서 특정 운영 환경에서 실행되는 적합한 리더(예: Adobe Acrobat)는 이러한 제한이 있습니다. PDF 리더 애플리케이션 설명서를 참조하십시오.

{{% /alert %}}

## 숨겨진 텍스트 블록을 만들고 마우스를 올리면 표시하기

Aspose.PDF에서는 숨김 동작을 구현하여 보이지 않는 버튼 위에 마우스를 올리거나 뗄 때 텍스트 상자 필드(또는 다른 유형의 주석)를 표시/숨길 수 있습니다. 이를 위해 Aspose.Pdf.Annotations.HideAction 클래스를 사용하여 텍스트 블록에 숨김/표시 동작을 할당합니다. 마우스를 올리거나 뗄 때 텍스트 블록을 표시/숨기기 위해 다음 코드 스니펫을 사용하십시오.

또한 문서 내 PDF 동작은 적합한 리더(예:
 Adobe Reader)에는 보증이 없지만 다른 PDF 리더(e.g. 웹 브라우저 플러그인)에는 보증이 없습니다. 우리는 간단한 조사를 제공하였고 다음과 같은 결과를 발견했습니다:

- PDF 문서의 숨기기 동작의 모든 구현이 Internet Explorer v.11.0에서 잘 작동합니다.
- 숨기기 동작의 모든 구현이 Opera v.12.14에서도 작동하지만, 문서를 처음 열 때 약간의 응답 지연이 발생합니다.
- Google Chrome v.61.0에서 문서를 탐색할 경우, 필드 이름을 수용하는 HideAction 생성자를 사용하는 구현만 작동합니다; Google Chrome에서 탐색이 중요할 경우 해당 생성자를 사용하십시오:

>buttonField.Actions.OnEnter = new HideAction(floatingField.FullName, false);
>buttonField.Actions.OnExit = new HideAction(floatingField.FullName);

```java
    public static void name() {
        String outputFile = _dataDir + "TextBlock_HideShow_MouseOverOut_out.pdf";

        // 텍스트가 포함된 샘플 문서 생성
        Document doc = new Document();
        doc.getPages().add().getParagraphs().add(new TextFragment("마우스 커서를 이곳에 이동하여 떠 있는 텍스트를 표시합니다"));
        doc.save(outputFile);

        // 텍스트가 포함된 문서 열기
        Document document = new Document(outputFile);
        // 정규 표현식과 일치하는 모든 구문을 찾기 위해 TextAbsorber 객체 생성
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("마우스 커서를 이곳에 이동하여 떠 있는 텍스트를 표시합니다");
        // 문서 페이지에 흡수기 적용
        document.getPages().accept(absorber);
        // 첫 번째로 추출된 텍스트 조각 가져오기
        TextFragmentCollection textFragments = absorber.getTextFragments();
        TextFragment fragment = textFragments.get_Item(1);

        // 페이지의 지정된 사각형에 떠 있는 텍스트를 위한 숨겨진 텍스트 필드 생성
        TextBoxField floatingField = new TextBoxField(fragment.getPage(), new Rectangle(100, 700, 220, 740));
        // 필드 값으로 표시될 텍스트 설정
        floatingField.setValue("이것은 \"떠 있는 텍스트 필드\"입니다.");
        // 이 시나리오에서 필드를 '읽기 전용'으로 설정하는 것을 권장합니다
        floatingField.setReadOnly(true);

        // 문서 열기 시 필드를 보이지 않도록 하기 위해 '숨김' 플래그 설정
        floatingField.setFlags(floatingField.getFlags() | AnnotationFlags.Hidden);

        // 고유한 필드 이름을 설정하는 것은 필수가 아니지만 허용됩니다
        floatingField.setPartialName("FloatingField_1");

        // 필드 외관의 특성을 설정하는 것은 필수가 아니지만 더 좋게 만듭니다
        DefaultAppearance da = new DefaultAppearance("Helvetica", 16, java.awt.Color.RED);
        floatingField.setDefaultAppearance(da);
        //new DefaultAppearance("Helv", 10, Color.getBlue()
        floatingField.getCharacteristics().setBackground(Color.getLightBlue());
        floatingField.getCharacteristics().setBorder(Color.getDarkBlue());;
        floatingField.setBorder(new Border(floatingField));
        floatingField.getBorder().setWidth(1);
        floatingField.setMultiline(true);

        // 문서에 텍스트 필드 추가
        document.getForm().add(floatingField);

        // 텍스트 조각 위치에 보이지 않는 버튼 생성
        Field buttonField = new ButtonField(fragment.getPage(), fragment.getRectangle());
        // 지정된 필드(주석)와 보이지 않는 플래그에 대한 새로운 숨기기 동작 생성
        // (위에서 지정한 경우 이름으로 떠 있는 필드를 참조할 수도 있습니다.)
        // 보이지 않는 버튼 필드에서 마우스 입력/출력 시 동작 추가
        buttonField.getActions().setOnEnter(new HideAction(floatingField, false));
        buttonField.getActions().setOnExit(new HideAction(floatingField));

        // 문서에 버튼 필드 추가
        document.getForm().add(buttonField);

        // 문서 저장
        document.save(outputFile);
    }
```