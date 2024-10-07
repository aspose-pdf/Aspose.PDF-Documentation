---
title: Aspose.PDF para .NET a través de COM Interop
type: docs
weight: 20
url: /net/use-aspose-pdf-for-net-via-com-interop/
---

{{% alert color="primary" %}}

La información en este tema se aplica a escenarios donde deseas usar [Aspose.PDF para .NET](/pdf/net/) a través de COM Interop en cualquiera de los siguientes lenguajes de programación:

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

Aspose.PDF para .NET se ejecuta bajo el control del Framework de .NET y esto se denomina código administrado. El código escrito en todos los lenguajes mencionados anteriormente se ejecuta fuera del Framework de .NET y se le llama código no administrado. La interacción entre el código no administrado y Aspose.PDF ocurre a través de una facilidad de .NET llamada COM Interop.

Los objetos de Aspose.PDF son objetos .NET, pero cuando se usan a través de COM Interop, aparecen como objetos COM en tu lenguaje de programación.
Los objetos Aspose.PDF son objetos .NET, pero cuando se utilizan a través de COM Interop, aparecen como objetos COM en su lenguaje de programación.

{{% alert color="primary" %}}

- En el mundo COM distinguimos entre servidor COM y cliente COM. El servidor COM almacena las clases COM mientras que el cliente COM solicita al servidor COM instancias de clases, es decir, objetos COM.
- El cliente COM o simplemente la aplicación cliente puede saber algo sobre el contenido de la clase COM o no tener ningún conocimiento sobre sus métodos y propiedades. Por lo tanto, la aplicación cliente puede descubrir la estructura de la clase COM al compilar/construir o solo durante la ejecución. El proceso de "descubrimiento" se conoce como vinculación, por lo que tenemos **vinculación temprana** y **vinculación tardía**.
- En resumen, la clase COM es como una caja negra y para trabajar con ella se necesita una biblioteca de tipos, este archivo binario tiene una descripción de los métodos, propiedades de la clase COM y cualquier lenguaje de alto nivel que admita trabajar con objetos COM a menudo tiene una expresión sintáctica para agregar la biblioteca de tipos, por ejemplo, esto es [**#import**](http://msdn.microsoft.com/en-us/library/8etzzkb6.aspx) en C++.
- En resumen, la clase COM es como una caja negra y para trabajar con ella se necesita una biblioteca de tipos, este archivo binario tiene la descripción de los métodos y propiedades de la clase COM, y cualquier lenguaje de alto nivel que soporte trabajar con objetos COM a menudo tiene una expresión sintáctica para agregar la biblioteca de tipos, por ejemplo, este es [**#import**](http://msdn.microsoft.com/en-us/library/8etzzkb6.aspx) en C++.
- La biblioteca de tipos se utiliza para la vinculación temprana.
- Un objeto COM puede exponer sus métodos y propiedades de dos maneras: mediante una **interfaz de despacho** (dispinterface) y en su **tabla virtual de funciones** (vtable).
- Dentro de la **dispinterface**, cada método y propiedad se identifica por un miembro único; este miembro es el identificador de despacho de la función (o **DispID**).
- **vtable** es solo un conjunto de punteros a funciones que la interfaz de clase COM soporta.
- Un objeto que expone sus métodos a través de ambas interfaces soporta una **interfaz dual**.
- Hay ventajas en ambos tipos de vinculación.
- existen ventajas en ambos tipos de vinculación.
- el mecanismo de vinculación tardía tiene una gran ventaja: si el creador del DLL COM decide lanzar una nueva versión, con un diseño de interfaz de función diferente, cualquier código que llame a esos métodos no se bloqueará a menos que los métodos ya no estén disponibles; incluso si el **vtable** es diferente, la vinculación tardía logra descubrir los nuevos DISPIDs y llamar a los métodos apropiados.
{{% /alert %}}

Aquí están los temas que eventualmente necesitarás dominar:
{{% alert color="primary" %}}

- Uso de objetos COM en tu lenguaje de programación. Consulta la documentación de tu lenguaje de programación y los temas específicos del lenguaje más adelante en esta documentación.

- Trabajo con objetos COM expuestos por .NET COM Interop. Consulta [Interoperando con código no administrado](http://msdn.microsoft.com/en-us/library/sd10k43k.aspx) y [Exponiendo componentes del .NET Framework a COM](http://msdn.microsoft.com/en-us/library/zsfww439%28v=vs.110%29.aspx) en MSDN.

- Modelo de objeto de documento Aspose.PDF.
- Modelo de objeto de documento Aspose.PDF.

{{% /alert %}}

## Registrar Aspose.PDF para .NET con COM Interop

Necesitas instalar Aspose.PDF para .NET y asegurarte de que está registrado con COM Interop (asegurando que se pueda llamar desde código no administrado).

{{% alert color="primary" %}}

Para registrar manualmente Aspose.PDF para .NET para COM Interop:

1. Desde el menú **Inicio**, selecciona **Todos los Programas**, luego **Microsoft Visual Studio**, **Herramientas de Visual Studio** y, finalmente, **Símbolo del sistema de Visual Studio**.
1. Ingresa el comando para registrar el ensamblado:
   1. .NET Framework 2.0
      regasm "C:\Program Files\Aspose\Aspose.PDF para .NET\bin\net2.0\Aspose.PDF.dll" /codebase
   1. .NET Framework 3.5
      regasm "C:\Program Files\Aspose\Aspose.PDF para .NET\bin\net3.5\Aspose.PDF.dll" /codebase
   1. .NET Framework 4.0
      regasm "C:\Program Files\Aspose\Aspose.PDF para .NET\bin\net4.0\Aspose.PDF.dll" /codebase

{{% /alert %}}

Presta atención que /codebase es necesario solo si Aspose.PDF.dll no está en GAC, usando esta opción hace que regasm ponga la ruta para el ensamblado en el registro.
{{% alert color="primary" %}}

regasm.exe es una herramienta incluida en el SDK de .NET Framework. Todas las herramientas del SDK de .NET Framework se encuentran en el directorio *\Microsoft .NET\Framework\<VersiónDelFramework>*, por ejemplo, *C:\Windows\Microsoft .NET\Framework\v4.0.30319*. Si usas Visual Studio .NET:
Desde el menú **Inicio**, selecciona **Programas**, seguido por **Microsoft Visual Studio .NET**, luego **Herramientas de Visual Studio .NET** y, finalmente, **Símbolo del sistema de Visual Studio .NET 2003**.
Ejecuta un símbolo del sistema con todas las variables de entorno necesarias configuradas.

{{% /alert %}}

### ProgIDs

ProgID significa "identificador programático". Es el nombre de una clase COM que se utilizó para crear un objeto. Los ProgIDs consisten en el nombre de la biblioteca "Aspose.PDF" y el nombre de la clase.

### Biblioteca de Tipos

{{% alert color="primary" %}}

Si tu lenguaje de programación (por ejemplo, Visual Basic o Delphi) te permite referenciar una biblioteca de tipos COM, entonces agrega una referencia a Aspose.PDF.tlb y para ver todas las clases, métodos, propiedades y enumeraciones de Aspose.PDF para .NET en tu Explorador de Objetos.
Si tu lenguaje de programación (por ejemplo, Visual Basic o Delphi) te permite hacer referencia a una biblioteca de tipos COM, entonces agrega una referencia a Aspose.PDF.tlb para ver todas las clases, métodos, propiedades y enumeraciones de Aspose.PDF para .NET en tu Explorador de Objetos.

Para generar un archivo TLB:

- .NET Framework 2.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net2.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net2.0\Aspose.PDF.tlb" /codebase
- .NET Framework 3.5
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net3.5\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net3.5\Aspose.PDF.tlb" /codebase
- .NET Framework 4.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.0\Aspose.PDF.tlb" /codebase

{{% /alert %}}

## Creación de Objetos COM

La creación de un objeto COM es similar a la creación de un objeto .NET normal:

```vb

'Instancia Pdf llamando a su constructor vacío

Dim pdf
Set pdf = CreateObject("Aspose.PDF.Generator.Pdf")

```
Una vez creado, podrás acceder a los métodos y propiedades del objeto, como si fuera un objeto COM:

```vb
'Add section to Pdf object
pdf.Sections.Add(pdfsection)
```

Algunos métodos tienen sobrecargas y serán expuestos por COM Interop con un sufijo numérico agregado a ellos, excepto por el primer método que permanece sin cambios. Por ejemplo, las sobrecargas del método Pdf.Save se convierten en Pdf.Save, Pdf.Save_2, y así sucesivamente.

Para más información, consulta los artículos específicos del idioma más adelante en esta documentación.

## Creando una Asamblea Contenedora

Si necesitas utilizar muchas clases, métodos y propiedades de Aspose.PDF para .NET, considera crear una asamblea contenedora (usando C# u otro lenguaje de programación .NET). Las asambleas contenedoras ayudan a evitar usar directamente Aspose.PDF para .NET desde código no gestionado.

Un buen enfoque es desarrollar una asamblea de .NET que haga referencia a Aspose.PDF para .NET y realice todo el trabajo con él, y solo exponga un conjunto mínimo de clases y métodos al código no gestionado.
Un buen enfoque es desarrollar un ensamblado .NET que haga referencia a Aspose.PDF para .NET y realice todo el trabajo con él, exponiendo solo un conjunto mínimo de clases y métodos al código no administrado.

Reducir el número de clases y métodos que necesitas invocar a través de COM Interop simplifica el proyecto. Utilizar clases .NET a través de COM Interop a menudo requiere habilidades avanzadas.
