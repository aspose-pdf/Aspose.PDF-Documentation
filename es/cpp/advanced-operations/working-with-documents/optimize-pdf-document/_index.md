---
title: Optimize PDF using C++
linktitle: Optimize PDF
type: docs
weight: 30
url: /es/cpp/optimize-pdf/
description: Optimizar archivo PDF, reducir todas las imágenes, disminuir el tamaño del PDF, desincrustar fuentes, habilitar la reutilización del contenido de la página, eliminar o aplanar anotaciones con C++.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

En primer lugar, cualquier optimización de PDF que realices es para el usuario. En los PDFs, la optimización para el usuario se centra principalmente en reducir el tamaño de tus PDFs para aumentar su velocidad de carga. Esta es la tarea más popular.
Podemos utilizar varias técnicas para optimizar el PDF, pero lo más esencial:

- Optimizar el contenido de la página para la navegación en línea
- Reducir o comprimir todas las imágenes
- Habilitar la reutilización del contenido de la página
- Unir flujos duplicados
- Desincrustar fuentes
- Eliminar objetos no utilizados
- Eliminar campos de formulario aplanados
- Eliminar o aplanar anotaciones

## Optimizar Documento PDF para la Web

Cuando te enfrentas a la tarea de optimizar el contenido de tu documento PDF para un mejor posicionamiento en los motores de búsqueda, Aspose.PDF para C++ tiene una solución.

1. Abra el documento de entrada en un objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Use el método [Optimize](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a04d95824c334f5e543c13f69a19d9cda).
1. Guarde el documento optimizado usando el método Save.

