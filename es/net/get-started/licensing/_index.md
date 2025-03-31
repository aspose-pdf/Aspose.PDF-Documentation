---
title: Licencia de Aspose PDF
linktitle: Licencias y limitaciones
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /es/net/licensing/
description: Aspose.PDF para .NET invita a sus clientes a obtener una licencia Clásica y una Licencia Medida. Así como usar una licencia limitada para explorar mejor el producto.
lastmod: "2025-02-07"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Aspose PDF for .NET License",
    "alternativeHeadline": "Licensing Options for Aspose.PDF for .NET Users",
    "abstract": "Aspose PDF para .NET introduce un robusto marco de licencias que incluye tanto licencias Clásicas como Medidas, permitiendo a los usuarios elegir entre precios fijos y opciones de facturación basadas en el uso. La licencia Clásica se puede cargar fácilmente desde un archivo o flujo, mientras que la innovadora licencia Medida proporciona un metraje flexible basado en el uso de la API, atendiendo a diversas necesidades de los usuarios. Esta estrategia de licenciamiento dual mejora la accesibilidad y escalabilidad de las soluciones PDF para desarrolladores.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "869",
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
    "url": "/net/licensing/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/licensing/"
    },
    "dateModified": "2025-02-07",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Limitación de una versión de evaluación

Queremos que nuestros clientes prueben a fondo nuestros componentes antes de comprar, por lo que la versión de evaluación permite usarlo como lo harías normalmente.

- **PDF creado con una marca de agua de evaluación.** La versión de evaluación de Aspose.PDF for .NET proporciona toda la funcionalidad del producto, pero todas las páginas en los documentos PDF generados están marcadas con el texto "Evaluación Solo. Creado con Aspose.PDF. Copyright 2002-2025 Aspose Pty Ltd." en la parte superior.

- **Limitar el número de páginas que se pueden procesar.**
En la versión de evaluación, solo puedes procesar las primeras cuatro páginas de un documento.

