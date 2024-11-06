---
title: Trabajar con Documentos PDF en Qt
type: docs
weight: 130
url: es/cpp/work-with-pdf-documents-in-qt/
lastmod: "2021-11-01"
---

Qt es un marco de desarrollo de aplicaciones multiplataforma que permite crear una variedad de aplicaciones de escritorio, móviles, web y sistemas embebidos. En este artículo, veremos cómo puede integrar nuestra biblioteca C++ PDF para trabajar con documentos PDF en sus aplicaciones Qt.

## Usando Aspose.PDF para C++ dentro de Qt

Para usar Aspose.PDF para C++ en su aplicación Qt en el sistema operativo Windows, descargue la última versión de la API desde la sección de [descargas](https://downloads.aspose.com/pdf/cpp). Una vez descargada la API, puede usar cualquiera de las siguientes opciones para utilizarla con Qt.

- Usando Qt Creator
- Usando Visual Studio

Aquí, demostraremos cómo integrar y usar Aspose.PDF para C++ dentro de una aplicación de consola Qt usando Qt Creator.

### Crear Aplicación de Consola Qt

{{% alert color="primary" %}}

Este artículo asume que ha instalado correctamente el entorno de desarrollo de Qt y Qt Creator.

{{% /alert %}}

- Abre Qt Creator y crea una nueva *Aplicación de Consola Qt*.

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Qt-Console-Application.jpg)

- Selecciona la opción QMake del desplegable *Sistema de Construcción*.

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Qt-Console-Application-QMake.jpg)

- Selecciona el kit apropiado y finaliza el asistente.

En este punto, deberías tener una Aplicación de Consola Qt ejecutable que debería compilar sin problemas.

### Integra Aspose.PDF para la API de C++ con Qt

- Extrae el archivo Aspose.PDF para C++ que descargaste anteriormente.
- Copia las carpetas *Aspose.Pdf.Cpp* y *CodePorting.Native.Cs2Cpp_vc14_20.4* del paquete extraído de Aspose.PDF para C++ en la raíz del proyecto. Tu proyecto debería verse como se muestra en la siguiente imagen.

![todo:image_alt_text](work-with-pdf-documents-in-qt_1.png)

- Para añadir rutas a las carpetas lib e include, haz clic derecho en el proyecto en el panel LHS y selecciona *Agregar Biblioteca*.

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Add-Word-Library.jpg)

- Seleccione la opción Biblioteca Externa y explore las rutas para incluir y lib carpetas una por una.

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Add-Word-Library-2.jpg)

- Una vez hecho esto, tu archivo de proyecto .pro contendrá las siguientes entradas:

![todo:image_alt_text](work-with-pdf-documents-in-qt_2.png)

- Compila la aplicación y habrás terminado con la integración.

### Crear Documento PDF en Qt

Ahora que Aspose.PDF para C++ ha sido integrado con Qt, estamos listos para crear un documento PDF con algo de texto y guardarlo en el disco. Para hacer esto:

- Incluye los siguientes encabezados en main.cpp

```cpp

    #include "Aspose.PDF.Cpp/Document.h"
    #include "Aspose.PDF.Cpp/Page_.h"
    #include "Aspose.PDF.Cpp/PageCollection.h"
    #include "Aspose.PDF.Cpp/Generator/Paragraphs.h"
    #include "Aspose.PDF.Cpp/Text/TextFragment.h"
```

- Inserta el siguiente código en la función principal para generar un documento PDF y guardarlo en el disco

```cpp

    using namespace System;
    using namespace Aspose::Pdf;
    using namespace Aspose::Pdf::Text;
    
    QString text = "Hola Mundo";
    auto doc = MakeObject<Document>();

    auto pages = doc->get_Pages();

    pages->Add();

    auto page = pages->idx_get(1);

    auto paragraps = page->get_Paragraphs();

    paragraps->Add(MakeObject<TextFragment>(text.toStdU16String().c_str()));

    doc->Save(file_name.toStdU16String().c_str());
```