---
title: Qt에서 PDF 문서 작업
type: docs
weight: 130
url: /cpp/work-with-pdf-documents-in-qt/
lastmod: "2021-11-01"
---

Qt는 다양한 데스크톱, 모바일, 웹 및 임베디드 시스템 애플리케이션을 만들 수 있는 크로스 플랫폼 애플리케이션 개발 프레임워크입니다. 이 기사에서는 Qt 애플리케이션에서 PDF 문서 작업을 위해 C++ PDF 라이브러리를 통합하는 방법을 알아보겠습니다.

## Qt 내에서 Aspose.PDF for C++ 사용

Windows 운영 체제의 Qt 애플리케이션에서 Aspose.PDF for C++를 사용하려면 [downloads](https://downloads.aspose.com/pdf/cpp) 섹션에서 API의 최신 버전을 다운로드하십시오. API를 다운로드한 후 다음 옵션 중 하나를 사용하여 Qt와 함께 사용할 수 있습니다.

- Qt Creator 사용
- Visual Studio 사용

여기에서는 Qt Creator를 사용하여 Qt 콘솔 애플리케이션 내에서 Aspose.PDF for C++를 통합하고 사용하는 방법을 보여줍니다.

### Qt 콘솔 애플리케이션 생성

{{% alert color="primary" %}}

이 문서는 Qt 개발 환경과 Qt Creator가 올바르게 설치되어 있다고 가정합니다.

{{% /alert %}}

- Qt Creator를 열고 새로운 *Qt 콘솔 애플리케이션*을 생성합니다.

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Qt-Console-Application.jpg)

- *Build System* 드롭다운에서 QMake 옵션을 선택합니다.

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Qt-Console-Application-QMake.jpg)

- 적절한 키트를 선택하고 마법사를 완료합니다.

이 시점에서 문제 없이 컴파일해야 하는 실행 가능한 Qt 콘솔 애플리케이션이 있어야 합니다.

### Aspose.PDF for C++ API를 Qt에 통합

- 이전에 다운로드한 Aspose.PDF for C++ 아카이브를 추출합니다.
- Aspose.PDF for C++의 추출된 패키지에서 *Aspose.Pdf.Cpp* 및 *CodePorting.Native.Cs2Cpp_vc14_20.4* 폴더를 프로젝트의 루트로 복사합니다. 프로젝트는 다음 이미지와 같이 보일 것입니다.

![todo:image_alt_text](work-with-pdf-documents-in-qt_1.png)

- lib 및 include 폴더에 경로를 추가하려면 LHS 패널에서 프로젝트를 마우스 오른쪽 버튼으로 클릭하고 *Add Library*를 선택합니다.

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Add-Word-Library.jpg)

- 외부 라이브러리 옵션을 선택하고 경로를 탐색하여 포함 및 lib 폴더를 하나씩 추가합니다.

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Add-Word-Library-2.jpg)

- 완료되면, .pro 프로젝트 파일에 다음 항목이 포함됩니다:

![todo:image_alt_text](work-with-pdf-documents-in-qt_2.png)

- 애플리케이션을 빌드하면 통합이 완료됩니다.

### Qt에서 PDF 문서 생성

이제 Aspose.PDF for C++가 Qt와 통합되었으므로, 텍스트가 포함된 PDF 문서를 생성하고 디스크에 저장할 준비가 되었습니다. 이를 수행하려면:

- main.cpp에 다음 헤더를 포함합니다.

```cpp

    #include "Aspose.PDF.Cpp/Document.h"
    #include "Aspose.PDF.Cpp/Page_.h"
    #include "Aspose.PDF.Cpp/PageCollection.h"
    #include "Aspose.PDF.Cpp/Generator/Paragraphs.h"
    #include "Aspose.PDF.Cpp/Text/TextFragment.h"
```

- main 함수에 다음 코드를 삽입하여 PDF 문서를 생성하고 디스크에 저장합니다.

```cpp

    using namespace System;
    using namespace Aspose::Pdf;
    using namespace Aspose::Pdf::Text;
    
    QString text = "안녕하세요 세계";
    auto doc = MakeObject<Document>();

    auto pages = doc->get_Pages();

    pages->Add();

    auto page = pages->idx_get(1);

    auto paragraps = page->get_Paragraphs();

    paragraps->Add(MakeObject<TextFragment>(text.toStdU16String().c_str()));

    doc->Save(file_name.toStdU16String().c_str());
```