>Si deseas probar Aspose.PDF for .NET sin las limitaciones de la versión de evaluación, también puedes solicitar una Licencia Temporal de 30 días. Por favor, consulta [¿Cómo obtener una Licencia Temporal?](https://purchase.aspose.com/temporary-license)

## Licencia Clásica

La licencia se puede cargar desde un archivo o un objeto de flujo. La forma más fácil de establecer una licencia es colocar el archivo de licencia en la misma carpeta que el archivo Aspose.PDF.dll y especificar el nombre del archivo sin una ruta, como se muestra en el ejemplo a continuación.

Si utilizas cualquier otro componente de Aspose para .NET junto con Aspose.PDF for .NET, por favor especifica el espacio de nombres para License como [Aspose.Pdf.License](https://reference.aspose.com/pdf/es/net/aspose.pdf/license).

### Cargando una licencia desde un archivo

La forma más fácil de aplicar una licencia es colocar el archivo de licencia en la misma carpeta que el archivo Aspose.PDF.dll y especificar solo el nombre del archivo sin una ruta.

Cuando llames al método [SetLicense](https://reference.aspose.com/pdf/es/net/aspose.pdf/license/methods/setlicense/index), el nombre de la licencia que pases debe ser el de tu archivo de licencia. Por ejemplo, si cambias el nombre del archivo de licencia a "Aspose.PDF.lic.xml", pasa ese nombre de archivo al método Pdf.SetLicense(…).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetLicenseExample()
{
    // Initialize license object
    var license = new Aspose.Pdf.License();
    try
    {
        // Set license
        license.SetLicense("Aspose.Pdf.lic");
    }
    catch (Exception)
    {
        // Something went wrong
        throw;
    }
    Console.WriteLine("License set successfully.");
}
```
### Cargando la licencia desde un objeto de flujo

El siguiente ejemplo muestra cómo cargar una licencia desde un flujo.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetLicenseFromStream()
{
    // Initialize license object
    var license = new Aspose.Pdf.License();
    // Load license from the file stream
    var myStream = new FileStream(
            "Aspose.Pdf.lic",
            FileMode.Open);
    // Set license
    license.SetLicense(myStream);
    Console.WriteLine("License set successfully.");
}
```
## Licencia Medida

Aspose.PDF permite a los desarrolladores aplicar una clave medida. El mecanismo de licenciamiento medido se utilizará junto con el método de licenciamiento existente. Aquellos clientes que deseen ser facturados en función del uso de las características de la API pueden utilizar el licenciamiento medido. Para más detalles, consulta la sección de Preguntas Frecuentes sobre Licencias Medidas.
Esta guía proporciona las mejores prácticas para una implementación fluida y para prevenir interrupciones debido a cambios en el estado de la licencia.

La clase "Metered" se utiliza para aplicar claves medidas. A continuación se muestra un código de muestra que demuestra cómo establecer claves públicas y privadas medidas.

Para más detalles, consulta la sección de [Preguntas Frecuentes sobre Licencias Medidas](https://purchase.aspose.com/faqs/licensing/metered).

__Métodos de Licenciamiento Medido__

Aplicando la Licencia Medida utiliza el método `SetMeteredKey` para activar la licencia medida proporcionando tus claves públicas y privadas. Esto debe hacerse una vez durante la inicialización de la aplicación para asegurar un licenciamiento adecuado.

Ejemplo:

```csharp
 var metered = new Aspose.Pdf.Metered();
 metered.SetMeteredKey("your-public-key", "your-private-key");
 ```
Comprobando el Estado de la Licencia utiliza `IsMeteredLicensed()` para verificar si la licencia medida está activa.

Ejemplo:

```csharp
bool isLicensed = Aspose.Pdf.License.IsMeteredLicensed();
if (!isLicensed) 
{
    metered.SetMeteredKey("your-public-key", "your-private-key");
}
 ```
El método `Metered.GetConsumptionCredit()` se utiliza para obtener información sobre los créditos de consumo.
El método `Metered.GetConsumptionQuantity()` se utiliza para obtener información sobre el tamaño del archivo de consumo.

Ejemplo:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetMeteredLicense()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
    // Set metered public and private keys
    var metered = new Aspose.Pdf.Metered();
    // Access the setMeteredKey property and pass public and private keys as parameters
    metered.SetMeteredKey("your public key", "your private key");

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
       // Add five pages
       AddPages(document, 5);
       // Save the document
       document.Save(dataDir + "output.pdf")
    }
}

private static void AddPages(Document document, int n)
{
    for(int i = 0; i < n; i++)
    {
        document.Pages.Add();
    }
}   
```

__Mejores Prácticas para Licenciamiento Medido__

✅ Enfoque Recomendado: Patrón Singleton
Para asegurar una configuración de licencia estable:

- Aplica la licencia una vez al inicio de la aplicación.
- Utiliza un patrón singleton (o un enfoque similar) para crear y reutilizar la instancia de la licencia medida.
- Verifica periódicamente el estado de la licencia utilizando `IsMeteredLicensed()`. Reaplica la licencia solo si se vuelve inválida.
- Si se implementa correctamente, la licencia permanece válida durante 24 horas incluso si el servidor de licencias está temporalmente no disponible.

Ejemplo: Implementación Singleton

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
public class AsposeLicenseManager
{
    private static AsposeLicenseManager _instance;
    private static readonly object _lock = new object();
    private Aspose.Pdf.Metered _metered;

    private AsposeLicenseManager()
    {
        _metered = new Aspose.Pdf.Metered();
        _metered.SetMeteredKey("your-public-key", "your-private-key");
    }

    public static AsposeLicenseManager Instance
    {
        get
        {
            lock (_lock)
            {
                if (_instance == null)
                {
                    _instance = new AsposeLicenseManager();
                }
                return _instance;
            }
        }
    }

    public void ValidateLicense()
    {
        if (!Aspose.Pdf.License.IsMeteredLicensed())
        {
        _metered.SetMeteredKey("your-public-key", "your-private-key");
        }
    }
}
```

❌ Errores Comunes a Evitar:

- Aplicaciones Frecuentes de Licencia
- No crees una nueva instancia de licencia medida para cada operación.
- Si el servidor de licencias no es accesible durante la inicialización, la licencia puede revertir al modo de evaluación.
- No apliques la licencia repetidamente para cada operación.
- Aplicaciones frecuentes de licencia pueden causar un retroceso al modo de prueba si el servidor de licencias está temporalmente no disponible.

__Resumen:__

✅ Establece la licencia medida una vez al inicio de la aplicación.
✅ Utiliza un patrón singleton para gestionar una única instancia.
✅ Verifica periódicamente y reaplica la licencia si es necesario.
❌ Evita aplicaciones frecuentes de licencia para prevenir retrocesos al modo de prueba.
Siguiendo estas mejores prácticas, aseguras un uso fluido e ininterrumpido de Aspose.PDF con licenciamiento medido.

Si la licencia fue inicializada, entonces mientras este objeto "viva", incluso si la conexión al servidor de licencias se pierde por alguna razón, la licencia se considerará activa durante otros 7 días. Si inicializas una licencia cada vez que necesitas hacer algo y no hay conexión al servidor en el momento de la inicialización, entonces la licencia pasará al modo Eval.
Cabe enfatizar que si un usuario ha inicializado una licencia, entonces mientras este objeto "viva", incluso si la conexión al servidor de licencias se pierde por alguna razón, la licencia se considerará activa durante otras 24 horas. Si inicializas una licencia cada vez que necesitas hacer algo y no hay conexión al servidor en el momento de la inicialización, entonces la licencia pasará al modo Eval.

Ten en cuenta que las aplicaciones COM que trabajan con **Aspose.PDF for .NET** también deben usar la clase License.

Un punto que necesita consideración:
Ten en cuenta que los recursos incrustados se incluyen en el ensamblaje tal como se añaden, es decir, si agregas un archivo de texto como un recurso incrustado en la aplicación y abres el EXE resultante en un bloc de notas, verás el contenido exacto del archivo de texto. Así que al usar el archivo de licencia como un recurso incrustado, cualquiera puede abrir el archivo exe en algún editor de texto simple y ver/extrair el contenido de la licencia incrustada.

Por lo tanto, para poner una capa adicional de seguridad al incrustar la licencia con la aplicación, puedes comprimir/encriptar la licencia y después, puedes incrustarla en el ensamblaje. Supongamos que tenemos el archivo de licencia Aspose.PDF.lic, así que hagamos Aspose.PDF.zip con contraseña test e incrustemos este archivo zip en la solución. El siguiente fragmento de código se puede usar para inicializar la licencia:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetLicenseFromStream()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
    var license = new Aspose.Pdf.License();
    license.SetLicense(GetSecureLicenseFromStream());
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the page count of document
        Console.WriteLine(document.Pages.Count);
    }
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
```