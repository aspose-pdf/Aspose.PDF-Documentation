---
title: Aspose.PDF for .NET a través de COM Interop
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /es/net/use-aspose-pdf-for-net-via-com-interop/
description: Descubre cómo usar Aspose.PDF for .NET a través de COM Interop para una integración fluida con aplicaciones que no son .NET.
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Aspose.PDF for .NET via COM Interop",
    "alternativeHeadline": "Aspose.PDF for .NET Enables COM Interop Usage",
    "abstract": "Aspose.PDF for .NET ahora soporta una integración fluida con varios lenguajes de programación a través de COM Interop, permitiendo a los desarrolladores utilizar sus poderosas capacidades de manipulación de PDF fuera del marco .NET. Esta característica mejora la flexibilidad al transformar objetos Aspose.PDF en objetos COM, simplificando las interacciones con código no administrado mientras se mantiene un alto rendimiento a través de técnicas de enlace temprano y tardío.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1338",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/use-aspose-pdf-for-net-via-com-interop/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/use-aspose-pdf-for-net-via-com-interop/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también enfrentar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

{{% alert color="primary" %}}

La información en este tema se aplica a escenarios donde deseas usar [Aspose.PDF for .NET](/pdf/net/) a través de COM Interop en cualquiera de los siguientes lenguajes de programación:

- ASP
- Delphi
- JScript
- Perl
- PHP
- PowerBuilder
- Python
- VBScript
- Visual Basic
- C++

{{% /alert %}}

## Trabajando con COM Interop

Aspose.PDF for .NET se ejecuta bajo el control del .NET Framework y esto se llama código administrado. El código escrito en todos los lenguajes mencionados anteriormente se ejecuta fuera del .NET Framework y se llama código no administrado. La interacción entre el código no administrado y Aspose.PDF ocurre a través de la instalación de .NET llamada COM Interop.

Los objetos Aspose.PDF son objetos .NET, pero cuando se utilizan a través de COM Interop, aparecen como objetos COM en tu lenguaje de programación. Por lo tanto, es mejor asegurarte de saber cómo crear y usar objetos COM en tu lenguaje de programación, antes de comenzar a usar [Aspose.PDF for .NET](/pdf/net/).

{{% alert color="primary" %}}

