---
title: Java에서 PDF 연산자로 작업
linktitle: 운영자와 협력
type: docs
weight: 90
url: /java/working-with-operators/
description: 콘텐츠 스트림 조작, 이미지 배치, XForm 재사용 및 그래픽 정리를 위해 Java에서 하위 수준 PDF 연산자를 사용하는 방법을 알아보세요.
lastmod: "2026-06-25"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java에서 콘텐츠 스트림 제어를 위해 하위 수준 PDF 연산자 사용
Abstract: 이 문서에서는 Aspose.PDF for Java에서 하위 수준 PDF 연산자로 작업하는 방법을 설명합니다. 이미지를 정확하게 배치하고, 재사용 가능한 XForm 콘텐츠를 그리고, PDF 페이지에서 그래픽 연산자를 제거하는 방법을 알아보세요.
---
## 
PDF 연산자 및 사용법 소개



연산자는 페이지에 그래픽 모양을 그리는 등 수행해야 할 일부 작업을 지정하는 PDF 키워드입니다. 연산자 키워드는 초기 사선 문자(2Fh)가 없다는 점에서 명명된 개체와 구별됩니다. 연산자는 콘텐츠 스트림 내에서만 의미가 있습니다.



콘텐츠 스트림은 페이지에 그려질 그래픽 요소를 설명하는 지침으로 데이터가 구성된 PDF 스트림 개체입니다. PDF 연산자에 대한 자세한 내용은 [PDF 사양](https://opensource.adobe.com/dc-acrobat-sdk-docs/)에서 확인할 수 있습니다.



명시적 행렬 수학을 사용하여 이미지 배치, XForm을 통해 동일한 그래픽 여러 번 재사용, 페이지에서 하위 수준 그리기 지침 삭제 등 Java에서 PDF 컨텐츠 스트림을 직접 제어해야 하는 경우 이 페이지를 사용하십시오.


## 
PDF 연산자로 이미지 추가



더 높은 수준의 레이아웃 API를 통하지 않고 콘텐츠 스트림 수준에서 이미지 배치를 정확하게 제어해야 하는 경우 낮은 수준 연산자를 사용하세요.


1. 
[문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)로 원본 PDF를 열고 대상 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)을 가져옵니다.

1. 
페이지 리소스에 입력 이미지 스트림을 추가하고 반환된 리소스 이름을 유지합니다.

1. 
대상 영역을 정의하는 [사각형](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/)을 만들고 그 경계에서 [행렬](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/)을 만듭니다.

1. 
현재 그래픽 상태를 유지하려면 [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/gsave/)를 사용하고, 이미지를 배치하려면 [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/concatenatematrix/)를 사용하고, 이미지를 그리려면 [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/do/)를 사용하고, 이전 상태를 복원하려면 [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/grestore/)를 사용하세요.

1. 
업데이트된 PDF 문서를 저장합니다.


```java
public static void addImageUsingPdfOperators(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().get_Item(1);
        String imageName = page.getResources().getImages().add(imageStream);

        Rectangle rectangle = new Rectangle(100, 100, 200, 200, true);
        Matrix matrix = new Matrix(new double[]{
                rectangle.getURX() - rectangle.getLLX(),
                0,
                0,
                rectangle.getURY() - rectangle.getLLY(),
                rectangle.getLLX(),
                rectangle.getLLY()
        });

        page.getContents().add(new GSave());
        page.getContents().add(new ConcatenateMatrix(matrix));
        page.getContents().add(new Do(imageName));
        page.getContents().add(new GRestore());
        document.save(outputFile.toString());
    }
    System.out.println("Image added with PDF operators to " + outputFile);
}
```

## 
페이지에 재사용 가능한 XForm 콘텐츠 그리기



PDF 파일의 리소스를 복제하지 않고 동일한 이미지나 그래픽을 두 번 이상 렌더링해야 하는 경우 이 접근 방식을 사용합니다.


