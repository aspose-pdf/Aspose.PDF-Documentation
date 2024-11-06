---
title: Usando el enlace tardío en CPP
type: docs
weight: 20
url: es/net/using-late-binding-in-cpp/
---

## Prerrequisitos

{{% alert color="primary" %}}

Por favor, registre Aspose.PDF para .NET con COM Interop, revise el artículo titulado [Usar Aspose.pdf para .NET a través de COM Interop](/pdf/net/use-aspose-pdf-for-net-via-com-interop/).

{{% /alert %}}

## Ejemplo

{{% alert color="primary" %}}

Este es un ejemplo simple de código C++ para extraer texto de PDF mediante COM Interop usando enlace tardío. Para más detalles, por favor mire [este](http://www.drdobbs.com/writing-com-clients-with-late-and-early/184403558) post.

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

    // crear ComHelper
    IDispatch* comHelperPtr;

    wcscpy_s(str, L"Aspose.PDF.ComHelper");
    CLSIDFromProgID(str, &pclsid);

    HRESULT hr = CoCreateInstance(pclsid, NULL, CLSCTX_ALL, IID_IDispatch, (void **)&comHelperPtr);
    if (FAILED(hr))
    {
        Console::WriteLine(L"Error ocurrido");
    }
    else
    {
        // establecer licencia
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

        // obtener Documento

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

        // obtener Páginas del Documento

        OLECHAR* pages =  L"Pages";

        hr = docPtr->GetIDsOfNames(IID_NULL, &pages, 1, GetUserDefaultLCID(), &dispid);

        dp.cArgs = 0;

        hr = docPtr->Invoke(dispid, IID_NULL, GetUserDefaultLCID(), DISPATCH_PROPERTYGET, &dp, &result, NULL, NULL);

        IDispatch* pagesPtr = result.pdispVal;

        //------------------------

        // crear Absorber

        IDispatch* absorberPtr;

        wcscpy_s(str, L"Aspose.PDF.Text.TextAbsorber");

        CLSIDFromProgID(str, &pclsid);

        hr = CoCreateInstance(pclsid, NULL, CLSCTX_ALL, IID_IDispatch, (void **)&absorberPtr);

        //------------------------

        // examinar texto

        arg.vt = VT_DISPATCH;

        arg.pdispVal = absorberPtr;

        vargs[0] = arg;

        dp.rgvarg = vargs;

        dp.cArgs = 1;

        OLECHAR* accept_4 = L"Accept_4";

        hr = pagesPtr->GetIDsOfNames(IID_NULL, &accept_4, 1, GetUserDefaultLCID(), &dispid);

        hr = pagesPtr->Invoke(dispid, IID_NULL, GetUserDefaultLCID(), DISPATCH_METHOD, &dp, &result, NULL, NULL);

        //------------------------

        // recuperar texto

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
        Console::WriteLine("Faltan parámetros\nUso:testCOM <archivo pdf>");
        return 0;
    }

    CoInitialize(NULL);
    String ^text = lateBinding(args[0]);
    CoUninitialize();
    Console::WriteLine("Texto extraído:");
    Console::WriteLine("---\n{0}", text != nullptr ? text->Trim() : "<vacío>");
    Console::WriteLine("---");
    return 0;

}

```