El siguiente fragmento de código muestra cómo optimizar un documento PDF para la web.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
//Optimize PDF Document for the Web
void OptimizeForWeb() {
    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String outfilename("OptimizeDocument_out.pdf");

    // Open document
    auto document = MakeObject<Document>();

    // Make some operations (add pages, images, etc) 
    // ...

    // Optimize for web
    document->Optimize();

    // Save output document
    document->Save(_dataDir + outfilename);
}
```

## Reducir el tamaño del PDF

El método [OptimizeResources()](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#aea33aac69a42423efb82bcdb359f2ec6) le permite reducir el tamaño del documento eliminando la información innecesaria. Por defecto, este método funciona de la siguiente manera:

- Los recursos que no se utilizan en las páginas del documento se eliminan
- Los recursos iguales se unen en un solo objeto
- Los objetos no utilizados se eliminan

El siguiente fragmento es un ejemplo. Sin embargo, tenga en cuenta que este método no puede garantizar la reducción del documento.

```cpp
void ReduceSizePDF() {

    // String para nombre de ruta
    String _dataDir("C:\\Samples\\");

    // String para nombre del archivo de entrada
    String outfilename("ShrinkDocument_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>();
    // Realizar algunas operaciones (agregar páginas, imágenes, etc.)
    // ...

    // Optimizar documento PDF. Sin embargo, tenga en cuenta que este método no puede garantizar la reducción del documento
    document->OptimizeResources();

    // Guardar documento de salida
    document->Save(_dataDir + outfilename);
}
```

## Gestión de la Estrategia de Optimización

También podemos personalizar la estrategia de optimización. Actualmente, el método [OptimizeResources()](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#aea33aac69a42423efb82bcdb359f2ec6) utiliza 5 técnicas. Estas técnicas se pueden aplicar utilizando el método OptimizeResources() con el parámetro [OptimizationOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document.optimization_options/).

### Reducir o Comprimir Todas las Imágenes

Para optimizar las imágenes en su documento PDF, utilizaremos [Aspose.Pdf.Optimization](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.optimization).
Para resolver el problema con la optimización de imágenes, tenemos las siguientes opciones: reducir la calidad de la imagen y/o cambiar su resolución. En cualquier caso, [ImageCompressionOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options/) debe ser aplicado. En el siguiente ejemplo, reducimos las imágenes disminuyendo [ImageQuality](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#a92ee855b042a6b310984b4966ea7154e) a 50.

```cpp
void CompressImage() {
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\");

    // Cadena para el nombre del archivo de entrada
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Inicializar OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Establecer opción CompressImages
    optimizationOptions->get_ImageCompressionOptions()->set_CompressImages(true);
    // Establecer opción ImageQuality
    optimizationOptions->get_ImageCompressionOptions()->set_ImageQuality(50);

    // Optimizar documento PDF usando OptimizationOptions
    document->OptimizeResources(optimizationOptions); 
    // Guardar documento actualizado
    document->Save(_dataDir + outfilename);
}
```
Para establecer la imagen a una resolución más baja, configure [ResizeImages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#a0e5aad7e140ee380c09ebbb8a5238ff6) en true y [MaxResolution](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#a05a4d1ace23ef074b3dc203cb213755e) al valor correspondiente.

```cpp
void ResizeImagesWithLowerResolution() {
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\");

    // Cadena para el nombre del archivo de entrada
    String infilename("ResizeImage.pdf");
    String outfilename("ResizeImages_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Inicializar OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Configurar opción CompressImages
    optimizationOptions->get_ImageCompressionOptions()->set_CompressImages(true);
    // Configurar opción ImageQuality
    optimizationOptions->get_ImageCompressionOptions()->set_ImageQuality(75);

    // Configurar opción ResizeImage
    optimizationOptions->get_ImageCompressionOptions()->set_ResizeImages(true);
    // Configurar opción MaxResolution
    optimizationOptions->get_ImageCompressionOptions()->set_MaxResolution(300);

    // Optimizar documento PDF usando OptimizationOptions
    document->OptimizeResources(optimizationOptions);
    // Guardar documento actualizado
    document->Save(_dataDir + outfilename);
}
```

Aspose.PDF para C++ también le ofrece control sobre la configuración de tiempo de ejecución. Hoy en día, podemos usar dos algoritmos: Estándar y Rápido. Para controlar el tiempo de ejecución debemos establecer una propiedad [Version](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#aa2f1d93725ce56f8fabe692152bbf3a4).

El siguiente fragmento demuestra el algoritmo Rápido:

```cpp
void ResizeImagesWithLowerResolutionFast() {
    auto time = System::DateTime::get_Now().get_Ticks();
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\");

    // Cadena para el nombre del archivo de entrada
    String infilename("ResizeImage.pdf");
    String outfilename("ResizeImages_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Inicializar OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Establecer opción CompressImages
    optimizationOptions->get_ImageCompressionOptions()->set_CompressImages(true);
    // Establecer opción ImageQuality
    optimizationOptions->get_ImageCompressionOptions()->set_ImageQuality(75);

    // Establecer opción ResizeImage
    optimizationOptions->get_ImageCompressionOptions()->set_ResizeImages(true);
    // Establecer la versión de compresión de imagen a rápido
    optimizationOptions->get_ImageCompressionOptions()->set_Version (Aspose::Pdf::Optimization::ImageCompressionVersion::Fast);

    // Optimizar documento PDF usando OptimizationOptions
    document->OptimizeResources(optimizationOptions);
    // Guardar documento actualizado
    document->Save(_dataDir + outfilename);
    std::cout << "Ticks: " << System::DateTime::get_Now().get_Ticks() - time << std::endl;
}
```

### Eliminando Objetos No Utilizados

A veces puede ser necesario eliminar algunos objetos no utilizados de su documento PDF que no están referenciados en las páginas. Esto puede suceder, por ejemplo, cuando se elimina una página del árbol de páginas del documento pero el objeto de la página en sí no se elimina. Eliminar estos objetos no invalida el documento sino que lo reduce. Consulte el siguiente fragmento de código:

```cpp
void RemovingUnusedObject() { 
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\");

    // Cadena para el nombre del archivo de entrada
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Inicializar OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Establecer opción RemoveUsedObject
    optimizationOptions->set_RemoveUnusedObjects(true);

    // Optimizar documento PDF usando OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Guardar documento actualizado
    document->Save(_dataDir + outfilename); 
}
```

### Eliminando Flujos No Utilizados

A veces el documento contiene flujos de recursos no utilizados. Estos flujos no son "objetos no utilizados" porque están referenciados desde un diccionario de recursos de página. Por lo tanto, no se eliminan con un método de "eliminar objetos no utilizados". Pero estos flujos nunca se usan con el contenido de la página. Esto puede suceder en casos cuando una imagen ha sido eliminada de la página pero no de los recursos de la página. Además, esta situación ocurre a menudo cuando las páginas son extraídas del documento y las páginas del documento tienen recursos "comunes", es decir, el mismo objeto Resources. Se analiza el contenido de la página para determinar si un flujo de recursos se utiliza o no. Los flujos no utilizados son eliminados. A veces disminuye el tamaño del documento. El uso de esta técnica es similar al paso anterior:

```cpp
void RemovingUnusedStreams() { 
    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Open document
    auto document = MakeObject<Document>();

    // Initialize OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Set RemoveUsedStreams option
    optimizationOptions->set_RemoveUnusedStreams(true);

    // Optimize PDF document using OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Save updated document
    document->Save(_dataDir + outfilename); 
}
```

### Vinculación de Flujos Duplicados

Algunos documentos pueden contener varios flujos de recursos duplicados (como imágenes, por ejemplo). Esto puede suceder, por ejemplo, cuando un documento se concatena consigo mismo. El documento de salida contiene dos copias independientes del mismo flujo de recursos. Analizamos todos los flujos de recursos y los comparamos. Si los flujos están duplicados, se fusionan, es decir, solo queda una copia. Las referencias se cambian adecuadamente y se eliminan las copias del objeto. En algunos casos, esto ayuda a disminuir el tamaño del documento.

```cpp
void LinkingDuplicateStreams() { 
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\");

    // Cadena para el nombre del archivo de entrada
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Inicializar OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Establecer opción LinkDuplicateStreams
    optimizationOptions->set_LinkDuplcateStreams(true);

    // Optimizar documento PDF usando OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Guardar documento actualizado
    document->Save(_dataDir + outfilename); 
}
```

Además, podemos usar la configuración de [AllowReusePageContent](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.optimization_options#aedaab36eaf8ed5059a2b1e11275bf6d8). Si esta propiedad se establece en true, el contenido de la página se reutilizará al optimizar el documento para páginas idénticas.

```cpp
void AllowReusePageContent() { 
    // String para el nombre de ruta
    String _dataDir("C:\\Samples\\");

    // String para el nombre del archivo de entrada
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Inicializar OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Establecer la opción AllowReusePageContent
    optimizationOptions->set_AllowReusePageContent(true);

    // Optimizar el documento PDF usando OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Guardar el documento actualizado
    document->Save(_dataDir + outfilename); 
}
```

### Desincrustar Fuentes

Cuando creas una versión PDF de tu archivo de diseño personal, se añade una copia de todas las fuentes necesarias al propio archivo PDF. Esto es incrustación. Independientemente de dónde se abra este PDF, ya sea en tu computadora, la computadora de un amigo o la computadora de tu proveedor de impresión, todas las fuentes correctas estarán allí y se mostrarán correctamente.

Pero, si el documento utiliza fuentes incrustadas, significa que todos los datos de las fuentes están almacenados en el documento. La ventaja es que el documento es visible independientemente de si la fuente está instalada en la máquina del usuario o no. Pero incrustar fuentes hace que el documento sea más grande. El método de desincrustar fuentes elimina todas las fuentes incrustadas. Así, el tamaño del documento disminuye, pero el propio documento puede volverse ilegible si la fuente correcta no está instalada.

```cpp
void UnembedFonts() {
    // String para el nombre de la ruta
    String _dataDir("C:\\Samples\\");

    // String para el nombre del archivo de entrada
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir+infilename);

    // Inicializar OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Establecer opción AllowReusePageContent
    optimizationOptions->set_UnembedFonts(true);

    // Optimizar documento PDF usando OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Guardar documento actualizado
    document->Save(_dataDir + outfilename);
}
```

Los recursos de optimización aplican estos métodos al documento. Si se aplica alguno de estos métodos, el tamaño del documento probablemente disminuirá. Si no se aplica ninguno de estos métodos, el tamaño del documento no cambiará, lo cual es obvio.

## Formas Adicionales de Reducir el Tamaño del Documento PDF

### Eliminación o Aplanamiento de Anotaciones

La presencia de anotaciones en su documento PDF aumenta su tamaño naturalmente. Las anotaciones pueden ser eliminadas cuando no son necesarias. Cuando son necesarias pero no requieren edición adicional, pueden ser aplanadas. Ambas técnicas reducirán el tamaño del archivo.

```cpp
void FlatteningAnnotation() {
    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String infilename("OptimizeDocument.pdf");
    // String for output file name
    String outfilename("OptimizeDocument_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Flatten annotations
    for(auto page : document->get_Pages())
    {
        for(auto annotation : page->get_Annotations())
        {
        annotation->Flatten();
        }
    }
    // Save updated document
    document->Save(_dataDir + outfilename);
}
```

### Eliminación de campos de formulario

Eliminar formularios de su PDF también optimizará su documento. Si el documento PDF contiene AcroForms, podemos intentar reducir el tamaño del archivo aplanando los campos del formulario.

```cpp
void FlatteningFormFields() {
    // String para el nombre de la ruta
    String _dataDir("C:\\Samples\\");

    // String para el nombre del archivo de entrada
    String infilename("OptimizeFormField.pdf");
    // String para el nombre del archivo de salida
    String outfilename("OptimizeFormField_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Aplanar campos de formulario
    // Aplanar formularios
    if (document->get_Form()->get_Fields()->get_Count() > 0)
    {
        for(auto item : document->get_Form()->get_Fields())
        {
            item->Flatten();
        }
    }
    // Guardar documento actualizado
    document->Save(_dataDir + outfilename);
}
```

### Convertir un PDF de espacio de color RGB a escala de grises

Un archivo PDF comprende Texto, Imagen, Adjuntos, Anotaciones, Gráficos y otros objetos. Puede que te encuentres con el requisito de convertir un PDF del espacio de color RGB a escala de grises para que sea más rápido al imprimir esos archivos PDF. Además, cuando el archivo se convierte a escala de grises, el tamaño del documento también se reduce, pero igualmente puede causar una disminución en la calidad del documento. Esta función es actualmente compatible con la función Pre-Flight de Adobe Acrobat, pero al hablar de automatización de Office, Aspose.PDF es una solución definitiva para proporcionar tales ventajas para la manipulación de documentos. Para cumplir con este requisito, se puede utilizar el siguiente fragmento de código.

```cpp
void ConvertPDFfromColorspaceToGrayscale() {
    // String para el nombre de la ruta
    String _dataDir("C:\\Samples\\");

    // String para el nombre del archivo de entrada
    String infilename("OptimizeDocument.pdf");
    // String para el nombre del archivo de salida
    String outfilename("Test-gray_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto strategy = MakeObject<Aspose::Pdf::RgbToDeviceGrayConversionStrategy>();
    for (int idxPage = 1; idxPage <= document->get_Pages()->get_Count(); idxPage++)
    {
        // Obtener instancia de la página particular dentro del PDF
        auto page = document->get_Pages()->idx_get(idxPage);
        // Convertir la imagen del espacio de color RGB a escala de grises
        strategy->Convert(page);
    }
    // Guardar el archivo resultante
    document->Save(_dataDir + outfilename); 
}
```
### Compresión FlateDecode

Aspose.PDF para C++ proporciona soporte para la compresión FlateDecode para la funcionalidad de Optimización de PDF.
Para optimizar la imagen usando la compresión FlateDecode, establezca las opciones de optimización en Flate.
El siguiente fragmento de código muestra cómo usar la opción en Optimización para almacenar imágenes con compresión **FlateDecode**:

```cpp
void FlatDecodeCompression() {
 // Cadena para el nombre de la ruta
 String _dataDir("C:\\Samples\\");

 // Cadena para el nombre del archivo de entrada
 String infilename("FlateDecodeCompression.pdf");
 // Cadena para el nombre del archivo de salida
 String outfilename("FlateDecodeCompression_out.pdf");

 // Abrir documento
 auto document = MakeObject<Document>(_dataDir + infilename);

 // Inicializar OptimizationOptions
 auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

 // Para optimizar la imagen usando la compresión FlateDecode, establezca las opciones de optimización en Flate
 optimizationOptions->get_ImageCompressionOptions()->set_Encoding(Aspose::Pdf::Optimization::ImageEncoding::Flate);

 // Optimizar el documento PDF usando OptimizationOptions
 document->OptimizeResources(optimizationOptions);

 // Guardar documento actualizado
 document->Save(_dataDir + outfilename);
}
```

### **Almacenar Imagen en XImageCollection**

Aspose.PDF para C++ proporciona la capacidad de almacenar nuevas imágenes en [XImageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image_collection) con compresión FlateDecode. Para habilitar esta opción, puede usar la bandera **ImageFilterType.Flate**. El siguiente fragmento de código muestra cómo utilizar esta funcionalidad:

```cpp
void StoreImageInXImageCollection() {

 // Cadena para el nombre de la ruta
 String _dataDir("C:\\Samples\\");

 // Cadena para el nombre del archivo de salida
 String outfilename("FlateDecodeCompression_out.pdf");

 // Abrir documento
 auto document = MakeObject<Document>();
 
 auto page = document->get_Pages()->Add();
 
 auto imageStream = System::IO::File::OpenRead(_dataDir + u"aspose-logo.jpg");
 
 page->get_Resources()->get_Images()->Add(imageStream, Aspose::Pdf::ImageFilterType::Flate);
 
 auto ximage = page->get_Resources()->get_Images()->idx_get(page->get_Resources()->get_Images()->get_Count());

 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());

 // Establecer coordenadas
 int lowerLeftX = 0;
 int lowerLeftY = 0;
 int upperRightX = 600;
 int upperRightY = 600;
 
 auto rectangle = MakeObject<Rectangle>(lowerLeftX, lowerLeftY, upperRightX, upperRightY);

 auto matrix = MakeObject<Matrix>(new double[] {rectangle->get_URX() - rectangle->get_LLX(), 0, 0, rectangle->get_URY() - rectangle->get_LLY(), rectangle->get_LLX(), rectangle->get_LLY()});
 // Usando el operador ConcatenateMatrix (concatenar matriz): define cómo se debe colocar la imagen
 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(matrix));
 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));
 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

 document->Save(_dataDir + outfilename);
}
```