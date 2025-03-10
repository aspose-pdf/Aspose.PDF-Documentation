---
title: Cómo instalar Aspose.PDF for .NET
linktitle: Instalación
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /es/net/installation/
description: Esta sección muestra una descripción del producto e instrucciones para instalar Aspose.PDF for .NET por su cuenta, así como usar NuGet.
lastmod: "2024-09-04"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to Install Aspose.PDF for .NET",
    "alternativeHeadline": "Seamless PDF Creation with Aspose.PDF for .NET",
    "abstract": "Aspose.PDF for .NET es un componente poderoso que permite a los desarrolladores generar y manipular documentos PDF programáticamente sin depender de Adobe Acrobat. Con soporte para insertar elementos complejos como tablas, imágenes y fuentes personalizadas, así como características de seguridad robustas e integración sin problemas a través de NuGet, esta herramienta versátil mejora la productividad y eficiencia en aplicaciones .NET",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Aspose.PDF, PDF documents, .NET component, NuGet installation, C# API, Temporary License, multithread safe, eval version limitations, .NET Core support, font installation",
    "wordcount": "1214",
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
    "url": "/net/installation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/installation/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también hacer frente a objetivos más complejos. Consulte la siguiente sección para usuarios avanzados y desarrolladores."
}
</script>

## Componente Aspose.PDF C#

{{% alert color="primary" %}}

**Aspose.PDF es un componente .NET** diseñado para permitir a los desarrolladores crear documentos PDF, ya sean simples o complejos, sobre la marcha programáticamente. Aspose.PDF for .NET permite a los desarrolladores insertar tablas, gráficos, imágenes, hipervínculos, fuentes personalizadas y más en documentos PDF. Además, también es posible comprimir documentos PDF. Aspose.PDF for .NET proporciona excelentes características de seguridad para desarrollar documentos PDF seguros. Y la característica más distintiva de Aspose.PDF for .NET es que admite la creación de documentos PDF tanto a través de una API como desde plantillas XML.

{{% /alert %}}

## Descripción del producto

**Aspose.PDF for .NET** es un componente .NET robusto que permite a los desarrolladores crear documentos PDF desde cero sin usar Adobe Acrobat. Proporciona una interfaz de programación de aplicaciones (API) simple que es fácil de aprender y usar.

**Aspose.PDF for .NET** está implementado utilizando C# administrado y se puede usar con cualquier lenguaje .NET como C#, VB.NET y J#, etc. Se puede integrar con cualquier tipo de aplicación, ya sea una aplicación web ASP.NET o una aplicación de Windows.

Para que los desarrolladores puedan comenzar rápidamente, Aspose.PDF for .NET proporciona demostraciones completamente funcionales y ejemplos de trabajo escritos en C#. Usando estas demostraciones, los desarrolladores pueden aprender rápidamente sobre las características proporcionadas por Aspose.PDF for .NET.

El componente rápido y ligero crea documentos PDF de manera eficiente y ayuda a que su aplicación funcione mejor. Aspose.PDF for .NET es la primera opción de nuestros clientes al crear documentos PDF debido a su precio, rendimiento excepcional y gran soporte.

**Aspose.PDF for .NET** es seguro para multihilos siempre que solo un hilo trabaje en un documento a la vez. Es un escenario típico tener un hilo trabajando en un documento. Diferentes hilos pueden trabajar de manera segura en diferentes documentos al mismo tiempo.

## Declaración

Todos los componentes Aspose .NET requieren un conjunto de permisos de Confianza Total. La razón es que los componentes Aspose .NET necesitan acceder a configuraciones del registro, archivos del sistema que no sean el directorio virtual para ciertas operaciones como el análisis de fuentes, etc. Además, los componentes Aspose .NET se basan en clases del sistema .NET que también requieren un conjunto de permisos de Confianza Total en muchos casos.

Los proveedores de servicios de Internet que alojan múltiples aplicaciones de diferentes empresas generalmente imponen un nivel de seguridad de Confianza Media. En el caso de .NET 2.0, dicho nivel de seguridad aplica las siguientes restricciones:

- **OleDbPermission no está disponible.** Esto significa que no puede usar el proveedor de datos OLE DB administrado de ADO.NET para acceder a bases de datos.
- **EventLogPermission no está disponible.** Esto significa que no puede acceder al registro de eventos de Windows.
- **ReflectionPermission no está disponible.** Esto significa que no puede usar reflexión.
- **RegistryPermission no está disponible.** Esto significa que no puede acceder al registro.
- **WebPermission está restringido.** Esto significa que su aplicación solo puede comunicarse con una dirección o rango de direcciones que defina en el elemento `<trust>`.
- **FileIOPermission está restringido.** Esto significa que solo puede acceder a archivos en la jerarquía del directorio virtual de su aplicación.
Debido a las razones especificadas anteriormente, los componentes Aspose .NET no se pueden usar en servidores que otorguen un conjunto de permisos diferente a Confianza Total.

## Instalación

### Evaluar Aspose.PDF for .NET

Puede descargar fácilmente Aspose.PDF for .NET para evaluación. La descarga de evaluación es la misma que la descarga comprada. La versión de evaluación simplemente se convierte en licenciada cuando agrega algunas líneas de código para aplicar la licencia.

La versión de evaluación de Aspose.PDF (sin una licencia especificada) proporciona toda la funcionalidad del producto. Sin embargo, tiene dos limitaciones: inserta una marca de agua de evaluación y solo se pueden ver/editar las primeras cuatro páginas de cualquier documento.

{{% alert color="primary" %}}

