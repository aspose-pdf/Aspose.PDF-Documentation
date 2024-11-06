---
title: CPP에서 초기 바인딩 사용하기
type: docs
weight: 10
url: ko/net/using-early-binding-in-cpp/
---

## 사전 요구 사항

{{% alert color="primary" %}}

Aspose.PDF for .NET을 COM Interop를 통해 등록하십시오. [Use Aspose.pdf for .NET via COM Interop](/pdf/net/use-aspose-pdf-for-net-via-com-interop/)라는 기사를 확인하세요.

{{% /alert %}}

## 예제

{{% alert color="primary" %}}

이것은 COM Interop를 사용하여 PDF 파일에서 텍스트를 추출하는 간단한 C++ 코드 예제입니다. 샘플을 실행하기 전에 주의하세요.

- **#import** *typelib.tlb*는 C++ 컴파일러가 *typelib.tlh*와 *typelib.tli* 두 파일을 생성하게 합니다. 기본적으로 이 파일들은 한 번만 생성되므로, 새로운 버전을 얻기 위해서는 프로젝트를 완전히 다시 컴파일해야 합니다.
- 종종 하나의 TLB 파일만 가져오면 많은 수의 컴파일러 오류가 발생합니다.
- 종종 하나의 TLB 파일만 가져오면 컴파일러 오류가 많이 발생합니다.

```cpp
// 교차 참조된 타입 라이브러리:
```

하나 이상의 **#import**가 있습니다. 주 타입 라이브러리를 가져오기 전에 코드에 복사하고 ***동일한*** 순서로 수행하십시오. 그러면 첫 번째 유형의 문제를 해결할 수 있습니다. 다음 유형의 문제는 C++ 환경에 매크로, 미리 정의된 함수 등이 많이 있어 타입 라이브러리 메소드와 충돌할 수 있다는 사실에서 비롯됩니다. 예를 들어, GetType은 C++에서 이미 널리 사용되고 있지만 Aspose.PDF도 그렇습니다. **#import** 지시문의 **rename** 및 **auto_rename** 속성은 경고 및 오류를 방지하는 데 매우 편리합니다.

- 때로는 **uses** 네임스페이스의 클래스가 타입 라이브러리의 이름과 충돌하여 이러한 경우 **using namespace** 대신 전체 클래스 이름을 사용해야 합니다. 아래 코드 스니펫에서 StringToBSTR이 호출되는 방식을 참조하십시오.
{{% /alert %}}

자세한 내용은 [이](http://www.drdobbs.com/writing-com-clients-with-late-and-early/184403558) 게시물을 참조하십시오.
자세한 내용은 [이](http://www.drdobbs.com/writing-com-clients-with-late-and-early/184403558) 포스트를 참조하세요.

C++ 예제

```cpp
#include "stdafx.h"
#import "C:\Windows\Microsoft.NET\Framework\v2.0.50727\System.Drawing.tlb"
#import "C:\Windows\Microsoft.NET\Framework\v4.0.30319\mscorlib.tlb" auto_rename

#import "C:\Temp\Aspose.PDF.tlb" rename("GetType", "GetType_") auto_rename

using namespace System;
String ^earlyBinding(String ^file)
{
    String ^text;
    // ComHelper 생성

    Aspose_Pdf::_ComHelperPtr comHelperPtr;
    HRESULT hr = comHelperPtr.CreateInstance(__uuidof(Aspose_Pdf::ComHelper));
    if (FAILED(hr))
    {
        Console::WriteLine(L"오류 발생");
    }
    else
    {
        // 라이센스 설정
        Aspose_Pdf::_LicensePtr licPtr;
        licPtr.CreateInstance(__uuidof(Aspose_Pdf::License));
        licPtr->SetLicense("C:\\Temp\\Aspose.PDF.lic");
        licPtr.Release();

        // 문서 가져오기
        Aspose_Pdf::_DocumentPtr docPtr;
        docPtr = comHelperPtr->OpenFile((BSTR)System::Runtime::InteropServices::Marshal::StringToBSTR(file).ToPointer());

        comHelperPtr.Release();

        // Absorber 생성
        Aspose_Pdf::_TextAbsorberPtr absorberPtr;
        HRESULT hRes = absorberPtr.CreateInstance(__uuidof(Aspose_Pdf::TextAbsorber));

        // 텍스트 탐색
        docPtr->GetPages()->Accept_4(absorberPtr);

        // 텍스트 검색
        BSTR extractedText = absorberPtr->GetText();
        text = gcnew String(extractedText);
        docPtr.Release();
        absorberPtr.Release();
    }
    return text;
}

int main(array<System::String ^> ^args)
{
    CoInitialize(NULL);
    if (args->Length != 1)
    {
        Console::WriteLine("파라미터 누락\n사용법:testCOM <pdf 파일>");
        return 0;
    }

    String ^text = earlyBinding(args[0]);
    CoUninitialize();
    Console::WriteLine("추출된 텍스트:");
    Console::WriteLine("---\n{0}", text != nullptr ? text->Trim() : "<empty>");
    Console::WriteLine("---");
    return 0;
}
```

