---
title: 레거시 Aspose.Pdf.Kit for Java에서의 마이그레이션
type: docs
weight: 10
url: /ko/java/migration-from-legacy-aspose-pdf-kit-for-java/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

현재의 Aspose.PDF.Kit for Java 컴포넌트는 기존 PDF 파일을 조작하는 기능을 제공했습니다. 그러나 조만간 이 컴포넌트는 별도의 제품으로서 단종될 예정입니다. 왜냐하면 우리는 모든 클래스와 열거형을 새로 자동 이식된 Aspose.PDF for Java(4.x.x)의 **com.aspose.pdf.facades** 패키지로 포팅했기 때문입니다. 이제 이 단일 자동 이식된 릴리스는 기존 PDF 파일을 생성하고 조작하는 기능을 제공합니다.

{{% /alert %}}

## 레거시 코드 지원

전체 마이그레이션 활동 동안, 우리는 이 활동이 기존 고객에게 미치는 영향을 확실히 고려했으며, 이 영향을 가능한 한 최소화하려고 최선을 다했습니다.
 또한, 기존 고객의 코드베이스가 최소한의 변경만 필요하도록 새로운 자동 포팅 릴리스를 이전 버전과 호환되게 만드는 데 중점을 두었습니다. 새로운 자동 포팅 릴리스는 com.aspose.pdf 패키지에서 문서 객체 모델(DOM)을 제공하여 기존 PDF 파일을 생성하고 조작할 수 있지만, Aspose.PDF.Kit for Java로 개발된 기존 코드를 계속 사용하고 싶다면 **com.aspose.pdf.facades** 패키지를 가져오기만 하면 되고, 코드가 작동해야 합니다 (*명시적 클래스 참조 업데이트는 제외*).

다음 코드 스니펫은 새로운 자동 포팅 Aspose.PDF for Java로 기존 Aspose.PDF.Kit for Java 코드를 실행하는 방법을 보여줍니다.

```java

 import com.aspose.pdf.facades.*;

public class template {

    public static void main(String[] args) {

        try{

            // 기존 PDF 파일 로드

            com.aspose.pdf.facades.PdfFileInfo fileInfo = new com.aspose.pdf.facades.PdfFileInfo("input.pdf");

            System.out.println("제목: " + fileInfo.getTitle());

            System.out.println("저자:" + fileInfo.getAuthor());

            System.out.println("생성일자:" + fileInfo.getCreationDate());

            System.out.println("제작자:" + fileInfo.getCreator());

            System.out.println("키워드:" + fileInfo.getKeywords());

            System.out.println("수정일자:" + fileInfo.getModDate());

           }


catch(Exception ex)


{System.out.println(ex);}


}

}
```

## ReplaceTextStrategy 클래스 사용

ReplaceTextStrategy 클래스의 코드를 마이그레이션하기 위해, **setScope(..)** 메서드가 **setReplaceScope(..)**로 업데이트되었습니다. 다음 코드 스니펫을 참조하십시오.

```java

// PdfContentEditor 객체를 인스턴스화

com.aspose.pdf.facades.PdfContentEditor editor = new com.aspose.pdf.facades.PdfContentEditor();

// 소스 PDF 파일 바인드

editor.bindPdf("input.pdf");

// 텍스트 교체 전략 생성

com.aspose.pdf.facades.ReplaceTextStrategy strategy = new com.aspose.pdf.facades.ReplaceTextStrategy();

// 텍스트 교체를 위한 정렬 설정

strategy.setAlignment(com.aspose.pdf.facades.AlignmentType.Left);

// 텍스트 교체 범위

strategy.setReplaceScope(com.aspose.pdf.facades.ReplaceTextStrategy.Scope.REPLACE_ALL);

// 교체 전략 설정

editor.setReplaceTextStrategy(strategy);

editor.replaceText("test","replaced");

// 업데이트된 파일 저장

editor.save("TxtReplaceTest.pdf");
```