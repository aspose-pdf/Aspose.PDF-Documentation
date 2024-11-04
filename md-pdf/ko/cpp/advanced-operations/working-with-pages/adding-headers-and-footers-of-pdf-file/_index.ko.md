---
title: PDF에 머리글과 바닥글 추가
linktitle: PDF에 머리글과 바닥글 추가
type: docs
weight: 70
url: /cpp/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for C++를 사용하여 PDF 파일에 TextStamp 클래스를 사용해 머리글과 바닥글을 추가할 수 있습니다.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for C++**를 사용하면 기존 PDF 파일에 머리글과 바닥글을 추가할 수 있습니다. PDF 문서에 이미지나 텍스트를 추가할 수 있습니다. 또한, C++로 하나의 PDF 파일에 다양한 머리글을 추가해 보세요.

## PDF 파일의 머리글에 텍스트 추가

[TextStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text_stamp) 클래스를 사용하여 PDF 파일의 머리글에 텍스트를 추가할 수 있습니다. 
TextStamp 클래스는 글꼴 크기, 글꼴 스타일 및 글꼴 색상 등과 같은 텍스트 기반 스탬프를 만드는 데 필요한 속성을 제공합니다. 헤더에 텍스트를 추가하려면 필요한 속성을 사용하여 Document 객체와 TextStamp 객체를 생성해야 합니다. 그런 다음, 페이지의 AddStamp 메서드를 호출하여 PDF의 헤더에 텍스트를 추가할 수 있습니다.

PDF의 헤더 영역에 텍스트가 조정되도록 TopMargin 속성을 설정해야 합니다. 또한 HorizontalAlignment를 Center로 설정하고 VerticalAlignment를 Top으로 설정해야 합니다.

다음 코드 스니펫은 C++로 PDF 파일의 헤더에 텍스트를 추가하는 방법을 보여줍니다.

```cpp
void AddingTextInHeaderOfPdfFile() {
    String _dataDir("C:\\Samples\\");
    String inputFileName("TextinHeader.pdf");
    String outputFileName("TextinHeader_out.pdf");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 헤더 생성
    auto textStamp = MakeObject<TextStamp>(u"Header Text");

    // 스탬프의 속성 설정
    textStamp->set_TopMargin(10);
    textStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    textStamp->set_VerticalAlignment(VerticalAlignment::Top);

    // 모든 페이지에 헤더 추가
    for(auto page : document->get_Pages())
    {
        page->AddStamp(textStamp);
    }

    // 업데이트된 문서 저장
    document->Save(_dataDir + outputFileName);
}
```
## PDF 파일의 바닥글에 텍스트 추가하기

TextStamp 클래스를 사용하여 PDF 파일의 바닥글에 텍스트를 추가할 수 있습니다. TextStamp 클래스는 글꼴 크기, 글꼴 스타일, 글꼴 색상 등 텍스트 기반 스탬프를 생성하는 데 필요한 속성을 제공합니다. 바닥글에 텍스트를 추가하려면, 필요한 속성을 사용하여 Document 객체와 TextStamp 객체를 생성해야 합니다. 그 후, PDF의 바닥글에 텍스트를 추가하기 위해 Page의 AddStamp 메서드를 호출할 수 있습니다.

{{% alert color="primary" %}}

PDF의 바닥글 영역에 텍스트가 조정되도록 하려면 Bottom Margin 속성을 설정해야 합니다. 또한, HorizontalAlignment를 Center로, VerticalAlignment를 Bottom으로 설정해야 합니다.

{{% /alert %}}

다음 코드 스니펫은 C++로 PDF 파일의 바닥글에 텍스트를 추가하는 방법을 보여줍니다.

```cpp
void AddingTextInFooterOfPdfFile() {
    String _dataDir("C:\\Samples\\");
    String inputFileName("TextinFooter.pdf");
    String outputFileName("TextinFooter_out.pdf");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 바닥글 생성
    auto textStamp = MakeObject<TextStamp>(u"Footer Text");

    // 스탬프의 속성 설정
    textStamp->set_BottomMargin(10);
    textStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    textStamp->set_VerticalAlignment(VerticalAlignment::Bottom);

    // 모든 페이지에 바닥글 추가
    for (auto page : document->get_Pages())
    {
        page->AddStamp(textStamp);
    }

    // 업데이트된 문서 저장
    document->Save(_dataDir + outputFileName);
}
```

## PDF 파일 헤더에 이미지 추가

[ImageStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_stamp) 클래스를 사용하여 PDF 파일의 헤더에 이미지를 추가할 수 있습니다. Image Stamp 클래스는 글꼴 크기, 글꼴 스타일, 글꼴 색상 등 이미지 기반 스탬프를 생성하는 데 필요한 속성을 제공합니다. 헤더에 이미지를 추가하려면 Document 객체와 필요한 속성을 사용하여 Image Stamp 객체를 생성해야 합니다. 그런 다음, PDF의 헤더에 이미지를 추가하기 위해 Page의 AddStamp 메서드를 호출할 수 있습니다.

다음 코드 스니펫은 C++로 PDF 파일의 헤더에 이미지를 추가하는 방법을 보여줍니다.

```cpp
void AddingImageInHeaderOfPdfFile() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("ImageinHeader.pdf");
    String outputFileName("ImageinHeader_out.pdf");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 헤더 생성
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");

    // 스탬프의 속성 설정
    imageStamp->set_TopMargin(10);
    imageStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    imageStamp->set_VerticalAlignment (VerticalAlignment::Top);

    // 모든 페이지에 헤더 추가
    for(auto page : document->get_Pages())
    {
        page->AddStamp(imageStamp);
    }

    // 업데이트된 문서 저장
    document->Save(_dataDir + outputFileName);
}
```

