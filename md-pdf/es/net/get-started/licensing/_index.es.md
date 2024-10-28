---
title: Aspose PDF License
linktitle: Licenciamiento y limitaciones
type: docs
weight: 90
url: /net/licensing/
description: Aspose. PDF para .NET invita a sus clientes a obtener una licencia Clásica y una Licencia Medida. Así como usar una licencia limitada para explorar mejor el producto.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Limitación de una versión de evaluación

Queremos que nuestros clientes prueben nuestros componentes a fondo antes de comprar, por lo que la versión de evaluación le permite usarla como lo haría normalmente.

- **PDF creado con una marca de agua de evaluación.** La versión de evaluación de Aspose.PDF para .NET ofrece toda la funcionalidad del producto, pero todas las páginas en los documentos PDF generados están marcadas con "Solo Evaluación. Creado con Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" en la parte superior.

- **El límite del número de elementos de colección que se pueden procesar.**
En la versión de evaluación de cualquier colección, solo puedes procesar cuatro elementos (por ejemplo, solo 4 páginas, 4 campos de formulario, etc.).
En la versión de evaluación de cualquier colección, solo puede procesar cuatro elementos (por ejemplo, solo 4 páginas, 4 campos de formulario, etc.).

>Si desea probar Aspose.HTML para .NET sin las limitaciones de la versión de evaluación, también puede solicitar una Licencia Temporal de 30 días. Por favor, consulte [Cómo obtener una Licencia Temporal?](https://purchase.aspose.com/temporary-license)

## Licencia clásica

La licencia se puede cargar desde un archivo o un objeto de flujo. La forma más fácil de configurar una licencia es colocar el archivo de licencia en la misma carpeta que el archivo Aspose.PDF.dll y especificar el nombre del archivo sin una ruta, como se muestra en el ejemplo a continuación.

Si usa cualquier otro componente de Aspose para .NET junto con Aspose.PDF para .NET, por favor especifique el espacio de nombres para License como [Aspose.Pdf.License](https://reference.aspose.com/pdf/net/aspose.pdf/license).

### Cargando una licencia desde un archivo

La forma más fácil de aplicar una licencia es colocar el archivo de licencia en la misma carpeta que el archivo Aspose.PDF.dll y especificar solo el nombre del archivo sin una ruta.

Cuando llama al método [SetLicense](https://reference.aspose.com/pdf/net/aspose.pdf/license/methods/setlicense/index), el nombre de la licencia que pasa debe ser el de su archivo de licencia.
Cuando llamas al método [SetLicense](https://reference.aspose.com/pdf/net/aspose.pdf/license/methods/setlicense/index), el nombre de la licencia que pasas debe ser el de tu archivo de licencia.

```csharp
public static void SetLicenseExample()
{
    // Inicializar el objeto de licencia
    Aspose.Pdf.License license = new Aspose.Pdf.License();
    try
    {
        // Establecer la licencia
        license.SetLicense("Aspose.Pdf.lic");
    }
    catch (Exception)
    {
        // algo salió mal
        throw;
    }
    Console.WriteLine("Licencia establecida correctamente.");
}
```
### Cargando la licencia desde un objeto de flujo

El siguiente ejemplo muestra cómo cargar una licencia desde un flujo.

```csharp
public static void SetLicenseFromStream()
{
    // Inicializar el objeto de licencia
    Aspose.Pdf.License license = new Aspose.Pdf.License();
    // Cargar la licencia del flujo de archivo
    System.IO.FileStream myStream =
        new System.IO.FileStream(
            "Aspose.Pdf.lic",
            System.IO.FileMode.Open);
    // Establecer la licencia
    license.SetLicense(myStream);
    Console.WriteLine("Licencia establecida correctamente.");
}
```
## Licencia medida

Aspose.PDF permite a los desarrolladores aplicar una clave medida. Es un nuevo mecanismo de licencia. El nuevo mecanismo de licencia se utilizará junto con el método de licencia existente. Aquellos clientes que deseen ser facturados en base al uso de las características de la API pueden usar la licencia medida. Para más detalles, por favor consulte la sección de Preguntas Frecuentes sobre Licencia Medida.

Se ha introducido una nueva clase Metered para aplicar la clave medida. A continuación se muestra el código de muestra que demuestra cómo configurar las claves públicas y privadas medidas.

Para más detalles, por favor consulte la sección de [Preguntas Frecuentes sobre Licencia Medida](https://purchase.aspose.com/faqs/licensing/metered).

```csharp
public static void SetMeteredLicense()
{
    // establecer claves públicas y privadas medidas
    Aspose.Pdf.Metered metered = new Aspose.Pdf.Metered();
    // Acceder a la propiedad setMeteredKey y pasar las claves públicas y privadas como parámetros
    metered.SetMeteredKey(
        "<escriba aquí la clave pública>",
        "<escriba aquí la clave privada>");

    // Cargar el documento desde el disco.
    Document doc = new Document("input.pdf");
    //Obtener el conteo de páginas del documento
    Console.WriteLine(doc.Pages.Count);
}
```
Tenga en cuenta que las aplicaciones COM que trabajan con **Aspose.PDF para .NET** también deben usar la clase License.

Un punto que requiere consideración:
Tenga en cuenta que los recursos incrustados se incluyen en el ensamblaje de la manera en que se agregan, es decir, si agrega un archivo de texto como recurso incrustado en la aplicación y abre el EXE resultante en el bloc de notas, verá el contenido exacto del archivo de texto. Por lo tanto, al usar el archivo de licencia como un recurso incrustado, cualquiera puede abrir el archivo exe en algún editor de texto simple y ver/extraer el contenido de la licencia incrustada.

Por lo tanto, para agregar una capa extra de seguridad al incrustar la licencia con la aplicación, puede comprimir/encriptar la licencia y después de eso, puede incrustarla en el ensamblaje. Supongamos que tenemos el archivo de licencia Aspose.PDF.lic, así que hagamos Aspose.PDF.zip con la contraseña test e incrustemos este archivo zip en la solución. El siguiente fragmento de código se puede usar para inicializar la licencia:

```csharp
using System;
using System.IO;
using System.IO.Compression;
using System.Reflection;

namespace Aspose.Pdf.Examples
{
    class ExampleLicensing
    {
        public static void LicenseDemo()
        {
            License license = new License();
            license.SetLicense(GetSecureLicenseFromStream());
            Document doc = new Document("document.pdf");
            //Obtener el recuento de páginas del documento
            Console.WriteLine(doc.Pages.Count);
        }

        private static Stream GetSecureLicenseFromStream()
        {
            var assembly = Assembly.GetExecutingAssembly();
            var memoryStream = new MemoryStream();
            using (var zipToOpen = assembly.GetManifestResourceStream("Aspose.Pdf.Examples.License.Aspose.PDF.zip"))
            {
                using (ZipArchive archive = new ZipArchive(zipToOpen ?? throw new InvalidOperationException(), ZipArchiveMode.Read))
                {
                    var unpackedLicense  = archive.GetEntry("Aspose.PDF.lic");
                    unpackedLicense?.Open().CopyTo(memoryStream);
                }
            }

            memoryStream.Position = 0;
            return memoryStream;
        }
    }
}
```
### Aplicando una Licencia Comprada Antes del 22/01/2005

Aspose.PDF para .NET ya no admite las licencias antiguas. Si tienes una licencia de antes del 22 de enero de 2005 y has actualizado a una versión más reciente de Aspose.PDF, por favor contacta a nuestro equipo de Ventas para obtener un nuevo archivo de licencia.
