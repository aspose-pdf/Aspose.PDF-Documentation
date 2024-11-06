---
title: 내장된 이미지의 해상도 및 치수 가져오기
linktitle: 해상도 및 치수 가져오기
type: docs
weight: 40
url: ko/java/get-resolution-and-dimensions-of-embedded-images/
description: 이 섹션은 내장된 이미지의 해상도 및 치수를 얻는 방법에 대한 세부 정보를 보여줍니다.
lastmod: "2021-06-05"
---

이 주제는 이미지를 추출하지 않고도 이미지에 대한 해상도 및 치수 정보를 얻을 수 있는 기능을 제공하는 Aspose.PDF 네임스페이스의 연산자 클래스를 사용하는 방법을 설명합니다.

이를 달성하는 데는 여러 가지 방법이 있습니다. 이 문서에서는 `arraylist`와 [이미지 배치 클래스](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacement)를 사용하는 방법을 설명합니다.

1. 먼저 소스 PDF 파일(이미지가 포함된)을 로드합니다.
1. 그런 다음 문서의 모든 이미지 이름을 저장할 ArrayList 객체를 만듭니다.
1. Page.Resources.Images 속성을 사용하여 이미지를 가져옵니다.
1. 이미지의 그래픽 상태를 저장할 스택 객체를 생성하고 이를 사용하여 다양한 이미지 상태를 추적합니다.

1. 현재 변환을 정의하는 ConcatenateMatrix 객체를 생성합니다. 이 객체는 콘텐츠의 크기 조정, 회전 및 왜곡도 지원합니다. 이 객체는 새로운 행렬을 이전 행렬과 결합합니다. 변환을 처음부터 정의할 수는 없으며 기존 변환만 수정할 수 있다는 점에 유의하세요.
2. ConcatenateMatrix로 행렬을 수정할 수 있기 때문에 원래 이미지 상태로 되돌려야 할 수도 있습니다. GSave 및 GRestore 연산자를 사용하세요. 이 연산자들은 쌍으로 사용되므로 함께 호출되어야 합니다. 예를 들어, 복잡한 변환으로 그래픽 작업을 수행한 후 최종적으로 변환을 초기 상태로 되돌리려면, 접근 방식은 다음과 같습니다:

```java
// 텍스트를 그립니다.
GSave

ConcatenateMatrix  // 연산자 이후 내용을 회전시킵니다.

// 그래픽 작업

ConcatenateMatrix // 연산자 이후 내용을 이전 회전과 함께 크기 조정합니다.

// 다른 그래픽 작업

GRestore

// 텍스트를 그립니다.
```

결과적으로, 텍스트는 일반 형식으로 그려지지만 텍스트 연산자 사이에 일부 변환이 수행됩니다.
 이미지를 표시하거나 폼 객체 및 이미지를 그리기 위해서는 Do 연산자를 사용해야 합니다.

또한 이미지의 크기를 가져오는 데 사용할 수 있는 Width와 Height라는 두 가지 속성을 제공하는 XImage라는 클래스도 있습니다.

1. 이미지 해상도를 계산하기 위한 계산을 수행합니다.
2. 이미지 이름과 함께 명령 프롬프트에 정보를 표시합니다.

다음 코드 스니펫은 PDF 문서에서 이미지를 추출하지 않고 이미지의 크기와 해상도를 가져오는 방법을 보여줍니다.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.operators.*;
import java.util.*;

public class ExampleImagesResolution {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExampleAddPageNumber() 
    {
        // 원본 PDF 파일을 로드합니다.
        Document doc = new Document(_dataDir+ "ImageInformation.pdf");
        
        // 이미지에 대한 기본 해상도를 정의합니다.
        int defaultResolution = 72;

        Stack<Object> graphicsState = new Stack<Object>();

        // 이미지 이름을 저장할 배열 목록 객체를 정의합니다.
        List<String> imageNames = Arrays.asList(doc.getPages().get_Item(1).getResources().getImages().getNames());
        //ArrayList imageNames = new ArrayList<>(Arrays.asList(names));
        // 스택에 객체를 삽입합니다.
        graphicsState.push(new Matrix(1, 0, 0, 1, 0, 0));

        // 문서의 첫 번째 페이지의 모든 연산자를 가져옵니다.
        for (Operator op : doc.getPages().get_Item(1).getContents())
        {
            // 변형을 이전에 설정한 상태로 되돌리기 위해 GSave/GRestore 연산자를 사용합니다.
            GSave opSaveState = (GSave) op;
            GRestore opRestoreState = (GRestore) op;
            // 현재 변환 행렬을 정의하는 ConcatenateMatrix 객체를 인스턴스화합니다.
            ConcatenateMatrix opCtm = (ConcatenateMatrix) op;
            // 리소스에서 객체를 그리는 Do 연산자를 생성합니다. 폼 객체와 이미지 객체를 그립니다.
            Do opDo = (Do) op;

            if (opSaveState != null)
            {
                // 이전 상태를 저장하고 현재 상태를 스택의 맨 위로 푸시합니다.
                Matrix m = new Matrix((Matrix)graphicsState.peek());
                graphicsState.push(m);
            }
            else if (opRestoreState != null)
            {
                // 현재 상태를 버리고 이전 상태로 복원합니다.
                graphicsState.pop();
            }
            else if (opCtm != null)
            {
                Matrix cm = new Matrix(
                (float)opCtm.getMatrix().getA(),
                (float)opCtm.getMatrix().getB(),
                (float)opCtm.getMatrix().getC(),
                (float)opCtm.getMatrix().getD(),
                (float)opCtm.getMatrix().getE(),
                (float)opCtm.getMatrix().getF());

                // 현재 행렬에 상태 행렬을 곱합니다.
                ((Matrix)graphicsState.peek()).multiply(cm);

                continue;
            }
            else if (opDo != null)
            {
                // 이미지 그리기 연산자인 경우
                if (imageNames.contains(opDo.getName()))
                {
                    Matrix lastCTM = (Matrix)graphicsState.peek();
                    // 첫 번째 PDF 페이지의 이미지를 저장할 XImage 객체를 생성합니다.
                    XImage image = doc.getPages().get_Item(1).getResources().getImages().get_Item(opDo.getName());

                    // 이미지 크기를 가져옵니다.
                    double scaledWidth = Math.sqrt(Math.pow(lastCTM.getElements()[0], 2) + Math.pow(lastCTM.getElements()[1], 2));
                    double scaledHeight = Math.sqrt(Math.pow(lastCTM.getElements()[2], 2) + Math.pow(lastCTM.getElements()[3], 2));
                    // 이미지의 높이와 너비 정보를 가져옵니다.
                    double originalWidth = image.getWidth();
                    double originalHeight = image.getHeight();

                    // 위 정보를 기반으로 해상도를 계산합니다.
                    double resHorizontal = originalWidth * defaultResolution / scaledWidth;
                    double resVertical = originalHeight * defaultResolution / scaledHeight;

                    // 각 이미지의 크기 및 해상도 정보를 표시합니다.
                    System.out.printf(_dataDir + "image %s (%.2f:%.2f): res %.2f x %.2f",
                                        opDo.getName(), scaledWidth, scaledHeight, resHorizontal,
                                        resVertical);
                }
                // 출력 문서를 저장합니다.
                doc.save(_dataDir);
            }
        }
    }
}
```