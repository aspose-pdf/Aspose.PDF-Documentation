---
title: Aspose PDF License
linktitle: Licensing and limitations
type: docs
weight: 90
url: /cpp/licensing/
description: Aspose. PDF for C++ invita a sus clientes a obtener una licencia Clásica y una Licencia Medida. Así como usar una licencia limitada para explorar mejor el producto.
lastmod: "2021-11-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Limitaciones de la Versión de Evaluación

Queremos que nuestros clientes prueben a fondo nuestros componentes antes de comprarlos, por lo que la versión de evaluación le permite usarlo como lo haría normalmente. Sin embargo, habría las siguientes limitaciones al usar una versión de evaluación de la API:

**PDF creado con una marca de agua de evaluación**  
La versión de evaluación de Aspose.PDF para C++ proporciona la funcionalidad completa del producto, pero todas las páginas en los documentos PDF generados están marcadas con "Evaluación solamente. Creado con Aspose.PDF. Copyright 2002-2017 Aspose Pty Ltd" en la parte superior.

**Límite en el Número de Elementos de Colección que se pueden Procesar**

En la versión de evaluación, solo se pueden procesar cuatro elementos de cualquier colección (por ejemplo, solo cuatro páginas, cuatro campos de formulario, etc.).

## Aplicar Licencia usando Archivo u Objeto de Flujo

La licencia se puede cargar desde un archivo u objeto de flujo. Aspose.PDF para C++ intentará encontrar la licencia en las siguientes ubicaciones:

1. Ruta explícita.
1. La carpeta que contiene Aspose.PDF.dll.
1. La carpeta que contiene el ensamblado que llamó a Aspose.PDF.dll.
1. La carpeta que contiene el ensamblado de entrada (su .exe).
1. Un recurso incrustado en el ensamblado que llamó a Aspose.PDF.dll.

La forma más fácil de establecer una licencia es colocar el archivo de licencia en la misma carpeta que el archivo Aspose.PDF.dll y especificar el nombre del archivo, sin una ruta, como se muestra en el ejemplo a continuación.

### Cargar una Licencia desde Archivo

La forma más fácil de aplicar una licencia es colocar el archivo de licencia en la misma carpeta que el archivo Aspose.PDF.dll y especificar solo el nombre del archivo sin una ruta.

{{% alert color="primary" %}}

Cuando llame al método SetLicense, el nombre de la licencia que pase debe ser el del archivo de licencia. Por ejemplo, si cambias el nombre del archivo de licencia a "Aspose.PDF.lic.xml" pasa ese nombre de archivo al método Pdf->SetLicense(…).

{{% /alert %}}

```cpp
auto lic = MakeObject<Aspose::Pdf::License>();
lic->SetLicense(L"Aspose.PDF.Cpp.lic");
```

### Cargando una Licencia desde un Objeto Stream

El siguiente ejemplo muestra cómo cargar una licencia desde un stream.

```cpp
intrusive_ptr<License>license = new License();
intrusive_ptr<FileStream> myStream = new FileStream(new String("Aspose.PDF.Cpp.lic"), FileMode_Open);

license->SetLicense(myStream);
```

## Licencia Medida

Aspose.PDF permite a los desarrolladores aplicar una clave medida. Es un nuevo mecanismo de licenciamiento. El nuevo mecanismo de licenciamiento se utilizará junto con el método de licenciamiento existente. Aquellos clientes que deseen ser facturados en función del uso de las características de la API pueden utilizar el licenciamiento medido. Para más detalles, por favor consulte la sección de Preguntas Frecuentes sobre Licenciamiento Medido.

Se ha introducido una nueva clase Metered para aplicar la clave medida. A continuación se muestra el código de ejemplo que demuestra cómo establecer las claves públicas y privadas medidas.

Para más detalles, por favor consulte la sección de [Preguntas Frecuentes sobre Licencias Medidas](https://purchase.aspose.com/faqs/licensing/metered).