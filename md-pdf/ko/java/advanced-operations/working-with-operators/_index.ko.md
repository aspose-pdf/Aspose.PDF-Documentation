---
title: 연산자 다루기
linktitle: 연산자 다루기
type: docs
weight: 170
url: /java/operators/
description: 이 주제는 Aspose.PDF와 함께 연산자를 사용하는 방법을 설명합니다. 연산자 클래스는 PDF 조작을 위한 훌륭한 기능을 제공합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 연산자 및 사용법 소개

연산자는 페이지에 그래픽 모양을 그리는 등 수행할 작업을 지정하는 PDF 키워드입니다. 연산자 키워드는 초기 솔리더스 문자(2Fh)가 없는 점에서 명명된 객체와 구별됩니다. 연산자는 콘텐츠 스트림 내에서만 의미가 있습니다.

콘텐츠 스트림은 페이지에 그려질 그래픽 요소를 설명하는 지침으로 구성된 데이터의 PDF 스트림 객체입니다. PDF 연산자에 대한 자세한 내용은 [PDF 사양](https://www.adobe.com/devnet/pdf/pdf_reference.html)에서 찾을 수 있습니다.

### 구현 세부사항

이 주제는 Aspose.PDF와 함께 연산자를 사용하는 방법을 설명합니다.
 선택된 예제는 개념을 설명하기 위해 PDF 파일에 이미지를 추가합니다. PDF 파일에 이미지를 추가하려면 다른 연산자가 필요합니다. 이 예제에서는 [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave), [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/ConcatenateMatrix), [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do), 그리고 [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore)를 사용합니다.

- [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave) 연산자는 PDF의 현재 그래픽 상태를 저장합니다.
- 이 주제는 Aspose.PDF와 함께 연산자를 사용하는 방법을 설명합니다. 선택된 예제는 개념을 설명하기 위해 PDF 파일에 이미지를 추가합니다. PDF 파일에 이미지를 추가하려면 다양한 연산자가 필요합니다. 이 예제에서는 [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave), [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/ConcatenateMatrix), [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do), 그리고 [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore)를 사용합니다.
(concatenate matrix) 연산자는 이미지가 PDF 페이지에 어떻게 배치되어야 하는지를 정의하는 데 사용됩니다.
- [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do) 연산자는 페이지에 이미지를 그립니다.
- [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore) 연산자는 그래픽 상태를 복원합니다.

PDF 파일에 이미지를 추가하려면:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체를 생성하고 입력 PDF 문서를 엽니다.
1. 이미지가 추가될 특정 페이지를 가져옵니다.
1. 페이지의 리소스 컬렉션에 이미지를 추가합니다.
1. 연산자를 사용하여 페이지에 이미지를 배치합니다:
   - 먼저, [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave) 연산자를 사용하여 현재 그래픽 상태를 저장합니다.
   - 그런 다음, [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/ConcatenateMatrix) 연산자를 사용하여 이미지가 배치될 위치를 지정합니다.
   - [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do) 연산자를 사용하여 페이지에 이미지를 그립니다.
1. 마지막으로, [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore) 연산자를 사용하여 업데이트된 그래픽 상태를 저장합니다.

다음 코드 스니펫은 PDF 연산자를 사용하는 방법을 보여줍니다.

```java
public class WorkingWithOperators {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Operators/";

    public static void AddImageUsingOpeartors() {

        // 새 PDF 문서를 만듭니다
        Document pdfDocument = new Document(_dataDir + "PDFOperators.pdf");

        // 이미지가 추가될 페이지를 가져옵니다
        Page page = pdfDocument.getPages().get_Item(1);

        // 좌표를 설정합니다
        int lowerLeftX = 100;
        int lowerLeftY = 100;
        int upperRightX = 200;
        int upperRightY = 200;

        // 이미지를 스트림으로 로드합니다
        FileInputStream imageStream = null;
        try {
            imageStream = new FileInputStream(_dataDir + "PDFOperators.jpg");
        } catch (FileNotFoundException e) {
            // TODO 자동 생성된 catch 블록
            e.printStackTrace();
        }

        // 페이지 리소스의 이미지 컬렉션에 이미지를 추가합니다
        page.getResources().getImages().add(imageStream);

        // GSave 연산자를 사용합니다: 이 연산자는 현재 그래픽 상태를 저장합니다
        page.getContents().add(new GSave());
        // Rectangle 및 Matrix 객체를 생성합니다
        Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0,
                rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });

        // ConcatenateMatrix (행렬 연결) 연산자를 사용합니다: 이미지가 어떻게 배치되어야 하는지를 정의합니다
        page.getContents().add(new ConcatenateMatrix(matrix));

        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
        // Do 연산자를 사용합니다: 이 연산자는 이미지를 그립니다
        page.getContents().add(new Do(ximage.getName()));
        // GRestore 연산자를 사용합니다: 이 연산자는 그래픽 상태를 복원합니다
        page.getContents().add(new GRestore());

        // 업데이트된 문서를 저장합니다
        pdfDocument.save(_dataDir + "PDFOperators_out.pdf");
    }
```


## 페이지에 XForm 그리기 - 연산자 사용

이 주제는 GSave/GRestore 연산자와 ConcatenateMatrix 연산자를 사용하여 xForm의 위치를 설정하고 Do 연산자를 사용하여 페이지에 xForm을 그리는 방법을 설명합니다.

아래 코드는 PDF 파일의 기존 내용을 GSave/GRestore 연산자 쌍으로 감쌉니다. 이 접근 방식은 기존 내용의 끝에서 초기 그래픽 상태를 얻는 데 도움이 됩니다. 이 접근 방식을 사용하지 않으면 기존 연산자 체인의 끝에 바람직하지 않은 변환이 남아 있을 수 있습니다.

```java
    public static void DrawXFormUsingOpeartors() {
        String imageFile = _dataDir + "aspose-logo.jpg";
        String inFile = _dataDir + "DrawXFormOnPage.pdf";
        String outFile = _dataDir + "blank-sample2_out.pdf";

        Document pdfDocument = new Document(inFile);
        OperatorCollection pageContents = pdfDocument.getPages().get_Item(1).getContents();

        // 예제는
        // GSave/GRestore 연산자 사용법
        // xForm 위치 설정을 위한 ConcatenateMatrix 연산자 사용법
        // 페이지에 xForm을 그리기 위한 Do 연산자 사용법

        // 기존 내용을 GSave/GRestore 연산자 쌍으로 감쌉니다
        // 이는 기존 내용의 끝에서 초기 그래픽 상태를 얻기 위함입니다
        // 그렇지 않으면 기존 연산자 체인의 끝에 바람직하지 않은 변환이 남아 있을 수 있습니다
        pageContents.insert(1, new GSave());
        pageContents.add(new GRestore());

        // 새로운 명령 후 그래픽 상태를 적절히 지우기 위해 그래픽 상태 저장 연산자를 추가합니다
        pageContents.add(new GSave());

        // xForm 생성
        XForm form = XForm.createNewForm(pdfDocument.getPages().get_Item(1), pdfDocument);
        pdfDocument.getPages().get_Item(1).getResources().getForms().add(form);
        form.getContents().add(new GSave());

        // 이미지 너비와 높이 정의
        form.getContents().add(new ConcatenateMatrix(200, 0, 0, 200, 0, 0));

        // 스트림에 이미지 로드
        FileInputStream imageStream = null;
        try {
            imageStream = new FileInputStream(imageFile);
        } catch (FileNotFoundException e) {
            // TODO 자동 생성된 catch 블록
            e.printStackTrace();
        }

        // XForm 리소스의 이미지 컬렉션에 이미지 추가
        form.getResources().getImages().add(imageStream);
        XImage ximage = form.getResources().getImages().get_Item(form.getResources().getImages().size());
        // Do 연산자 사용: 이 연산자는 이미지를 그립니다
        form.getContents().add(new Do(ximage.getName()));
        form.getContents().add(new GRestore());

        pageContents.add(new GSave());
        // x=100 y=500 좌표에 폼 배치
        pageContents.add(new ConcatenateMatrix(1, 0, 0, 1, 100, 500));
        // Do 연산자로 폼 그리기
        pageContents.add(new Do(form.getName()));
        pageContents.add(new GRestore());

        pageContents.add(new GSave());

        // x=100 y=300 좌표에 폼 배치
        pageContents.add(new ConcatenateMatrix(1, 0, 0, 1, 100, 300));

        // Do 연산자로 폼 그리기
        pageContents.add(new Do(form.getName()));
        pageContents.add(new GRestore());

        // // GSave 이후 GRestore로 그래픽 상태 복원
        pageContents.add(new GRestore());
        pdfDocument.save(outFile);
    }
```


## 연산자 클래스를 사용하여 그래픽 개체 제거하기

연산자 클래스는 PDF 조작에 대한 훌륭한 기능을 제공합니다. PDF 파일에 [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) 클래스의 [DeleteImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#deleteImage--) 메서드를 사용하여 제거할 수 없는 그래픽이 포함된 경우, 대신 연산자 클래스를 사용하여 이를 제거할 수 있습니다.

다음 코드 스니펫은 그래픽을 제거하는 방법을 보여줍니다. PDF 파일에 그래픽에 대한 텍스트 레이블이 포함된 경우, 이 방법을 사용해도 PDF 파일에 남을 수 있음을 유의하십시오. 그러므로 이러한 이미지를 삭제하기 위한 대체 방법을 위해 그래픽 연산자를 검색하십시오.

```java
    public static void RemoveGraphicsOpeartors() {
        Document pdfDocument  = new Document(_dataDir+ "RemoveGraphicsObjects.pdf");
        Page page = pdfDocument.getPages().get_Item(2);
        OperatorCollection oc = page.getContents();

        // 경로-채색 연산자 사용
        Operator[] operators = new Operator[] {
                new Stroke(),
                new ClosePathStroke(),
                new Fill()
        };

        oc.delete(operators);
        pdfDocument.save(_dataDir+ "No_Graphics_out.pdf");
    }
```


## PDF 문서의 색상 공간 변경

{{% alert color="primary" %}}

Aspose.PDF for Java 9.0.0은 PDF 문서의 색상 공간 변경을 지원합니다. RGB 색상을 CMYK로, 혹은 그 반대로 변경할 수 있습니다.

{{% /alert %}}

색상 공간을 변경할 수 있도록 [Operator](https://reference.aspose.com/java/pdf/com.aspose.pdf/Operator) 클래스에 다음 메서드가 구현되었습니다. 이를 사용하여 특정 RGB/CMYK 색상을 CMYK/RGB 색상 공간으로 변경하고 나머지 PDF 문서는 그대로 유지할 수 있습니다.

{{% alert color="primary" %}}
**공용 API 변경**
다음 메서드가 구현되었습니다:

- com.aspose.pdf.Operator.SetRGBColorStroke.getCMYKColor(new double[3], new double[4])
- com.aspose.pdf.Operator.SetRGBColor.getCMYKColor(new double[3], new double[4])
- com.aspose.pdf.Operator.SetCMYKColorStroke.getRGBColor(new double[4], new double[3])
- com.aspose.pdf.Operator.SetCMYKColor.getRGBColor(new double[4], new double[3])

{{% /alert %}}

다음 코드 스니펫은 Aspose.PDF for Java를 사용하여 색상 공간을 변경하는 방법을 보여줍니다.

```java
Document doc = new Document("input_color.pdf");
OperatorCollection contents = doc.getPages().get_Item(1).getContents();
System.out.println("pdf 문서에서 RGB 색상 연산자의 값");
for (int j = 1; j <= contents.size(); j++) {
    Operator oper = contents.get_Item(j);
    if (oper instanceof Operator.SetRGBColor || oper instanceof Operator.SetRGBColorStroke)
        try {
            // RGB를 CMYK 색상으로 변환
            System.out.println(oper.toString());

            double[] rgbFloatArray = new double[] { Double.valueOf(oper.getParameters().get(0).toString()), Double.valueOf(oper.getParameters().get(1).toString()), Double.valueOf(oper.getParameters().get(2).toString()), };
            double[] cmyk = new double[4];
            if (oper instanceof Operator.SetRGBColor) {
                ((Operator.SetRGBColor) oper).getCMYKColor(rgbFloatArray, cmyk);
                contents.set_Item(j, new Operator.SetCMYKColor(cmyk[0], cmyk[1], cmyk[2], cmyk[3]));
            } else if (oper instanceof Operator.SetRGBColorStroke) {
                ((Operator.SetRGBColorStroke) oper).getCMYKColor(rgbFloatArray, cmyk);
                contents.set_Item(j, new Operator.SetCMYKColorStroke(cmyk[0], cmyk[1], cmyk[2], cmyk[3]));
            } else
                throw new java.lang.Throwable("지원되지 않는 명령");

        } catch (Throwable e) {
            e.printStackTrace();
        }
}
doc.save("input_colorout.pdf");

// 결과 테스트
System.out.println("결과 pdf 문서에서 변환된 CMYK 색상 연산자의 값");
doc = new Document("input_colorout.pdf");
contents = doc.getPages().get_Item(1).getContents();
for (int j = 1; j <= contents.size(); j++) {
    Operator oper = contents.get_Item(j);
    if (oper instanceof Operator.SetCMYKColor || oper instanceof Operator.SetCMYKColorStroke) {
        System.out.println(oper.toString());
    }
}
```