## PDF 파일의 바닥글에 이미지 추가하기

PDF 파일의 바닥글에 이미지를 추가하기 위해서는 Image Stamp 클래스를 사용할 수 있습니다. Image Stamp 클래스는 글꼴 크기, 글꼴 스타일, 글꼴 색상 등 이미지 기반의 스탬프를 생성하는 데 필요한 속성을 제공합니다. 바닥글에 이미지를 추가하려면, 필요한 속성을 사용하여 Document 객체와 Image Stamp 객체를 생성해야 합니다. 그 후, PDF의 바닥글에 이미지를 추가하기 위해 Page의 AddStamp 메서드를 호출할 수 있습니다.

PDF의 바닥글 영역에 이미지를 조정할 수 있도록 [BottomMargin](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.stamp#aeab91949cf3eb473018b31a74fed7173) 속성을 설정해야 합니다. 또한, [HorizontalAlignment](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#aefec9c0bf30ee5e6fb2640e69aed6cd9)를 `Center`로, [VerticalAlignment](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ad4956d03096fc515eaa34319a6bf636a)를 `Bottom`으로 설정해야 합니다.

다음 코드 스니펫은 C++를 사용하여 PDF 파일의 바닥글에 이미지를 추가하는 방법을 보여줍니다.

```cpp
void AddingImageInFooterOfPdfFile() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("ImageinFooter.pdf");
    String outputFileName("ImageinFooter_out.pdf");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 헤더 생성
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");

    // 스탬프의 속성 설정
    imageStamp->set_TopMargin(10);
    imageStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    imageStamp->set_VerticalAlignment(VerticalAlignment::Top);

    // 모든 페이지에 헤더 추가
    for (auto page : document->get_Pages())
    {
        page->AddStamp(imageStamp);
    }

    // 업데이트된 문서 저장
    document->Save(_dataDir + outputFileName);
}
```

## 하나의 PDF 파일에 다른 헤더 추가하기

우리는 TopMargin 또는 Bottom Margin 속성을 사용하여 문서의 헤더/푸터 섹션에 TextStamp를 추가할 수 있다는 것을 알고 있지만, 때로는 단일 PDF 문서에 여러 헤더/풋터를 추가해야 할 필요가 있을 수 있습니다. **Aspose.PDF for C++**는 이를 수행하는 방법을 설명합니다.

이 요구 사항을 달성하기 위해, 개별 TextStamp 객체(필요한 헤더/푸터의 수에 따라 객체 수가 결정됨)를 만들고 이를 PDF 문서에 추가할 것입니다. 개별 스탬프 객체에 대해 다른 서식 정보를 지정할 수도 있습니다. 다음 예에서는 Document 객체와 세 개의 TextStamp 객체를 생성한 후, [AddStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a3b998038dedf5266b4d60586b1b53d02) 메서드를 사용하여 PDF의 헤더 섹션에 텍스트를 추가했습니다. 다음 코드 스니펫은 Aspose.PDF for C++를 사용하여 PDF 파일의 푸터에 이미지를 추가하는 방법을 보여줍니다.

```cpp
void AddingDifferentHeadersInOnePDFFile()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("multiheader.pdf");
    String outputFileName("multiheader_out.pdf");

    // Open source document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Create three stamps
    auto stamp1 = MakeObject<TextStamp>("Header 1");
    auto stamp2 = MakeObject<TextStamp>("Header 2");
    auto stamp3 = MakeObject<TextStamp>("Header 3");

    // Set stamp alignment (place stamp on page top, centered horiznotally)
    stamp1->set_VerticalAlignment(VerticalAlignment::Top);
    stamp1->set_HorizontalAlignment(HorizontalAlignment::Center);
    // Specify the font style as Bold
    stamp1->get_TextState()->set_FontStyle(FontStyles::Bold);
    // Set the text fore ground color information as red
    stamp1->get_TextState()->set_ForegroundColor(Color::get_Red());
    // Specify the font size as 14
    stamp1->get_TextState()->set_FontSize(14);

    // Now we need to set the vertical alignment of 2nd stamp object as Top
    stamp2->set_VerticalAlignment(VerticalAlignment::Top);
    // Set Horizontal alignment information for stamp as Center aligned
    stamp2->set_HorizontalAlignment (HorizontalAlignment::Center);
    // Set the zooming factor for stamp object
    stamp2->set_Zoom(10);

    // Set the formatting of 3rd stamp object
    // Specify the Vertical alignment information for stamp object as TOP
    stamp3->set_VerticalAlignment(VerticalAlignment::Top);
    // Set the Horizontal alignment inforamtion for stamp object as Center aligned
    stamp3->set_HorizontalAlignment(HorizontalAlignment::Center);
    // Set the rotation angle for stamp object
    stamp3->set_RotateAngle(35);
    // Set pink as background color for stamp
    stamp3->get_TextState()->set_BackgroundColor(Color::get_Pink());
    // Change the font face information for stamp to Verdana
    stamp3->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));

    // First stamp is added on first page;
    document->get_Pages()->idx_get(1)->AddStamp(stamp1);
    // Second stamp is added on second page;
    document->get_Pages()->idx_get(2)->AddStamp(stamp2);
    // Third stamp is added on third page.
    document->get_Pages()->idx_get(3)->AddStamp(stamp3);

    // Save updated document
    document->Save(_dataDir + outputFileName);
}
```