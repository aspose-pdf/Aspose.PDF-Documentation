---
title: Uso del enlace temprano en CPP
type: docs
weight: 10
url: /es/net/using-early-binding-in-cpp/
---

## Prerrequisitos

{{% alert color="primary" %}}

Por favor, registre Aspose.PDF para .NET con COM Interop, consulte el artículo titulado [Usar Aspose.pdf para .NET vía COM Interop](/pdf/es/net/use-aspose-pdf-for-net-via-com-interop/).

{{% /alert %}}

## Ejemplo

{{% alert color="primary" %}}

Este es un ejemplo simple de código C++ para extraer texto de archivos PDF usando COM Interop mediante enlace temprano. Antes de ejecutar el ejemplo preste atención a que

- **#import** *typelib.tlb* hace que el compilador de C++ genere 2 archivos: *typelib.tlh* y *typelib.tli*. Por defecto, estos archivos se generan solo una vez, por lo que necesita recompilar completamente el proyecto para obtener nuevas versiones de ellos.
- a menudo importar solo un archivo TLB conduce a una gran cantidad de errores de compilador.

{{% /alert %}}
- A menudo, importar solo un archivo TLB conduce a un gran número de errores de compilación.

```cpp
// Bibliotecas de tipos cruzadas:
```
{{% alert color="primary" %}}

y tiene uno o más **#import**. Simplemente cópielos en su código antes de importar la biblioteca de tipos principal y hágalo en el ***mismo*** orden. Así evitarás el primer tipo de problema. El siguiente tipo de problema proviene del hecho de que el entorno C++ tiene un gran número de macros, funciones predefinidas, etc., que pueden entrar en conflicto con los métodos de la biblioteca de tipos. Por ejemplo, GetType ya ha sido ampliamente utilizado en C++, pero también lo tiene Aspose.PDF. Descubrí que los atributos **rename** y **auto_rename** de la directiva **#import** son muy convenientes para evitar posibles advertencias y errores.

- a veces las clases en los espacios de nombres **uses** entran en conflicto con los nombres en la biblioteca de tipos, por lo que en tales casos se debe usar el nombre completo de la clase en lugar de **using namespace**. Por ejemplo, vea cómo se llama a StringToBSTR en el fragmento de código a continuación.
{{% /alert %}}

Para más detalles, por favor mire [este](http://www.drdobbs.com/writing-com-clients-with-late-and-early/184403558) artículo.
Para obtener más detalles, consulte [este](http://www.drdobbs.com/writing-com-clients-with-late-and-early/184403558) artículo.

Ejemplo en C++

```cpp
#include "stdafx.h"
#import "C:\Windows\Microsoft.NET\Framework\v2.0.50727\System.Drawing.tlb"
#import "C:\Windows\Microsoft.NET\Framework\v4.0.30319\mscorlib.tlb" auto_rename

#import "C:\Temp\Aspose.PDF.tlb" rename("GetType", "GetType_") auto_rename

using namespace System;
String ^earlyBinding(String ^file)
{
    String ^text;
    // crear ComHelper

    Aspose_Pdf::_ComHelperPtr comHelperPtr;
    HRESULT hr = comHelperPtr.CreateInstance(__uuidof(Aspose_Pdf::ComHelper));
    if (FAILED(hr))
    {
        Console::WriteLine(L"Se produjo un error");
    }
    else
    {
        // establecer licencia
        Aspose_Pdf::_LicensePtr licPtr;
        licPtr.CreateInstance(__uuidof(Aspose_Pdf::License));
        licPtr->SetLicense("C:\\Temp\\Aspose.PDF.lic");
        licPtr.Release();

        // obtener Documento
        Aspose_Pdf::_DocumentPtr docPtr;
        docPtr = comHelperPtr->OpenFile((BSTR)System::Runtime::InteropServices::Marshal::StringToBSTR(file).ToPointer());

        comHelperPtr.Release();

        // crear Absorber
        Aspose_Pdf::_TextAbsorberPtr absorberPtr;
        HRESULT hRes = absorberPtr.CreateInstance(__uuidof(Aspose_Pdf::TextAbsorber));

        // recorrer texto
        docPtr->GetPages()->Accept_4(absorberPtr);

        // recuperar texto
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
        Console::WriteLine("Faltan parámetros\nUso: testCOM <archivo pdf>");
        return 0;
    }

    String ^text = earlyBinding(args[0]);
    CoUninitialize();
    Console::WriteLine("Texto extraído:");
    Console::WriteLine("---\n{0}", text != nullptr ? text->Trim() : "<vacío>");
    Console::WriteLine("---");
    return 0;
}
```

