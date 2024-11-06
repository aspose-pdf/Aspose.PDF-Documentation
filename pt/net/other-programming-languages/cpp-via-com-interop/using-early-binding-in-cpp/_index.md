---
title: Usando vinculação antecipada em CPP
type: docs
weight: 10
url: pt/net/using-early-binding-in-cpp/
---

## Pré-requisitos

{{% alert color="primary" %}}

Por favor, registre o Aspose.PDF para .NET com COM Interop, verifique o artigo chamado [Use Aspose.pdf para .NET via COM Interop](/pdf/net/use-aspose-pdf-for-net-via-com-interop/).

{{% /alert %}}

## Exemplo

{{% alert color="primary" %}}

Este é um simples exemplo de código C++ para extrair texto de arquivos PDF usando COM Interop com vinculação antecipada. Antes de executar o exemplo, preste atenção que

- **#import** *typelib.tlb* faz o compilador C++ gerar 2 arquivos: *typelib.tlh* e *typelib.tli*. Por padrão, esses arquivos são gerados apenas uma vez, então você precisa recompilar completamente o projeto para obter novas versões deles.
- frequentemente, importar apenas um arquivo TLB leva a um grande número de erros de compilador.
- muitas vezes, importar apenas um arquivo TLB resulta em um grande número de erros de compilação.

```cpp
// Bibliotecas de tipos cruzadas:
```

e tem um ou mais **#import**. Apenas copie-os para o seu código antes de importar a biblioteca de tipos principal e faça isso na ***mesma*** ordem. Assim, você combaterá o primeiro tipo de problema. O próximo tipo de problema vem do fato de que o ambiente C++ possui um grande número de macros, funções predefinidas, etc., que podem entrar em conflito com os métodos da biblioteca de tipos. Por exemplo, GetType já foi amplamente utilizado em C++, mas também o Aspose.PDF o possui. Eu descobri que os atributos **rename** e **auto_rename** da diretiva **#import** são muito convenientes para evitar possíveis avisos e erros.

- às vezes classes em namespaces **uses** entram em conflito com nomes na biblioteca de tipos, então nesses casos, o nome completo da classe deve ser usado em vez de **using namespace**. Por exemplo, veja como o StringToBSTR é chamado no trecho de código abaixo.
{{% /alert %}}

Para mais detalhes, por favor, veja [este](http://www.drdobbs.com/writing-com-clients-with-late-and-early/184403558) post.
Para mais detalhes, por favor, veja [este](http://www.drdobbs.com/writing-com-clients-with-late-and-early/184403558) post.

Exemplo em C++

```cpp
#include "stdafx.h"
#import "C:\Windows\Microsoft.NET\Framework\v2.0.50727\System.Drawing.tlb"
#import "C:\Windows\Microsoft.NET\Framework\v4.0.30319\mscorlib.tlb" auto_rename

#import "C:\Temp\Aspose.PDF.tlb" rename("GetType", "GetType_") auto_rename

using namespace System;
String ^earlyBinding(String ^file)
{
    String ^text;
    // criar ComHelper

    Aspose_Pdf::_ComHelperPtr comHelperPtr;
    HRESULT hr = comHelperPtr.CreateInstance(__uuidof(Aspose_Pdf::ComHelper));
    if (FAILED(hr))
    {
        Console::WriteLine(L"Erro ocorrido");
    }
    else
    {
        // definir licença
        Aspose_Pdf::_LicensePtr licPtr;
        licPtr.CreateInstance(__uuidof(Aspose_Pdf::License));
        licPtr->SetLicense("C:\\Temp\\Aspose.PDF.lic");
        licPtr.Release();

        // obter Documento
        Aspose_Pdf::_DocumentPtr docPtr;
        docPtr = comHelperPtr->OpenFile((BSTR)System::Runtime::InteropServices::Marshal::StringToBSTR(file).ToPointer());

        comHelperPtr.Release();

        // criar Absorvedor
        Aspose_Pdf::_TextAbsorberPtr absorberPtr;
        HRESULT hRes = absorberPtr.CreateInstance(__uuidof(Aspose_Pdf::TextAbsorber));

        // navegar pelo texto
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
        Console::WriteLine("Parâmetros ausentes\nUso:testCOM <arquivo pdf>");
        return 0;
    }

    String ^text = earlyBinding(args[0]);
    CoUninitialize();
    Console::WriteLine("Texto extraído:");
    Console::WriteLine("---\n{0}", text != nullptr ? text->Trim() : "<vazio>");
    Console::WriteLine("---");
    return 0;
}
```

