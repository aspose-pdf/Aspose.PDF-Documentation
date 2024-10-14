---
title: Creando un Ensamblado Contenedor
type: docs
weight: 80
url: /net/creating-a-wrapper-assembly/
---

{{% alert color="primary" %}}

Si necesita utilizar muchas clases, métodos y propiedades de Aspose.PDF para .NET, considere crear un ensamblado contenedor (usando C# u otro lenguaje de programación .NET). Los ensamblados contenedores ayudan a evitar el uso directo de Aspose.PDF para .NET desde código no administrado.

Un buen enfoque es desarrollar un ensamblado .NET que haga referencia a Aspose.PDF para .NET y realice todo el trabajo con él, y solo exponga un conjunto mínimo de clases y métodos al código no administrado. Su aplicación entonces debería trabajar solo con su biblioteca contenedora.

Reducir el número de clases y métodos que necesita invocar a través de COM Interop simplifica el proyecto. Usar clases .NET a través de COM Interop a menudo requiere habilidades avanzadas.

{{% /alert %}}

## Envoltorio Aspose.PDF para .NET

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

            // crear objeto TextAbsorber para extraer texto
            TextAbsorber absorber = new TextAbsorber();

            // aceptar el absorber para todas las páginas del documento
            doc.Pages.Accept(absorber);

            // obtener el texto extraído
            string text = absorber.Text;
            return text;

        }
    }
}

```

