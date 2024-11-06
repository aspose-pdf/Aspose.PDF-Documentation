---
title: Criando uma Assembly de Wrapper
type: docs
weight: 80
url: pt/net/creating-a-wrapper-assembly/
---

{{% alert color="primary" %}}

Se você precisa usar muitas classes, métodos e propriedades do Aspose.PDF para .NET, considere criar uma assembly de wrapper (usando C# ou qualquer outra linguagem de programação .NET). Assemblies de wrapper ajudam a evitar o uso direto do Aspose.PDF para .NET a partir de código não gerenciado.

Uma boa abordagem é desenvolver uma assembly .NET que referencia o Aspose.PDF para .NET e realiza todo o trabalho com ele, expondo apenas um conjunto mínimo de classes e métodos para o código não gerenciado. Sua aplicação então deve trabalhar apenas com sua biblioteca de wrapper.

Reduzir o número de classes e métodos que você precisa invocar via COM Interop simplifica o projeto. Usar classes .NET via COM Interop frequentemente requer habilidades avançadas.

{{% /alert %}}

## Wrapper do Aspose.PDF para .NET

```csharp

using System;
using System.Runtime.InteropServices;
namespace PdfText
{
    [Guid("FC969AC9-6591-46FB-A4AB-DB12A776F3BF")]
    [InterfaceType(ComInterfaceType.InterfaceIsIDispatch)]
    public interface IPetriever
    {
        [DispId(1)]
        void SetLicense(string file);

        [DispId(2)]
        string GetText(string file);
    }

    [Guid("3D59100F-3CC5-463D-B509-58FA0520B436")]
    [ClassInterface(ClassInterfaceType.None)]

    [ComSourceInterfaces(typeof(IPetriever))]

    public class Petriever : IPetriever
    {
        public void SetLicense(string file)
        {
            License lic = new License();
            lic.SetLicense(file);
        }

        public string GetText(string file)
        {
            // abrir documento
            Document doc = new Document(file);

            // criar objeto TextAbsorber para extrair texto
            TextAbsorber absorber = new TextAbsorber();

            // aceitar o absorvedor para todas as páginas do documento
            doc.Pages.Accept(absorber);

            // obter o texto extraído

            string text = absorber.Text;
            return text;

        }
    }
}

```