- En el mundo COM distinguimos entre servidor COM y cliente COM. El servidor COM almacena clases COM mientras que el cliente COM solicita instancias de clases al servidor COM, es decir, objetos COM.
- El cliente COM o simplemente la aplicación cliente puede conocer algo sobre el contenido de la clase COM o estar totalmente inconsciente de sus métodos y propiedades. Por lo tanto, la aplicación cliente puede descubrir la estructura de la clase COM al compilar/construir o solo durante la ejecución. El proceso de "descubrimiento" se conoce como enlace y así tenemos **enlace temprano** y **enlace tardío**.
- en resumen, la clase COM es como una caja negra y para trabajar con ella se necesita una biblioteca de tipos, este archivo binario tiene la descripción de los métodos, propiedades de la clase COM y cualquier lenguaje de alto nivel que soporte trabajar con objetos COM a menudo tiene una expresión de sintaxis para agregar la biblioteca de tipos, por ejemplo, esto es [**#import**](http://msdn.microsoft.com/en-us/library/8etzzkb6.aspx) en C++.
- la biblioteca de tipos se utiliza para el enlace temprano.
- un objeto COM puede exponer sus métodos y propiedades de dos maneras: por medio de una **interfaz de despacho** (dispinterface) y en su **vtable** (tabla de funciones virtuales).
- dentro de la **dispinterface**, cada método y propiedad se identifica por un miembro único; este miembro es el identificador de despacho de la función (o **DispID**).
- **vtable** es solo un conjunto de punteros a funciones que la interfaz de clase COM soporta.
- un objeto que expone sus métodos a través de ambas interfaces soporta una **interfaz dual**.
- hay ventajas en ambos tipos de enlace. El enlace temprano te proporciona un mayor rendimiento y verificación de sintaxis en tiempo de compilación. El enlace tardío es más ventajoso cuando estás escribiendo clientes que pretendes que sean ***compatibles con versiones futuras*** de tu clase COM. Con el enlace tardío, la información de la biblioteca de tipos no está "fijada" en tu cliente, por lo que puedes tener mayor confianza en que tu cliente puede trabajar con versiones futuras de la clase COM sin cambios en el código.
- el mecanismo de enlace tardío tiene una gran ventaja: si el creador del DLL COM decide lanzar una nueva versión, con un diseño de interfaz de función diferente, cualquier código que llame a esos métodos no fallará a menos que los métodos ya no estén disponibles; incluso si la **vtable** es diferente, el enlace tardío logra descubrir los nuevos DISPIDs y llamar a los métodos apropiados.
{{% /alert %}}

Aquí están los temas que eventualmente necesitarás dominar:
{{% alert color="primary" %}}

- Usar objetos COM en tu lenguaje de programación. Consulta la documentación de tu lenguaje de programación y los temas específicos del lenguaje más adelante en esta documentación.

- Trabajar con objetos COM expuestos por .NET COM Interop. Consulta [Interoperando con Código No Administrado](http://msdn.microsoft.com/en-us/library/sd10k43k.aspx) y [Exponiendo Componentes del .NET Framework a COM](http://msdn.microsoft.com/en-us/library/zsfww439%28v=vs.110%29.aspx) en MSDN.

- Modelo de objeto de documento Aspose.PDF. Consulta [Guía del Programador de Aspose.PDF](http://www.aspose.com/docs/display/pdfnet/Programmers+Guide) y [Referencia de API](http://www.aspose.com/docs/display/pdfnet/Aspose.PDF+for+.NET+API+Reference).

{{% /alert %}}

## Registrar Aspose.PDF for .NET con COM Interop

Necesitas instalar Aspose.PDF for .NET y asegurarte de que esté registrado con COM Interop (asegurando que pueda ser llamado desde código no administrado).

{{% alert color="primary" %}}

Para registrar Aspose.PDF for .NET para COM Interop manualmente:

1. Desde el menú **Inicio**, selecciona **Todos los programas**, luego **Microsoft Visual Studio**, **Herramientas de Visual Studio** y, finalmente, **Símbolo del sistema de Visual Studio**.
1. Ingresa el comando para registrar el ensamblado:
   1. .NET Framework 4.8.1
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.8.1\Aspose.PDF.dll" /codebase
   1. .NET 6.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net6.0\Aspose.PDF.dll" /codebase
   1. .NET 7.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net7.0\Aspose.PDF.dll" /codebase
   1. .NET 8.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net8.0\Aspose.PDF.dll" /codebase
   1. .NET Standard 2.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\netstandard2.0\Aspose.PDF.dll" /codebase

{{% /alert %}}

Presta atención a que /codebase es necesario solo si Aspose.PDF.dll no está en GAC, usar esta opción hace que regasm coloque la ruta del ensamblado en el registro.

{{% alert color="primary" %}}

regasm.exe es una herramienta incluida en el SDK de .NET Framework. Todas las herramientas del SDK de .NET Framework se encuentran en el directorio *\Microsoft .NET\Framevork\<FrameworkVersion>*, por ejemplo *C:\Windows\Microsoft .NET\Framework\v4.0.30319*. Si usas Visual Studio .NET:
Desde el menú **Inicio**, selecciona **Programas**, seguido de **Visual Studio 2022**, finalmente, **Símbolo del sistema para desarrolladores de VS 2022**.
Esto ejecuta un símbolo del sistema con todas las variables de entorno necesarias configuradas.

{{% /alert %}}

### ProgIDs

ProgID significa “identificador programático”. Es el nombre de una clase COM que se utiliza para crear un objeto. Los ProgIDs consisten en el nombre de la biblioteca "Aspose.PDF" y el nombre de la clase.

### Biblioteca de Tipos

{{% alert color="primary" %}}

Si tu lenguaje de programación (por ejemplo, Visual Basic o Delphi) te permite hacer referencia a una biblioteca de tipos COM, entonces agrega una referencia a Aspose.PDF.tlb y para ver todas las clases, métodos, propiedades y enumeraciones de Aspose.PDF for .NET en tu Explorador de Objetos.

Para generar un archivo TLB:

- .NET Framework 4.8.1
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.8.1\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.8.1\Aspose.PDF.tlb" /codebase
- .NET 6.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net6.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net6.0\Aspose.PDF.tlb" /codebase
- .NET 7.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net7.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net7.0\Aspose.PDF.tlb" /codebase
- .NET 8.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net8.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net8.0\Aspose.PDF.tlb" /codebase
- .NET Standard 2.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\netstandard2.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\netstandard2.0\Aspose.PDF.tlb" /codebase

{{% /alert %}}

## Creando Objetos COM

La creación de un objeto COM es similar a la creación de un objeto .NET normal:

```vb
'Instantiate Pdf instance by calling its empty constructor
Dim document
Set document = CreateObject("Aspose.Pdf.Document")

```

Una vez creado, puedes acceder a los métodos y propiedades del objeto, como si fuera un objeto COM:

```vb
'Add page to the document
document.Pages.Add()
```

Algunos métodos tienen sobrecargas y serán expuestos por COM Interop con un sufijo numérico añadido a ellos, excepto por el primer método que permanece sin cambios. Por ejemplo, las sobrecargas del método Document.Save se convierten en Document.Save, Document.Save_2, y así sucesivamente.

Para más información, consulta los artículos específicos del lenguaje más adelante en esta documentación.

## Creando un Ensamblado Wrapper

Si necesitas usar muchas de las clases, métodos y propiedades de Aspose.PDF for .NET, considera crear un ensamblado wrapper (usando C# o cualquier otro lenguaje de programación .NET). Los ensamblados wrapper ayudan a evitar usar Aspose.PDF for .NET directamente desde código no administrado.

Un buen enfoque es desarrollar un ensamblado .NET que haga referencia a Aspose.PDF for .NET y realice todo el trabajo con él, y solo exponga un conjunto mínimo de clases y métodos a código no administrado. Tu aplicación debería trabajar solo con tu biblioteca wrapper.

Reducir el número de clases y métodos que necesitas invocar a través de COM Interop simplifica el proyecto. Usar clases .NET a través de COM Interop a menudo requiere habilidades avanzadas.