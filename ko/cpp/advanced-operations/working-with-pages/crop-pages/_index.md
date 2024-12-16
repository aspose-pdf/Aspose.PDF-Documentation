---
title: C++에서 프로그래밍 방식으로 PDF 페이지 자르기
linktitle: 페이지 자르기
type: docs
weight: 80
url: /ko/cpp/crop-pages/
description: Aspose.PDF for C++를 사용하여 너비, 높이, 블리드, 크롭 및 트림 박스와 같은 페이지 속성을 가져올 수 있습니다.
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 페이지 속성 가져오기

PDF 파일의 각 페이지에는 너비, 높이, 블리드, 크롭 및 트림 박스와 같은 여러 속성이 있습니다. Aspose.PDF를 사용하면 이러한 속성에 액세스할 수 있습니다.

- **미디어 박스**: 미디어 박스는 가장 큰 페이지 박스입니다. 이는 문서가 PostScript 또는 PDF로 인쇄될 때 선택된 페이지 크기(예: A4, A5, 미국 레터 등)에 해당합니다. 즉, 미디어 박스는 PDF 문서가 표시되거나 인쇄되는 매체의 물리적 크기를 결정합니다.
- **블리드 박스**: 문서에 블리드가 있는 경우, PDF는 블리드 박스를 포함하게 됩니다. Bleed는 페이지 가장자리를 넘어 확장되는 색상(또는 아트워크)의 양입니다. 문서가 인쇄되고 크기에 맞게 잘렸을 때("재단"), 잉크가 페이지 가장자리까지 가도록 하기 위해 사용됩니다. 페이지가 잘못 재단되더라도 - 재단 표시에서 약간 벗어나게 잘리더라도 - 페이지에 흰색 가장자리가 나타나지 않습니다.
- **Trim box**: Trim box는 인쇄 및 재단 후 문서의 최종 크기를 나타냅니다.
- **Art box**: Art box는 문서의 실제 내용 주위에 그려진 상자입니다. 이 페이지 상자는 다른 응용 프로그램에서 PDF 문서를 가져올 때 사용됩니다.
- **Crop box**: Crop box는 Adobe Acrobat에서 PDF 문서가 표시되는 "페이지" 크기입니다. 일반 보기에서는 Adobe Acrobat에서 crop box의 내용만 표시됩니다. 이러한 속성에 대한 자세한 설명은 Adobe.Pdf 명세서, 특히 10.10.1 Page Boundaries를 참조하십시오.
- **Page.Rect**: MediaBox와 DropBox의 교차점(일반적으로 보이는 직사각형)입니다. 아래 그림은 이러한 속성을 설명합니다.  
자세한 내용은 [이 페이지](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html)를 방문하십시오.

아래 스니펫은 페이지를 자르는 방법을 보여줍니다:

```cpp
void CropPagesPDF()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("crop_page.pdf");
    String outputFileName("crop_page_out.pdf");

    // 소스 문서 열기
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    Console::WriteLine(document->get_Pages()->idx_get(1)->get_CropBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_TrimBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_ArtBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_BleedBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_MediaBox());

    // 새로운 박스 직사각형 만들기
    auto newBox = MakeObject<Rectangle>(200, 220, 2170, 1520);
    document->get_Pages()->idx_get(1)->set_CropBox(newBox);
    document->get_Pages()->idx_get(1)->set_TrimBox(newBox);
    document->get_Pages()->idx_get(1)->set_ArtBox (newBox);
    document->get_Pages()->idx_get(1)->set_BleedBox (newBox);

    // 업데이트된 문서 저장
    document->Save(_dataDir + outputFileName);
}
```
In this example we used a sample file [here](crop_page.pdf). Initially our page looks like shown on the Figure 1.  
![Figure 1. Cropped Page](crop_page.png)

이 예제에서는 [여기](crop_page.pdf)에서 샘플 파일을 사용했습니다. 처음에 우리의 페이지는 그림 1에 표시된 대로 보입니다.  
![Figure 1. 잘린 페이지](crop_page.png)

After the change, the page will look like Figure 2.  
![Figure 2. Cropped Page](crop_page2.png)

변경 후, 페이지는 그림 2처럼 보일 것입니다.  
![Figure 2. 잘린 페이지](crop_page2.png)