1. 
[문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)로 소스 PDF를 열고 대상 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 가져온 다음 해당 [OperatorCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/operatorcollection/)에 액세스하세요.

1. 
기존 페이지 콘텐츠를 [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/gsave/) 및 [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/grestore/)로 래핑하여 나중에 변환 시 원본 콘텐츠 스트림으로 유출되지 않도록 하세요.

1. 
[XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) 리소스를 생성하고, 양식 리소스에 이미지를 추가하고, [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/concatenatematrix/)와 [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/do/)를 사용하여 양식 내부에 이미지를 그립니다.

1. 
변환 행렬을 추가하고 `Do` 연산자로 양식 이름을 실행하여 여러 페이지 좌표에 동일한 양식을 배치합니다.

1. 
그래픽 상태를 복원하고 출력 PDF를 저장합니다.


```java
public static void drawXFormOnPage(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().get_Item(1);
        OperatorCollection pageContents = page.getContents();

        pageContents.insert(1, new GSave());
        pageContents.add(new GRestore());
        pageContents.add(new GSave());

        XForm form = XForm.createNewForm(page, document);
        page.getResources().getForms().add(form);

        form.getContents().add(new GSave());
        form.getContents().add(new ConcatenateMatrix(200, 0, 0, 200, 0, 0));
        String imageName = form.getResources().getImages().add(imageStream);
        form.getContents().add(new Do(imageName));
        form.getContents().add(new GRestore());

        addFormAt(pageContents, form.getName(), 100, 500);
        addFormAt(pageContents, form.getName(), 100, 300);

        pageContents.add(new GRestore());
        document.save(outputFile.toString());
    }
    System.out.println("XForm drawn on page in " + outputFile);
}

private static void addFormAt(OperatorCollection pageContents, String formName, double x, double y) {
    pageContents.add(new GSave());
    pageContents.add(new ConcatenateMatrix(1, 0, 0, 1, x, y));
    pageContents.add(new Do(formName));
    pageContents.add(new GRestore());
}
```

## 
페이지에서 그래픽 연산자 제거



콘텐츠 스트림에서 직접 제거해야 하는 벡터 드로잉 연산자가 페이지에 포함되어 있는 경우 이 예를 사용하세요.


1. 
[문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)로 원본 PDF를 열고 대상 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)을 가져옵니다.

1. 
페이지 콘텐츠 연산자를 반복하고 [Stroke](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/stroke/), [ClosePathStroke](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/closepathstroke/) 및 [Fill](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/fill/)의 인스턴스를 수집합니다.

1. 
페이지 콘텐츠에서 수집된 연산자를 삭제하고 업데이트된 PDF를 저장합니다.



이 기술은 대상 그리기 지침만 제거합니다. 페이지에 관련 텍스트 레이블이나 기타 비그래픽 연산자도 포함되어 있는 경우 해당 항목은 콘텐츠 스트림에 남아 있으며 별도의 정리 단계가 필요할 수 있습니다.


```java
public static void removeGraphicsObjects(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        List<Operator> operatorsToRemove = new ArrayList<>();
        for (Object item : page.getContents()) {
            Operator operator = (Operator) item;
            if (operator instanceof Stroke || operator instanceof ClosePathStroke || operator instanceof Fill) {
                operatorsToRemove.add(operator);
            }
        }
        page.getContents().delete(operatorsToRemove);
        document.save(outputFile.toString());
    }
    System.out.println("Graphics operators removed in " + outputFile);
}
```

## 
관련 주제


- 
[Java의 고급 PDF 작업](/pdf/java/advanced-operations/)

- 
[Java를 사용하여 PDF의 이미지 작업](/pdf/java/working-with-images/)

- 
[Java에서 PDF 페이지 작업](/pdf/java/working-with-pages/)

- 
[Java에서 벡터 그래픽 작업](/pdf/java/working-with-vector-graphics/)