Si desea probar Aspose.PDF for .NET sin las limitaciones de la versión de evaluación, también puede solicitar una Licencia Temporal de 30 días. Consulte [¿Cómo obtener una Licencia Temporal?](https://purchase.aspose.com/temporary-license)

{{% /alert %}}

### Instalando Aspose.PDF for .NET a través de NuGet

NuGet es un sistema de gestión de paquetes gratuito y de código abierto enfocado en desarrolladores para la plataforma .NET, con la intención de simplificar el proceso de incorporación de bibliotecas de terceros en una aplicación .NET durante el desarrollo. Es una extensión de Visual Studio que facilita agregar, eliminar y actualizar bibliotecas y herramientas en proyectos de Visual Studio que utilizan el marco .NET. Una biblioteca o herramienta se puede compartir fácilmente con otros desarrolladores creando un paquete NuGet y almacenándolo dentro de un repositorio NuGet. Cuando instala el paquete, NuGet copia archivos a su solución y realiza automáticamente los cambios necesarios, como agregar referencias y cambiar sus archivos app.config o web.config. Si decide eliminar la biblioteca, NuGet elimina archivos y revierte cualquier cambio que haya realizado en su proyecto para que no quede desorden.

### Referenciando Aspose.PDF for .NET

#### Instalar paquete usando la Consola del Administrador de Paquetes

- Abra su aplicación .NET en Visual Studio.
- En el menú Herramientas, seleccione **Administrador de Paquetes NuGet** y luego **Consola del Administrador de Paquetes**.
- Escriba el comando `Install-Package Aspose.PDF` para instalar la última versión completa, o escriba el comando `Install-Package Aspose.PDF -prerelease` para instalar la última versión que incluye correcciones rápidas.
- Presione `Enter`.

#### Actualizar paquete usando la Consola del Administrador de Paquetes

Si ya ha referenciado el componente a través de NuGet, siga estos pasos para actualizar la referencia a la última versión:

- Abra su aplicación .NET en Visual Studio.
- En el menú Herramientas, seleccione **Administrador de Paquetes NuGet** y luego **Consola del Administrador de Paquetes**.
- Escriba el comando `Update-Package Aspose.PDF` para referenciar la última versión completa, o escriba el comando `Update-Package Aspose.PDF -prerelease` para instalar la última versión que incluye correcciones rápidas.

#### Instalar Paquete usando la GUI del Administrador de Paquetes

Siga estos pasos para referenciar el componente usando la GUI del administrador de paquetes:

- Abra su aplicación .NET en Visual Studio.

- Desde el menú Proyecto seleccione **Administrar Paquetes NuGet**.

![Installation_step](../images/install_step.png)

- Seleccione la pestaña **Broswe**.

![Installation_step1](../images/install_step1.png)

- Escriba Aspose.PDF en el cuadro de búsqueda para encontrar Aspose.PDF for .NET.

- Haga clic en Instalar/Actualizar junto a la última versión de Aspose.PDF for .NET.

![Installation_step2](../images/Install_step2.png)

- Y haga clic en Aceptar en la ventana emergente.

![Installation_step3](../images/Install_step3.png)

![Installation](../images/install.gif)

### Trabajando con DLLs de .NET Core en Entornos No Windows

Dado que Aspose.PDF for .NET proporciona soporte para .NET Standard 2.0 (.NET Core 2.0), se puede usar en aplicaciones Core que se ejecutan en sistemas operativos similares a Linux. Estamos trabajando constantemente para mejorar el soporte de .NET Core en nuestra API. Sin embargo, hay algunas operaciones que recomendamos a nuestros clientes realizar para obtener mejores resultados al usar las características de Aspose.PDF for .NET:

Por favor, instale:

- paquete libgdiplus
- paquete con fuentes compatibles con Microsoft: **ttf-mscorefonts-installer**. (por ejemplo, `sudo apt-get install ttf-mscorefonts-installer`)
Estas fuentes deben colocarse en el directorio "/usr/share/fonts/truetype/msttcorefonts" ya que Aspose.PDF for .NET escanea esta carpeta en sistemas operativos similares a Linux. En caso de que el sistema operativo tenga otra carpeta/directorio predeterminado para fuentes, debe usar la siguiente línea de código antes de realizar cualquier operación usando Aspose.PDF.

```csharp
Aspose.Pdf.Text.FontRepository.Sources.Add(new FolderFontSource("<user's path to ms fonts>"));
```

#### Configurar Aspose.PDF for .NET en Visual Studio Code
- Instalar .NET SDK

1. Visite el sitio web oficial de [Microsoft .NET](https://dotnet.microsoft.com/download).
2. Descargue el último .NET SDK.
3. Ejecute el instalador.
4. Abra una terminal y verifique la instalación ejecutando:
```bash
dotnet --version
```

- Instalar Visual Studio Code

1. Vaya a https://code.visualstudio.com/.
2. Descargue la versión adecuada para su sistema operativo.

- Instalar Extensiones Requeridas de VS Code

1. Abra Visual Studio Code.
2. Haga clic en el ícono de vista de Extensiones (ícono cuadrado en la barra lateral izquierda).
3. Busque e instale las siguientes extensiones:
   - "C#" de Microsoft
   - "C# Dev Kit" de Microsoft
   - ".NET Core Test Explorer" (opcional, pero recomendado)

- Crear un nuevo proyecto .NET

1. Abra Visual Studio Code
2. Vaya a Terminal > Nueva Terminal
3. Navegue a su directorio de proyecto deseado
```bash
# Create a new console application
dotnet new console -n AsposePDFNetDemo
# Navigate into the project directory
cd AsposePDFNetDemo
```

- Agregar paquete NuGet

```bash
# Install Aspose.PDF package
dotnet add package Aspose.PDF
```

- Verificar instalación del paquete

1. Abra el archivo `.csproj`
2. Confirme que la referencia del paquete Aspose.PDF se haya agregado:
```xml
<ItemGroup>
  <PackageReference Include="Aspose.PDF" Version="x.x.x" />
</ItemGroup>
```

- Crear Configuración de Depuración

1. Presione Ctrl+Shift+P (Cmd+Shift+P en Mac).
2. Escriba ">.NET: Generar activos para construir y depurar".
3. Seleccione su proyecto.
4. Cree o modifique `.vscode/launch.json`:
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": ".NET Core Launch (console)",
            "type": "coreclr",
            "request": "launch",
            "preLaunchTask": "build",
            "program": "${workspaceFolder}/bin/Debug/net7.0/AsposePDFNetDemo.dll",
            "args": [],
            "cwd": "${workspaceFolder}",
            "console": "internalConsole",
            "stopAtEntry": false
        }
    ]
}
```

- Escribir código de ejemplo en Program.cs

Reemplace el contenido de `Program.cs` con:
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
using System;
using Aspose.Pdf;
using Aspose.Pdf.Text;

class Program 
{
    static void Main(string[] args)
    {
        // Activate your license, you can comment out these codelines to use library in Evaluation mode
        var license = new Aspose.Pdf.License();
        license.SetLicense("Aspose.PDF.NET.lic");

        // Create PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            var page = document.Pages.Add();
            
            // Create a text fragment
            var textFragment = new Aspose.Pdf.Text.TextFragment("Hello, Aspose.PDF for .NET!");
            textFragment.Position = new Aspose.Pdf.Text.Position(100, 600);
            
            // Add text to the page
            page.Paragraphs.Add(textFragment);
            
            // Save PDF document
            document.Save("sample.pdf");
        }
    }
}
```

- Compilar y ejecutar

```bash
dotnet restore
dotnet build
dotnet run
```