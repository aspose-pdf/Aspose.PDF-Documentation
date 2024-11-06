---
title: CPP에서 늦은 바인딩 사용하기
type: docs
weight: 20
url: ko/net/using-late-binding-in-cpp/
---

## Prerequisites

{{% alert color="primary" %}}

Aspose.PDF for .NET을 COM Interop로 등록하십시오. [Use Aspose.pdf for .NET via COM Interop](/pdf/net/use-aspose-pdf-for-net-via-com-interop/) 문서를 확인해 주세요.

{{% /alert %}}

## Sample

{{% alert color="primary" %}}

이것은 COM Interop를 사용하여 PDF에서 텍스트를 추출하기 위한 간단한 C++ 코드 샘플입니다. 자세한 내용은 [this](http://www.drdobbs.com/writing-com-clients-with-late-and-early/184403558) 포스트를 참조해 주세요.

{{% /alert %}}

```cpp

#include "stdafx.h"
#include "comdef.h"

using namespace System;

String ^lateBinding(String ^file)
{
    String^ text;
    DISPID dispid;
    DISPPARAMS dp = { NULL, NULL, 0, 0};
    VARIANTARG vargs[1];
    VARIANT arg, result;
    WCHAR str[255];
    CLSID pclsid;

    // ComHelper 생성
    IDispatch* comHelperPtr;

    wcscpy_s(str, L"Aspose.PDF.ComHelper");
    CLSIDFromProgID(str, &pclsid);

    HRESULT hr = CoCreateInstance(pclsid, NULL, CLSCTX_ALL, IID_IDispatch, (void **)&comHelperPtr);
    if (FAILED(hr))
    {
        Console::WriteLine(L"오류 발생");
    }
    else
    {
        // 라이선스 설정
        IDispatch* licPtr;
        wcscpy_s(str, L"Aspose.PDF.License");
        CLSIDFromProgID(str, &pclsid);

        HRESULT hr = CoCreateInstance(pclsid, NULL, CLSCTX_ALL, IID_IDispatch, (void **)&licPtr);

        OLECHAR* setLicense =  L"SetLicense";

        hr = licPtr->GetIDsOfNames(IID_NULL, &setLicense, 1, GetUserDefaultLCID(), &dispid);
        arg.vt = VT_BSTR;

        BSTR lic = SysAllocString(L"C:\\Temp\\Aspose.PDF.lic");

        arg.bstrVal = lic;

        vargs[0] = arg;

        dp.rgvarg = vargs;

        dp.cArgs = 1;

        hr = licPtr->Invoke(dispid, IID_NULL, GetUserDefaultLCID(), DISPATCH_METHOD, &dp, &result, NULL, NULL);

        SysFreeString(lic);

        licPtr.Release();

        // 문서 가져오기

        OLECHAR* openFile =  L"OpenFile";

        hr = comHelperPtr->GetIDsOfNames(IID_NULL, &openFile, 1, GetUserDefaultLCID(), &dispid);

        arg.vt = VT_BSTR;

        arg.bstrVal = (BSTR)System::Runtime::InteropServices::Marshal::StringToBSTR(file).ToPointer();

        vargs[0] = arg;

        dp.rgvarg = vargs;

        dp.cArgs = 1;

        hr = comHelperPtr->Invoke(dispid, IID_NULL, GetUserDefaultLCID(), DISPATCH_METHOD, &dp, &result, NULL, NULL);

        IDispatch* docPtr = result.pdispVal;

        comHelperPtr.Release();

        //------------------------

        // 문서의 페이지 가져오기

        OLECHAR* pages =  L"Pages";

        hr = docPtr->GetIDsOfNames(IID_NULL, &pages, 1, GetUserDefaultLCID(), &dispid);

        dp.cArgs = 0;

        hr = docPtr->Invoke(dispid, IID_NULL, GetUserDefaultLCID(), DISPATCH_PROPERTYGET, &dp, &result, NULL, NULL);

        IDispatch* pagesPtr = result.pdispVal;

        //------------------------

        // Absorber 생성

        IDispatch* absorberPtr;

        wcscpy_s(str, L"Aspose.PDF.Text.TextAbsorber");

        CLSIDFromProgID(str, &pclsid);

        hr = CoCreateInstance(pclsid, NULL, CLSCTX_ALL, IID_IDispatch, (void **)&absorberPtr);

        //------------------------

        // 텍스트 탐색

        arg.vt = VT_DISPATCH;

        arg.pdispVal = absorberPtr;

        vargs[0] = arg;

        dp.rgvarg = vargs;

        dp.cArgs = 1;

        OLECHAR* accept_4 = L"Accept_4";

        hr = pagesPtr->GetIDsOfNames(IID_NULL, &accept_4, 1, GetUserDefaultLCID(), &dispid);

        hr = pagesPtr->Invoke(dispid, IID_NULL, GetUserDefaultLCID(), DISPATCH_METHOD, &dp, &result, NULL, NULL);

        //------------------------

        // 텍스트 검색

        OLECHAR* _text = L"Text";

        dp.cArgs = 0;

        hr = absorberPtr->GetIDsOfNames(IID_NULL, &_text, 1, GetUserDefaultLCID(), &dispid);

        hr = absorberPtr->Invoke(dispid, IID_NULL, GetUserDefaultLCID(), DISPATCH_PROPERTYGET, &dp, &result, 0, 0);

        //------------------------

        text = gcnew String(result.bstrVal);

        docPtr.Release();

        pagesPtr.Release();

        absorberPtr.Release();

    }

    return text;

}

int main(array<System::String ^> ^args)
{
    if (args->Length != 1)
    {
        Console::WriteLine("매개 변수 누락\n사용법: testCOM <pdf 파일>");
        return 0;
    }

    CoInitialize(NULL);
    String ^text = lateBinding(args[0]);
    CoUninitialize();
    Console::WriteLine("추출된 텍스트:");
    Console::WriteLine("---\n{0}", text != nullptr ? text->Trim() : "<empty>");
    Console::WriteLine("---");
    return 0;

}

```

