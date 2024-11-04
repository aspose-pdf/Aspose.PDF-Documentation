---
title: CPP에서 래퍼 사용하기
type: docs
weight: 30
url: /net/using-wrapper-in-cpp/
---

## 사전 요구 사항

{{% alert color="primary" %}}

Aspose.PDF for .NET을 COM Interop와 함께 등록하십시오. [Use Aspose.pdf for .NET via COM Interop](/pdf/net/use-aspose-pdf-for-net-via-com-interop/)라는 문서를 확인하세요.

{{% /alert %}}

## 구현

{{% alert color="primary" %}}

PDF 문서에서 텍스트를 검색하기 위해 [래퍼](https://docs.aspose.com/pdf/net/creating-a-wrapper-assembly/)를 사용할 것입니다.

{{% /alert %}}

```cpp

#include "stdafx.h"
#import "C:\\Temp\\PdfText.tlb"
using namespace System;

String^ wrapper(String^ file)
{
    String^ text;
    // ComHelper 생성

    PdfText::IPetrieverPtr retrieverPtr;
    HRESULT hr = retrieverPtr.CreateInstance(__uuidof(PdfText::Petriever));

    if (FAILED(hr))
    {
        Console::WriteLine(L"오류 발생");
    }
    else
    {
        // 라이선스 설정
        retrieverPtr->SetLicense("C:\\Temp\\Aspose.PDF.lic");
        // 텍스트 검색

        BSTR extractedText = retrieverPtr->GetText((BSTR)System::Runtime::InteropServices::Marshal::StringToBSTR(file).ToPointer());
        text = gcnew String(extractedText);
        retrieverPtr.Release();
    }
    return text;
}

int main(array<System::String ^> ^args)
{
    CoInitialize(NULL);
    if (args->Length != 1)
    {
        Console::WriteLine("매개변수가 누락되었습니다\n사용법: testCOM <pdf 파일>");
        return 0;
    }

    String ^text = wrapper(args[0]);
    CoUninitialize();
    Console::WriteLine("추출된 텍스트:");
    Console::WriteLine("---\n{0}", text != nullptr ? text->Trim() : "<empty>");
    Console::WriteLine("---");
    return 0;
}

```

